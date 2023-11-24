---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 네트워크 요청 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift에서 NVActivityIndicatorView를 사용하여 네트워크 요청 상태를 표시하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 쉽게 사용할 수 있는 간단한 애니메이션 라이브러리입니다.

## 시작하기 전에

먼저, NVActivityIndicatorView를 프로젝트에 추가해야 합니다. 이를 위해 CocoaPods를 사용하겠습니다. Podfile에 다음과 같이 작성합니다.

```ruby
platform :ios, '11.0'
use_frameworks!

target 'YourProjectName' do
    pod 'NVActivityIndicatorView'
end
```

그리고 터미널에서 다음 명령어를 실행하여 CocoaPods를 설치합니다.

```bash
pod install
```

이제 준비가 모두 완료되었습니다. 이제부터 NVActivityIndicatorView를 사용해보겠습니다.

## NVActivityIndicatorView 사용하기

먼저, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

다음으로, NVActivityIndicatorView를 초기화하고 원하는 위치에 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .blue, padding: nil)
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
```

여기서 `type`은 애니메이션 종류를 선택하는데 사용되며, `color`는 애니메이션의 색상을 나타냅니다. 필요에 따라 `frame`과 `padding`을 조정할 수도 있습니다.

이제, 데이터를 가져오기 전에 애니메이션을 시작하고, 가져온 후에 정지시킵니다.

```swift
activityIndicatorView.startAnimating()

// 네트워크 요청 코드 작성

activityIndicatorView.stopAnimating()
```

이렇게 하면 네트워크 요청이 진행되는 동안 애니메이션이 표시됩니다.

## 추가 옵션

NVActivityIndicatorView에는 다양한 추가 옵션들이 있습니다. 몇 가지 예시를 살펴보겠습니다.

```swift
activityIndicatorView.backgroundColor = .white // 배경색 변경
activityIndicatorView.hidesWhenStopped = true // 정지했을 때 숨김 여부
activityIndicatorView.startAnimating(animate: true, completion: {
    // 애니메이션이 시작된 후 실행되는 클로저
})
```

추가 옵션을 사용하여 NVActivityIndicatorView를 보다 세밀하게 커스터마이징할 수 있습니다.

## 결론

이번에는 Swift에서 NVActivityIndicatorView를 사용하여 네트워크 요청 상태를 표시하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 간단하게 사용할 수 있는 애니메이션 라이브러리로, 네트워크 요청을 진행할 때 사용자에게 진행 중임을 시각적으로 알려주는 데 유용합니다.