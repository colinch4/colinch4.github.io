---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 속성 읽기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

이 문서에서는 Swift와 [RxBluetoothKit](https://github.com/Polidea/RxBluetoothKit) 라이브러리를 사용하여 Bluetooth 장치의 속성을 읽는 방법을 알아보겠습니다. RxBluetoothKit은 ReactiveX의 개념을 기반으로 한 Bluetooth Low Energy(BLE) 기기와의 상호작용을 간편하게 처리할 수 있는 라이브러리입니다.

Bluetooth 장치의 속성을 읽기 위해서는 다음의 단계를 따라야 합니다:

1. `CentralManager` 인스턴스 생성
2. Bluetooth 장치 검색
3. 원하는 속성 읽기

먼저, RxBluetoothKit을 프로젝트에 추가하고 `import` 문을 사용하여 RxBluetoothKit을 가져옵니다:

```swift
import RxBluetoothKit
```

다음으로, `CentralManager` 인스턴스를 생성합니다:

```swift
let manager = CentralManager(queue: .main)
```

Bluetooth 장치를 검색하기 위해 `scanForPeripherals` 메서드를 사용합니다. 아래는 예제 코드입니다:

```swift
manager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        // 검색된 장치를 처리하는 로직을 작성합니다.
        // 예: 이름이 "MyDevice"인 장치를 찾은 경우, 속성을 읽기 위해 연결합니다.
        if scannedPeripheral.peripheral.name == "MyDevice" {
            scannedPeripheral.peripheral.establishConnection()
                .subscribe(onNext: { peripheral in
                    // 연결이 성공하면, 원하는 속성을 읽습니다.
                    peripheral.readCharacteristic(UUID: characteristicUUID)
                        .subscribe(onSuccess: { characteristic in
                            // 속성을 읽은 후, 처리하는 로직을 작성합니다.
                        }, onError: { error in
                            // 속성 읽기에 실패한 경우, 실패 처리 로직을 작성합니다.
                        })
                })
        }
    })
```

위의 코드에서 `characteristicUUID`는 읽고자 하는 속성의 UUID 값입니다. 이 값을 알아내기 위해서는 장치의 제조사 사양서 또는 Bluetooth 서비스에 대한 문서를 참조해야 합니다.

추가로, Bluetooth 연결 후에는 연결을 해제해야 합니다. 아래는 연결을 해제하는 코드입니다:

```swift
peripheral.cancelConnection()
```

이제 Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 속성을 읽는 방법을 알게 되었습니다. RxBluetoothKit을 사용하면 BLE 기기와의 상호작용을 훨씬 간단하게 처리할 수 있습니다. 상세한 사용법은 [RxBluetoothKit GitHub](https://github.com/Polidea/RxBluetoothKit) 페이지와 다양한 예제 코드를 확인할 수 있는 [공식 문서](https://polidea.github.io/RxBluetoothKit/)를 참조하세요.