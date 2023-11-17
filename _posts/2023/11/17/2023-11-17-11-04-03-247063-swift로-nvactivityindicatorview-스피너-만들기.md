---
layout: post
title: "[swift] Swift로 NVActivityIndicatorView 스피너 만들기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

스피너는 애플리케이션에서 작업이 진행되고 있음을 시각적으로 보여주는 데 도움이 되는 중요한 요소입니다. NVActivityIndicatorView는 Swift로 작성된 iOS 애플리케이션에서 사용할 수 있는 인기있는 라이브러리로, 다양한 스피너 스타일을 제공합니다. 이번 블로그에서는 NVActivityIndicatorView를 사용하여 스피너를 만드는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 라이브러리 가져오기

먼저, NVActivityIndicatorView를 프로젝트에 추가해야 합니다. Cocoapods와 Swift Package Manager를 사용하여 설치할 수 있습니다. 여기서는 Cocoapods를 사용하는 방법을 소개하겠습니다. 

1. Podfile을 프로젝트 디렉토리에 생성합니다.
2. Podfile을 열고 다음과 같이 작성합니다:

   ```
   platform :ios, '10.0'
   target 'YourProjectTargetName' do
     use_frameworks!
     pod 'NVActivityIndicatorView'
   end
   ```

3. 터미널을 열고 `pod install` 명령어를 실행합니다.

## NVActivityIndicatorView로 스피너 만들기

NVActivityIndicatorView를 사용하여 스피너를 만들어 보겠습니다.

1. UIViewController에 NVActivityIndicatorView를 추가하기 위해 다음과 같이 코드를 작성합니다:

   ```swift
   import NVActivityIndicatorView
   
   class ViewController: UIViewController {
       
       private var activityIndicatorView: NVActivityIndicatorView!
       
       override func viewDidLoad() {
           super.viewDidLoad()
           
           activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: view.frame.size.width/2 - 25, y: view.frame.size.height/2 - 25, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
           
           view.addSubview(activityIndicatorView)
       }
       
       // Start the spinner animation
       func startLoading() {
           activityIndicatorView.startAnimating()
       }
       
       // Stop the spinner animation
       func stopLoading() {
           activityIndicatorView.stopAnimating()
       }
   }
   ```

   이 코드에서는 NVActivityIndicatorView 인스턴스를 UIViewController에 추가하고, 위치와 크기를 설정합니다. `type` 매개변수를 사용하여 스피너의 스타일을 선택할 수 있습니다. `color` 매개변수를 사용하여 스피너의 색상을 지정할 수 있습니다.

2. 스피너를 활성화하려면 `startLoading()` 메서드를 호출하고, 비활성화하려면 `stopLoading()` 메서드를 호출하면 됩니다.

## 스피너 사용하기

스피너를 사용하여 애플리케이션에서 작업이 진행되고 있는 동안 스피너를 표시할 수 있습니다. 예를 들어, 네트워크 요청이나 데이터베이스 작업이 진행될 때 스피너를 사용할 수 있습니다.

다음은 스피너를 사용하여 네트워크 요청 중에 스피너를 표시하는 예제 코드입니다:

```swift
class NetworkManager {
    
    static let shared = NetworkManager()
    
    private let viewController: ViewController
    
    private init() {
        viewController = ViewController()
    }
    
    func makeNetworkRequest() {
        // Show the spinner
        viewController.startLoading()
        
        // Make the network request
        // ...
        
        // Stop the spinner after the request is finished
        viewController.stopLoading()
    }
}
```

위의 코드에서는 `NetworkManager` 클래스가 스피너를 사용하여 네트워크 요청을 처리합니다. `makeNetworkRequest()` 메서드 내에서 스피너를 활성화하고, 요청이 완료된 후에 비활성화합니다.

이제 NVActivityIndicatorView를 사용하여 스피너를 만들고 표시하는 방법을 알게 되었습니다. 앱에서 작업이 실행되는 동안 사용자에게 진행 상황을 시각적으로 보여주는 강력한 기능을 활용하여 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)