---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 특정 작업 진행 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift 프로그래밍 언어에서 NVActivityIndicatorView 라이브러리를 사용하여 특정 작업의 진행 상태를 표시하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 로딩 상태를 표시하기 위한 라이브러리입니다. 다양한 스타일과 크기의 로딩 애니메이션을 제공하므로 작업 진행 중에 사용자에게 진행 상황을 시각적으로 보여줄 수 있습니다.

## NVActivityIndicatorView 설치하기

우선, NVActivityIndicatorView를 설치해야합니다. Swift Package Manager를 통해 라이브러리를 추가할 수 있으며, Xcode에서 다음 단계를 따르면 됩니다.

1. Xcode를 열고 프로젝트를 선택합니다.
2. 상단 메뉴에서 `File`을 선택한 후 `Swift Packages`와 `Add Package Dependency`를 차례로 선택합니다.
3. 팝업창에서 `https://github.com/ninjaprox/NVActivityIndicatorView.git`을 입력하고 `Next`를 클릭합니다.
4. 버전을 선택하고 `Next`를 클릭합니다.
5. `NVActivityIndicatorView`를 체크하고 `Finish`를 클릭합니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 상태를 표시할 뷰를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. 로딩 상태 표시할 뷰의 스타일과 색상을 설정합니다.

```swift
activityIndicatorView.type = .ballSpinFadeLoader
activityIndicatorView.color = .red
```

4. 로딩 상태를 표시할 위치와 크기를 설정합니다.

```swift
activityIndicatorView.center = view.center
activityIndicatorView.frame.size = CGSize(width: 50, height: 50)
```

5. 로딩 상태를 표시하고 감추기 위해 다음 메서드를 사용합니다.

```swift
// 로딩 상태 표시
activityIndicatorView.startAnimating()

// 로딩 상태 감춤
activityIndicatorView.stopAnimating()
```

6. 로딩 상태 표시할 뷰를 현재 뷰 계층에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

## 요약

이제 Swift에서 NVActivityIndicatorView를 사용하여 특정 작업의 진행 상태를 표시하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 설치하고 사용하기 위해 필요한 단계를 소개했으며, 로딩 상태 표시를 위한 뷰를 생성하고 설정하는 방법도 알아보았습니다. 이를 참고하여 작업 진행 상태 표시 기능을 손쉽게 구현해보세요!

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)