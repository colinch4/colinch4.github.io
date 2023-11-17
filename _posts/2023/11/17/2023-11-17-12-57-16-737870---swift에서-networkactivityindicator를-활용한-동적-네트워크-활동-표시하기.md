---
layout: post
title: "[swift] - Swift에서 NetworkActivityIndicator를 활용한 동적 네트워크 활동 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

네트워크 요청이 발생하는 동안 사용자에게 진행 중인 작업을 알려주는 것은 사용자 경험을 향상시키는데 도움이 됩니다. Swift에서는 NetworkActivityIndicator를 사용하여 네트워크 활동을 표시할 수 있습니다. 이 기능을 사용하면 애플리케이션의 타이틀 바에 동적으로 인디케이터를 표시할 수 있습니다.

## NetworkActivityIndicator란?

iOS에서 NetworkActivityIndicator는 애플리케이션의 표시줄에 나타나는 작은 회전 인디케이터입니다. 이 인디케이터는 네트워크 활동이 진행 중임을 사용자에게 알려줍니다. 앱이 네트워크 요청을 보내는 경우, 이 인디케이터를 표시하여 사용자에게 현재 작업이 진행 중임을 시각적으로 전달할 수 있습니다.

## NetworkActivityIndicator 사용 방법

### 1. UIApplication의 shared 인스턴스에 접근

```swift
let app = UIApplication.shared
```

### 2. NetworkActivityIndicator 상태 설정

네트워크 요청을 보내기 전에 NetworkActivityIndicator 상태를 설정해야 합니다. 네트워크 활동이 시작되면 `app.isNetworkActivityIndicatorVisible`을 `true`로 설정하고, 활동이 완료되면 `false`로 설정합니다.

```swift
app.isNetworkActivityIndicatorVisible = true  // 네트워크 활동 시작
// 네트워크 요청 코드
app.isNetworkActivityIndicatorVisible = false  // 네트워크 활동 완료
```

### 3. NetworkActivityIndicator 사용 예시

실제로 네트워크 요청을 보내는 예시를 살펴보겠습니다. 아래 코드는 `URLSession`을 사용하여 GET 요청을 보내는 코드입니다.

```swift
func sendRequest() {
    let urlString = "https://api.example.com/data"
    guard let url = URL(string: urlString) else { return }

    // 네트워크 활동 시작
    UIApplication.shared.isNetworkActivityIndicatorVisible = true

    let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
        // 네트워크 응답 처리
        // ...

        // 네트워크 활동 완료
        DispatchQueue.main.async {
            UIApplication.shared.isNetworkActivityIndicatorVisible = false
        }
    }

    task.resume()
}
```

이 예시에서는 `sendRequest` 함수가 호출되었을 때, 네트워크 요청이 시작되고, 응답을 받을 때까지 NetworkActivityIndicator가 표시됩니다. 응답을 처리한 후에는 `DispatchQueue.main.async`를 사용하여 메인 스레드에서 `isNetworkActivityIndicatorVisible`를 다시 `false`로 설정합니다.

## 결론

Swift에서 NetworkActivityIndicator를 사용하면 애플리케이션의 네트워크 활동 상태를 사용자에게 시각적으로 전달할 수 있습니다. 앱의 사용자 경험을 향상시키기 위해 네트워크 요청 중에 인디케이터를 표시하는 것은 좋은 아이디어입니다. 사용자가 앱이 적극적으로 작업 중임을 알고 있다면, 더 나은 사용자 경험을 제공할 수 있습니다.

---

참고 자료:
- [UIApplication.shared](https://developer.apple.com/documentation/uikit/uiapplication/1623073-shared)
- [isNetworkActivityIndicatorVisible](https://developer.apple.com/documentation/uikit/uiapplication/1623053-isnetworkactivityindicatorvisible)