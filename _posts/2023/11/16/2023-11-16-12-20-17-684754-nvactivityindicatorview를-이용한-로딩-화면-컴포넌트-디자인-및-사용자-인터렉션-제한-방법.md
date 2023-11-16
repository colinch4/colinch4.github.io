---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 로딩 화면 컴포넌트 디자인 및 사용자 인터렉션 제한 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

> 본 게시물은 Swift 언어를 기반으로 작성되었습니다.

## 개요
앱 사용 중 사용자에게 긴 기다림 시간 동안 로딩 상태를 보여주는 로딩 화면은 사용자 경험 측면에서 중요합니다. 이러한 로딩 화면을 구현하기 위해 NVActivityIndicatorView 라이브러리를 사용할 수 있습니다. 이 라이브러리는 여러 종류의 로딩 애니메이션을 제공하며 사용이 간편합니다.

이 글에서는 NVActivityIndicatorView를 이용하여 로딩 화면 컴포넌트를 디자인하고, 사용자의 인터랙션을 제한하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 Swift로 작성된 iOS 및 macOS용 로딩 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 로딩 중에 보여줄 수 있는 다양한 스피너 디자인을 쉽게 구현할 수 있습니다.

## 설치
NVActivityIndicatorView를 설치하려면 Swift Package Manager를 사용할 수 있습니다. 다음의 단계를 따라서 설치하세요:

1. Xcode 프로젝트를 엽니다.
2. File > Swift Packages > Add Package Dependency... 메뉴를 선택합니다.
3. "https://github.com/ninjaprox/NVActivityIndicatorView"를 입력하고 Next를 클릭합니다.
4. 원하는 버전을 선택한 후 Add를 클릭합니다.

## 사용법
NVActivityIndicatorView를 사용하려면 다음의 단계를 따라야 합니다:

1. NVActivityIndicatorView를 Import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView의 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballSpinFadeLoader, color: .black, padding: 20)
```

이때 `frame`은 로딩 애니메이션의 크기와 위치를 나타냅니다. `type`은 사용할 로딩 애니메이션의 종류를 선택하는데, 다양한 종류의 로딩 애니메이션을 지원합니다. `color`는 로딩 애니메이션의 색상을 나타내며, `padding`은 로딩 애니메이션과 경계 사이의 여백을 제공합니다.

3. 로딩 화면을 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

4. 로딩 화면을 중지하고 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 사용자 인터랙션 제한 방법
로딩 화면을 표시하는 동안 사용자의 인터랙션을 제한하기 위해 다음의 단계를 따릅니다:

1. 로딩 화면을 추가하기 전에 사용자 인터랙션을 비활성화합니다.

```swift
UIApplication.shared.beginIgnoringInteractionEvents()
```

2. 로딩 화면을 중지하고 제거하는 코드에 사용자 인터랙션을 활성화합니다.

```swift
UIApplication.shared.endIgnoringInteractionEvents()
```

## 마무리
NVActivityIndicatorView를 이용하여 로딩 화면을 구현해보았습니다. 이를 통해 사용자에게 로딩 중임을 알리고, 사용자 인터랙션을 제한하는 기능을 추가할 수 있습니다. 이를 통해 사용자 경험을 향상시킬 수 있습니다. NVActivityIndicatorView의 다양한 옵션을 활용하여 앱에 적합한 로딩 화면을 구성해보세요.

> 참고: [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)