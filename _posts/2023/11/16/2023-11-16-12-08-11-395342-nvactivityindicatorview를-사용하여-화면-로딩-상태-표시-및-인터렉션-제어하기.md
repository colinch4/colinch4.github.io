---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태 표시 및 인터렉션 제어하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱을 개발할 때 사용자가 데이터를 로딩하는 동안 로딩 상태를 표시하는 것은 중요합니다. NVActivityIndicatorView는 iOS 앱에서 화면 로딩 상태를 더 쉽게 표시할 수 있도록 도와주는 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 로딩 애니메이션을 제공하며, 인터렉션을 제어할 수 있는 강력한 기능을 제공합니다.

## 1. NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 설치해야 합니다. Cocoapods를 사용한다면, Podfile에 다음과 같이 추가해주세요:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드하고 설치하세요.

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해서는 몇 가지 단계를 거쳐야 합니다. 먼저, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

다음으로, 로딩 애니메이션을 표시할 뷰를 생성합니다. 이 뷰는 화면의 어느 곳에든 배치될 수 있습니다. 예를 들어, 화면 중앙에 로딩 뷰를 배치하려면 다음과 같이 코드를 작성할 수 있습니다:

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase)
loadingView.color = .gray
loadingView.center = view.center
view.addSubview(loadingView)
```

위 코드에서 `type` 속성을 통해 로딩 애니메이션의 모양을 선택할 수 있습니다. 또한, `color` 속성을 통해 로딩 애니메이션의 색상을 지정할 수 있습니다.

로딩 상태를 표시하기 위해 로딩 애니메이션을 실행하고 정지시키는 방법은 다음과 같습니다:

```swift
// 로딩 애니메이션 시작
loadingView.startAnimating()

// 로딩 애니메이션 정지
loadingView.stopAnimating()
```

로딩 상태를 표시할 때 다른 인터렉션을 제어하려면 다음과 같이 코드를 작성할 수 있습니다:

```swift
// 로딩 애니메이션 시작
loadingView.startAnimating()

// 인터렉션 제어 예시 - 버튼 비활성화
button.isEnabled = false

// 인터렉션 제어 예시 - 화면 터치 불가능
view.isUserInteractionEnabled = false

// 로딩 애니메이션 정지
loadingView.stopAnimating()

// 인터렉션 제어 예시 - 버튼 활성화
button.isEnabled = true

// 인터렉션 제어 예시 - 화면 터치 가능
view.isUserInteractionEnabled = true
```

위의 예제에서는 로딩 상태를 표시할 때 버튼의 활성화 상태와 화면의 터치 가능 여부를 조정하는 방법을 보여줍니다.

## 3. 결론

NVActivityIndicatorView는 iOS 앱에서 로딩 상태를 표시하고 인터렉션을 제어하기 위한 강력한 도구입니다. 이 라이브러리를 사용하면 앱의 사용자 경험을 개선하고, 사용자에게 데이터 로딩이 진행 중임을 시각적으로 안내할 수 있습니다.

더 많은 정보와 사용 예제는 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조해주세요.