---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치 검색하기"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth는 기기 간에 데이터를 전송하고 통신하는 데 사용되는 무선 기술입니다. Swift RxBluetoothKit은 iOS 기기에서 Bluetooth 장치와 상호 작용하기 위한 강력한 라이브러리입니다. 이 블로그 게시물에서는 Swift RxBluetoothKit을 사용하여 Bluetooth 장치를 검색하는 방법에 대해 알아보겠습니다.

## 1. RxBluetoothKit 설치하기
RxBluetoothKit을 사용하기 위해 먼저 CocoaPods를 사용하여 프로젝트에 RxBluetoothKit을 설치해야 합니다. 터미널에서 프로젝트 폴더로 이동한 후 다음 명령어를 실행합니다.

```
$ pod init
```

그런 다음 Podfile을 열어 다음 줄을 추가합니다.

```ruby
pod 'RxBluetoothKit'
```

프로젝트 폴더에서 다음 명령어를 실행하여 RxBluetoothKit을 설치합니다.

```
$ pod install
```

## 2. RxBluetoothKit을 사용하여 Bluetooth 장치 검색하기
RxBluetoothKit을 사용하여 Bluetooth 장치를 검색하려면 몇 가지 단계를 거쳐야 합니다.

첫째, `CentralManager` 인스턴스를 생성합니다. 이 인스턴스는 Bluetooth 장치와의 상호 작용을 관리합니다. 다음 코드는 `CentralManager` 인스턴스를 생성하는 예입니다.

```swift
import CoreBluetooth
import RxBluetoothKit

let centralManager = CentralManager(queue: .main)
```

둘째, Bluetooth 장치를 검색하기 위해 `scanForPeripherals` 메서드를 사용합니다. 이 메서드는 검색을 시작하고, 발견된 장치를 발견할 때마다 콜백으로 결과를 반환합니다. 다음 코드는 Bluetooth 장치 검색을 시작하는 예입니다.

```swift
let scanDisposable = centralManager.rx.scanForPeripherals(withServices: nil)
    .subscribe(onNext: { scannedPeripheral in
        print("Discovered peripheral: \(scannedPeripheral)")
    })
```

셋째, 검색을 멈추고 결과를 처리하기 전에 `scanDisposable`을 `dispose`하여 검색을 중단합니다.

```swift
// 검색 중단
scanDisposable.dispose()
```

## 마무리
이렇게 Swift RxBluetoothKit을 사용하여 Bluetooth 장치를 검색하는 방법을 알아보았습니다. 추가로 기기와 상호 작용하거나 데이터를 전송하는 방법에 대해서도 RxBluetoothKit 문서와 예제를 참조할 수 있습니다. RxBluetoothKit은 강력한 도구이며 Bluetooth 기능을 손쉽게 구현할 수 있도록 도와줍니다.

## 참고 자료
- [RxBluetoothKit GitHub 페이지](https://github.com/Polidea/RxBluetoothKit)
- [RxBluetoothKit 문서](https://rxbluetoothkit.com/docs/)