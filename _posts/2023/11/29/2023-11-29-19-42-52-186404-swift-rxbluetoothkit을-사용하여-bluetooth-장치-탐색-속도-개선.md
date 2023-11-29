---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth 장치 탐색 속도 개선"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Swift RxBluetoothKit은 Swift로 작성된 Bluetooth Low Energy (BLE) 장치와의 상호작용을 쉽게 구현할 수 있도록 도와주는 라이브러리입니다. 이 라이브러리를 사용하여 Bluetooth 장치 탐색 속도를 개선하는 방법을 살펴보겠습니다.

## 1. 필요한 라이브러리 설치

RxBluetoothKit을 사용하려면 먼저 프로젝트에 해당 라이브러리를 설치해야 합니다. `Podfile`에 다음과 같이 RxBluetoothKit을 추가합니다.

```ruby
pod 'RxBluetoothKit', '~>4.5'
```

그런 다음 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 2. Bluetooth 스캔 설정

Bluetooth 장치를 탐색하기 전에 스캔 설정을 구성해야 합니다. 스캔 설정을 통해 검색할 장치의 필터링, 스캔 모드 및 탐색 시간을 설정할 수 있습니다. 아래는 기본 스캔 설정 예제입니다.

```swift
import RxBluetoothKit

let manager = BluetoothManager()

// 필터 설정
let scanFilter = ScanFilter()
    .setDeviceName(nil) // 탐색할 장치의 이름 (nil로 설정하면 모든 장치 탐색)
    .setDeviceUUIDs(nil) // 탐색할 장치의 UUIDs (nil로 설정하면 모든 장치 탐색)

// 스캔 모드 설정
let scanSettings = ScanSettings()
    .setScanMode(.lowLatency) // 스캔 모드 설정 (여기서는 최적 성능을 위해 lowLatency 모드 사용)
    .setReportDelay(0) // 리포트 지연 시간 (0으로 설정하면 즉시 리포트)

// 탐색 시간 설정
let scanDuration = 10 // 10초 동안 탐색

// 탐색 시작
manager.scanContinuously(withServices: nil, // 탐색할 서비스 UUIDs (nil로 설정하면 모든 서비스 탐색)
                        scanSettings: scanSettings,
                        scanFilter: scanFilter)
    .take(duration)
    .subscribe(onNext: { scannedPeripheral in
        // 탐색된 장치 처리
    })
    .disposed(by: disposeBag)
```

## 3. 속도 개선을 위한 팁

Bluetooth 장치 탐색 속도를 개선하기 위해 다음 팁을 고려해 볼 수 있습니다.

- 필요한 서비스와 장치만 탐색하기 위해 `setDeviceName` 및 `setDeviceUUIDs`를 사용하여 필터를 구성합니다.
- `setScanMode`를 `lowLatency`로 설정하여 탐색 속도를 최적화합니다.
- `setReportDelay`를 0으로 설정하여 탐색 리포트의 지연 시간을 최소화합니다.
- 필요한 탐색 시간 동안만 탐색을 수행하도록 `take` 오퍼레이터를 사용합니다.

## 참고 자료

- [RxBluetoothKit GitHub Repository](https://github.com/Polidea/RxBluetoothKit)
- [RxSwift GitHub Repository](https://github.com/ReactiveX/RxSwift)