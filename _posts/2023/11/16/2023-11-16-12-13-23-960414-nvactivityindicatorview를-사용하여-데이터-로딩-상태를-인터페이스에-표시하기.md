---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 인터페이스에 표시하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 개요
앱 사용 중 데이터 로딩이 필요한 경우, 사용자는 다운로드나 서버와의 통신이 진행 중임을 알 수 있도록 인터페이스에 로딩 표시기를 추가하는 것이 좋습니다. NVActivityIndicatorView는 간단하고 아름다운 로딩 표시기를 제공하는 유용한 라이브러리입니다. 이 블로그 포스트에서는 Swift 언어를 사용하여 NVActivityIndicatorView를 통해 데이터 로딩 상태를 인터페이스에 표시하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 설치
NVActivityIndicatorView는 [CocoaPods](https://cocoapods.org/)를 통해 쉽게 설치할 수 있습니다. Podfile에 다음 라인을 추가한 후 `pod install` 명령어를 실행하면 됩니다.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기
1. NVActivityIndicatorView를 사용하기 위해 먼저 import 문을 추가합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 표시기를 추가할 View를 생성합니다. 예를 들어, UIViewController에 로딩 표시기를 추가할 경우, IBOutlet을 생성하여 이를 연결하거나 코드로 직접 추가할 수 있습니다.

```swift
@IBOutlet weak var loadingIndicator: NVActivityIndicatorView!
```

3. 로딩 표시기를 초기화하고 활성화하기 위해 viewDidLoad() 메소드에서 다음 코드를 추가합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    // 로딩 표시기 초기화
    loadingIndicator.type = .circleStrokeSpin
    loadingIndicator.color = .gray
    loadingIndicator.startAnimating()
    loadingIndicator.hidesWhenStopped = true
}
```

4. 데이터 로딩이 완료되었을 때 로딩 표시기를 중지하고 숨기기 위해 다음 코드를 추가합니다.

```swift
// 로딩 표시기 중지
loadingIndicator.stopAnimating()
```

## 추가적인 옵션
NVActivityIndicatorView를 보다 다양하게 사용하기 위해 다음과 같은 옵션들도 사용할 수 있습니다.

- 로딩 표시기 스타일 변경:
```swift
loadingIndicator.type = .pacman
```

- 로딩 표시기 크기 변경:
```swift
loadingIndicator.frame = CGRect(x: 0, y: 0, width: 50, height: 50)
```

- 로딩 표시기 색상 변경:
```swift
loadingIndicator.color = .blue
```

- 로딩 표시기 애니메이션 속도 변경:
```swift
loadingIndicator.speed = 1.5
```

보다 자세한 옵션은 NVActivityIndicatorView의 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

## 결론
이제 NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 인터페이스에 표시하는 방법을 알게 되었습니다. NVActivityIndicatorView는 간단한 설정으로 아름다운 로딩 표시기를 쉽게 추가할 수 있습니다. 이를 통해 사용자에게 어플리케이션의 로딩 상태를 시각적으로 표현하여 더 나은 사용자 경험을 제공할 수 있습니다.