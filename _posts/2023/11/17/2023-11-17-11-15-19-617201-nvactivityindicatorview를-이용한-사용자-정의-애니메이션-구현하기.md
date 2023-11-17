---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 정의 애니메이션 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱 개발 중에 사용자에게 액티비티 인디케이터를 보여주는 기능을 구현해야하는 경우가 있습니다. 이때 NVActivityIndicatorView 라이브러리를 사용하면 매우 간편하게 사용자 정의 애니메이션을 구현할 수 있습니다. 이번 블로그에서는 NVActivityIndicatorView를 이용하여 사용자 정의 애니메이션을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS 애니메이션 인디케이터 라이브러리입니다. 이 라이브러리를 사용하면 다양한 스타일과 크기의 인디케이터를 쉽게 구현할 수 있습니다.

NVActivityIndicatorView의 주요 특징은 다음과 같습니다:
- 다양한 스타일의 인디케이터를 제공합니다.
- 크기를 조절하여 다양한 화면에 적용할 수 있습니다.
- 간단한 코드로 사용자 정의 애니메이션을 구현할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 관련 패키지를 설치해야 합니다. CocoaPods를 사용하고 있다면, Podfile에 다음과 같은 내용을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 패키지를 설치합니다:

```bash
pod install
```

CocoaPods를 사용하지 않는다면, 수동으로 해당 라이브러리를 프로젝트에 추가하면 됩니다.

## NVActivityIndicatorView 사용법

1. 프로젝트에서 NVActivityIndicatorView를 import 합니다:

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성하고 원하는 위치에 추가합니다. 예를 들어, 뷰의 중앙에 인디케이터를 추가하고 싶다면 다음과 같이 코드를 작성합니다:

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .red, padding: nil)
indicatorView.center = view.center
view.addSubview(indicatorView)
indicatorView.startAnimating()
```

위 코드에서 type, color, padding 등을 사용자의 선호에 맞게 변경할 수 있습니다. 예를 들어, 인디케이터의 스타일을 변경하려면 `type`을 다른 값으로 설정하면 됩니다.

## 사용자 정의 애니메이션 구현하기

NVActivityIndicatorView는 다양한 스타일을 제공하지만, 사용자가 원하는 애니메이션을 완벽하게 제공해주지는 않습니다. 따라서 사용자 정의 애니메이션을 구현하고 싶다면, NVActivityIndicatorViewDelegate를 사용하여 직접 구현해야 합니다.

1. NVActivityIndicatorViewDelegate를 구현합니다:

```swift
class ViewController: UIViewController, NVActivityIndicatorViewable {
    //...
}

extension ViewController: NVActivityIndicatorViewable {
    func startAnimating() {
        // 사용자 정의 애니메이션을 시작하는 코드 작성
    }

    func stopAnimating() {
        // 사용자 정의 애니메이션을 종료하는 코드 작성
    }
}
```

2. 사용자 정의 애니메이션을 시작하는 코드와 종료하는 코드를 작성합니다. 이 코드는 사용자의 특정 요구 사항에 따라 달라질 수 있습니다. 예를 들어, 이미지를 사용하여 커스텀 애니메이션을 구현하거나, CALayer의 특정 속성을 조정하여 애니메이션을 만들 수 있습니다.

```swift
func startAnimating() {
    let customAnimationView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50)) // 사용자 정의 애니메이션을 위한 뷰 생성
    view.addSubview(customAnimationView)
    customAnimationView.startAnimating()
}

func stopAnimating() {
    if let customAnimationView = view.subviews.first(where: { $0 is NVActivityIndicatorView }) as? NVActivityIndicatorView {
        customAnimationView.stopAnimating()
    }
}
```

위 코드에서는 `startAnimating()` 메서드 내에서 사용자 정의 애니메이션을 위한 뷰를 생성하고, 화면에 추가한 후 애니메이션을 시작합니다. `stopAnimating()` 메서드에서는 해당 뷰를 찾아서 애니메이션을 종료시킵니다.

## 결론

이번 블로그에서는 NVActivityIndicatorView 라이브러리를 사용하여 사용자 정의 애니메이션을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 다양한 스타일의 애니메이션을 손쉽게 구현할 수 있으며, NVActivityIndicatorViewDelegate를 사용하여 사용자 정의 애니메이션을 만들 수도 있습니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하시기 바랍니다.