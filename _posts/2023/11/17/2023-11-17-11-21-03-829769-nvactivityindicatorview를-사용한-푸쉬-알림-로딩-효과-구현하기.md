---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 푸쉬 알림 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

푸쉬 알림을 받을 때 로딩 효과를 동적으로 표시하는 것은 사용자 경험을 향상시키는 좋은 방법입니다. 이번에는 Swift 언어에서 NVActivityIndicatorView를 사용하여 푸쉬 알림 로딩 효과를 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 간단하게 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 다양한 스타일과 색상으로 로딩 효과를 구현할 수 있으며, 사용하기도 매우 간편합니다.

## NVActivityIndicatorView 설치

먼저, Cocoapods를 통해 NVActivityIndicatorView를 설치해야 합니다. 프로젝트의 Podfile에 다음 라인을 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령을 실행하여 NVActivityIndicatorView를 설치합니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성하고 원하는 위치에 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballBeat, color: .white, padding: nil)
view.addSubview(activityIndicatorView)
```

3. NVActivityIndicatorView를 시작하거나 정지시킵니다.

```swift
activityIndicatorView.startAnimating() // 애니메이션 시작

activityIndicatorView.stopAnimating() // 애니메이션 정지
```

## 푸쉬 알림 로딩 효과 구현하기

푸쉬 알림을 받을 때 NVActivityIndicatorView를 이용하여 로딩 효과를 구현할 수 있습니다. 

예를 들어, 푸쉬 알림을 받으면 알림 UI가 화면 상단에 표시되고, 동시에 로딩 효과가 나타나도록 아래와 같이 구현할 수 있습니다.

```swift
// AppDelegate.swift

func application(_ application: UIApplication, didReceiveRemoteNotification userInfo: [AnyHashable : Any]) {
    // 푸쉬 알림 수신 시
    showPushNotification(userInfo)
}

func showPushNotification(_ userInfo: [AnyHashable : Any]) {
    // 알림 UI 표시
    let notificationView = UIView(frame: CGRect(x: 0, y: 0, width: UIScreen.main.bounds.width, height: 50))
    notificationView.backgroundColor = UIColor.blue
    window?.addSubview(notificationView)

    // 로딩 효과 표시
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 10, y: 10, width: 30, height: 30), type: .ballBeat, color: .white, padding: nil)
    notificationView.addSubview(activityIndicatorView)
    activityIndicatorView.startAnimating()

    // 일정 시간 후 알림 UI 및 로딩 효과 제거
    DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
        activityIndicatorView.stopAnimating()
        notificationView.removeFromSuperview()
    }
}
```

위 코드는 푸쉬 알림을 수신하면 알림 UI를 상단에 표시하고, 로딩 효과를 추가로 표시한 후 일정 시간(여기서는 2초)이 지나면 알림 UI와 로딩 효과를 제거합니다.

## 결론

이번에는 Swift에서 NVActivityIndicatorView를 사용하여 푸쉬 알림 로딩 효과를 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 매우 유용한 라이브러리로, 로딩 인디케이터를 손쉽게 구현할 수 있습니다. 푸쉬 알림과 같은 상황에서 사용자 경험을 개선하기 위해 로딩 효과를 적용해 보세요!