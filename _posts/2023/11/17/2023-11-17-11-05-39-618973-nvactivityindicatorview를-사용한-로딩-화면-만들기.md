---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 로딩 화면 만들기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱을 개발할 때 사용자의 대기 시간 동안 로딩 화면을 보여주는 것은 좋은 사용자 경험을 제공하는 데 도움이 됩니다. 이번에는 Swift에서 NVActivityIndicatorView를 사용하여 로딩 화면을 만드는 방법을 알아보겠습니다.

### NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift에서 사용할 수 있는 애니메이션 라이브러리입니다. 다양한 스타일과 색상의 로딩 인디케이터를 제공하여 앱에 맞는 디자인으로 로딩 화면을 구현할 수 있습니다.

### 설치하기

NVActivityIndicatorView를 사용하려면 먼저 CocoaPods를 이용하여 라이브러리를 설치해야 합니다. Podfile에 다음과 같이 추가하고 `pod install` 명령어를 실행하세요.

```swift
pod 'NVActivityIndicatorView'
```
### 사용하기

1. `import NVActivityIndicatorView`로 NVActivityIndicatorView를 가져옵니다.
2. 로딩 화면을 표시할 뷰를 생성합니다.
3. NVActivityIndicatorView를 초기화하고 로딩 화면의 스타일, 색상, 크기 등을 설정합니다.
4. 생성한 NVActivityIndicatorView를 표시할 뷰에 추가합니다.
5. 로딩 화면을 시작하려면 `startAnimating()` 메서드를 호출하고, 종료하려면 `stopAnimating()` 메서드를 호출합니다.

다음은 간단한 예제 코드입니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!
  
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 화면을 표시할 뷰를 생성
        let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: view.frame.width, height: view.frame.height))
        loadingView.backgroundColor = UIColor.white
        view.addSubview(loadingView)
      
        // NVActivityIndicatorView 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: loadingView.frame.width/2 - 25, y: loadingView.frame.height/2 - 25, width: 50, height: 50), type: .ballSpinFadeLoader, color: UIColor.black, padding: nil)
        
        // NVActivityIndicatorView를 표시할 뷰에 추가
        loadingView.addSubview(activityIndicatorView)
        
        // 로딩 화면 시작
        activityIndicatorView.startAnimating()
        
        // 3초 후에 로딩 화면 종료
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            self.activityIndicatorView.stopAnimating()
            loadingView.removeFromSuperview()
        }
    }
}
```

이제 NVActivityIndicatorView를 사용하여 로딩 화면을 만들어보았습니다. 테스트해보고 앱에 적용해보세요!

### 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)
- [CocoaPods](https://cocoapods.org/)