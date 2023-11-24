---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 앱 실행 시 초기 데이터 로딩 인디케이터 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱을 개발할 때, 초기 데이터 로딩이 오래 걸릴 수 있습니다. 사용자가 앱이 정상적으로 작동하고 있는지 인지할 수 있도록 초기 데이터 로딩 상태를 시각적으로 표시하는 것은 중요합니다. 이를 위해 NVActivityIndicatorView를 사용하여 인디케이터를 구현할 수 있습니다. NVActivityIndicatorView는 Swift로 작성된 인디케이터 라이브러리로, 간단한 코드로 다양한 스타일의 인디케이터를 표시할 수 있습니다.

## NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 사용하여 설치할 수 있습니다. Podfile에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행합니다:

```shell
pod install
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해, 먼저 해당 라이브러리를 import해야 합니다:

```swift
import NVActivityIndicatorView
```

다음으로, 인디케이터를 추가하고 싶은 앱의 뷰 컨트롤러에서 NVActivityIndicatorView를 선언합니다:

```swift
var activityIndicatorView: NVActivityIndicatorView!
```

이제 viewDidLoad() 메서드에서 activityIndicatorView를 초기화하고, 스타일과 색상을 설정합니다:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
    activityIndicatorView.center = view.center
    view.addSubview(activityIndicatorView)
}
```

이제 원하는 시점에 인디케이터를 화면에 표시하고, 데이터 로딩이 완료된 후에는 숨겨야 합니다. 아래 예제는 데이터 로딩 시작 전에 인디케이터를 표시하고, 데이터 로딩이 완료된 후에는 인디케이터를 숨깁니다:

```swift
func loadData() {
    activityIndicatorView.startAnimating()
    
    // 데이터 로딩 로직
    // ...
    
    activityIndicatorView.stopAnimating()
}
```

## NVActivityIndicatorView 사용 시 주의사항

NVActivityIndicatorView를 사용할 때 주의해야 할 몇 가지 사항이 있습니다. 

1. NVActivityIndicatorView를 사용하는 뷰 컨트롤러의 화면이 전환될 때, 인디케이터도 함께 움직여야 한다면 해당 뷰 컨트롤러에서 NVActivityIndicatorView를 추가하고 제거해야 합니다.

2. NVActivityIndicatorView의 프레임 크기와 위치를 조절하여 화면에 원하는 위치에 인디케이터를 표시할 수 있습니다.

3. NVActivityIndicatorView의 색상과 스타일을 원하는 대로 설정할 수 있습니다. 

더 많은 정보와 예제는 [NVActivityIndicatorView 공식 GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

이렇게 NVActivityIndicatorView를 사용하여 앱 실행 시 초기 데이터 로딩 인디케이터를 표시할 수 있습니다. 사용자의 경험을 향상시키기 위해 인디케이터를 활용하여 앱의 로딩 상태를 시각적으로 표시하는 것은 매우 유용한 기능입니다.