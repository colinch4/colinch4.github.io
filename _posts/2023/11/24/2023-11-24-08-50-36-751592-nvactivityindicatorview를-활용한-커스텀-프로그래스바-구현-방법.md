---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 커스텀 프로그래스바 구현 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 iOS 앱에서 커스텀 프로그래스바를 구현하는 방법을 알아보겠습니다. NVActivityIndicatorView는 Swift 프로젝트에서 많이 사용되는 라이브러리 중 하나로, 다양한 스타일의 프로그래스바를 쉽게 구현할 수 있도록 도와줍니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 모바일 앱에서 프로그래스바 기능을 구현하는 데 사용되는 오픈 소스 라이브러리입니다. 이 라이브러리는 Swift로 작성되었으며, 다양한 스타일의 프로그래스바를 제공합니다. iOS와 tvOS에서 사용할 수 있으며, 간편한 설정 및 사용법으로 인해 개발자들에게 많이 선호되고 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 전에, 먼저 cocoapods를 통해 설치해야 합니다. Cocoapods를 사용하지 않는 경우 수동으로 라이브러리를 다운로드하여 프로젝트에 추가해야 합니다.

1. 터미널을 열고 프로젝트 폴더로 이동합니다.
2. `pod init` 명령을 실행하여 Podfile을 생성합니다.
3. 생성된 Podfile을 텍스트 에디터로 열고 아래의 라인을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

4. 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.
5. 설치가 완료되면 프로젝트의 `.xcworkspace` 파일을 열어주세요.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 사용하기 위해, 우선 import 문을 추가합니다.

```swift
import NVActivityIndicatorView
```

2. 인터페이스 파일(.xib 또는 Storyboard)에서 해당 컨트롤러에 UIView를 추가하고, 클래스를 NVActivityIndicatorView로 설정합니다.
3. IBOutlet을 생성하고, 해당 UIView와 연결합니다.

```swift
@IBOutlet weak var activityIndicator: NVActivityIndicatorView!
```

4. viewDidLoad() 메서드에 다음 코드를 추가하여 프로그래스바를 설정합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // 프로그래스바 크기 설정
    activityIndicator.frame = CGRect(x: 0, y: 0, width: 40, height: 40)
    // 프로그래스바 색상 설정
    activityIndicator.color = .blue
    // 프로그래스바 스타일 설정
    activityIndicator.type = .ballSpinFadeLoader

    // 프로그래스바 시작
    activityIndicator.startAnimating()
}
```

5. 필요에 따라 프로그래스바를 중지하고 다시 시작할 수 있습니다.

```swift
activityIndicator.stopAnimating()
// 프로그래스바 숨기기
activityIndicator.isHidden = true

activityIndicator.startAnimating()
// 프로그래스바 다시 표시
activityIndicator.isHidden = false
```

이제 NVActivityIndicatorView를 사용하여 커스텀 프로그래스바를 구현하는 방법을 알게 되었습니다. 이 라이브러리를 사용하여 앱에 멋진 프로그래스바를 추가해보세요!

## 참고 자료
- [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 공식 문서](https://cocoapods.org/pods/NVActivityIndicatorView)