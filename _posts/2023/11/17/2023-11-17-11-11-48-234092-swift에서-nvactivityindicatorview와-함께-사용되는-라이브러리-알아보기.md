---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용되는 라이브러리 알아보기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 UI에 로딩 인디케이터를 추가하려는 경우, NVActivityIndicatorView는 훌륭한 옵션입니다. 이 글에서는 Swift에서 NVActivityIndicatorView를 사용하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 활성화 인디케이터를 구현하기 위한 Swift 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 간편하게 사용할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 Cocoapods를 통해 라이브러리를 설치해야 합니다. 아래의 단계를 따라 진행해보세요.

1. `Podfile`을 프로젝트 폴더에 생성합니다.
2. `Podfile` 안에 아래의 코드를 추가합니다.
```
platform :ios, '13.0'
use_frameworks!

target 'YourProjectName' do
    pod 'NVActivityIndicatorView'
end
```
3. 터미널을 열고 프로젝트 폴더로 이동한 뒤, `pod install` 명령을 실행합니다.
4. 설치가 완료되면 Xcode에서 생성된 `.xcworkspace` 파일을 열어 사용을 시작할 수 있습니다.

## NVActivityIndicatorView 사용하기

1. Xcode에서 원하는 뷰 컨트롤러를 선택합니다.
2. 뷰 컨트롤러 상단에 아래의 import 코드를 추가합니다.
```swift
import NVActivityIndicatorView
```
3. 로딩 인디케이터를 표시할 때 사용할 `NVActivityIndicatorView` 인스턴스를 선언합니다.
```swift
var activityIndicatorView: NVActivityIndicatorView!
```
4. 인스턴스를 초기화하고 위치와 스타일을 설정합니다.
```swift
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScale, color: .blue, padding: nil)
```
5. 원하는 시점에 로딩 인디케이터를 화면에 추가하고 시작합니다.
```swift
activityIndicatorView.startAnimating()
view.addSubview(activityIndicatorView)
```
6. 작업이 완료되면 로딩 인디케이터를 제거합니다.
```swift
activityIndicatorView.stopAnimating()
```

## 사용 가능한 스타일

NVActivityIndicatorView는 다양한 스타일의 로딩 인디케이터를 제공합니다. 위의 코드에서 `.ballScale` 스타일을 사용했지만, 다른 스타일을 사용할 수도 있습니다. 자세한 스타일에 대해서는 [NVActivityIndicatorView의 공식 GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.

## 요약

이 글에서는 Swift에서 NVActivityIndicatorView와 함께 사용되는 라이브러리에 대해 알아보았습니다. NVActivityIndicatorView를 사용하여 쉽게 로딩 인디케이터를 구현할 수 있으며, 다양한 스타일을 선택할 수 있습니다. 자세한 내용은 NVActivityIndicatorView의 공식 문서를 참고하세요.