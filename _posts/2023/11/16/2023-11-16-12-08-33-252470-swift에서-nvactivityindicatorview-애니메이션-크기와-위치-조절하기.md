---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 위치 조절하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift에서 NVActivityIndicatorView 라이브러리를 사용하여 애니메이션의 크기와 위치를 조절하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 사용할 수 있는 간단하고 유연한 로딩 애니메이션 라이브러리입니다. 다양한 스타일과 색상으로 구성된 다양한 종류의 로딩 애니메이션을 제공하여 애플리케이션의 사용자 인터페이스를 보다 흥미롭게 만들어줍니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하려면 먼저 CocoaPods를 사용하여 프로젝트에 라이브러리를 추가해야 합니다. `Podfile`에 다음과 같이 NVActivityIndicatorView를 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령을 실행하여 라이브러리를 설치합니다.

```bash
$ pod install
```

## 애니메이션 크기 조절하기

NVActivityIndicatorView의 애니메이션 크기를 조절하려면 먼저 `NVActivityIndicatorView.DEFAULT_BLOCKER_SIZE` 상수를 사용하여 기본 크기를 설정할 수 있습니다. 다음은 크기를 설정하는 예시입니다.

```swift
NVActivityIndicatorView.DEFAULT_BLOCKER_SIZE = CGSize(width: 100, height: 100)
```

위의 코드는 애니메이션의 크기를 100x100으로 설정합니다. 원하는 크기로 값을 변경하여 사용하세요.

## 애니메이션 위치 조절하기

NVActivityIndicatorView의 애니메이션 위치를 조절하려면, 뷰 컨트롤러에서 NVActivityIndicatorView를 추가하고 원하는 위치로 조절해야 합니다. 다음은 예시 코드입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
```

위의 코드는 애니메이션을 뷰의 가운데에 위치시킵니다. `CGRect`를 사용하여 원하는 크기와 위치를 설정하고 `center` 속성을 사용하여 위치를 조절하세요.

## 마무리

이제 Swift에서 NVActivityIndicatorView의 애니메이션 크기와 위치를 조절하는 방법에 대해 알아보았습니다. 사용자의 필요에 따라 크기와 위치를 조절하여 애플리케이션에 맞는 로딩 애니메이션을 구현해보세요.

더 많은 정보를 원한다면 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 확인해보세요.