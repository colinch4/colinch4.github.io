---
layout: post
title: "[swift] Swift 프로젝트에 NVActivityIndicatorView 라이브러리 추가하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift 프로젝트에 NVActivityIndicatorView 라이브러리를 추가하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 로딩 인디케이터를 사용하기 위한 유용한 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 로딩 인디케이터 라이브러리로, 다양한 스타일의 로딩 애니메이션을 제공합니다. 간단한 코드로 로딩 인디케이터를 생성하고 커스터마이즈할 수 있습니다.

## 라이브러리 추가하기

1. 프로젝트에 NVActivityIndicatorView를 추가하기 위해 CocoaPods를 사용하겠습니다. 먼저 Terminal을 열고 프로젝트 폴더로 이동합니다.

2. `Podfile`을 만듭니다. 프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
pod init
```

3. `Podfile`을 열고 아래 코드를 추가합니다.

```swift
# Uncomment the next line to define a global platform for your project
# platform :ios, '9.0'

target 'YourProjectName' do
  # Comment the next line if you're not using Swift and don't want to use dynamic frameworks
  use_frameworks!

  # Pods for YourProjectName
  pod 'NVActivityIndicatorView'
end
```

4. Terminal에서 다음 명령어를 실행하여 라이브러리를 설치합니다.

```bash
pod install
```

5. 설치가 완료되면 `.xcworkspace` 파일을 열어 Xcode를 실행합니다.

6. 프로젝트 내에서 `import NVActivityIndicatorView` 문을 추가하여 NVActivityIndicatorView를 사용할 준비가 되었습니다.

```swift
import NVActivityIndicatorView
```

## 사용법

NVActivityIndicatorView의 사용법은 다음과 같습니다.

```swift
// 인디케이터 생성
let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
let activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballScaleRippleMultiple, color: .blue, padding: 0)

// 화면에 인디케이터 추가
view.addSubview(activityIndicatorView)

// 인디케이터 시작
activityIndicatorView.startAnimating()

// 인디케이터 중지
activityIndicatorView.stopAnimating()
```

위의 코드에서 `type` 매개변수는 로딩 인디케이터의 스타일을 설정하고, `color` 매개변수는 인디케이터의 색상을 설정합니다. `startAnimating()` 함수를 호출하여 인디케이터를 시작하고, `stopAnimating()` 함수를 호출하여 인디케이터를 중지할 수 있습니다.

## 마무리

이제 Swift 프로젝트에 NVActivityIndicatorView 라이브러리를 추가하고 사용하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하여 앱에 멋진 로딩 인디케이터를 추가해보세요!