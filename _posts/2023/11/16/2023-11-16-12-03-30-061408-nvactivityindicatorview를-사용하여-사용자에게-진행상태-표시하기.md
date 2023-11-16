---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 사용자에게 진행상태 표시하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱에서 긴 작업이 진행될 때 사용자에게 진행 상태를 시각적으로 표시하는 것은 좋은 사용자 경험을 제공하는 중요한 요소입니다. 이를 위해 NVActivityIndicatorView를 사용할 수 있습니다. NVActivityIndicatorView는 많은 다양한 스타일의 로딩 인디케이터를 제공하는 오픈 소스 라이브러리입니다.

## 1. NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 CocoaPods를 이용하여 설치해야 합니다. Podfile에 다음과 같이 추가해주세요:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 Terminal을 열고 다음 명령어를 실행하여 프로젝트에 라이브러리를 설치합니다:

```shell
pod install
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 다음과 같은 단계를 따릅니다:

### 2.1. NVActivityIndicatorView import하기

NVActivityIndicatorView를 사용하려면 import 문을 추가해야 합니다. 특히 ViewController 클래스와 같은 위치에 import 문을 추가합니다:

```swift
import NVActivityIndicatorView
```

### 2.2. NVActivityIndicatorView 인스턴스 생성하기

로딩 인디케이터를 표시하기 위해 NVActivityIndicatorView 인스턴스를 생성합니다. 일반적으로 뷰 컨트롤러 내에서 인스턴스를 선언합니다:

```swift
var activityIndicatorView: NVActivityIndicatorView!
```

### 2.3. NVActivityIndicatorView 설정하기

인스턴스를 생성하고 나면 로딩 인디케이터의 속성을 설정해야 합니다. 일반적으로 viewDidLoad() 메서드에서 다음과 같이 설정합니다:

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
    activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballScale, color: .blue, padding: nil)
    activityIndicatorView.center = view.center
    view.addSubview(activityIndicatorView)
}
```

### 2.4. 로딩 인디케이터 제어하기

로딩 인디케이터를 시작하고 중지하는 방법은 다음과 같습니다:

#### 시작하기

로딩 인디케이터를 시작하려면 다음 메서드를 호출합니다:

```swift
activityIndicatorView.startAnimating()
```

#### 중지하기

로딩 인디케이터를 중지하려면 다음 메서드를 호출합니다:

```swift
activityIndicatorView.stopAnimating()
```

## 3. 마무리

이제 NVActivityIndicatorView를 사용하여 사용자에게 진행 상태를 표시할 수 있습니다. 로딩 인디케이터를 시작하고 중지하는 방법을 알았으니, 앱의 필요에 따라 이를 활용할 수 있습니다.

더 자세한 정보는 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.