---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 활용한 게임 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift에서 NVActivityIndicatorView를 사용하여 게임 로딩 화면을 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 많은 종류의 로딩 인디케이터 스타일을 제공하며, 간단하게 사용할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods를 사용하여 프로젝트에 라이브러리를 추가해야 합니다.

1. 터미널을 열고 프로젝트 폴더로 이동합니다.
2. Podfile을 생성하고 다음 내용을 추가한 후 저장합니다.

```ruby
platform :ios, '11.0'
use_frameworks!

target 'YourProjectName' do
    pod 'NVActivityIndicatorView', '~> 5.0.0'
end
```

3. 다시 터미널로 돌아가서 `pod install` 명령어를 실행합니다.
4. 설치가 완료되면 `.xcworkspace` 파일을 열어서 프로젝트를 실행합니다.

## 게임 로딩 화면 구현하기

1. 먼저 NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 원하는 위치에 NVActivityIndicatorView를 추가합니다. 보통은 ViewController의 `viewDidLoad` 메서드 내부에서 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .white, padding: nil)
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위의 코드에서는 원하는 위치(x: 0, y: 0)에 크기가 50x50인 NVActivityIndicatorView를 추가하고, `.ballRotateChase` 스타일로 표시하며, 색상은 흰색으로 설정되어 있습니다.

3. 작업이 완료되면 NVActivityIndicatorView를 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

위의 코드는 작업이 완료되었을 때 NVActivityIndicatorView를 제거하는 코드입니다.

## 다양한 스타일 사용하기

NVActivityIndicatorView는 다양한 스타일을 제공합니다. 위의 예시에서 사용한 `.ballRotateChase` 스타일 외에도 다음과 같은 스타일을 사용할 수 있습니다.

- `.ballPulse`
- `.lineSpinFade`
- `.orbit`
- `.audioEqualizer`

사용할 스타일에 따라서 인스턴스를 생성할 때 type 매개변수를 변경하여 사용하면 됩니다.

## 결론

Swift에서 NVActivityIndicatorView를 사용하여 게임 로딩 화면을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 간편하게 로딩 인디케이터를 추가할 수 있어서 많은 iOS 앱 프로젝트에서 사용되는 인기 있는 라이브러리입니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.