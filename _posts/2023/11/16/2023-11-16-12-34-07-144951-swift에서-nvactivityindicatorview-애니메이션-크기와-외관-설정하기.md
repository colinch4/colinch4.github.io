---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 외관 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 미리 만들어진 애니메이션 라이브러리입니다. 이 라이브러리를 사용하여 간단하게 로딩 애니메이션을 구현할 수 있습니다. 이번 글에서는 NVActivityIndicatorView의 애니메이션 크기와 외관을 설정하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 Cocoapods를 통해 해당 라이브러리를 설치해야 합니다. 아래의 명령어를 사용하여 Cocoapods를 설치합니다.

```shell
$ sudo gem install cocoapods
```

그리고 프로젝트 디렉토리에 있는 `Podfile` 파일에 다음과 같이 NVActivityIndicatorView를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

변경된 `Podfile`을 저장한 후, 아래의 명령어를 사용하여 라이브러리를 설치합니다.

```shell
$ pod install
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 먼저 `import NVActivityIndicatorView`를 통해 해당 모듈을 import 해줍니다. 그리고 애니메이션을 표현할 뷰를 만들고, 해당 뷰에 NVActivityIndicatorView를 추가해줍니다. 아래의 코드를 참고해보세요.

```swift
import NVActivityIndicatorView

let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: 0)

loadingView.startAnimating()

// 뷰에 추가
view.addSubview(loadingView)
```

위의 코드에서 `frame`은 애니메이션 뷰의 위치와 크기를 설정하는 속성입니다. `type`은 원하는 애니메이션 스타일을 선택하는 속성으로, 여러 다른 스타일이 제공됩니다. `color`는 애니메이션의 색상을 선택하는 속성이며, `padding`은 애니메이션 내부와 애니메이션 뷰 사이의 여백을 설정하는 속성입니다.

## 3. 크기와 외관 설정하기

NVActivityIndicatorView는 다양한 크기와 외관을 설정할 수 있습니다. 아래의 코드를 참고해보세요.

```swift
// NVActivityIndicatorView 인스턴스 생성
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: 0)

// 크기 설정
loadingView.frame = CGRect(x: 0, y: 0, width: 100, height: 100)

// 코너 라운딩 설정
loadingView.layer.cornerRadius = 10
loadingView.layer.masksToBounds = true

// 배경색 설정
loadingView.backgroundColor = .gray

// 외곽선 설정
loadingView.layer.borderWidth = 1
loadingView.layer.borderColor = UIColor.black.cgColor
```

위의 코드에서 `frame` 속성을 통해 애니메이션 크기를 설정할 수 있습니다. 또한 `layer.cornerRadius`와 `layer.masksToBounds` 속성을 사용하여 애니메이션 뷰의 코너를 둥글게 만들 수 있습니다. `backgroundColor`를 사용하여 애니메이션 뷰의 배경색을 설정하고, `layer.borderWidth`와 `layer.borderColor` 속성을 사용하여 애니메이션 뷰의 외곽선을 설정할 수 있습니다.

이제 여러분은 NVActivityIndicatorView를 Swift 프로젝트에서 사용하고, 애니메이션 크기와 외관을 설정하는 방법을 알게 되었습니다. 더 많은 설정 옵션과 스타일을 살펴보려면 [NVActivityIndicatorView GitHub repository](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.