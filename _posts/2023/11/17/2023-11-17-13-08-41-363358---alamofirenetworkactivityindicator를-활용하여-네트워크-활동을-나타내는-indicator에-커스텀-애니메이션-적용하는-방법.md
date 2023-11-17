---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 활용하여 네트워크 활동을 나타내는 Indicator에 커스텀 애니메이션 적용하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

많은 앱에서 네트워크 활동을 나타내는 Indicator를 사용하고 있습니다. 그러나 기본 제공된 Indicator의 디자인이나 애니메이션을 커스텀하고 싶다면 어떻게 해야 할까요? 이번 포스트에서는 AlamofireNetworkActivityIndicator를 사용하여 Indicator에 커스텀 애니메이션을 적용하는 방법을 알아보겠습니다.

## AlamofireNetworkActivityIndicator란?

AlamofireNetworkActivityIndicator는 Alamofire라이브러리를 사용하여 네트워크 활동을 감지하고 이를 Indicator에 나타내는 역할을 합니다. 이 라이브러리는 앱의 네트워크 활동을 추적하여 앱 상단에 표시되는 지름이 나타나는 Indicator를 자동으로 관리합니다.

## 커스텀 애니메이션 적용 방법

1. 다음과 같이 AlamofireNetworkActivityIndicator 라이브러리를 프로젝트에 추가합니다. 

   ```swift
   pod 'AlamofireNetworkActivityIndicator'
   ```

2. AppDelegate.swift에서 AlamofireNetworkActivityIndicator를 import 합니다.

   ```swift
   import AlamofireNetworkActivityIndicator
   ```

3. didFinishLaunchingWithOptions 함수에서 `AlamofireNetworkActivityIndicatorManager.shared.isEnabled`를 true로 설정하여 Indicator를 활성화합니다. 

   ```swift
   func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
       AlamofireNetworkActivityIndicatorManager.shared.isEnabled = true
       // ...
       return true
   }
   ```

4. 커스텀 애니메이션을 적용하려면 Indicator View를 커스터마이즈 할 수 있습니다. 이를 위해 UIViewController의 viewDidLoad 함수에서 다음 코드를 추가합니다.

   ```swift
   override func viewDidLoad() {
       super.viewDidLoad()
       
       AlamofireNetworkActivityIndicatorManager.shared.completionDelay = 0.2 // 딜레이 값을 변경하여 애니메이션 속도를 조정할 수 있습니다.
       AlamofireNetworkActivityIndicatorManager.shared.completionThreshold = 0.5 // 애니메이션을 시작하기 전의 최소 시간과 시간 간격을 조정할 수 있습니다.
   }
   ```

   이제 Indicator의 커스텀 애니메이션을 적용할 준비가 끝났습니다.

5. Indicator의 커스텀 애니메이션을 적용하려면 다음 코드를 사용하십시오.

   ```swift
   Alamofire.request("https://api.example.com").response { response in
       // 네트워크 요청 후에 애니메이션이 표시됩니다.
       // 요청이 완료된 후에는 애니메이션이 멈춥니다.
   }
   ```

   이렇게 하면 AlamofireNetworkActivityIndicator가 자동으로 Indicator를 관리하여 커스텀 애니메이션을 표시하게 됩니다.

이제 AlamofireNetworkActivityIndicator를 활용하여 네트워크 활동을 나타내는 Indicator에 커스텀 애니메이션을 적용하는 방법을 알게 되었습니다. 이제 앱의 UI에 따라 원하는 디자인과 애니메이션을 추가하여 사용자에게 더 흥미로운 경험을 제공할 수 있습니다.

## 참고 자료

- [Alamofire - AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)