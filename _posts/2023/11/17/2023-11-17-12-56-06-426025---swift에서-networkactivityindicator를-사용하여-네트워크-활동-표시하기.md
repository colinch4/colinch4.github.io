---
layout: post
title: "[swift] - Swift에서 NetworkActivityIndicator를 사용하여 네트워크 활동 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

iOS 애플리케이션을 개발할 때, 네트워크 요청이 진행 중인지 사용자에게 시각적인 피드백을 제공하는 것이 중요합니다. 이를 위해 iOS는 NetworkActivityIndicator라는 기능을 제공합니다. 이 기능을 사용하면 앱의 타이틀 바 상단에 회전하는 인디케이터를 표시하여 네트워크 활동을 시각적으로 나타낼 수 있습니다.

## NetworkActivityIndicator를 사용하는 방법

1. AppDelegate.swift 파일을 엽니다.
2. `application:didFinishLaunchingWithOptions` 메서드 내에 다음 코드를 추가합니다:

```swift
UIApplication.shared.isNetworkActivityIndicatorVisible = true
```

3. 네트워크 요청을 시작하기 전에 인디케이터를 활성화하려면 다음 코드를 추가합니다:

```swift
UIApplication.shared.isNetworkActivityIndicatorVisible = true
```

4. 네트워크 요청이 완료되면 다음 코드를 추가하여 인디케이터를 비활성화합니다:

```swift
UIApplication.shared.isNetworkActivityIndicatorVisible = false
```

## 예제 코드

```swift
import UIKit

class NetworkManager {
    func fetchData() {
        // 네트워크 요청 시작 시 인디케이터 활성화
        UIApplication.shared.isNetworkActivityIndicatorVisible = true
        
        // 네트워크 요청 로직 실행
        // ...
        
        // 네트워크 요청 완료 시 인디케이터 비활성화
        UIApplication.shared.isNetworkActivityIndicatorVisible = false
    }
}

class ViewController: UIViewController {
    let networkManager = NetworkManager()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // 버튼을 통해 네트워크 요청을 시작하는 예제
        let button = UIButton(frame: CGRect(x: 100, y: 100, width: 200, height: 50))
        button.setTitle("Fetch Data", for: .normal)
        button.addTarget(self, action: #selector(fetchDataButtonTapped), for: .touchUpInside)
        
        view.addSubview(button)
    }
    
    @objc func fetchDataButtonTapped() {
        networkManager.fetchData()
    }
}
```

위 예제 코드에서는 `NetworkManager` 클래스가 네트워크 요청을 관리하고, `fetchData` 메서드 내에서 요청을 처리하기 전과 후에 `UIApplication.shared.isNetworkActivityIndicatorVisible`을 사용하여 인디케이터를 활성화 및 비활성화합니다. `ViewController` 클래스의 `fetchDataButtonTapped` 메서드에서는 `NetworkManager`의 `fetchData` 메서드를 호출하여 네트워크 요청을 시작합니다.

## 참고 자료

- [Apple Developer Documentation - UIApplication.isNetworkActivityIndicatorVisible](https://developer.apple.com/documentation/uikit/uiapplication/1623032-isnetworkactivityindicatorvisib)
- [Stack Overflow - How to use NetworkActivityIndicator in Swift](https://stackoverflow.com/questions/28335717/how-to-use-networkactivityindicator-in-swift)