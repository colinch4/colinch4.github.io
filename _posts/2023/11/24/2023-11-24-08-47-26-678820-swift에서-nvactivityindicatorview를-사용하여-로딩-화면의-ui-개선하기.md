---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 로딩 화면의 UI 개선하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱에서 네트워크 요청이나 데이터 처리와 같은 작업을 수행할 때, 사용자에게 로딩 화면을 표시하는 것은 좋은 사용성을 제공하는 방법입니다. Swift에서 NVActivityIndicatorView를 사용하면 간편하게 로딩 화면을 구현할 수 있습니다.

## NVActivityIndicatorView 소개

NVActivityIndicatorView는 Swift에서 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 여러 가지 모양과 스타일을 제공하며, 애니메이션으로 로딩 상태를 시각적으로 표현할 수 있습니다.

## 설치

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음과 같이 추가합니다:

```swift
pod 'NVActivityIndicatorView'
```

그리고 `pod install` 명령을 실행하여 라이브러리를 설치합니다. 이제 프로젝트에서 NVActivityIndicator를 사용할 준비가 되었습니다.

## 사용 방법

1. 먼저 NVActivityIndicatorView를 import합니다:

```swift
import NVActivityIndicatorView
```

2. 로딩 화면을 표시할 UIView를 생성합니다. 보통은 모든 뷰를 가리키기 위해 앱의 가장 상위 UIWindow를 사용합니다:

```swift
let window = UIApplication.shared.windows.first
let loadingView = NVActivityIndicatorView(frame: window!.bounds)
```

3. 원하는 스타일과 크기의 로딩 인디케이터를 설정합니다:

```swift
loadingView.type = .ballPulse
loadingView.color = .blue
loadingView.padding = 20
loadingView.layer.cornerRadius = 10
```

4. 로딩 화면을 표시합니다:

```swift
window?.addSubview(loadingView)
loadingView.startAnimating()
```

5. 작업이 완료되면 로딩 화면을 제거합니다:

```swift
loadingView.stopAnimating()
loadingView.removeFromSuperview()
```

## 예제

다음은 URLSession을 사용하여 네트워크 요청을 수행하는 동안 NVActivityIndicatorView를 사용하여 로딩 화면을 표시하는 예제입니다:

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let loadingView = NVActivityIndicatorView(frame: UIScreen.main.bounds)

    override func viewDidLoad() {
        super.viewDidLoad()
        
        setLoadingView()
        fetchDataFromAPI()
    }
    
    func setLoadingView() {
        loadingView.type = .ballClipRotatePulse
        loadingView.color = .gray
        loadingView.padding = 20
        loadingView.layer.cornerRadius = 10
        view.addSubview(loadingView)
    }
    
    func fetchDataFromAPI() {
        loadingView.startAnimating()
        
        // 네트워크 요청 코드
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) { [weak self] in
            self?.loadingView.stopAnimating()
            self?.loadingView.removeFromSuperview()
            // 요청 완료 처리
        }
    }

}
```

이 예제에서는 ViewController의 viewDidLoad()에서 setLoadingView()를 호출하여 로딩 화면을 설정하고, fetchDataFromAPI()에서 네트워크 요청을 수행합니다. 요청이 완료되면 로딩 화면을 제거합니다.

## 결론

Swift에서 NVActivityIndicatorView를 사용하면 로딩 화면의 UI 개선이 간편하게 가능합니다. 다양한 스타일과 크기의 로딩 인디케이터를 사용하여 사용자에게 진행 중인 작업을 시각적으로 알려줄 수 있습니다.

더 많은 정보와 사용 예제는 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.