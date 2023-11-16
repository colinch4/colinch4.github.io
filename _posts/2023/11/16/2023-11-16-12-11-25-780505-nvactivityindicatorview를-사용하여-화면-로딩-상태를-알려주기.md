---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 알려주기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱에 긴 작업이나 네트워크 요청 등으로 인해 로딩이 필요한 경우, 사용자에게 로딩 상태를 시각적으로 알려주는 것은 좋은 사용자 경험을 제공하는 중요한 요소입니다. NVActivityIndicatorView는 Swift로 작성된 iOS 앱에서 간단하게 화면 로딩 상태를 표시해주는 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 다양한 로딩 인디케이터(Different Loading Indicators)를 제공하는 Swift 라이브러리입니다. 사용자의 요청에 따라 다양한 스타일의 로딩 인디케이터를 선택할 수 있으며, 사용하기 쉽고 커스터마이징할 수 있는 기능을 제공합니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 Cocoapods를 통해 설치해야 합니다. Cocoapods가 설치되어있지 않다면, 먼저 Cocoapods를 설치해주세요.

터미널을 열고 프로젝트의 Podfile이 위치한 디렉토리로 이동한 뒤, 아래의 명령어를 실행하여 NVActivityIndicatorView를 설치합니다.

```bash
pod 'NVActivityIndicatorView'
```

설치가 완료되면, 프로젝트의 .xcworkspace 파일을 열어주세요.

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 다음의 단계를 따르세요.

1. NVActivityIndicatorView를 뷰에 추가하려는 UIViewController에서 NVActivityIndicatorViewDelegate를 추가합니다.

```swift
class MyViewController: UIViewController, NVActivityIndicatorViewDelegate {
    // ...
}
```

2. NVActivityIndicatorView 인스턴스를 생성하고 뷰에 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 80, height: 80), type: .ballRotateChase, color: .systemBlue)
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

3. 로딩 상태를 보여주고 싶은 경우, 아래의 메소드를 호출하여 NVActivityIndicatorView를 시작합니다.

```swift
activityIndicatorView.startAnimating()
```

4. 로딩 상태를 숨기고 싶은 경우, 아래의 메소드를 호출하여 NVActivityIndicatorView를 중지합니다.

```swift
activityIndicatorView.stopAnimating()
```

## NVActivityIndicatorView 커스터마이징하기

NVActivityIndicatorView는 기본 스타일 이외에도 다양한 커스텀 스타일을 제공합니다. 아래의 예제 코드는 NVActivityIndicatorView를 커스텀하는 방법을 보여줍니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 80, height: 80), type: .custom(nil), color: .red, padding: nil)
activityIndicatorView.backgroundColor = .yellow
activityIndicatorView.startAnimating()
```

## 마무리

NVActivityIndicatorView를 사용하여 앱의 로딩 상태를 사용자에게 시각적으로 알려줄 수 있습니다. 앱이 긴 작업을 수행할 때나 네트워크 요청 등으로 인해 시간이 오래 걸릴 때, 사용자에게 로딩 상태를 보여주어 좋은 사용자 경험을 제공할 수 있습니다.