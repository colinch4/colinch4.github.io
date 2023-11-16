---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 완료 후 콜백 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 앱에서 쉽게 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 이 라이브러리를 사용하여 로딩 중에 애니메이션을 보여줄 수 있습니다. 이번에는 NVActivityIndicatorView가 애니메이션을 완료한 후에 콜백 함수를 호출하는 방법에 대해 알아보겠습니다.

NVActivityIndicatorView를 사용하기 위해 아래와 같이 라이브러리를 설치합니다. Podfile에 다음 코드를 추가하고 `pod install`을 실행하세요.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 애니메이션 완료 콜백 설정하기

먼저, 필요한 파일에서 NVActivityIndicatorView를 import해야 합니다.

```swift
import NVActivityIndicatorView
```

NVActivityIndicatorView를 사용하여 로딩 애니메이션을 생성하고 보여주는 코드는 아래와 같습니다. 여기서 `type`은 로딩 애니메이션의 종류를 나타냅니다. `startAnimating()` 메소드를 호출하면 애니메이션이 시작됩니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: view.frame, type: .ballRotateChase)
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

NVActivityIndicatorView의 애니메이션이 완료되면 콜백 함수를 호출하려면 `stopAnimating()` 메소드를 호출한 다음에 원하는 콜백 함수를 작성하면 됩니다. 예를 들어, 아래와 같이 구현할 수 있습니다.

```swift
activityIndicatorView.stopAnimating()
myCallbackFunction()
```

위의 코드에서 `myCallbackFunction()`은 로딩 애니메이션이 완료된 후 실행될 로직을 나타냅니다. 원하는 작업을 수행하는 코드를 해당 함수에 작성하면 됩니다.

이제 Swift에서 NVActivityIndicatorView 애니메이션 완료 후 콜백 함수를 설정하는 방법을 알게 되었습니다. 이를 활용하여 로딩 인디케이터를 사용할 때 원하는 작업을 수행할 수 있습니다.

## 참고 자료
- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)