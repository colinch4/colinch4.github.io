---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치에 연결하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Swift RxBluetoothKit은 Swift에서 Bluetooth 장치와 통신하기 위한 라이브러리입니다. 이를 사용하면 iOS나 macOS 애플리케이션에서 Bluetooth 장치와 연결, 데이터 송수신 및 제어를 쉽게 할 수 있습니다.

## 1. RxBluetoothKit 설치하기

RxBluetoothKit은 CocoaPods를 통해 설치할 수 있습니다. 프로젝트의 Podfile에 다음과 같이 추가합니다.

```markdown
pod 'RxBluetoothKit'
```

다음으로 터미널을 열고 프로젝트가 있는 디렉토리로 이동한 후 다음 명령어를 실행합니다.

```markdown
pod install
```

## 2. Bluetooth 장치 검색하기

먼저 Bluetooth 장치를 검색하여 사용 가능한 장치들을 찾아야 합니다. 다음 코드는 RxBluetoothKit을 사용하여 장치 검색을 시작하는 예제입니다.

```swift
import RxBluetoothKit
import CoreBluetooth

let centralManager = CentralManager()

centralManager.observeState()
    .startWith(centralManager.state)
    .filter { $0 == .poweredOn }
    .flatMap { _ in centralManager.scanForPeripherals(withServices: nil) }
    .subscribe(onNext: { scannedPeripheral in
        // 장치 검색 결과 처리 로직 작성
        print(scannedPeripheral)
    })
    .disposed(by: disposeBag)
```

위 코드에서 `CentralManager()`를 사용하여 Central Manager 객체를 생성합니다. `observeState()` 메소드를 사용하여 Central Manager의 상태 변화를 관찰합니다. 상태가 `.poweredOn`인 경우에만 `scanForPeripherals` 메소드를 사용하여 장치 검색을 시작합니다. 검색된 장치는 `subscribe(onNext:)`에서 처리할 수 있습니다.

## 3. Bluetooth 장치에 연결하기

Bluetooth 장치를 발견한 후에는 해당 장치에 연결할 수 있습니다. 다음 코드는 RxBluetoothKit을 사용하여 Bluetooth 장치와 연결하는 예제입니다.

```swift
centralManager.connect(peripheral: discoveredPeripheral)
    .subscribe(onNext: { connectedPeripheral in
        // 장치 연결 성공 처리 로직 작성
        print("Connected to \(connectedPeripheral)")
    }, onError: { error in
        // 장치 연결 실패 처리 로직 작성
        print("Failed to connect: \(error)")
    })
    .disposed(by: disposeBag)
```

위 코드에서는 `connect(peripheral:)` 메소드를 사용하여 Bluetooth 장치에 연결합니다. 장치 연결에 성공한 경우 `subscribe(onNext:)`에서 처리할 수 있고, 연결에 실패한 경우 `onError:` 블록에서 처리할 수 있습니다.

## 4. Bluetooth 장치와 데이터 통신하기

Bluetooth 장치에 연결한 후에는 데이터를 송수신할 수 있습니다. 다음 코드는 RxBluetoothKit을 사용하여 데이터를 송수신하는 예제입니다.

```swift
let data = "Hello, Bluetooth!"

centralManager.write(data: data.data(using: .utf8)!, to: connectedPeripheral, characteristic: characteristic)
    .subscribe(onCompleted: {
        // 데이터 송신 완료 처리 로직 작성
        print("Data sent successfully")
    }, onError: { error in
        // 데이터 송신 실패 처리 로직 작성
        print("Failed to send data: \(error)")
    })
    .disposed(by: disposeBag)
```

위 코드에서는 `write(data:to:characteristic:)` 메소드를 사용하여 데이터를 Bluetooth 장치로 전송합니다. 송신이 완료되면 `onCompleted:` 블록에서 처리할 수 있고, 실패한 경우 `onError:` 블록에서 처리할 수 있습니다.

## 마무리

위와 같이 Swift RxBluetoothKit을 사용하여 Bluetooth 장치에 연결하는 방법에 대해 알아보았습니다. RxBluetoothKit은 Bluetooth 통신을 간편하게 처리할 수 있는 도구이므로, Bluetooth 기능을 사용하는 애플리케이션을 개발할 때 유용하게 활용할 수 있습니다.

참고 문서: [https://github.com/Polidea/RxBluetoothKit](https://github.com/Polidea/RxBluetoothKit)