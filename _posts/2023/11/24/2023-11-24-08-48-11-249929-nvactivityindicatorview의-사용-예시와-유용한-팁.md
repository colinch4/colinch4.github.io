---
layout: post
title: "[swift] NVActivityIndicatorView의 사용 예시와 유용한 팁"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 활동 표시기(loading indicator) 라이브러리입니다. 이 라이브러리는 사용자에게 애플리케이션이 작업 중임을 시각적으로 표시하기 위해 사용됩니다. 이번 포스트에서는 NVActivityIndicatorView의 사용 예시와 몇 가지 유용한 팁에 대해 알아보겠습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView는 Cocoapods를 통해 설치할 수 있습니다. `Podfile`에 다음 줄을 추가하고 `pod install`을 실행하여 라이브러리를 설치합니다.

```swift
pod 'NVActivityIndicatorView', '~> 5.1'
```

## NVActivityIndicatorView 사용 예시

1. `NVActivityIndicatorView`를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. `NVActivityIndicatorView` 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballClipRotate, color: .red, padding: nil)
```

3. 액티비티 표시기를 화면에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

4. 표시기를 시작하거나 중지합니다.

```swift
activityIndicatorView.startAnimating()
activityIndicatorView.stopAnimating()
```

## 유용한 팁

- 코드에서 액티비티 표시기의 색상을 변경하려면 `color` 파라미터를 수정하십시오.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballClipRotate, color: .blue, padding: nil)
```

- `padding` 파라미터를 사용하여 표시기의 내부 패딩을 조정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballClipRotate, color: .red, padding: 20)
```

- 다양한 타입의 액티비티 표시기를 사용할 수 있습니다. `type` 파라미터를 수정하여 원하는 형태의 표시기를 선택할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .lineScalePulseOut, color: .red, padding: nil)
```

## 결론

NVActivityIndicatorView는 애플리케이션의 작업 상태를 시각적으로 표시하기 위해 유용한 Swift 라이브러리입니다. 위의 예시와 팁을 참고하여 NVActivityIndicatorView를 효과적으로 활용해보세요.

---

참고: [NVActivityIndicatorView 공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)