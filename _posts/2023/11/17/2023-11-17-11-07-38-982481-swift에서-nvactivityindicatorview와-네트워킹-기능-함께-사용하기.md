---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 네트워킹 기능 함께 사용하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift는 기존에 제공하는 풍부한 라이브러리와 프레임워크를 통해 다양한 기능을 구현할 수 있습니다. 이 중에서도 NVActivityIndicatorView는 로딩 인디케이터를 쉽게 구현할 수 있도록 도와주는 라이브러리입니다. 이번에는 NVActivityIndicatorView와 함께 네트워킹 기능을 구현하는 방법에 대해 알아보겠습니다.

### 1. NVActivityIndicatorView 설치하기

먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. Cocoapods를 사용하는 경우, Podfile에 다음과 같은 내용을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

### 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 먼저 import 구문을 추가합니다.

```swift
import NVActivityIndicatorView
```

다음으로, 로딩 인디케이터를 나타낼 뷰를 생성합니다. 보통 작은 사이즈의 UIView를 사용하며, 로딩 인디케이터의 스타일과 색상을 설정할 수 있습니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScaleRipple, color: .gray, padding: nil)
```

이제 로딩 인디케이터를 원하는 위치에 추가하고 시작하면 됩니다.

```swift
indicatorView.center = view.center
view.addSubview(indicatorView)
indicatorView.startAnimating()
```

### 3. 네트워킹 기능과 함께 사용하기

NVActivityIndicatorView를 네트워킹 기능과 함께 사용하려면, 네트워킹 요청을 보내기 전에 로딩 인디케이터를 시작하고, 응답을 받은 후에 멈추도록 구현할 수 있습니다.

```swift
// 로딩 인디케이터 시작
indicatorView.startAnimating()

// 네트워킹 요청 전송
NetworkManager.shared.request(url: "https://api.example.com/data") { result in
    // 네트워킹 응답 처리
    switch result {
    case .success(let data):
        // 데이터 처리 로직
        // ...
        
    case .failure(let error):
        // 에러 처리 로직
        // ...
    }
    
    // 로딩 인디케이터 멈춤
    indicatorView.stopAnimating()
}
```

위의 예제에서는 `NetworkManager`라는 클래스를 사용하여 네트워킹 요청을 보냈습니다. 실제로는 네트워킹 라이브러리를 사용하거나 URLSession 등을 통해 요청을 보내면 됩니다.

### 4. 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)

이제 Swift에서 NVActivityIndicatorView와 네트워킹 기능을 함께 사용하는 방법을 알게 되었습니다. 이를 활용하여 사용자에게 로딩 상태를 보여주고 네트워크 요청에 대한 응답을 처리할 수 있습니다.