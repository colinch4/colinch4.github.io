---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView로 커스텀 애니메이션 만들기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 앱에서 스피너 애니메이션을 쉽게 추가할 수 있는 오픈 소스 라이브러리입니다. NVActivityIndicatorView를 사용하여 커스텀 애니메이션을 만드는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 가져오기

먼저, NVActivityIndicatorView를 프로젝트에 추가해야 합니다. 가장 간단한 방법은 CocoaPods를 사용하는 것입니다. `Podfile`로 가서 다음 라인을 추가하고 `pod install`을 실행합니다.

```ruby
pod 'NVActivityIndicatorView'
```

## 커스텀 애니메이션 만들기

NVActivityIndicatorView는 다양한 스타일의 애니메이션을 제공합니다. 기본적으로 제공되는 스타일 외에도 나만의 커스텀 애니메이션을 만들 수 있습니다.

1. 먼저, `NVActivityIndicatorViewable` 프로토콜을 채택한 뷰 컨트롤러에 extension을 만듭니다.

```swift
extension ViewController: NVActivityIndicatorViewable {

}
```

2. 커스텀 애니메이션을 만들기 위해 `startAnimating()` 메서드를 구현합니다.

```swift
func startAnimating() {
    let activityData = ActivityData(type: .custom, color: .red, padding: 10)
    NVActivityIndicatorPresenter.sharedInstance.startAnimating(activityData)
}
```

3. `startAnimating()` 메서드를 호출하여 애니메이션을 시작합니다.

```swift
self.startAnimating()
```

코드의 `type` 파라미터를 `.custom`로 설정하여 커스텀 애니메이션을 사용하고, `color` 파라미터로 원하는 색상을 선택할 수 있습니다. `padding` 파라미터는 애니메이션의 여백을 설정합니다.

이제 커스텀 애니메이션을 만들어 사용할 수 있습니다!

## 참고 자료

- [NVActivityIndicatorView 공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)