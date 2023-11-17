---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 활용하기 - 검색 결과 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 NVActivityIndicatorView를 사용하여 검색 결과 로딩 화면을 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱의 로딩 인디케이터를 구현하기 위한 오픈 소스 라이브러리입니다. 다양한 스타일과 색상으로 커스터마이징이 가능하며, 간단한 코드로 로딩 화면을 구현할 수 있습니다.

## NVActivityIndicatorView 설치하기

먼저, Cocoapods를 통해 NVActivityIndicatorView를 설치합니다. `Podfile` 파일에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드하고 프로젝트에 적용합니다.

## NVActivityIndicatorView를 이용한 로딩 화면 구현하기

1. NVActivityIndicatorView를 import 합니다:

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 추가할 뷰를 생성합니다. 예를 들어, 로딩 화면을 표시할 `UIView`를 생성합니다:

```swift
let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 80, height: 80))
loadingView.backgroundColor = UIColor.black.withAlphaComponent(0.6)
loadingView.center = self.view.center
loadingView.clipsToBounds = true
loadingView.layer.cornerRadius = 10
self.view.addSubview(loadingView)
```

3. NVActivityIndicatorView를 생성하고 설정합니다. 예를 들어, 크기와 색상을 지정합니다:

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .circleStrokeSpin, color: .white, padding: nil)
indicatorView.center = CGPoint(x: loadingView.bounds.width / 2, y: loadingView.bounds.height / 2)
loadingView.addSubview(indicatorView)
```

4. NVActivityIndicatorView를 시작하고 중지합니다:

```swift
indicatorView.startAnimating() // 로딩 시작
indicatorView.stopAnimating() // 로딩 중지
```

5. 필요에 따라 로딩 화면을 표시하거나 숨깁니다:

```swift
loadingView.isHidden = false // 로딩 화면 숨기지 않음
loadingView.isHidden = true // 로딩 화면 숨김
```

## 결론

이제 Swift에서 NVActivityIndicatorView를 사용하여 검색 결과 로딩 화면을 구현하는 방법을 알아보았습니다. NVActivityIndicatorView는 간편한 코드와 다양한 스타일로 로딩 화면을 구현하는 데 도움이 될 것입니다.

더 많은 옵션과 사용법을 알고 싶다면 NVActivityIndicatorView의 공식 문서를 참조하세요.

- [NVActivityIndicatorView Github](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md)