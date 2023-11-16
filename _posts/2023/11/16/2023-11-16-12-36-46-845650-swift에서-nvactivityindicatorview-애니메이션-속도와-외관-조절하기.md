---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 속도와 외관 조절하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션의 속도와 외관을 조절하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 애플리케이션의 로딩 상태를 시각적으로 표현하기 위한 라이브러리입니다. 다양한 애니메이션 스타일을 제공하며, 사용자가 직접적으로 속도와 외관을 조절할 수 있습니다.

## 설치

NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods를 통해 설치해야 합니다. Podfile에 다음의 내용을 추가하고 `pod install` 명령어를 실행하세요.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

아래의 예제 코드는 NVActivityIndicatorView를 사용하여 애니메이션을 보여주는 간단한 방법입니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    var activityIndicator: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 애니메이션 스타일과 크기 설정
        let frame = CGRect(x: 0, y: 0, width: 100, height: 100)
        activityIndicator = NVActivityIndicatorView(frame: frame, type: .ballScaleRippleMultiple, color: .red)

        // 화면에 추가
        view.addSubview(activityIndicator)

        // 애니메이션 시작
        activityIndicator.startAnimating()
    }

    // 화면이 사라질 때 애니메이션을 중지시킴
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)

        activityIndicator.stopAnimating()
    }
}
```

## 애니메이션 속도 조절

NVActivityIndicatorView의 애니메이션 속도는 `animationDuration` 프로퍼티를 통해 조절할 수 있습니다. 이 값은 애니메이션 한 사이클을 완료하는 데 걸리는 시간을 의미합니다. 기본값은 1.0으로 설정되어 있으며, 0.0으로 설정하면 애니메이션은 멈추게 됩니다.

```swift
activityIndicator.animationDuration = 0.5 // 애니메이션 속도를 반으로 빠르게 설정
```

## 애니메이션 외관 조절

NVActivityIndicatorView의 애니메이션 외관은 `color`, `backgroundColor`, `backgroundPadding`, `lineWidth` 등의 프로퍼티를 통해 조절할 수 있습니다. 이 프로퍼티들을 사용하여 애니메이션의 색상, 배경색, 패딩, 선의 두께 등을 설정할 수 있습니다.

```swift
activityIndicator.color = .blue // 애니메이션의 색상을 파란색으로 설정
activityIndicator.backgroundColor = .clear // 애니메이션의 배경색을 투명하게 설정
activityIndicator.backgroundPadding = 10 // 애니메이션의 배경 패딩을 10으로 설정
activityIndicator.lineWidth = 2 // 애니메이션의 선의 두께를 2로 설정
```

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)

위의 코드와 설명을 참고하여 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션의 속도와 외관을 조절해보세요.