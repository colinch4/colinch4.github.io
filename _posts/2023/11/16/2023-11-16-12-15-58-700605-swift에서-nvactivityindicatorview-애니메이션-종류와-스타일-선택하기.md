---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 종류와 스타일 선택하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

![NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Demo.gif)

NVActivityIndicatorView는 Swift에서 사용할 수 있는 다양한 애니메이션 효과를 제공하는 라이브러리입니다. 이 라이브러리를 사용하면 간단한 코드 몇 줄만으로 애니메이션 효과를 쉽게 구현할 수 있습니다. 이번 포스트에서는 NVActivityIndicatorView의 애니메이션 종류와 스타일을 선택하는 방법에 대해서 알아보겠습니다.

## 애니메이션 종류 선택하기

NVActivityIndicatorView에는 다양한 애니메이션 종류가 제공됩니다. 이 애니메이션 종류를 사용하기 위해서는 먼저 이 라이브러리를 프로젝트에 추가해야 합니다. 다음의 단계를 따라 NVActivityIndicatorView를 프로젝트에 추가합니다.
1. [Cocoapods](https://cocoapods.org)를 사용하여 NVActivityIndicatorView를 설치합니다. `Podfile`에 다음의 라인을 추가하고 `pod install` 명령어를 실행합니다.
```swift
pod 'NVActivityIndicatorView'
```
2. `import NVActivityIndicatorView` 문을 추가하여 NVActivityIndicatorView를 코드에서 사용할 수 있도록 합니다.

애니메이션 종류를 선택하기 위해서는 `NVActivityIndicatorType` 열거형을 사용합니다. `NVActivityIndicatorType`은 다양한 애니메이션 종류를 제공하는데, 예를 들어 `.ballPulse`, `.lineScaleParty`, `.triangleSkewSpin`, 등이 있습니다.

다음은 `NVActivityIndicatorView`를 사용하여 간단한 애니메이션을 구현하는 예시입니다.
```swift
import NVActivityIndicatorView
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100),
                                                                                type: .ballPulse,
                                                                                color: UIColor.red,
                                                                                padding: .none)
        view.addSubview(activityIndicatorView)
        activityIndicatorView.startAnimating()
    }
}
```

## 스타일 선택하기

NVActivityIndicatorView는 다양한 스타일 옵션을 제공합니다. 이 스타일 옵션을 사용하여 애니메이션의 색상, 크기, 패딩 등을 변경할 수 있습니다.

`NVActivityIndicatorView`의 초기화 시에는 다음의 파라미터를 지정해야 합니다.
- `frame`: 애니메이션 뷰의 프레임을 지정합니다.
- `type`: 애니메이션 종류를 지정합니다.
- `color`: 애니메이션의 색상을 지정합니다.
- `padding`: 애니메이션의 패딩을 지정합니다.

이외에도 `NVActivityIndicatorView`는 다양한 프로퍼티와 메서드를 제공하여 더욱 정교한 커스터마이징을 할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100),
                                                   type: .ballPulse,
                                                   color: UIColor.red,
                                                   padding: .none)
```

## 결론

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션 종류와 스타일을 선택하는 방법에 대해서 알아보았습니다. NVActivityIndicatorView는 간단한 코드로 다양한 애니메이션 효과를 구현할 수 있도록 도와줍니다. NVActivityIndicatorView에 대한 더 자세한 내용은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고해주세요.