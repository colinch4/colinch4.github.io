---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하고 인터렉션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱이 데이터를 로딩하는 동안 사용자에게 로딩 상태를 시각적으로 표시하고, 로딩 중에는 사용자의 인터랙션을 제한하는 것은 중요합니다. 이러한 작업을 쉽게 해주는 라이브러리 중 하나인 NVActivityIndicatorView에 대해 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 Swift로 작성된 iOS용 활동 표시기(로딩 인디케이터) 라이브러리입니다. 다양한 스타일과 기능을 제공하며, 앱의 데이터 로딩 상태를 시각적으로 표시하는 데 사용할 수 있습니다.

## 설치하기
NVActivityIndicatorView를 사용하기 위해, 먼저 CocoaPods를 사용하여 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. `Podfile`에 다음과 같은 내용을 추가하고, 터미널에서 `pod install`을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## 사용하기
1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성하고, 원하는 스타일과 크기를 설정합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 40, height: 40),
    type: .ballSpinFadeLoader,
    color: .gray,
    padding: nil
)
```

3. 인디케이터를 화면에 추가하고 중앙에 위치시킵니다.

```swift
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
```

4. 로딩 상태를 표시할 때는 인디케이터를 시작하고, 로딩이 완료되면 중지합니다.

```swift
// 로딩 시작
activityIndicatorView.startAnimating()

// 로딩 완료 후 중지
activityIndicatorView.stopAnimating()
```

5. 로딩 중에 인터랙션을 제한하려면, 사용자 인터랙션을 비활성화하고, 다시 활성화해야 합니다.

```swift
// 인터랙션 제한
UIApplication.shared.beginIgnoringInteractionEvents()

// 인터랙션 활성화
UIApplication.shared.endIgnoringInteractionEvents()
```

NVActivityIndicatorView는 다양한 스타일과 옵션을 제공하여 원하는 대로 로딩 인디케이터를 사용자 정의할 수 있습니다. 자세한 내용은 공식 문서를 참조하시기 바랍니다.

## 결론
NVActivityIndicatorView는 데이터 로딩 상태를 시각적으로 표시하고, 사용자의 인터랙션을 제한하는 데 도움을 주는 훌륭한 라이브러리입니다. 쉽게 설치하고 사용할 수 있으며, 다양한 스타일과 옵션을 통해 사용자 정의할 수 있습니다.