---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 라이브러리 사용하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift에서 활동 표시를 위한 NVActivityIndicatorView 라이브러리를 사용하는 방법을 알아보겠습니다. NVActivityIndicatorView는 로딩, 로딩 오류 등 다양한 상태를 나타내는 활동 표시를 제공하는 라이브러리입니다.

## NVActivityIndicatorView 설치하기

먼저, CocoaPods를 사용하여 NVActivityIndicatorView를 프로젝트에 설치해야 합니다. 터미널을 열고 프로젝트 폴더로 이동한 다음, `Podfile`을 엽니다. 만약 `Podfile`이 없다면, 프로젝트 폴더에서 `pod init` 명령어를 실행하여 생성할 수 있습니다.

```ruby
platform :ios, '10.0'

target 'YourProjectName' do
    use_frameworks!
    pod 'NVActivityIndicatorView'
end
```

위와 같이 Podfile에 `NVActivityIndicatorView`를 추가한 후 저장합니다. 그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 활동 표시를 표시할 뷰를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScaleRippleMultiple, color: .blue, padding: nil)
```

위 코드는 활동 표시기의 사이즈, 스타일, 색상 및 패딩을 설정하는 예시입니다. 적절한 값으로 수정해야 합니다.

3. 활동 표시 뷰를 원하는 위치에 추가합니다.

```swift
activityIndicatorView.center = self.view.center
self.view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위 코드는 활동 표시기를 화면 중앙에 위치시킨 후, 애니메이션을 시작합니다. `startAnimating()` 함수 호출을 통해 활동 표시를 시작할 수 있습니다.

4. 활동 표시를 중지할 때는 다음과 같이 코드를 작성합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

`stopAnimating()` 함수 호출을 통해 활동 표시를 중지하고, `removeFromSuperview()` 함수 호출을 통해 뷰에서 제거합니다.

## 결과 확인하기

위와 같이 NVActivityIndicatorView를 사용하면 다양한 활동 표시를 손쉽게 구현할 수 있습니다. 실행하여 결과를 확인하고, 스타일, 색상 등을 필요에 따라 변경하여 원하는 디자인을 구현해보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)