---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 활용하기 - 통화 기록 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift 언어를 사용하여 NVActivityIndicatorView를 활용하여 통화 기록 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

NVActivityIndicatorView는 화면에 로딩 인디케이터를 표시하기 위한 오픈 소스 라이브러리입니다. 이를 사용하면 간단하게 로딩 화면을 구현할 수 있습니다.

## 1. NVActivityIndicatorView 설치하기

먼저, Cocoapods를 통해 NVActivityIndicatorView를 설치해야 합니다. `Podfile`에 아래의 라인을 추가해주세요.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 다음과 같이 몇 가지 단계를 따라야 합니다.

### 2.1. NVActivityIndicatorView 추가하기

로딩 화면을 표시할 뷰 컨트롤러에 NVActivityIndicatorView를 추가합니다. 이를 위해 `import NVActivityIndicatorView`를 추가하고, 로딩 화면을 표시할 UIView를 생성합니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {
    
    var activityIndicatorView: NVActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 화면을 표시할 UIView 생성
        let frame = CGRect(x: 0, y: 0, width: 100, height: 100)
        let activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballSpinFadeLoader, color: .white, padding: nil)
        
        // UIView를 추가하고 중앙에 위치시킴
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }
}
```

### 2.2. 로딩 화면 표시하기

로딩 화면을 표시할 때는 NVActivityIndicatorView가 시작하도록 해야 합니다.

```swift
class LoadingViewController: UIViewController {
    
    // ...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // ...
        
        // 로딩 화면 표시
        activityIndicatorView.startAnimating()
    }
}
```

### 2.3. 로딩 화면 종료하기

로딩 화면을 종료할 때는 NVActivityIndicatorView를 중단해야 합니다.

```swift
class LoadingViewController: UIViewController {
    
    // ...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // ...
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        // 로딩 화면 종료
        activityIndicatorView.stopAnimating()
        
        // 다음 화면으로 이동
        // ...
    }
}
```

## 3. 결과 확인하기

위의 과정을 모두 마쳤으면, 앱을 실행하여 통화 기록 로딩 화면이 정상적으로 표시되면 성공입니다.

## 결론

이번에는 Swift 언어를 사용하여 NVActivityIndicatorView를 활용하여 통화 기록 로딩 화면을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 간단하게 로딩 화면을 구현할 수 있으며, 사용법은 위와 같습니다.