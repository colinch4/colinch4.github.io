---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 로딩 인디케이터 디자인하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

로딩 인디케이터는 앱이 작업을 수행하는 동안 사용자에게 진행 상황을 시각적으로 보여주는 중요한 구성 요소입니다. Swift에서는 NVActivityIndicatorView라는 라이브러리를 사용하여 간단하고 멋진 로딩 인디케이터를 디자인할 수 있습니다.

### NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS용 로딩 인디케이터를 쉽게 구현하는 라이브러리입니다. 다양한 스타일과 색상의 로딩 인디케이터를 제공하여 앱의 디자인에 맞게 사용할 수 있습니다.

### NVActivityIndicatorView 설치

NVActivityIndicatorView는 CocoaPods를 통해 손쉽게 설치할 수 있습니다. 프로젝트의 Podfile에 다음과 같은 코드를 추가하고 `pod install` 명령을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

### NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성하고 화면에 추가합니다. 다음은 로딩 인디케이터를 표시할 뷰 컨트롤러의 viewDidLoad 메서드 내부에 위치한 예시입니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    // 로딩 인디케이터를 생성합니다.
    let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 80, height: 80), type: .ballBeat, color: .blue, padding: nil)
    
    // 로딩 인디케이터를 중앙에 배치합니다.
    indicatorView.center = CGPoint(x: view.frame.size.width / 2, y: view.frame.size.height / 2)
    
    // 로딩 인디케이터를 화면에 추가합니다.
    view.addSubview(indicatorView)
    
    // 로딩 인디케이터를 시작합니다.
    indicatorView.startAnimating()
}
```

3. 로딩 작업이 완료되었을 때 로딩 인디케이터를 제거합니다. 다음은 해당 예시의 로딩 작업이 완료되었을 때 호출되는 메서드입니다.

```swift
func loadingComplete() {
    // 로딩 인디케이터를 제거합니다.
    indicatorView.stopAnimating()
    indicatorView.removeFromSuperview()
}
```

### NVActivityIndicatorView 스타일 및 색상 변경하기

여러 가지 스타일과 색상의 로딩 인디케이터를 사용할 수 있습니다. NVActivityIndicatorView를 초기화할 때 `type` 및 `color` 매개변수를 사용하여 스타일과 색상을 지정할 수 있습니다. 예를 들어, `.circleStrokeSpin` 스타일과 `.red` 색상의 로딩 인디케이터를 생성하는 방법은 다음과 같습니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 80, height: 80), type: .circleStrokeSpin, color: .red, padding: nil)
```

### 결론

Swift에서 NVActivityIndicatorView를 사용하면 간단하고 멋진 로딩 인디케이터를 쉽게 디자인할 수 있습니다. NVActivityIndicatorView는 다양한 스타일과 색상을 제공하여 앱의 디자인에 맞게 사용할 수 있습니다. 즉, 앱의 사용자 경험을 향상시키고 작업의 진행 상황을 보여주기 위해 로딩 인디케이터를 사용하는 것은 좋은 아이디어입니다.

### 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)