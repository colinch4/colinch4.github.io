---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 기능 활성화 및 비활성화"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth는 모바일 애플리케이션에서 외부 장치와의 통신을 위해 중요한 요소입니다. Swift RxBluetoothKit을 사용하면 Bluetooth 장치의 기능을 쉽게 활성화하고 비활성화할 수 있습니다. 이 글에서는 Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 기능을 활성화 및 비활성화하는 방법에 대해 알아보겠습니다.

## 1. RxBluetoothKit 설치

RxBluetoothKit을 사용하기 위해 먼저 프로젝트에 RxSwift 및 RxBluetoothKit을 설치해야 합니다. CocoaPods을 사용하는 경우, Podfile에 다음과 같이 추가합니다:

```
pod 'RxBluetoothKit'
```

설치가 완료되면 프로젝트를 업데이트하고, `import RxBluetoothKit`으로 RxBluetoothKit을 임포트할 수 있습니다.

## 2. Bluetooth 기능 활성화

Bluetooth 기능을 활성화하려면 `CentralManager`를 생성하고 Bluetooth 상태를 모니터링해야 합니다. 이를 위해 다음 코드를 사용할 수 있습니다:

```swift
import RxBluetoothKit
import RxSwift

let disposeBag = DisposeBag()

let centralManager = CentralManager()
centralManager.rx
    .state
    .subscribe(onNext: { state in
        switch state {
        case .poweredOn:
            print("Bluetooth is powered on.")
            // Bluetooth 기능이 활성화되었을 때 수행할 작업을 추가하세요.
        case .poweredOff:
            print("Bluetooth is powered off.")
            // Bluetooth 기능이 비활성화되었을 때 수행할 작업을 추가하세요.
        default:
            break
        }
    })
    .disposed(by: disposeBag)
```

위 코드는 `CentralManager`의 `rx.state`를 구독하여 Bluetooth의 상태를 모니터링합니다. `state`가 `.poweredOn`으로 변경되면 Bluetooth 기능이 활성화된 것이므로 수행할 작업을 추가하면 됩니다. 마찬가지로, `state`가 `.poweredOff`로 변경되면 Bluetooth 기능이 비활성화된 것이므로 수행할 작업을 추가할 수 있습니다.

## 3. Bluetooth 기능 비활성화

Bluetooth 기능을 비활성화하려면 `centralManager.cancelPeripheralConnection(_:)` 메서드를 사용하여 연결된 장치와의 연결을 해제해야 합니다. 다음 코드는 연결된 장치와의 연결을 해제하는 예입니다:

```swift
centralManager.cancelPeripheralConnection(peripheral)
    .subscribe(onNext: { disconnectedPeripheral in
        print("Disconnected from peripheral: \(disconnectedPeripheral)")
        // 연결 해제 후 수행할 작업을 추가하세요.
    }, onError: { error in
        print("Failed to disconnect peripheral: \(error)")
    })
    .disposed(by: disposeBag)
```

위 코드에서 `peripheral`은 연결 해제할 Bluetooth 장치를 나타내는 것으로 대체해야 합니다.

## 마치며

이제 Swift RxBluetoothKit을 사용하여 Bluetooth 장치의 기능을 활성화 및 비활성화할 수 있는 방법을 알게 되었습니다. Bluetooth 기능이 활성화되었는지 여부를 모니터링하고, 필요에 따라 장치와의 연결을 해제할 수 있습니다. 이를 활용하여 외부 장치와의 통신을 보다 간편하게 구현할 수 있습니다.

더 많은 RxBluetoothKit의 기능과 API에 대해서는 [RxBluetoothKit 공식 문서](https://github.com/Polidea/RxBluetoothKit)를 참조하세요.