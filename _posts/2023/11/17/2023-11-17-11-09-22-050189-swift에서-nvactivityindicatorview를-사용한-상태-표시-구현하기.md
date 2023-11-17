---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 상태 표시 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱 또는 웹 애플리케이션을 개발하다 보면 사용자에게 실행 중인 작업 상태를 표시해야 할 때가 있습니다. 이를 위해 "NVActivityIndicatorView"라는 Swift 라이브러리를 사용하면 간편하게 상태 표시 기능을 구현할 수 있습니다.

NVActivityIndicatorView는 다양한 모양과 크기의 로딩 인디케이터를 제공합니다. 이 라이브러리는 사용하기 쉽고 커스터마이징도 가능하며, Swift 4.2 버전부터 Swift 5 버전까지 모두 지원됩니다.

### NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 CocoaPods를 사용하여 프로젝트에 라이브러리를 추가해야 합니다. 프로젝트의 Podfile에 다음과 같이 NVActivityIndicatorView를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

추가한 후에는 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

### NVActivityIndicatorView 사용하기

1. `import NVActivityIndicatorView`를 사용하여 NVActivityIndicatorView를 가져옵니다.
2. NVActivityIndicatorView가 표시될 컨테이너 뷰를 생성합니다.
3. NVActivityIndicatorView 인스턴스를 생성하고 컨테이너 뷰에 추가합니다.

아래는 NVActivityIndicatorView를 사용하여 상태 표시를 구현하는 간단한 예제입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 컨테이너 뷰 생성
        let containerView = UIView(frame: CGRect(x: 0, y: 0, width: view.frame.width, height: view.frame.height))
        containerView.backgroundColor = UIColor.black.withAlphaComponent(0.3)
        
        // 상단 중앙에 인디케이터 표시
        activityIndicatorView.center = view.center
        activityIndicatorView.type = .ballSpinFadeLoader
        activityIndicatorView.color = .white
        
        // 컨테이너 뷰에 인디케이터 추가
        containerView.addSubview(activityIndicatorView)
        
        // 메인 뷰에 컨테이너 뷰 추가
        view.addSubview(containerView)
        
        // 인디케이터 시작
        activityIndicatorView.startAnimating()
    }
    
    func stopActivityIndicator() {
        // 인디케이터 종료
        activityIndicatorView.stopAnimating()
    }
}
```

위의 예제에서는 NVActivityIndicatorView를 생성하고, 로딩 인디케이터를 화면 중앙에 표시합니다. 인디케이터의 모양은 `.ballSpinFadeLoader`로 설정되어 있으며, 적절한 모양을 선택하여 사용할 수 있습니다. `activityIndicatorView.startAnimating()` 메소드를 호출하여 인디케이터를 시작하고, `activityIndicatorView.stopAnimating()` 메소드를 호출하여 인디케이터를 중지할 수 있습니다.

### 결론

Swift에서 NVActivityIndicatorView를 사용하면 앱 또는 웹 애플리케이션의 상태 표시 기능을 간단하게 구현할 수 있습니다. 이 라이브러리는 사용하기 쉽고, 다양한 모양과 크기를 제공하여 개발자가 원하는 스타일로 커스터마이징할 수 있습니다.