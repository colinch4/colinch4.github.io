---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 특정 작업 진행 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift에서 NVActivityIndicatorView를 사용하여 특정 작업 진행 상태를 표시하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 iOS 앱에서 로딩 스피너를 구현하기 위해 사용되는 강력한 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS용 로딩 스피너 라이브러리입니다. 이 라이브러리는 다양한 디자인과 애니메이션 효과를 제공하여 사용자에게 작업이 진행 중임을 시각적으로 알려줄 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 Swift 패키지 매니저를 통해 NVActivityIndicatorView를 프로젝트에 추가해야 합니다. 이를 위해 다음 명령을 터미널에서 실행합니다.

```bash
$ swift package init --type executable
```

프로젝트 폴더에 `Package.swift` 파일이 생성되면, 다음과 같이 파일을 열어 의존성으로 NVActivityIndicatorView를 추가합니다.

```swift
// Package.swift

// ...
dependencies: [
.package(url: "https://github.com/ninjaprox/NVActivityIndicatorView.git", from: "5.1.0")
],
targets: [
.target(name: "YourTarget", dependencies: ["NVActivityIndicatorView"]),
]
// ...
```

의존성을 추가하고 나서는 다음 명령으로 패키지를 업데이트합니다.

```bash
$ swift package update
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하여 작업 진행 상태를 표시하려면 다음 단계를 따르세요.

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView의 인스턴스를 만듭니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50),
                                                    type: .ballSpinFadeLoader,
                                                    color: .white,
                                                    padding: nil)
```

여기서 `frame`은 로딩 스피너의 크기와 위치를 정의하고, `type`은 원하는 애니메이션 스타일을 선택합니다. `color`는 스피너의 색상을 정의합니다.

3. NVActivityIndicatorView를 화면에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

4. 작업이 시작될 때 NVActivityIndicatorView를 표시합니다.

```swift
activityIndicatorView.startAnimating()
```

5. 작업이 완료된 후 NVActivityIndicatorView를 숨깁니다.

```swift
activityIndicatorView.stopAnimating()
```

## 마무리

이렇게 Swift에서 NVActivityIndicatorView를 사용하여 특정 작업의 진행 상태를 표시하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 사용자에게 작업이 진행 중임을 명확하게 표시할 수 있으므로 앱의 사용자 경험을 향상시킬 수 있습니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하십시오.