---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 채팅방 입장 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

채팅 앱에서 사용자가 채팅방에 입장할 때, 로딩 효과를 보여줄 수 있으면 사용자 경험을 향상시킬 수 있습니다. 이번 기사에서는 NVActivityIndicatorView 라이브러리를 사용하여 채팅방 입장 로딩 효과를 구현하는 방법을 알아보겠습니다.

### NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 로딩 애니메이션을 쉽게 구현할 수 있는 라이브러리입니다. 다양한 스타일과 색상의 로딩 애니메이션을 제공하며, 사용하기 쉬운 인터페이스를 제공합니다.

### NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음 코드를 추가하고, 터미널에서 `pod install` 명령을 실행하세요.

```swift
pod 'NVActivityIndicatorView'
```

### 채팅방 입장 로딩 효과 구현하기

먼저, NVActivityIndicatorView 라이브러리를 가져옵니다.

```swift
import NVActivityIndicatorView
```

다음으로, NVActivityIndicatorView의 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballRotateChase, color: .blue, padding: nil)
```

- `frame`: 애니메이션 뷰의 프레임을 설정합니다.
- `type`: 사용할 애니메이션 스타일을 선택합니다.
- `color`: 애니메이션의 색상을 설정합니다.
- `padding`: 애니메이션 내부와 경계 간의 여백을 설정합니다. (Optional)

이제, 로딩 효과를 보여줄 때와 숨길 때 사용할 함수를 구현합니다.

```swift
func showLoadingIndicator() {
    // 채팅방 뷰에 애니메이션 뷰를 추가합니다.
    self.view.addSubview(activityIndicatorView)
    activityIndicatorView.center = self.view.center
    activityIndicatorView.startAnimating()
}

func hideLoadingIndicator() {
    // 애니메이션 뷰를 제거합니다.
    activityIndicatorView.stopAnimating()
    activityIndicatorView.removeFromSuperview()
}
```

- `showLoadingIndicator()`: 채팅방 입장 로딩 효과를 보여줍니다.
- `hideLoadingIndicator()`: 로딩 효과를 숨깁니다.

이제, 사용자가 채팅방에 입장할 때와 나갈 때 로딩 효과를 호출하면 됩니다.

```swift
// 채팅방에 입장할 때
showLoadingIndicator()

// 채팅방에서 나갈 때
hideLoadingIndicator()
```

이렇게 NVActivityIndicatorView를 사용하여 채팅방 입장 로딩 효과를 구현할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하십시오.