---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 간단한 애니메이션 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

애니메이션 효과를 사용하여 iOS 앱을 더욱 동적이고 흥미로운 디자인으로 만들 수 있습니다. NVActivityIndicatorView는 iOS 앱에 다양한 형태의 인디케이터를 쉽게 추가할 수 있는 라이브러리입니다. 이번 블로그 포스트에서는 NVActivityIndicatorView를 사용하여 간단한 애니메이션 효과를 추가하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Objective-C와 Swift를 지원하는 iOS용 인디케이터 뷰입니다. 다양한 스타일을 제공하며, 인디케이터의 색상, 크기 및 애니메이션 속도를 사용자 지정할 수 있습니다. 또한, 인디케이터가 로딩 중임을 나타내는 기능도 제공합니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 Cocoapods를 사용하여 프로젝트에 라이브러리를 추가해야 합니다. 다음 명령어를 사용하여 Cocoapods를 설치합니다.

```shell
$ sudo gem install cocoapods
```

그리고 Podfile을 생성하여 아래와 같이 NVActivityIndicatorView를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 다음 명령어를 사용하여 라이브러리를 설치합니다.

```shell
$ pod install
```

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 인디케이터의 프레임을 설정합니다. 알맞은 크기와 위치로 조절합니다.

```swift
let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
```

3. NVActivityIndicatorView 인스턴스를 생성하고 프레임을 설정합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: frame)
```

4. 인디케이터의 스타일을 설정합니다.

```swift
activityIndicatorView.type = .ballSpinFadeLoader
```

5. 인디케이터의 색상을 설정합니다.

```swift
activityIndicatorView.color = UIColor.red
```

6. 뷰에 인디케이터를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

7. 인디케이터를 실행시킵니다.

```swift
activityIndicatorView.startAnimating()
```

8. 인디케이터를 중지시킵니다.

```swift
activityIndicatorView.stopAnimating()
```

9. 뷰에서 인디케이터를 제거합니다.

```swift
activityIndicatorView.removeFromSuperview()
```

## 참고자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)

이제 NVActivityIndicatorView를 사용하여 간단한 애니메이션 효과를 추가하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 앱에 더욱 동적이고 사용자 친화적인 인디케이터를 쉽게 추가할 수 있습니다. 추가적인 기능과 사용법은 NVActivityIndicatorView의 공식 문서를 참고하시기 바랍니다.