---
layout: post
title: "[swift] NVActivityIndicatorView 커스터마이징"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 앱에서 로딩 인디케이터를 구현하기 위해 사용되는 인기 있는 라이브러리입니다. 이 라이브러리는 많은 다양한 로딩 애니메이션을 제공하며, 기본 값으로 제공되는 스타일을 사용할 수 있습니다. 그러나 때로는 이 스타일을 변경하거나 사용자 정의 로딩 애니메이션을 만들어야 할 수도 있습니다. 이번 블로그에서는 NVActivityIndicatorView를 커스터마이징하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 설치해야 합니다. Swift Package Manager, CocoaPods 또는 Carthage를 사용하여 설치할 수 있습니다. 이번 예시에서는 CocoaPods를 사용하도록 하겠습니다.

```swift
// Podfile

platform :ios, '10.0'
use_frameworks!

target 'YourAppTarget' do
  pod 'NVActivityIndicatorView'
end
```

## 커스텀 스타일 만들기

NVActivityIndicatorView를 사용하려면 먼저 커스텀 스타일을 만들어야 합니다. 커스텀 스타일은 NVActivityIndicatorType과 NVActivityIndicatorColor를 조합하여 정의됩니다. NVActivityIndicatorType은 로딩 애니메이션의 유형을 나타내는 열거형입니다. NVActivityIndicatorColor는 로딩 애니메이션의 색상을 정의하는 UIColor입니다.

```swift
import NVActivityIndicatorView

let myCustomStyle = NVActivityIndicatorType(rawValue: 30)

let myCustomColor = UIColor(red: 0.5, green: 0.8, blue: 0.2, alpha: 1.0)

NVActivityIndicatorView.DEFAULT_TYPE = myCustomStyle
NVActivityIndicatorView.DEFAULT_COLOR = myCustomColor
```

## 커스텀 로딩 애니메이션 만들기

만약 기본 제공되는 로딩 애니메이션 중에서 원하는 스타일이 없다면, 커스텀 로딩 애니메이션을 만들 수도 있습니다. 이를 위해서는 NVActivityIndicatorAnimationDelegate를 채택하여 커스텀 로딩 애니메이션 클래스를 만들어야 합니다.

```swift
import NVActivityIndicatorView

class MyCustomAnimation: NSObject, NVActivityIndicatorViewable, NVActivityIndicatorAnimationDelegate {
  func setUpAnimation(in layer: CALayer, size: CGSize, color: UIColor) {
    // 애니메이션을 layer에 추가하는 코드 작성
  }
}
```

로딩 애니메이션을 layer에 추가하는 방법은 `setUpAnimation` 메서드 내에 작성해야 합니다. 추가로, `size`와 `color` 매개 변수를 이용하여 원하는 크기와 색상을 사용자가 지정할 수 있습니다.

## 커스텀 로딩 애니메이션 사용하기

마지막으로, 커스텀 로딩 애니메이션을 사용하는 방법입니다. `NVActivityIndicatorView`의 `startAnimating()` 메서드를 호출하여 로딩 애니메이션을 시작할 수 있습니다. 원하는 로딩 애니메이션 스타일과 색상을 지정해주어야 합니다.

```swift
import NVActivityIndicatorView

let customAnimation = MyCustomAnimation(size: CGSize(width: 50, height: 50), color: .green)
NVActivityIndicatorView.DEFAULT_TYPE = .blank
NVActivityIndicatorView.DEFAULT_CUSTOM_STYLE = customAnimation

let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
view.addSubview(activityIndicatorView)

activityIndicatorView.startAnimating()
```

위의 예시에서는 `MyCustomAnimation` 클래스를 사용하여 커스텀 로딩 애니메이션을 만들고, 이를 `NVActivityIndicatorView.DEFAULT_CUSTOM_STYLE`에 할당합니다. 마지막으로, `startAnimating` 메서드를 호출하여 로딩 애니메이션을 시작합니다. 

이제 NVActivityIndicatorView를 커스터마이징하는 방법을 알게 되었습니다. 원하는 스타일과 색상을 가진 로딩 인디케이터를 만들어 앱에 통합해보세요!

---

참고문서:
- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)