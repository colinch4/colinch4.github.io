---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 활용한 애니메이션 효과 추가 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 NVActivityIndicatorView를 활용하여 애니메이션 효과를 추가하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 로딩 상태를 나타내는 애니메이션을 제공하는 오픈 소스 라이브러리입니다. 다양한 스타일의 로딩 애니메이션을 쉽게 구현할 수 있도록 도와줍니다.

## NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 사용하신다면, `Podfile`에 다음과 같은 내용을 추가하세요.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 설치하세요.

```
$ pod install
```

CocoaPods를 사용하지 않는다면, [GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 수동으로 다운로드하여 프로젝트에 추가해야 합니다.

## NVActivityIndicatorView 사용하기

1. 먼저, 애니메이션을 추가할 뷰 컨트롤러에 `import NVActivityIndicatorView`를 추가합니다.

2. NVActivityIndicatorView를 추가할 부분을 지정합니다. 예를 들어, `loadingView`라는 UIView를 생성하여 애니메이션을 추가하고 싶은 위치에 추가합니다.

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .blue, padding: nil)
loadingView.center = view.center
view.addSubview(loadingView)
```

3. 원하는 애니메이션 스타일 및 색상을 선택합니다. 위의 코드에서 `type: .circleStrokeSpin`과 `color: .blue` 부분을 원하는 스타일과 색상으로 변경할 수 있습니다. 다양한 스타일과 색상을 확인하려면 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView#usage)를 참조하세요.

4. 원하는 타이밍에 애니메이션을 시작하거나 중지할 수 있습니다.

```swift
loadingView.startAnimating() // 애니메이션 시작
loadingView.stopAnimating() // 애니메이션 중지
```

## NVActivityIndicatorView 커스터마이징하기

NVActivityIndicatorView는 다양한 커스터마이징 옵션을 제공합니다. 예를 들어, 애니메이션의 크기, 패딩, 애니메이션 속도 등을 변경할 수 있습니다. 자세한 내용은 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView#customization)를 참조하세요.

## 마무리

이렇게 Swift에서 NVActivityIndicatorView를 활용하여 애니메이션 효과를 추가할 수 있습니다. NVActivityIndicatorView를 사용하면 로딩 상태를 시각적으로 표현하는 데 유용하며, 다양한 스타일과 커스터마이징 옵션을 제공하여 필요에 맞게 변경할 수 있습니다.

더 자세한 내용은 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조해보세요.