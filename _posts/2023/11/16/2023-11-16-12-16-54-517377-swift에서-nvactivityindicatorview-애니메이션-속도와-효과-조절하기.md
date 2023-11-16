---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 속도와 효과 조절하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱을 개발하다 보면 사용자들에게 시각적인 피드백을 주는 다양한 애니메이션 효과를 구현해야 할 때가 있습니다. NVActivityIndicatorView는 인기있는 Swift 라이브러리로, 다양한 스타일의 로딩 인디케이터를 제공합니다. 이 라이브러리를 사용하여 로딩 인디케이터의 속도와 효과를 조절하는 방법을 알아보겠습니다.

## 1. NVActivityIndicatorView 설치

먼저, NVActivityIndicatorView를 프로젝트에 추가하는 작업부터 진행해야 합니다. NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. 다음과 같이 Podfile에 라이브러리를 추가합니다.

```
platform :ios, '9.0'
use_frameworks!

target 'YourProjectName' do
   pod 'NVActivityIndicatorView'
end
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다.

```
pod install
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해, import 문을 통해 해당 모듈을 가져와야 합니다. 다음과 같이 코드 상단에 import 구문을 추가합니다.

```swift
import NVActivityIndicatorView
```

이제 NVActivityIndicatorView를 생성하여 추가할 UIView에 로딩 인디케이터를 표시할 준비가 되었습니다. UIView를 생성하고, NVActivityIndicatorView 객체를 만들어 해당 뷰에 추가합니다. 이때, NVActivityIndicatorView.Style 열거형을 사용하여 인디케이터의 스타일을 선택할 수 있습니다.

```swift
let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
loadingView.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위 코드에서 `type` 매개변수를 조정하여 로딩 인디케이터의 스타일을 변경할 수 있습니다. NVActivityIndicatorView에서 제공하는 다양한 스타일을 사용해보세요.

## 3. 인디케이터 설정하기

NVActivityIndicatorView는 인디케이터의 크기, 색상, 속도 등 다양한 속성을 조정할 수 있습니다. 원하는 효과를 얻기 위해 이러한 속성들을 조절해보세요.

### 크기 설정하기

```swift
activityIndicatorView.frame = CGRect(x: 0, y: 0, width: 100, height: 100)
```

위 코드에서 `width`와 `height`를 조정하여 인디케이터의 크기를 변경할 수 있습니다.

### 색상 설정하기

```swift
activityIndicatorView.color = .red
```

위 코드에서 `.red`를 다른 적절한 UIColor로 변경하여 인디케이터의 색상을 변경할 수 있습니다.

### 속도 설정하기

```swift
activityIndicatorView.animationDuration = 2.0
```

위 코드에서 `animationDuration` 속성을 조정하여 인디케이터의 애니메이션 속도를 조절할 수 있습니다. 기본적으로 1.0으로 설정되어 있으며, 이 값을 늘리면 인디케이터의 속도가 줄어들고, 반대로 값을 줄이면 속도가 빨라집니다.

## 마치며

이제 Swift에서 NVActivityIndicatorView를 사용하여 로딩 인디케이터의 속도와 효과를 조절하는 방법을 알게 되었습니다. NVActivityIndicatorView를 사용하여 다양한 스타일의 로딩 인디케이터를 구현해보세요. 라이브러리의 문서나 예제를 참고하여 자세한 사용 방법을 익히는 것도 좋은 방법입니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)