---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 화면 전환 중 로딩 인디케이터 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

iOS 앱 개발 중에는 화면 전환 시 로딩 인디케이터를 표시하는 것이 중요합니다. 이를 위해 Swift에서 NVActivityIndicatorView 라이브러리를 사용할 수 있습니다. 이 라이브러리는 많은 종류의 인디케이터를 제공하며, 다양한 옵션을 설정할 수 있습니다.

## NVActivityIndicatorView 설치

먼저, NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Swift Package Manager를 사용하여 설치할 수 있습니다. 

1. Xcode에서 프로젝트를 엽니다.
2. File > Swift Packages > Add Package Dependency...를 선택합니다.
3. 패키지 URL에 "https://github.com/ninjaprox/NVActivityIndicatorView.git"을 입력하고, Next를 클릭합니다.
4. 원하는 버전을 선택하고, Add를 클릭합니다.
5. 필요한 경우, 프로젝트 설정에 라이브러리를 추가합니다.

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 전에, 로딩 화면을 표시할 뷰 컨트롤러에서 NVActivityIndicatorView를 import해야 합니다.

```swift
import NVActivityIndicatorView
```

이제, 로딩 인디케이터를 표시할 때 사용할 NVActivityIndicatorView 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
activityIndicatorView.center = self.view.center
activityIndicatorView.type = .ballScale
activityIndicatorView.color = .blue
```

위 코드에서, activityIndicatorView의 프레임과 위치를 설정하고, 인디케이터의 종류와 색상을 지정합니다. 다양한 옵션과 인디케이터 종류에 대한 자세한 내용은 NVActivityIndicatorView의 [문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.

로딩 인디케이터를 표시하려는 시점에, 아래 코드를 사용하여 인디케이터를 추가하고 애니메이션을 시작합니다.

```swift
self.view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

로딩이 완료된 후에는, 아래 코드를 사용하여 인디케이터를 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

이제, Swift에서 NVActivityIndicatorView를 사용하여 화면 전환 중 로딩 인디케이터를 표시하는 방법을 알게 되었습니다. 이제 이를 활용하여 앱의 사용자 경험을 향상시킬 수 있습니다.