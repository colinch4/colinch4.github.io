---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 외관 조절하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 애플리케이션에서 사용할 수 있는 강력한 애니메이션 라이브러리입니다. 이 라이브러리를 사용하여 로딩 인디케이터나 기타 사용자 정의 애니메이션을 만들 수 있습니다.

이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView의 애니메이션 크기와 외관을 조절하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 전에 먼저 Cocoapods를 사용하여 프로젝트에 라이브러리를 설치해야 합니다. Podfile에 다음 줄을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 애니메이션 크기 설정

NVActivityIndicatorView의 애니메이션 크기는 크게 5가지로 설정할 수 있습니다: small, medium, large, xlarge, xxlarge. 기본적으로 medium 크기로 설정되어 있습니다.

애니메이션 크기를 설정하려면 먼저 애니메이션 뷰를 생성해야 합니다. 다음과 같은 코드를 사용하여 애니메이션 뷰를 생성합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
```

여기서 `frame`을 이용하여 애니메이션 뷰의 크기를 설정할 수 있습니다. 해당 프레임에서 애니메이션 뷰를 원하는 크기로 조정할 수 있습니다.

그런 다음 `type` 매개변수를 사용하여 애니메이션의 스타일을 선택할 수 있습니다. 예를 들어 `.ballSpinFadeLoader`는 공 모양의 스핀 애니메이션이고, `.lineScale`은 선 모양의 스케일 애니메이션이 됩니다.

애니메이션 크기를 설정하기 위해 다음 코드를 사용합니다:

```swift
activityIndicatorView.size = CGSize(width: 100, height: 100) // 원하는 크기로 변경
```

위 코드에서 size 속성을 사용하여 애니메이션 크기를 변경할 수 있습니다.

## 애니메이션 외관 설정

NVActivityIndicatorView는 애니메이션의 외관도 커스터마이징할 수 있습니다. 색상, 패딩 및 코너 라운딩을 조절할 수 있습니다.

애니메이션의 색상을 변경하려면 다음과 같은 코드를 사용합니다:

```swift
activityIndicatorView.color = .green // 원하는 색상으로 변경
```

패딩을 조절하여 애니메이션 요소 간에 공간을 추가할 수도 있습니다:

```swift
activityIndicatorView.padding = 20 // 애니메이션 요소 간에 20 포인트의 공간 추가
```

또한 애니메이션 뷰의 모서리를 둥글게 만들고 싶다면 다음 코드를 사용합니다:

```swift
activityIndicatorView.layer.cornerRadius = 10 // 10 포인트의 코너 라운딩
activityIndicatorView.layer.masksToBounds = true // 코너 라운딩을 적용하기 위해 마스킹 사용
```

## 애니메이션 시작 및 중지

애니메이션 뷰를 생성한 후에는 `startAnimating()` 메서드를 호출하여 애니메이션을 시작할 수 있습니다:

```swift
activityIndicatorView.startAnimating()
```

애니메이션을 중지하려면 `stopAnimating()` 메서드를 호출합니다:

```swift
activityIndicatorView.stopAnimating()
```

## 결론

이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView의 애니메이션 크기와 외관을 조절하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하여 애플리케이션에 멋진 로딩 인디케이터를 추가할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하십시오.