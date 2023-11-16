---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 반복 횟수 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 인기있는 로딩 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 편리하게 다양한 스타일의 로딩 애니메이션을 구현할 수 있습니다.

NVActivityIndicatorView의 기본 동작은 애니메이션을 무한 반복하는 것입니다. 그러나 때로는 특정 횟수만큼 애니메이션을 반복하고 싶을 수도 있습니다. 이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView 애니메이션의 반복 횟수를 설정하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 라이브러리 설치

먼저 NVActivityIndicatorView 라이브러리를 설치해야 합니다. CocoaPods를 사용하는 경우 `Podfile`에 다음과 같이 라이브러리를 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 2. NVActivityIndicatorView 애니메이션 반복 횟수 설정

NVActivityIndicatorView에서 애니메이션의 반복 횟수를 설정하려면 `numberOfLoops` 속성을 사용합니다. 원하는 반복 횟수를 `numberOfLoops`에 할당하면 됩니다.

다음은 NVActivityIndicatorView를 사용하여 애니메이션을 시작하고 3번 반복하는 예제 코드입니다:

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // NVActivityIndicatorView 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
        
        // 애니메이션 스타일 설정
        activityIndicatorView.type = .ballClipRotatePulse
        
        // 애니메이션 반복 횟수 설정
        activityIndicatorView.numberOfLoops = 3
        
        // 애니메이션 시작
        activityIndicatorView.startAnimating()
    }
}
```

위의 예제 코드에서 `numberOfLoops` 속성을 3으로 설정하여 애니메이션을 3번 반복하도록 했습니다.

## 결론

Swift에서 NVActivityIndicatorView 애니메이션의 반복 횟수를 설정하는 방법을 알아보았습니다. `numberOfLoops` 속성을 사용하여 애니메이션의 반복 횟수를 원하는대로 조정할 수 있습니다. 이를 통해 더욱 다양하고 유연한 로딩 애니메이션을 구현할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)