---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 메모리 로딩 텍스트 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

![NVActivityIndicatorView](https://cloud.githubusercontent.com/assets/7645180/12764219/8558f2c6-c9e6-11e5-9b0a-ddb8791d8603.gif)

메모리 로딩 텍스트 효과는 앱이 사용자에게 데이터를 로딩 중임을 시각적으로 나타내는 효과입니다. 이 효과는 NVActivityIndicatorView 라이브러리를 사용하여 구현할 수 있습니다. NVActivityIndicatorView는 iOS 앱에서 간편하게 로딩 효과를 만들어주는 오픈 소스 라이브러리입니다.

## NVActivityIndicatorView 라이브러리 설치

CocoaPods를 사용하여 NVActivityIndicatorView를 프로젝트에 추가합니다. `Podfile`에 다음과 같은 내용을 추가한 후, `pod install` 명령을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 로딩 효과 구현하기

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 효과를 표시할 뷰를 생성합니다.

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: NVActivityIndicatorType.ballScaleMultiple, color: .black, padding: nil)
```

3. 뷰의 위치를 설정합니다.

```swift
loadingView.center = self.view.center
```

4. 로딩 효과를 시작합니다.

```swift
loadingView.startAnimating()
```

5. 로딩 효과를 멈추고, 뷰를 제거합니다.

```swift
loadingView.stopAnimating()
loadingView.removeFromSuperview()
```

## 예시 코드

다음은 NVActivityIndicatorView를 사용하여 메모리 로딩 텍스트 효과를 구현하는 예시 코드입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {
    let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: NVActivityIndicatorType.ballScaleMultiple, color: .black, padding: nil)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        loadingView.center = self.view.center
        self.view.addSubview(loadingView)
        
        startLoading()
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 5) {
            self.stopLoading()
        }
    }
    
    func startLoading() {
        loadingView.startAnimating()
    }
    
    func stopLoading() {
        loadingView.stopAnimating()
        loadingView.removeFromSuperview()
    }
}
```

## 참고 자료

- [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)