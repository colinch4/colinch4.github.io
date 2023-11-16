---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 속성 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 소개

NVActivityIndicatorView는 iOS 애플리케이션에서 사용할 수 있는 쉽고 간편한 액티비티 인디케이터 라이브러리입니다. 이 라이브러리를 사용하면 로딩 중임을 사용자에게 시각적으로 알릴 수 있습니다. 이번 포스트에서는 Swift에서 NVActivityIndicatorView의 크기와 속성을 설정하는 방법에 대해 알아보겠습니다.

## 시작하기 전에

NVActivityIndicatorView를 사용하기 위해 프로젝트에 이 라이브러리를 설치해야 합니다. 가장 간단한 방법은 CocoaPods를 사용하는 것입니다.  이를 위해 터미널에서 다음 명령을 실행하세요.

```shell
$ pod install
```

이제 NVActivityIndicatorView의 최신 버전이 프로젝트에 추가되었습니다. 

## NVActivityIndicatorView 구성

NVActivityIndicatorView를 사용할 뷰 컨트롤러에서 다음과 같이 뷰를 추가하고, NVActivityIndicatorView를 생성합니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    private var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView를 추가합니다.
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))

        // 원하는 애니메이션 유형을 설정합니다.
        activityIndicatorView.type = .ballPulse

        // NVActivityIndicatorView 색상을 설정합니다.
        activityIndicatorView.color = .red

        // NVActivityIndicatorView를 추가한 뒤, 중앙에 위치시킵니다.
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }
}
```

## 크기 조정

`NVActivityIndicatorView`의 크기는 `frame` 속성을 통해 조정할 수 있습니다. 위의 예제에서는 너비와 높이를 50으로 설정했습니다. 필요에 따라 원하는 크기로 조정할 수 있습니다.

```swift
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
```

## 속성 설정

`NVActivityIndicatorView`의 속성을 설정하여 다양한 스타일과 효과를 적용할 수 있습니다. 예를 들어, 다음과 같이 애니메이션 타입을 설정할 수 있습니다.

```swift
activityIndicatorView.type = .ballClipRotateMultiple
```

또는 다음과 같이 색상을 설정할 수도 있습니다.

```swift
activityIndicatorView.color = .blue
```

`NVActivityIndicatorView`의 다양한 속성을 사용하여 원하는 스타일과 효과를 구현할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.

## 결론

이번 포스트에서는 Swift에서 NVActivityIndicatorView의 크기와 속성을 설정하는 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 iOS 애플리케이션에서 로딩 중임을 사용자에게 시각적으로 표시할 수 있으며, 이를 통해 사용자 경험을 향상시킬 수 있습니다.

다양한 속성과 스타일을 조정하여 원하는 디자인과 효과를 적용해 보세요.  NVActivityIndicatorView를 사용하면 애플리케이션의 브랜딩과 일관된 커스터마이징이 가능합니다.