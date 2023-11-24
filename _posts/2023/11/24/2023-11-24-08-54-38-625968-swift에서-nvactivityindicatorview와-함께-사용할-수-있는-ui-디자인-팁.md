---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 UI 디자인 팁"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서 NVActivityIndicatorView는 활발한로딩 인디케이터를 구현하는 데 사용되는 유용한 오픈 소스 라이브러리입니다. 이 라이브러리를 사용하면 앱에 매력적인 로딩 효과를 추가할 수 있습니다. 하지만 로딩 인디케이터를 사용할 때 몇 가지 디자인 팁을 따르면 사용자 경험을 향상시킬 수 있습니다.

## 1. 로딩 인디케이터의 크기 조정하기

NVActivityIndicatorView는 다양한 크기의 인디케이터를 제공합니다. 기본적으로 인디케이터의 크기는 화면의 중앙에 적절히 맞춰져 있지만, 때로는 더 작은 인디케이터를 사용하는 것이 적합할 수도 있습니다. 

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
activityIndicatorView.type = .ballSpinFadeLoader
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위의 예제에서는 인디케이터의 크기를 40x40으로 설정하고 있습니다. 필요에 따라 이 값을 조정하여 로딩 인디케이터의 크기를 변경할 수 있습니다.

## 2. 커스텀 로딩 인디케이터 디자인 사용하기

NVActivityIndicatorView는 다양한 유형의 로딩 인디케이터를 제공하지만, 때로는 앱의 디자인과 일치하는 커스텀 디자인을 사용하고 싶을 수도 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .circleStrokeSpin, color: .red, padding: nil)
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위의 예제에서는 `.circleStrokeSpin` 유형의 인디케이터를 사용하고 색상을 빨간색으로 설정하였습니다. 필요에 따라 유형과 색상을 조정하여 자신만의 커스텀 디자인을 만들어 사용할 수 있습니다.

## 3. 로딩 인디케이터의 배경색 조정하기

로딩 인디케이터의 배경색을 조정하여 앱의 전반적인 디자인에 맞출 수 있습니다. 기본적으로 배경색은 투명으로 설정되어 있지만, 필요에 따라 배경색을 변경할 수도 있습니다.

```swift
activityIndicatorView.backgroundColor = .white
activityIndicatorView.backgroundPadding = UIEdgeInsets(top: 5, left: 5, bottom: 5, right: 5)
```

위의 예제에서는 인디케이터의 배경색을 흰색으로 설정하고 있습니다. 필요에 따라 다른 색상으로 변경하고 패딩을 추가하여 인디케이터와 배경 사이에 여백을 설정할 수 있습니다.

## 4. 로딩 인디케이터의 위치 조정하기

NVActivityIndicatorView는 기본적으로 화면의 중앙에 위치하도록 설정되어 있지만, 필요에 따라 다른 위치에 인디케이터를 배치할 수도 있습니다.

```swift
let customFrame = CGRect(x: 100, y: 200, width: 40, height: 40)
let activityIndicatorView = NVActivityIndicatorView(frame: customFrame)
activityIndicatorView.center = CGPoint(x: customFrame.midX, y: customFrame.midY)
```

위의 예제에서는 인디케이터를 화면의 (100, 200) 좌표에 배치하고 있습니다. 필요에 따라 다른 위치에 인디케이터를 배치하여 앱의 디자인에 맞출 수 있습니다.

위의 팁들을 따르면 Swift에서 NVActivityIndicatorView를 사용하는 동안 로딩 인디케이터를 더 잘 활용할 수 있으며, 앱의 사용자 경험을 향상시킬 수 있습니다. 자세한 내용은 [NVActivityIndicatorView 공식 GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하십시오.