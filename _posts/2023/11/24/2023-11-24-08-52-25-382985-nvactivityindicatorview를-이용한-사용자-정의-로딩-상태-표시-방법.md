---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 정의 로딩 상태 표시 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱 개발 중에는 네트워크 요청이나 데이터 처리와 같은 작업을 수행하는 동안 사용자에게 로딩 상태를 표시하는 것이 중요합니다. 이러한 로딩 상태를 표시하기 위해 NVActivityIndicatorView를 사용할 수 있습니다. 이 라이브러리는 Swift로 작성된 모바일 앱에서 로딩 인디케이터를 구현하는 데 도움을 줍니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 인디케이터를 표시하기 위한 오픈 소스 Swift 라이브러리입니다. 이 라이브러리를 사용하면 다양한 스타일과 애니메이션으로 사용자에게 로딩 상태를 시각적으로 표시할 수 있습니다. 

## NVActivityIndicatorView 사용하기

먼저 프로젝트에 NVActivityIndicatorView 라이브러리를 추가해야 합니다. CocoaPods를 사용하여 프로젝트에 라이브러리를 추가할 수 있습니다. `Podfile` 파일에 다음 코드를 추가한 후, `pod install` 명령어를 실행하세요.

```ruby
target 'YourProjectName' do
    use_frameworks!
    pod 'NVActivityIndicatorView'
end
```

라이브러리를 추가한 후, 로딩 상태를 표시할 뷰 컨트롤러에 다음 코드를 추가해주세요.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 인디케이터 초기화
        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulseSync, color: .systemBlue, padding: nil)
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
        
        // 로딩 상태 표시
        activityIndicatorView.startAnimating()
    }
}
```

위의 코드는 뷰 컨트롤러에서 NVActivityIndicatorView를 초기화하고, 로딩 상태를 표시하는 방법을 보여줍니다. `type` 매개변수를 사용하여 로딩 인디케이터의 스타일을 선택하고, `color` 매개변수를 사용하여 로딩 인디케이터의 색상을 선택할 수 있습니다.

## 추가 설정

NVActivityIndicatorView는 많은 사용자 설정을 제공하여 로딩 인디케이터를 보다 다양하게 표시할 수 있습니다. NVActivityIndicatorView의 공식 문서를 참고하여 원하는 스타일 및 설정을 적용할 수 있습니다.

## 결론

NVActivityIndicatorView를 사용하면 간단하게 로딩 상태를 표시할 수 있습니다. 이 라이브러리를 사용하여 사용자에게 직관적이고 시각적으로 로딩 상태를 알려주는 인터페이스를 구현할 수 있습니다.

참고: [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)