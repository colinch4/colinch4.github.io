---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현하고 사용자 인터랙션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱 개발시에는 서버와의 통신이나 데이터 로딩 등의 작업이 필요할 때가 있습니다. 이러한 작업을 할 때에는 사용자에게 작업 진행 상태를 시각적으로 표현하여 효과적인 사용자 경험을 제공하는 것이 중요합니다. 이를 위해 NVActivityIndicatorView 라이브러리를 사용하여 화면 로딩 상태를 시각적으로 표현하고, 동시에 사용자의 인터랙션을 제한하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 상태를 표현하기 위한 오픈 소스 라이브러리입니다. 다양한 로딩 애니메이션 스타일을 제공하며, 쉽게 사용할 수 있습니다.

## NVActivityIndicatorView 설치하기

먼저, Cocoapods을 사용하여 NVActivityIndicatorView를 프로젝트에 추가해야 합니다. 

```swift
pod 'NVActivityIndicatorView'
```

프로젝트 디렉토리에서 터미널을 열고 다음 명령어를 실행하세요.

```bash
pod install
```

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .white, padding: nil)
```

- frame: 로딩 애니메이션을 표시할 뷰의 위치와 크기를 지정합니다.
- type: 로딩 애니메이션의 스타일을 선택합니다.
- color: 로딩 애니메이션의 색상을 지정합니다.
- padding: 로딩 애니메이션의 패딩 값을 설정할 수도 있습니다.

3. 로딩 애니메이션을 표시할 뷰에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

4. 로딩 애니메이션을 시작합니다.

```swift
activityIndicatorView.startAnimating()
```

5. 작업이 완료되면 로딩 애니메이션을 중지하고 화면에서 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 사용자 인터랙션 제한하기

로딩 애니메이션을 표시할 때에는 사용자의 인터랙션을 제한하여 작업이 완료될 때까지 다른 작업을 수행하지 못하도록 해야합니다. NVActivityIndicatorView는 활성화되거나 비활성화될 때 사용자 인터랙션을 제어하는 기능을 제공합니다.

1. 활성화 시에는 사용자 인터랙션을 제한합니다.

```swift
NVActivityIndicatorView.DEFAULT_BLOCKER_SIZE = CGSize(width: 50, height: 50)
NVActivityIndicatorView.DEFAULT_BLOCKER_MESSAGE = "Loading..."
activityIndicatorView.startAnimating(blockUI: true)
```

2. 비활성화 시에는 사용자 인터랙션을 허용합니다.

```swift
activityIndicatorView.stopAnimating(removeFromSuperView: true, blockUI: true)
```

## 결론

NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현하고 사용자 인터랙션을 제한할 수 있습니다. 이를 통해 앱 사용자에게 작업 진행 상태를 명확하게 전달하고, 로딩 중에는 다른 작업을 수행할 수 없도록 제한할 수 있습니다. NVActivityIndicatorView의 다양한 옵션과 기능을 활용하여 사용자에게 최적의 경험을 제공하세요.

## 참고 자료

- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)