---
layout: post
title: "[swift] Swift RxBluetoothKit을 사용하여 Bluetooth Low Energy 장치와 보안 통신 진행"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

Bluetooth Low Energy(BLE)는 저전력 무선 기술로, 스마트 홈 기기, 웨어러블 디바이스 등 다양한 IoT 기기와의 통신에 사용됩니다. Swift RxBluetoothKit은 Swift에서 BLE 통신을 쉽게 구현할 수 있도록 도와주는 라이브러리입니다. 이 글에서는 Swift RxBluetoothKit을 사용하여 BLE 장치와의 보안 통신을 진행하는 방법에 대해 알아보겠습니다.

## 1. RxBluetoothKit 설치

먼저, 프로젝트에 RxBluetoothKit을 설치해야 합니다. CocoaPods를 사용하는 경우, `Podfile`에 다음과 같은 dependency를 추가하고 `pod install` 명령어로 라이브러리를 설치합니다. 

```swift
pod 'RxBluetoothKit'
```

RxSwift를 사용하고 있다면, RxBluetoothKit에서 제공하는 Observable 기반의 BLE 통신을 활용할 수 있습니다. 따라서 `RxSwift`와 `RxCocoa`도 `Podfile`에 함께 추가해줍니다.

```swift
pod 'RxSwift'
pod 'RxCocoa'
```

## 2. BLE 장치 검색

RxBluetoothKit을 사용하여 BLE 장치를 검색하는 방법은 간단합니다. `CentralManager` 객체를 생성하고 `scanForPeripherals` 함수를 호출하여 주변 장치를 검색합니다. 검색된 장치는 `subscribe` 메서드를 사용하여 감시할 수 있습니다.

```swift
import RxBluetoothKit

let centralManager = CentralManager()
let scanDisposable = centralManager.scanForPeripherals(withServices: nil)
                                        .subscribe(onNext: { scanResult in
                                            // 검색된 장치 처리
                                        })
```

## 3. 장치 연결

검색된 장치 중에서 원하는 장치를 선택하여 연결할 수 있습니다. `Peripheral` 객체를 이용하여 연결을 시도하고, `connect` 함수를 호출하여 연결을 수행합니다. 연결 상태는 `Observable`을 통해 관찰할 수 있습니다.

```swift
let peripheral: Peripheral = ... // 연결할 장치
let connectionDisposable = centralManager.connect(peripheral)
                                        .subscribe(onNext: { peripheral in
                                            // 장치 연결 성공
                                        }, onError: { error in
                                            // 장치 연결 오류
                                        })
```

## 4. 보안 통신

BLE 통신은 대부분 보안이 필요한 경우가 많습니다. RxBluetoothKit은 보안 관련 기능을 제공하여 안전한 통신을 할 수 있도록 도와줍니다.

### 4.1. 페어링

BLE 장치와의 보안 통신을 위해서는 페어링 과정이 필요합니다. `pairing` 함수를 호출하여 페어링을 시도합니다. 연결된 장치의 페어링 상태는 `Observable`을 통해 관찰할 수 있습니다.

```swift
centralManager.pairing(peripheral)
              .subscribe(onNext: { peripheral in
                  // 페어링 성공
              }, onError: { error in
                  // 페어링 실패
              })
```

### 4.2. 보안 요청

보안 요청은 `requestConnectionPriority` 함수를 사용하여 수행합니다. 다음과 같이 `requestSecurity` 매개변수를 `.high` 또는 `.low`로 설정하여 보안 수준을 조절할 수 있습니다.

```swift
centralManager.requestConnectionPriority(.high, for: peripheral)
              .subscribe(onNext: { peripheral in
                  // 보안 요청 성공
              }, onError: { error in
                  // 보안 요청 실패
              })
```

### 4.3. 데이터 전송

보안 통신이 수립되면 데이터 전송을 시작할 수 있습니다. `writeValue` 함수를 사용하여 데이터를 작성할 수 있습니다. 데이터 쓰기가 완료되면 결과를 `Observable`로받을 수 있습니다.

```swift
let data: Data = ... // 전송할 데이터
centralManager.writeValue(data, for: characteristic, type: .withResponse)
              .subscribe(onNext: { characteristic in
                  // 데이터 전송 성공
              }, onError: { error in
                  // 데이터 전송 실패
              })
```

## 5. 정리

이렇게 Swift RxBluetoothKit을 사용하여 BLE 장치와 보안 통신을 진행하는 방법을 알아보았습니다. BLE를 통해 안전하게 데이터를 전송하고 제어하기 위해서는 보안 요청과 페어링 절차를 거쳐야 합니다. Swift RxBluetoothKit은 RxSwift와 결합하여 BLE 통신을 간편하게 구현할 수 있습니다.

더 자세한 내용은 [RxBluetoothKit 공식 문서](https://github.com/Polidea/RxBluetoothKit)를 참조하시기 바랍니다.