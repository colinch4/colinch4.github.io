---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 딜레이 및 반복 횟수 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 애니메이션 라이브러리입니다. 이 라이브러리를 사용하여 원하는 딜레이와 반복 횟수를 설정할 수 있습니다. 이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView 애니메이션의 딜레이와 반복 횟수를 설정하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 설치하기

먼저 NVActivityIndicatorView를 설치해야 합니다. Swift 프로젝트의 `Podfile`에 다음과 같이 NVActivityIndicatorView를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 애니메이션 딜레이 설정하기

NVActivityIndicatorView의 애니메이션 딜레이를 설정하기 위해서는 `startAnimating()` 메서드를 호출하기 전에 딜레이를 설정해야 합니다. 다음 예제 코드를 참고하세요.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .blue, padding: nil)
activityIndicatorView.startAnimating()
DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
    activityIndicatorView.stopAnimating()
}
```

위 예제 코드에서는 `startAnimating()` 메서드를 호출한 후 `DispatchQueue`를 사용하여 2초 후에 `stopAnimating()` 메서드를 호출하여 애니메이션을 중지합니다.

## 애니메이션 반복 횟수 설정하기

NVActivityIndicatorView의 애니메이션 반복 횟수를 설정하기 위해서는 `startAnimating()` 메서드 호출 시 `numberOfLoops` 매개변수를 사용합니다. `numberOfLoops` 매개변수에 `-1`을 전달하면 무한 반복됩니다. 다음 예제 코드를 참고하세요.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .blue, padding: nil)
activityIndicatorView.startAnimating(numberOfLoops: -1)
```

위 예제 코드에서는 `startAnimating()` 메서드를 호출할 때 `numberOfLoops` 매개변수에 `-1`을 전달하여 애니메이션을 무한 반복합니다.

## 결론

이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView 애니메이션의 딜레이 및 반복 횟수를 설정하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 다양한 애니메이션 옵션과 설정을 제공하여 사용자 정의화를 할 수 있습니다. 더 자세한 정보를 원하신다면 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.