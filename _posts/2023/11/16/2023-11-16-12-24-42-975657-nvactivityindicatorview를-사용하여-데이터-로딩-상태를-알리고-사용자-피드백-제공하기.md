---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 알리고 사용자 피드백 제공하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

데이터 로딩 상태를 사용자에게 시각적으로 알려주는 것은 앱 사용성을 향상시키는 중요한 요소입니다. 이를 위해 NVActivityIndicatorView를 사용하여 데이터 로딩 인디케이터를 구현할 수 있습니다. NVActivityIndicatorView는 Swift로 작성된 오픈 소스 라이브러리로, 다양한 스타일의 로딩 인디케이터를 제공합니다.

## NVActivityIndicatorView 설치하기

먼저, Cocoapods를 사용하여 NVActivityIndicatorView를 설치해야 합니다. 프로젝트의 Podfile에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

### Step 1: Import 구문 추가하기

NVActivityIndicatorView를 사용하기 위해 해당 뷰 컨트롤러에 import 구문을 추가해야 합니다:

```swift
import NVActivityIndicatorView
```

### Step 2: NVActivityIndicatorView 인스턴스 생성하기

로딩 인디케이터를 사용할 뷰 컨트롤러의 IBOutlet 변수를 선언한 후, viewDidLoad() 메서드에서 해당 변수에 NVActivityIndicatorView 인스턴스를 생성합니다:

```swift
@IBOutlet weak var activityIndicatorView: NVActivityIndicatorView!

override func viewDidLoad() {
    super.viewDidLoad()
    
    // 로딩 인디케이터 스타일과 크기 설정
    activityIndicatorView.type = .ballRotateChase
    activityIndicatorView.color = UIColor.red
    activityIndicatorView.padding = 20
}
```

### Step 3: 데이터 로딩 시작 및 종료 시 로딩 인디케이터 표시하기

데이터 로딩 시작 전에 로딩 인디케이터를 표시하고, 로딩 종료 후에 숨기는 코드를 추가해야 합니다:

```swift
// 데이터 로딩 시작 시
activityIndicatorView.startAnimating()

// 데이터 로딩 종료 시
activityIndicatorView.stopAnimating()
```

## 결론

NVActivityIndicatorView를 사용하면 데이터 로딩 상태를 시각적으로 알리고 사용자에게 피드백을 제공할 수 있습니다. 해당 라이브러리는 다양한 스타일과 커스텀 옵션을 제공하여 앱의 디자인을 개선하는 데 도움을 줍니다.

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)