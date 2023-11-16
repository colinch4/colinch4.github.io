---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 위치 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

`NVActivityIndicatorView`는 Swift에서 사용할 수 있는 애니메이션 뷰 라이브러리입니다. 이 라이브러리는 다양한 종류의 로딩 인디케이터를 제공하여 앱에서 사용자에게 진행 중인 작업을 시각적으로 표시할 수 있습니다.

이번에는 `NVActivityIndicatorView`를 사용하여 애니메이션의 크기와 위치를 설정하는 방법을 알아보겠습니다.

## 1. NVActivityIndicatorView 설치하기
먼저, `NVActivityIndicatorView` 라이브러리를 프로젝트에 설치해야합니다. `CocoaPods`를 사용하는 경우, `Podfile`에 다음과 같이 라이브러리를 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

설치가 완료되었으면, 프로젝트에서 `import NVActivityIndicatorView` 문을 추가합니다.

## 2. NVActivityIndicatorView 애니메이션 추가하기
`NVActivityIndicatorView`의 인스턴스를 생성하여 애니메이션을 추가해야합니다. 해당 인스턴스를 뷰에 추가하여 애니메이션을 표시할 수 있습니다. 

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
self.view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위의 코드에서는 크기와 위치를 설정하기 위해 `CGRect`를 사용하였습니다. 여기서 type은 애니메이션의 스타일을 나타내며, color는 애니메이션의 색상을 설정합니다. 

## 3. NVActivityIndicatorView 크기와 위치 설정하기
`NVActivityIndicatorView`의 크기와 위치를 변경하기 위해서는 `frame` 속성을 사용합니다. `frame`은 애니메이션의 위치와 크기를 나타내는 `CGRect` 값입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 100, y: 200, width: 100, height: 100), type: .ballSpinFadeLoader, color: .blue, padding: nil)
```

위의 코드에서는 애니메이션의 위치를 x: 100, y: 200으로 설정하고, 크기를 `width: 100, height: 100`으로 설정하였습니다. 필요한 경우, 값을 조정하여 원하는 크기와 위치로 애니메이션을 배치할 수 있습니다.

## 4. NVActivityIndicatorView 애니메이션 시작하기
애니메이션을 시작하려면 `startAnimating()`을 호출하여 애니메이션을 활성화합니다.

```swift
activityIndicatorView.startAnimating()
```

애니메이션이 활성화되면, 사용자에게 로딩 인디케이터가 표시되며 작업이 진행 중임을 알립니다.

## 5. NVActivityIndicatorView 애니메이션 정지하기
애니메이션을 정지하려면 `stopAnimating()`을 호출하여 애니메이션을 비활성화합니다.

```swift
activityIndicatorView.stopAnimating()
```

애니메이션이 비활성화되면, 로딩 인디케이터가 사라지고 작업이 완료되었음을 나타냅니다.

## 참고 자료
- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView Documentation](https://ninjaprox.github.io/NVActivityIndicatorView/)

이제, 앱의 로딩 상태를 시각적으로 표시하려면 `NVActivityIndicatorView`를 사용하여 애니메이션의 크기와 위치를 설정할 수 있습니다.