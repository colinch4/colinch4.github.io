---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator 설정하는 방법과 사용법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## AlamofireNetworkActivityIndicator란?
AlamofireNetworkActivityIndicator는 Alamofire를 사용하여 네트워크 요청이 진행 중일 때 액티비티 인디케이터를 표시하는 기능을 제공하는 라이브러리입니다. 이를 통해 사용자에게 네트워크 요청이 진행 중임을 시각적으로 알려주어 사용자 경험을 개선할 수 있습니다.

## AlamofireNetworkActivityIndicator 설치
AlamofireNetworkActivityIndicator를 사용하기 위해서는 먼저 CocoaPods를 통해 Alamofire와 함께 설치해야 합니다. Podfile에 다음과 같이 추가합니다:

```ruby
pod 'Alamofire'
pod 'AlamofireNetworkActivityIndicator'
```

그리고 터미널에서 다음 명령어로 Cocoapods를 설치합니다:

```
$ pod install
```

## AlamofireNetworkActivityIndicator 사용하기
AlamofireNetworkActivityIndicator를 사용하기 위해서는 먼저 import 문을 통해 라이브러리를 가져와야 합니다:

```swift
import AlamofireNetworkActivityIndicator
```

이제 네트워크 요청이 시작되기 전에 액티비티 인디케이터를 활성화해야 합니다. 보통 앱의 AppDelegate.swift 파일의 didFinishLaunchingWithOptions 메서드에서 활성화하는 것이 일반적입니다. 다음과 같이 코드를 추가합니다:

```swift
NetworkActivityIndicatorManager.shared.isEnabled = true
```

이제 Alamofire를 사용하여 네트워크 요청을 보낼 때마다 액티비티 인디케이터가 표시될 것입니다. 네트워크 요청이 완료되면 자동으로 액티비티 인디케이터가 숨겨집니다.

## AlamofireNetworkActivityIndicator 설정 변경하기
AlamofireNetworkActivityIndicator에서는 몇 가지 설정을 변경할 수 있습니다. 다음은 일부 설정에 대한 예시입니다:

### 액티비티 인디케이터 스타일 변경
액티비티 인디케이터의 스타일을 변경하려면 다음과 같이 코드를 추가합니다:

```swift
NetworkActivityIndicatorManager.shared.style = .gray
```

### 액티비티 인디케이터 인터벌 변경
액티비티 인디케이터의 표시 지연 시간을 변경하려면 다음과 같이 코드를 추가합니다:

```swift
NetworkActivityIndicatorManager.shared.delay = 0.1
```

### 액티비티 인디케이터 오프셋 변경
액티비티 인디케이터의 위치를 오프셋으로 조정하려면 다음과 같이 코드를 추가합니다:

```swift
NetworkActivityIndicatorManager.shared.offset = UIOffset(horizontal: 0, vertical: 20)
```

## 결론
AlamofireNetworkActivityIndicator를 사용하면 Alamofire를 사용할 때 네트워크 요청 진행 상태를 사용자에게 시각적으로 알려줄 수 있습니다. 액티비티 인디케이터의 스타일, 인터벌, 오프셋 등을 조정하여 앱의 사용자 경험을 더욱 개선할 수 있습니다.

## 참고 자료
- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)
- [AlamofireNetworkActivityIndicator GitHub Repository](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)