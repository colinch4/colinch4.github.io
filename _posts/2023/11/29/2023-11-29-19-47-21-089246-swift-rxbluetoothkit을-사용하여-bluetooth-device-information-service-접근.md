---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Device Information Service 접근"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth 기능을 개발하는 경우, 디바이스의 정보에 접근하는 것은 중요한 작업입니다. Swift RxBluetoothKit은 Bluetooth 기능을 더 쉽게 구현할 수 있도록 도와주는 라이브러리입니다. 이 글에서는 Swift RxBluetoothKit을 사용하여 Bluetooth 디바이스의 정보 서비스에 접근하는 방법을 다루겠습니다.

## 1. RxBluetoothKit 설치

RxBluetoothKit을 사용하기 위해, 먼저 프로젝트에 RxBluetoothKit을 설치해야 합니다. [CocoaPods](https://cocoapods.org/)를 사용하여 다음과 같이 라이브러리를 설치할 수 있습니다.

```swift
pod 'RxBluetoothKit'
```

설치가 완료되면, 프로젝트에서 import 문을 추가하여 RxBluetoothKit을 사용할 수 있도록 해야 합니다.

```swift
import RxBluetoothKit
```

## 2. Device Information Service 접근

Device Information Service는 Bluetooth 디바이스의 기본 정보를 제공하는 서비스입니다. 다음 코드를 사용하여 Bluetooth 디바이스의 Device Information Service에 접근할 수 있습니다.

```swift
let disposeBag = DisposeBag()

// CentralManager 인스턴스 생성
let centralManager = CentralManager()
        
// Bluetooth 디바이스 스캔 시작
centralManager.scanForPeripherals(withServices: [DeviceInformationService.uuid])
    .subscribe(onNext: { scannedPeripheral in
        print("디바이스 스캔됨: \(scannedPeripheral)")
        
        // 디바이스 연결
        centralManager.connect(scannedPeripheral)
            .subscribe(onNext: { connectedPeripheral in
                print("디바이스 연결됨: \(connectedPeripheral)")
                
                // Device Information Service 접근
                connectedPeripheral.discoverServices([DeviceInformationService.uuid])
                    .subscribe(onNext: { services in
                        for service in services {
                            print("Service 발견됨: \(service)")
                            
                            // Characteristic 접근
                            connectedPeripheral.discoverCharacteristics([DeviceInformationService.hardwareRevision.uuid], for: service)
                                .subscribe(onNext: { characteristics in
                                    for characteristic in characteristics {
                                        print("Characteristic 발견됨: \(characteristic)")
                                        
                                        // Characteristic 읽기
                                        connectedPeripheral.readValue(for: characteristic)
                                            .subscribe(onNext: { data in
                                                let value = String(data: data, encoding: .utf8)
                                                print("Characteristic 값: \(value ?? "")")
                                            })
                                            .disposed(by: self.disposeBag)
                                    }
                                })
                                .disposed(by: self.disposeBag)
                        }
                    })
                    .disposed(by: self.disposeBag)
            })
            .disposed(by: self.disposeBag)
    })
    .disposed(by: disposeBag)
```

위의 코드에서 사용된 `DeviceInformationService.uuid`는 RxBluetoothKit이 제공하는 `DeviceInformationService`의 uuid입니다. 이 uuid는 Bluetooth 디바이스의 Device Information Service를 식별하는데 사용됩니다.

위의 코드는 Bluetooth 디바이스의 정보를 불러오기 위해 Device Information Service에만 집중하였지만, 다른 Service나 Characteristic에도 접근할 수 있습니다. 필요에 따라 코드를 수정하여 다른 Service나 Characteristic에 접근해보세요.

## 참고 자료

- [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)
- [RxBluetoothKit 문서](https://polidea.github.io/RxBluetoothKit/)
- [RxSwift GitHub 페이지](https://github.com/ReactiveX/RxSwift)