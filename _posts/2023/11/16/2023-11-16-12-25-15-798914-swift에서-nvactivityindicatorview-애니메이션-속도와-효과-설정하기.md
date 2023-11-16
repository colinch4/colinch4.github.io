---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 속도와 효과 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 앱에서 진행 중인 작업을 시각적으로 표시하는 데 사용되는 애니메이션 라이브러리입니다. 이 라이브러리는 다양한 종류의 애니메이션과 설정 옵션을 제공하며, 이를 사용하여 앱에 독특한 스피닝 로더를 추가할 수 있습니다.

이번 튜토리얼에서는 Swift에서 NVActivityIndicatorView 애니메이션의 속도와 효과를 설정하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 사용하여 프로젝트에 NVActivityIndicatorView를 추가할 수 있습니다. Podfile에 다음 코드를 추가하고, 터미널에서 `pod install`을 실행하면 됩니다.

```swift
pod 'NVActivityIndicatorView'
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView의 속도와 효과를 설정하려면 먼저 해당 뷰를 초기화해야 합니다. 다음은 초기화 예제입니다.

```swift
import UIKit
import NVActivityIndicatorView

class MyViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
        activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballClipRotate, color: .blue, padding: nil)
        
        view.addSubview(activityIndicatorView)
        activityIndicatorView.startAnimating()
    }
}
```

위의 예제에서는 `NVActivityIndicatorView`를 초기화하고, 원하는 타입과 색상을 설정한 후, 해당 뷰를 추가하고 애니메이션을 시작하도록 설정하였습니다.

## 3. 애니메이션 속도와 효과 설정하기

NVActivityIndicatorView는 `type` 프로퍼티를 통해 다양한 애니메이션 효과를 제공합니다. 예를 들어, `.ballPulse`, `.lineScalePulseOut`, `.ballRotate` 등의 다양한 타입을 사용할 수 있습니다. `type` 속성을 원하는 타입으로 설정하여 다양한 애니메이션 효과를 적용할 수 있습니다.

속도와 관련하여 NVActivityIndicatorView는 다음과 같은 속성을 제공합니다.

- `animationDuration`: 애니메이션의 전체 지속 시간을 설정합니다. 기본값은 1.0입니다. 더 작은 값을 설정하면 더 빠른 애니메이션이 생성됩니다.
- `durationRatio`: 각 애니메이션 단계의 지속 시간을 설정합니다. 배열로 값을 설정할 수 있으며, 기본값은 `[1.0]`입니다. 값이 작을수록 해당 애니메이션 단계가 더 빠르게 진행됩니다.

예를 들어, 애니메이션 속도를 더 빠르게 설정하려면 다음과 같이 속성을 변경할 수 있습니다.

```swift
activityIndicatorView.animationDuration = 0.5
activityIndicatorView.durationRatio = [0.8, 0.8, 0.8]
```

위의 예제에서는 `animationDuration` 속성을 0.5로 설정하여 애니메이션의 전체 지속 시간을 줄이고, `durationRatio` 속성을 `[0.8, 0.8, 0.8]`으로 설정하여 각 애니메이션 단계의 지속 시간을 줄였습니다.

NVActivityIndicatorView는 이 외에도 다양한 설정 옵션을 제공하고 있으니, 필요에 따라 공식 문서를 참고하시기 바랍니다.

## 결론

Swift에서 NVActivityIndicatorView 애니메이션의 속도와 효과를 설정하는 방법을 알아보았습니다. NVActivityIndicatorView를 사용하여 앱에 진행 중인 작업을 시각적으로 표시할 때, 애니메이션 속도와 효과를 조절하여 보다 독특하고 직관적인 사용자 경험을 제공할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)