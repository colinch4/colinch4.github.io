---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 사용하여 다중 네트워크 요청 상태 바에 Indicator 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

간단하고 효과적인 방법으로 앱에서 다중 네트워크 요청이 진행 중인지 표시하는 것은 중요한 기능입니다. 이렇게 하면 사용자가 앱이 작동 중이라는 것을 인지할 수 있고, 응답이 오기 전까지 기다리고 있다는 것을 알 수 있습니다. 이번에는 AlamofireNetworkActivityIndicator를 사용하여 Swift로 다중 네트워크 요청 상태 바에 Indicator를 표시하는 방법에 대해 알아보겠습니다.

## AlamofireNetworkActivityIndicator란?

AlamofireNetworkActivityIndicator는 Alamofire에서 제공하는 간단한 도구입니다. 이 도구를 사용하면 Alamofire에서 네트워크 요청이 진행 중일 때 상태 바에 Indicator를 표시할 수 있습니다. Indicator는 네트워크 요청이 진행 중임을 나타내며, 요청이 완료되면 Indicator가 자동으로 사라집니다.

## AlamofireNetworkActivityIndicator 설정하기

1. 먼저, Alamofire를 프로젝트에 추가해야 합니다. Cocoapods를 사용하여 프로젝트에 Alamofire를 추가할 수 있습니다. Podfile을 열고 다음 라인을 추가합니다.

```swift
pod 'Alamofire'
```

2. 터미널을 열고 프로젝트 디렉토리로 이동한 후 다음 명령어를 실행하여 Alamofire를 설치합니다.

```bash
pod install
```

3. 이제 AlamofireNetworkActivityIndicator를 설정해보겠습니다. UIKit을 임포트한 후 AppDelegate.swift 파일에 다음 코드를 추가합니다.

```swift
import UIKit
import AlamofireNetworkActivityIndicator

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        NetworkActivityIndicatorManager.shared.isEnabled = true
        return true
    }

}
```

위의 코드에서는 `NetworkActivityIndicatorManager.shared.isEnabled`를 true로 설정하는 것을 볼 수 있습니다. 이렇게 하면 Alamofire가 네트워크 요청 상태 신호를 관리하고 상태 바에 Indicator를 표시할 수 있게 됩니다.

4. 이제 Alamofire로 네트워크 요청을 보낼 때마다 Indicator가 표시됩니다. 예를 들어 ViewController.swift 파일에 다음과 같이 GET 요청을 보내는 코드를 추가해보겠습니다.

```swift
import UIKit
import Alamofire

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        AF.request("https://api.example.com/data").responseJSON { response in
            debugPrint(response)
        }
    }
}
```

위의 코드에서는 Alamofire의 `AF.request` 메서드를 사용하여 GET 요청을 보내고 있습니다. 이 코드를 실행하면 네트워크 요청이 시작되면 상태 바에 Indicator가 표시됩니다.

## 결론

AlamofireNetworkActivityIndicator를 사용하여 다중 네트워크 요청 상태 바에 Indicator를 표시하는 것은 간단하고 효과적인 방법입니다. 이를 통해 앱 사용자에게 네트워크 요청이 진행 중임을 시각적으로 알려줄 수 있습니다. 이를 통해 앱의 사용자 경험을 향상시킬 수 있습니다.

참고 자료:
- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)
- [AlamofireNetworkActivityIndicator GitHub Repository](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)