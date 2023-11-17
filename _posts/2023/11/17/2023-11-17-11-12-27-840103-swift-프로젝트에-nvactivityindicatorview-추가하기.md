---
layout: post
title: "[swift] Swift 프로젝트에 NVActivityIndicatorView 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이 포스트에서는 Swift 프로젝트에 `NVActivityIndicatorView`를 추가하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

`NVActivityIndicatorView`는 로딩 인디케이터를 만드는 데 사용되는 오픈 소스 프레임워크입니다. 다양한 스타일과 애니메이션을 제공하여 앱에 맞는 로딩 인디케이터를 손쉽게 구현할 수 있습니다.

## Step 1: CocoaPods 설치하기

`NVActivityIndicatorView`를 설치하기 위해 CocoaPods를 사용합니다. CocoaPods를 설치하기 위해 다음 명령어를 터미널에서 실행하세요:

```bash
$ gem install cocoapods
```

## Step 2: Podfile 작성하기

프로젝트 폴더 내에 있는 `Podfile`을 열고 다음과 같이 `NVActivityIndicatorView`를 추가해주세요:

```ruby
platform :ios, '11.0'
use_frameworks!

target 'YourProjectName' do
  pod 'NVActivityIndicatorView'
end
```

프로젝트 이름으로 작성된 부분은 실제 프로젝트의 이름으로 변경해야 합니다.

## Step 3: 의존성 설치하기

터미널에서 프로젝트 폴더로 이동하고 다음 명령어를 실행하여 `NVActivityIndicatorView`를 설치하세요:

```bash
$ pod install
```

## Step 4: 프로젝트에 NVActivityIndicatorView 사용하기

프로젝트의 코드에서 `NVActivityIndicatorView`를 사용할 준비가 되었습니다. 먼저, 로딩 인디케이터를 추가할 뷰 컨트롤러를 열어주세요.

```swift
import NVActivityIndicatorView
```

로딩 인디케이터를 사용할 `UIView`를 생성하고, 원하는 스타일과 애니메이션을 설정하세요. 예를 들어, 다음과 같이 설정할 수 있습니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
```

로딩 인디케이터를 표시할 때는 `startAnimating()` 메서드를 호출하고, 감추고자 할 때는 `stopAnimating()` 메서드를 호출하세요.

```swift
activityIndicatorView.startAnimating()
```

```swift
activityIndicatorView.stopAnimating()
```

## 결론

이제 `NVActivityIndicatorView`를 성공적으로 Swift 프로젝트에 추가하였습니다. 로딩 인디케이터와 함께 앱의 사용자 경험을 향상시킬 수 있습니다.

더 많은 사용 방법은 `NVActivityIndicatorView`의 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

Happy coding!