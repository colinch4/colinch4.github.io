---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치와 데이터 암호화"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy (BLE)는 저전력 블루투스 프로토콜로서, 주로 센서와 같은 IoT 장치와의 통신에 사용되는 기술입니다. iOS 애플리케이션에서 BLE 장치와 통신하기 위해서는 CoreBluetooth 프레임워크를 사용해야 합니다. 그리고 RxSwift 라이브러리와 함께 RxBluetoothKit을 사용하면 BLE 통신을 보다 쉽고 간편하게 처리할 수 있습니다.

이번 글에서는 Swift RxBluetoothKit을 사용하여 BLE 장치와의 통신을 설정하고, 데이터를 암호화하여 보내고 받는 방법에 대해 알아보겠습니다.

## RxBluetoothKit 및 CryptoSwift 설치

먼저, 프로젝트에 Swift RxBluetoothKit과 CryptoSwift를 설치해야 합니다. 이를 위해서는 CocoaPods 또는 Swift Package Manager를 사용할 수 있습니다.

### CocoaPods를 사용하여 설치하는 방법

Podfile에 다음과 같이 RxBluetoothKit과 CryptoSwift를 추가합니다.

```ruby
pod 'RxBluetoothKit'
pod 'CryptoSwift'
```

그리고 터미널에서 다음 명령어를 실행하여 CocoaPods를 설치합니다.

```
$ pod install
```

### Swift Package Manager를 사용하여 설치하는 방법

Xcode에서 "File" 탭에서 "Swift Packages"를 선택한 후 "Add Package Dependency"를 선택합니다. 다음 URL을 입력하고 "Next"를 클릭합니다.

```
https://github.com/Polidea/RxBluetoothKit.git
```

그리고 "Rules"에서 "Up to Next Major"을 선택하고, "Next"를 클릭합니다. 이후 "CryptoSwift"도 같은 방식으로 추가합니다.

## BLE 장치와 연결하기

Swift RxBluetoothKit을 사용하여 BLE 장치와 연결하기 위해서는 몇 가지 단계를 거쳐야 합니다.

1. CentralManager 객체를 생성합니다.
2. BLE 장치를 검색하여 해당 장치와 연결합니다.
3. 연결된 장치와 데이터를 주고받기 위해 Service와 Characteristic을 찾습니다.
4. 데이터를 암호화하여 장치로 전송합니다.
5. 장치로부터 암호화된 데이터를 수신합니다.

다음은 Swift 코드로 작성된 예시입니다.

```swift
import CoreBluetooth
import RxSwift
import RxBluetoothKit
import CryptoSwift

// CentralManager 객체 생성
let centralManager = CentralManager(queue: .main)

// BLE 장치 검색 및 연결
centralManager.scanForPeripherals(withServices: nil, options: nil)
    .flatMap { $0.peripheral.establishConnection() }
    .subscribe(onNext: { peripheral in
        // Service 및 Characteristic 검색
        peripheral.discoverServices([serviceUUID])
            .flatMap { $0.discoverCharacteristics([characteristicUUID]) }
            .subscribe(onNext: { characteristic in
                // 데이터 암호화 및 장치로 전송
                let data = "Hello, BLE device!".data(using: .utf8)!
                let encryptedData = try! data.encrypt(withKey: encryptionKey)
                peripheral.writeValue(encryptedData, for: characteristic, type: .withResponse)
                    .subscribe()
                    .disposed(by: disposeBag)
            })
            .disposed(by: disposeBag)
    })
    .disposed(by: disposeBag)

// 장치로부터 암호화된 데이터 수신
centralManager.observeValueUpdateAndSetNotification(for: characteristic)
    .subscribe(onNext: { characteristic in
        let encryptedData = characteristic.value!
        let decryptedData = try! encryptedData.decrypt(withKey: encryptionKey)
        let message = String(data: decryptedData, encoding: .utf8)!
        print("Received data: \(message)")
    })
    .disposed(by: disposeBag)
```

위 코드에서는 CryptoSwift를 사용하여 데이터를 암호화하기 위해 `encrypt`와 `decrypt` 함수를 사용했습니다. `encryptionKey`는 사전에 약속된 비밀키입니다. BLE 장치에서는 동일한 비밀키를 사용하여 데이터를 복호화합니다.

이렇게 Swift RxBluetoothKit을 사용하여 BLE 장치와 데이터를 암호화하여 주고받을 수 있습니다. 더 자세한 정보와 예시는 [RxBluetoothKit GitHub 저장소](https://github.com/Polidea/RxBluetoothKit)를 참고하시기 바랍니다.