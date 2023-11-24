---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 유용한 UI 효과 구현 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

UI 효과는 모바일 애플리케이션을 더욱 동적이고 흥미롭게 만들어줍니다. 이번 글에서는 Swift 프로그래밍 언어를 사용하여 NVActivityIndicatorView를 활용하여 유용한 UI 효과를 구현하는 방법을 알아보겠습니다. 

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift를 지원하는 iOS 애플리케이션에서 사용할 수 있는 오픈 소스 라이브러리입니다. 이 라이브러리는 간단한 코드만으로 다양한 로딩 인디케이터를 구현할 수 있게 해줍니다. 

## 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 Cocoapods를 설치해야 합니다. 터미널을 열고 다음 명령을 실행하여 Cocoapods를 설치합니다:

```
$ sudo gem install cocoapods
```

설치가 완료되면 `Podfile`이라는 파일을 프로젝트 루트 디렉토리에 생성하고 다음 내용을 추가합니다:

```
platform :ios, '9.0'
use_frameworks!

target 'YourApp' do
    pod 'NVActivityIndicatorView'
end
```

그런 다음 터미널에서 프로젝트 루트 디렉토리로 이동한 후 다음 명령을 실행하여 Cocoapods를 설치합니다:

```
$ pod install
```

이제 NVActivityIndicatorView를 사용할 준비가 되었습니다. 

## 사용하기

NVActivityIndicatorView를 사용하려면 다음과 같은 단계를 따라야 합니다:

1. UIViewController에 NVActivityIndicatorView를 추가합니다.
2. NVActivityIndicatorView를 제어하는 코드를 작성합니다.
3. 원하는 UI 효과를 설정합니다.

### 1. UIViewController에 NVActivityIndicatorView 추가하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 UIViewController에 해당 뷰를 추가해야 합니다. 다음 코드를 사용하여 UIViewController에 NVActivityIndicatorView를 추가합니다:

```swift
import NVActivityIndicatorView

class YourViewController: UIViewController {
    private var activityIndicator: NVActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // NVActivityIndicatorView 인스턴스 생성
        activityIndicator = NVActivityIndicatorView(frame: .zero)
        activityIndicator.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(activityIndicator)
        
        // 제약 조건 설정
        activityIndicator.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        activityIndicator.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
    }
}
```

### 2. NVActivityIndicatorView를 제어하는 코드 작성하기

NVActivityIndicatorView를 제어하기 위해서는 다음과 같은 코드를 작성해야 합니다:

```swift
// 로딩 시작
activityIndicator.startAnimating()

// 로딩 중지
activityIndicator.stopAnimating()
```

### 3. UI 효과 설정하기

NVActivityIndicatorView는 여러 가지 스타일을 제공합니다. 다음 코드를 사용하여 원하는 스타일로 설정할 수 있습니다:

```swift
// activityIndicator 스타일 설정
activityIndicator.type = .ballPulse

// activityIndicator 색상 설정
activityIndicator.color = .red

// activityIndicator 크기 설정
activityIndicator.size = CGSize(width: 50, height: 50)
```

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)

이번에는 NVActivityIndicatorView를 활용하여 유용한 UI 효과를 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 간편하게 사용할 수 있는 라이브러리이므로, 사용하여 애플리케이션에 다양한 UI 효과를 추가해보세요.