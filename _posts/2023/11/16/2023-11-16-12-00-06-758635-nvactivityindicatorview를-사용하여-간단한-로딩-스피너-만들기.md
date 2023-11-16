---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 간단한 로딩 스피너 만들기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 NVActivityIndicatorView를 사용하여 간단한 로딩 스피너를 만드는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS 앱에서 사용할 수 있는 로딩 스피너 라이브러리입니다. 이 라이브러리를 통해 다양한 모양의 로딩 스피너를 만들 수 있으며, 사용하기도 매우 간단합니다.

## NVActivityIndicatorView 설치하기

먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. 이를 위해 CocoaPods를 사용할 수 있습니다. `Podfile`에 다음과 같이 NVActivityIndicatorView를 추가해주세요.

```ruby
target 'YourProject' do
  # ...
  pod 'NVActivityIndicatorView'
end
```

그리고 터미널에서 아래 명령어를 실행하여 CocoaPods를 설치합니다.

```shell
pod install
```

이제 프로젝트에 NVActivityIndicatorView가 설치되었습니다.

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 원하는 위치에 NVActivityIndicatorView 인스턴스를 생성합니다. 로딩 스피너의 크기와 모양, 색상 등을 설정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .blue)
```

3. 인스턴스를 뷰에 추가합니다. 예를 들어, 기존의 UIViewController의 view에 추가하려면 다음과 같이 하면 됩니다.

```swift
self.view.addSubview(activityIndicatorView)
```

4. 로딩 스피너를 시작하려면 `startAnimating()` 메서드를 호출합니다.

```swift
activityIndicatorView.startAnimating()
```

5. 로딩이 완료되었을 때는 `stopAnimating()` 메서드를 호출하여 로딩 스피너를 중지합니다.

```swift
activityIndicatorView.stopAnimating()
```

## 예제

다음은 NVActivityIndicatorView를 사용하여 간단한 로딩 스피너를 만드는 예제 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    private var activityIndicatorView: NVActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 스피너 설정
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .blue)
        
        // 로딩 스피너를 뷰에 추가
        self.view.addSubview(activityIndicatorView)
        
        // 로딩 시작
        activityIndicatorView.startAnimating()
        
        // 일정 시간 후 로딩 중지
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            self.activityIndicatorView.stopAnimating()
        }
    }
}
```

이 예제 코드를 실행하면 로딩 스피너가 화면에 표시되고, 3초 후에 중지됩니다.

## 마무리

이렇게 NVActivityIndicatorView를 사용하여 간단한 로딩 스피너를 만들었습니다. NVActivityIndicatorView를 사용하면 iOS 앱에서 사용자에게 로딩 중임을 알리는 효과적인 방법을 구현할 수 있습니다.

더 자세한 사용법과 라이브러리 설정에 대해서는 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조해주세요.