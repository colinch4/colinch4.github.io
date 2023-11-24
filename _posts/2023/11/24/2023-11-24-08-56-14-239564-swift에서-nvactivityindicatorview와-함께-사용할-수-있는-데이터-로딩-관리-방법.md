---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 데이터 로딩 관리 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift로 작성된 iOS 앱에서 사용할 수 있는 강력한 로딩 인디케이터 라이브러리입니다. 데이터를 로딩하는 동안 사용자에게 진행 상황을 시각적으로 표시할 수 있습니다. 이 글에서는 Swift에서 NVActivityIndicatorView를 사용하여 데이터 로딩을 관리하는 방법에 대해 소개하겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용자에게 로딩 중임을 시각적으로 알려주는 인디케이터입니다. 다양한 스타일과 컬러로 설정할 수 있으며, 기본적으로 제공되는 스타일 외에도 사용자 정의 스타일을 만들 수도 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 CocoaPods을 통해 설치할 수 있습니다. `Podfile`에 다음과 같이 라이브러리를 추가해 주세요.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치해 주세요.

```shell
pod install
```

## NVActivityIndicatorView 사용하기

### 1. NVActivityIndicatorView 인스턴스 생성하기

먼저, NVActivityIndicatorView를 사용하기 위해 인스턴스를 생성해야 합니다. 보통은 UIViewController나 UIView의 일부로 생성되며, 아래와 같은 코드로 생성할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

### 2. NVActivityIndicatorView 설정하기

생성된 NVActivityIndicatorView 인스턴스를 화면에 추가하고, 스타일과 컬러를 설정해야 합니다. 아래 예시 코드는 NVActivityIndicatorView를 화면 중앙에 표시하고, 스타일을 .ballPulse 스타일로 설정한 예시입니다.

```swift
activityIndicatorView.center = view.center
activityIndicatorView.type = .ballPulse
activityIndicatorView.color = UIColor.red
```

### 3. NVActivityIndicatorView 시작 및 중지하기

데이터 로딩이 시작되는 시점에는 인디케이터를 시작하고, 데이터 로딩이 완료되면 중지해야 합니다. 아래 예시 코드는 데이터 로딩 시작 및 완료 시점에 NVActivityIndicatorView를 시작 및 중지하는 방법을 보여줍니다.

```swift
func startLoading() {
    view.addSubview(activityIndicatorView)
    activityIndicatorView.startAnimating()
}

func stopLoading() {
    activityIndicatorView.stopAnimating()
    activityIndicatorView.removeFromSuperview()    
}
```

## 결론

이제 Swift에서 NVActivityIndicatorView를 사용하여 데이터 로딩을 관리하는 방법을 알아보았습니다. NVActivityIndicatorView를 사용하면 사용자에게 진행 상황을 시각적으로 표시하여 더 나은 사용자 경험을 제공할 수 있습니다. 추가적으로 NVActivityIndicatorView에서 제공하는 다양한 설정 옵션들을 살펴보고, 앱에 맞게 사용해 보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md)