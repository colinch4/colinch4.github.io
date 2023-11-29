---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 특성 쓰기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy(GATT)를 사용하여 기기와 통신할 때는 GATT 특성에 값을 쓰는 것이 중요합니다. 이번 블로그 글에서는 Swift RxBluetoothKit을 사용하여 GATT 특성에 값을 쓰는 방법을 알아보겠습니다.

## RxBluetoothKit 설치

RxBluetoothKit은 Bluetooth Low Energy(GATT) 기능을 사용하기 위한 RxSwift 기반 라이브러리입니다. 먼저 프로젝트에 RxBluetoothKit을 설치해야 합니다. CocoaPods를 사용하는 경우 Podfile에 다음과 같이 추가합니다:

```ruby
target 'YourProject'
  use_frameworks!
  pod 'RxBluetoothKit'
end
```

프로젝트 디렉토리에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## GATT 특성 쓰기

특성에 값을 쓰기 위해서는 다음과 같은 단계를 따라야 합니다:

1. `CentralManager`의 인스턴스를 생성합니다:

```swift
let centralManager = CentralManager(queue: .main)
```

2. 특성을 찾습니다. `peripheral.discoverServices()`를 사용하여 지원되는 서비스를 찾고, `service.discoverCharacteristics()`를 사용하여 해당 서비스의 특성을 찾습니다:

```swift
let peripheral: Peripheral = ...
peripheral.discoverServices([serviceUUID])
    .subscribe(onNext: { services in
        guard let service = services.first else { return }
        service.discoverCharacteristics([characteristicUUID])
    })
    .disposed(by: disposeBag)
```

3. 특성을 쓰기 위해 값을 변환합니다. `Observable.from([value])`을 사용하여 값을 변환합니다:

```swift
let value = Data([0x01, 0x02, 0x03])
let writeValueObservable = Observable.from([value])
```

4. 변환된 값을 특성에 씁니다. `characteristic.writeValue()`를 사용하여 값을 씁니다. 

```swift
let characteristic: Characteristic = ...
writeValueObservable
    .flatMap { value in
        characteristic.writeValue(value)
    }
    .subscribe(onNext: {
        // 옵저버블을 구독하여 값을 씀
    })
    .disposed(by: disposeBag)
```

위와 같은 방식으로 GATT 특성에 값을 쓸 수 있습니다.

## 결론

이번 글에서는 Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy GATT 특성에 값을 쓰는 방법에 대해 알아보았습니다. RxBluetoothKit의 강력한 기능을 활용하여 Bluetooth Low Energy 기기와 효과적으로 통신할 수 있습니다. 추가적인 정보는 [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)를 참고해 주세요.