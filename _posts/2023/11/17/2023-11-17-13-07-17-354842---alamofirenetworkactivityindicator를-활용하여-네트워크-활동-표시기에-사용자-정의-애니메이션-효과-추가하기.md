---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 활용하여 네트워크 활동 표시기에 사용자 정의 애니메이션 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱에서 네트워크 활동을 표시하기 위해 AlamofireNetworkActivityIndicator를 사용할 수 있습니다. 이 기능을 통해 네트워크 요청이 진행 중일 때 상태 바에 애니메이션 효과를 추가할 수 있습니다.

### 필요한 준비물

- Alamofire 라이브러리: [Alamofire GitHub 링크](https://github.com/Alamofire/Alamofire)
- 네트워크 요청을 실행하는 코드

### AlamofireNetworkActivityIndicator 추가하기

1. 먼저, Alamofire 라이브러리를 프로젝트에 추가하세요. Cocoapods를 사용한다면, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'Alamofire'
```

2. 이제 Alamofire를 사용하여 네트워크 요청을 실행해 주세요. 아래는 예시 코드입니다.

```swift
import Alamofire

Alamofire.request("https://api.example.com/data").responseJSON { response in
    // 네트워크 요청 완료 후 실행할 코드
}
```

3. 네트워크 요청 진행 중일 때, 상태 바에 애니메이션 효과를 추가하기 위해 AlamofireNetworkActivityIndicator를 사용합니다. AppDelegate.swift 파일에 다음 코드를 추가해 주세요.

```swift
import AlamofireNetworkActivityIndicator

// didFinishLaunchingWithOptions 함수 내에 추가
NetworkActivityIndicatorManager.shared.isEnabled = true
```

4. 이제 네트워크 요청이 진행 중일 때 상태 바에 애니메이션 효과가 표시될 것입니다.

### 사용자 정의 애니메이션 효과 추가하기

상태 바에 기본적으로 제공되는 애니메이션 효과 외에 사용자 정의 애니메이션 효과를 추가할 수 있습니다. 다음은 사용자 정의 애니메이션 효과를 추가하는 예시입니다.

1. NetworkActivityIndicatorManager 인스턴스를 직접 생성하여 사용자 정의 애니메이션 효과를 추가할 수 있습니다. AppDelegate.swift 파일에서 다음 코드를 추가하세요.

```swift
NetworkActivityIndicatorManager.shared.startAnimation()
```

2. 애니메이션을 정지하려면 다음 코드를 사용하세요.

```swift
NetworkActivityIndicatorManager.shared.stopAnimation()
```

주의: 사용자 정의 애니메이션을 추가하기 전에, 사용 가능한 동작이 있는지 확인하고, 중복 애니메이션을 방지하기 위해 애니메이션 시작과 종료를 적절하게 관리해야 합니다.

이제 Alamofire를 사용하여 네트워크 요청을 진행할 때 사용자 정의 애니메이션 효과를 추가할 수 있습니다. 네트워크 요청이 진행 중인 동안 애니메이션 효과가 표시되면 사용자에게 진행 중임을 시각적으로 알려줄 수 있습니다.