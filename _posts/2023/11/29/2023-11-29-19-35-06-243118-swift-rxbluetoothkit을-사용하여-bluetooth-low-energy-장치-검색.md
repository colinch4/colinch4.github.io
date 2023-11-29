---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치 검색"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy (BLE)는 저전력 무선 통신 프로토콜로, 주변 장치와의 통신에 사용됩니다. Swift RxBluetoothKit은 제공되는 ReactiveX 인터페이스를 활용하여 BLE 장치 검색을 간편하게 할 수 있도록 지원하는 라이브러리입니다. 이번 글에서는 Swift RxBluetoothKit을 사용하여 BLE 장치를 검색하는 방법을 알아보겠습니다.

## 1. RxBluetoothKit 설치

먼저, RxBluetoothKit을 프로젝트에 추가하기 위해서는 Swift Package Manager 또는 CocoaPods를 통해 라이브러리를 설치해야 합니다. 다음은 CocoaPods를 사용하여 RxBluetoothKit을 설치하는 방법입니다.

```ruby
# Podfile

target 'YourProject' do
  use_frameworks!
  pod 'RxBluetoothKit'
end
```

위와 같이 Podfile에 RxBluetoothKit을 추가하고, 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 2. BLE 장치 검색하기

RxBluetoothKit을 사용하여 BLE 장치를 검색하려면 다음 단계를 따라야 합니다.

### 2.1. CentralManager 생성

```swift
import RxBluetoothKit

let centralManager = CentralManager(queue: .main)
```

### 2.2. BLE 장치 검색

```swift
centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        // 검색된 BLE 장치 처리
    }, onError: { error in
        // 에러 처리
    })
    .disposed(by: disposeBag)
```

`scanForPeripherals(withServices:)` 메서드를 사용하여 BLE 장치 검색을 시작할 수 있습니다. `withServices` 매개 변수를 사용하여 특정 서비스의 BLE 장치만 검색할 수도 있습니다.

### 2.3. 검색된 BLE 장치 처리

```swift
centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("검색된 장치: \(scannedPeripheral)")
    })
    .disposed(by: disposeBag)
```

`subscribe(onNext:)`를 사용하여 검색된 장치에 대한 처리를 할 수 있습니다. 여기서는 간단하게 장치를 콘솔에 출력하도록 하였습니다.

## 3. 종합 예제

다음은 RxBluetoothKit을 사용하여 BLE 장치 검색을 실행하는 전체 예제 코드입니다.

```swift
import RxBluetoothKit

let centralManager = CentralManager(queue: .main)
let disposeBag = DisposeBag()

centralManager.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("검색된 장치: \(scannedPeripheral)")
    }, onError: { error in
        print("에러 발생: \(error)")
    })
    .disposed(by: disposeBag)
```

위의 코드를 실행하면 BLE 장치 검색이 시작되고, 검색된 장치는 콘솔에 출력됩니다.

## 결론

이번 글에서는 Swift RxBluetoothKit을 사용하여 BLE 장치 검색을 하는 방법을 알아보았습니다. RxBluetoothKit을 통해 간편한 블루투스 장치 검색을 구현할 수 있으며, 다양한 BLE 관련 기능도 활용할 수 있습니다. Swift RxBluetoothKit의 공식 문서를 참고하여 더 자세한 사용법과 기능을 확인해보세요.

## 참고 자료

- [RxBluetoothKit 공식 GitHub 저장소](https://github.com/Polidea/RxBluetoothKit)
- [RxBluetoothKit 공식 문서](https://polidea.github.io/RxBluetoothKit/docs/index.html)