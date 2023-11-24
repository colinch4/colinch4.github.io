---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView의 색상 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 애니메이션 로딩 인디케이터를 만들기 위한 강력한 라이브러리입니다. 이 라이브러리를 사용하면 사용자에게 로딩 중임을 알리는 아름다운 애니메이션을 손쉽게 구현할 수 있습니다.

이번에는 NVActivityIndicatorView에서 인디케이터의 색상을 설정하는 방법에 대해 알아보겠습니다.

먼저, NVActivityIndicatorView를 설치하고 프로젝트에 추가해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

설치를 완료하면 Import 문을 사용하여 NVActivityIndicatorView를 가져옵니다.

```swift
import NVActivityIndicatorView
```

이제 NVActivityIndicatorView를 생성하고 색상을 설정하는 방법을 알아보겠습니다. NVActivityIndicatorView는 다양한 프로퍼티를 제공하므로 선택한 색상으로 인디케이터를 사용자 정의할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100),
                                                    type: .ballRotateChase,
                                                    color: UIColor.red)
```

위의 예제에서는 NVActivityIndicatorView의 프레임을 설정하고, 인디케이터의 유형을 `ballRotateChase`로 설정하였으며, 색상을 빨간색으로 설정하였습니다.

만일 기본 색상보다 더 많은 색상 옵션을 사용하고 싶다면, `color` 매개변수에 `UIColor` 객체 대신 원하는 색을 사용할 수 있습니다. 예를 들어, RGB 값을 사용하여 사용자 지정 색상을 설정할 수 있습니다.

```swift
let customColor = UIColor(red: 0.2, green: 0.8, blue: 0.4, alpha: 1.0)
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100),
                                                    type: .ballRotateChase,
                                                    color: customColor)
```

위의 예제에서는 사용자 정의된 녹색 색상을 사용하여 NVActivityIndicatorView를 생성하였습니다.

이로써, Swift에서 NVActivityIndicatorView의 색상 설정 방법에 대해 알아보았습니다. NVActivityIndicatorView는 다양한 옵션을 제공하므로, 프로젝트 요구에 따라 인디케이터의 색상을 적절하게 설정하여 사용할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)