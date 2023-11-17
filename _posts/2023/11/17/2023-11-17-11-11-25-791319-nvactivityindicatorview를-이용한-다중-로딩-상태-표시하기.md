---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 다중 로딩 상태 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱을 개발할 때, 다중 로딩 상태를 표시하는 것은 중요한 요소입니다. 사용자가 어떤 작업이 진행 중인지 인식할 수 있도록 하는 것으로, 사용자 경험을 향상시키는 데 도움이 됩니다. 

NVActivityIndicatorView는 Swift에서 사용할 수 있는 로딩 인디케이터 라이브러리로, 여러 가지 다양한 스타일의 로딩 인디케이터를 제공합니다. 이 라이브러리는 인디케이터를 쉽게 커스텀하고, 애니메이션 기능을 설정할 수 있어 매우 유용합니다.

## NVActivityIndicatorView 설치하기

먼저, `Podfile` 에 다음과 같이 NVActivityIndicatorView를 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그런 다음 터미널을 열고 다음 명령어를 실행하여 종속성을 설치합니다.

```bash
$ pod install
```

## NVActivityIndicatorView 사용하기

`NVActivityIndicatorView`를 사용하기 위해, 다음과 같이 import 문을 추가합니다.

```swift
import NVActivityIndicatorView
```

로딩 상태를 표시할 뷰에 `NVActivityIndicatorView`를 추가합니다. 예를 들어, `UIViewController`의 `viewDidLoad` 메서드에서 다음과 같이 코드를 작성할 수 있습니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
    activityIndicatorView.center = view.center
    view.addSubview(activityIndicatorView)
    
    // 인디케이터 스타일 설정
    activityIndicatorView.type = .ballSpinFadeLoader
    
    // 인디케이터 색상 설정
    activityIndicatorView.color = .blue
    
    // 인디케이터 시작
    activityIndicatorView.startAnimating()
}
```

위 코드에서는 `activityIndicatorView`를 생성하고, 중앙에 위치하도록 설정한 후, 해당 뷰의 서브뷰로 추가합니다. `type` 속성을 사용하여 인디케이터의 스타일을 설정하고, `color` 속성을 사용하여 인디케이터의 색상을 설정합니다. 마지막으로 `startAnimating()` 메서드를 호출하여 인디케이터를 시작합니다.

## 커스텀 로딩 인디케이터

NVActivityIndicatorView 라이브러리는 다양한 로딩 인디케이터 스타일을 제공합니다. 스타일을 변경하려면 `type` 속성을 다른 값을 할당하십시오. 몇 가지 예시를 살펴보겠습니다.

- BallPulse: `.ballPulse`
- BallGridPulse: `.ballGridPulse`
- LineScale: `.lineScale`
- LineSpinFadeLoader: `.lineSpinFadeLoader`
- CircleStrokeSpin: `.circleStrokeSpin`

커스텀 로딩 인디케이터의 전체 목록은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

## 결론

NVActivityIndicatorView를 사용하면 앱의 로딩 상태를 표시하는 데 도움이되는 다양한 스타일의 인디케이터를 쉽게 구현할 수 있습니다. 다양한 인디케이터 스타일을 사용하여 사용자 경험을 향상시키고, 앱에 전문성과 부드러움을 더할 수 있습니다.

더 많은 정보 및 예제 코드를 확인하려면 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 방문하세요.