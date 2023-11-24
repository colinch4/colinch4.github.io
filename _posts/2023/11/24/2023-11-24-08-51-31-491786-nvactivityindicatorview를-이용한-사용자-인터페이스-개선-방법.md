---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 인터페이스 개선 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

> 이번 튜토리얼에서는 NVActivityIndicatorView 라이브러리를 사용하여 iOS 앱의 사용자 인터페이스를 개선하는 방법을 살펴보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS에서 사용할 수 있는 사용자 인터페이스 컴포넌트로, 다양한 스타일의 로딩 인디케이터를 제공합니다. 이 라이브러리를 사용하면 앱에서 데이터를 로딩하는 동안 사용자에게 진행 상태를 시각적으로 보여줄 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 Cocoapods를 통해 라이브러리를 설치해야 합니다. 아래 명령을 터미널에서 실행하여 Cocoapods를 설치합니다.

```shell
$ gem install cocoapods
```

그리고 프로젝트의 `Podfile` 파일에 다음과 같이 NVActivityIndicatorView를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

설정이 끝나면 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

### 1. NVActivityIndicatorView 인스턴스 생성하기

먼저, NVActivityIndicatorView 인스턴스를 생성해야 합니다. UIViewController의 viewDidLoad() 메서드나 다른 적절한 메서드에서 다음과 같이 인스턴스를 생성합니다.

```swift
import NVActivityIndicatorView

class MyViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }

    // ...
}
```

### 2. 로딩 시작 및 종료

데이터를 로딩할 때 로딩 인디케이터를 시작하고, 로딩이 완료되면 종료해야 합니다. 다음과 같은 코드를 사용하여 로딩 인디케이터를 시작하고 종료할 수 있습니다.

```swift
// 로딩 시작
activityIndicatorView.startAnimating()

// 로딩 종료
activityIndicatorView.stopAnimating()
```

### 3. 스타일 및 색상 사용

NVActivityIndicatorView는 다양한 스타일과 색상을 제공합니다. 아래 예제 코드에서는 로딩 인디케이터의 스타일을 `BallBeat`로 설정하고, 색상을 `UIColor.red`로 설정하는 방법을 보여줍니다.

```swift
// 스타일 설정
activityIndicatorView.type = .ballBeat

// 색상 설정
activityIndicatorView.color = UIColor.red
```

### 4. 참조

NVActivityIndicatorView에 대한 자세한 사용법은 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.

## 결론

이번 튜토리얼에서는 NVActivityIndicatorView를 사용하여 iOS 앱의 사용자 인터페이스를 개선하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 직관적인 인터페이스와 다양한 스타일, 색상을 제공하여 사용자에게 진행 상태를 시각적으로 전달하는 데 유용한 라이브러리입니다.