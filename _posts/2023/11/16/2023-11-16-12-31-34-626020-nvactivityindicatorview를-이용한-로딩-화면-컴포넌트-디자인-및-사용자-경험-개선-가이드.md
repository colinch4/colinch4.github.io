---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 로딩 화면 컴포넌트 디자인 및 사용자 경험 개선 가이드"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

로딩 화면은 앱이나 웹 페이지에서 데이터를 로드하거나 처리하는 동안 사용자에게 진행 중임을 알려주는 중요한 요소입니다. 이 때 NVActivityIndicatorView를 사용하면 쉽게 화려하고 사용자 친화적인 로딩 화면을 구현할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 개발된 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 화면을 손쉽게 만들 수 있도록 도와줍니다. 또한, 커스텀 디자인에 대한 자유도가 높아 다양한 사용자 경험을 제공할 수 있습니다.

## 설치 및 설정

NVActivityIndicatorView를 사용하기 위해 아래와 같이 CocoaPods를 통해 라이브러리를 설치합니다.

```swift
pod 'NVActivityIndicatorView'
```

설치 후, 프로젝트에서 `import NVActivityIndicatorView`를 추가하여 라이브러리를 사용할 수 있습니다.

## 기본 사용법

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위 코드는 기본적으로 NVActivityIndicatorView를 생성하고 화면에 추가한 뒤 애니메이션을 시작하는 예시입니다. 

- `frame`: 로딩 화면의 위치와 크기를 지정합니다.
- `type`: 로딩 화면의 스타일을 선택합니다. 미리 정의된 다양한 스타일이 제공됩니다.
- `color`: 로딩 화면의 색상을 지정합니다.
- `padding`: 로딩 화면 주위에 여백을 추가할 수 있습니다.

### 로딩 화면 제거

로딩이 완료되었을 때 NVActivityIndicatorView를 제거해야 합니다. 아래와 같이 `stopAnimating()` 메서드를 호출하여 로딩 화면을 중지합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 커스텀 디자인

NVActivityIndicatorView는 기본 스타일 외에도 사용자가 직접 디자인을 커스터마이징할 수 있습니다. `NVActivityIndicatorShape` 프로토콜을 채택하고, 각각의 구현체에서 원하는 디자인을 구현할 수 있습니다.

```swift
class CustomActivityIndicator: UIView, NVActivityIndicatorable {
    // 커스텀 디자인 구현
}
```

위와 같이 커스텀한 UIView 클래스를 생성한 뒤 `NVActivityIndicatorable` 프로토콜을 채택하여 원하는 디자인을 구현합니다.

## 결론

NVActivityIndicatorView를 사용하면 다양한 스타일의 로딩 화면을 손쉽게 구현할 수 있습니다. 이를 통해 앱이나 웹 페이지의 사용자 경험을 개선하고 동시에 로딩 시간 동안 사용자에게 진행 상태를 시각적으로 알림으로써 UX를 향상시킬 수 있습니다.

---

참고:
- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 예제](https://github.com/ninjaprox/NVActivityIndicatorView/tree/master/Demo)
- [CocoaPods 공식 홈페이지](https://cocoapods.org/)