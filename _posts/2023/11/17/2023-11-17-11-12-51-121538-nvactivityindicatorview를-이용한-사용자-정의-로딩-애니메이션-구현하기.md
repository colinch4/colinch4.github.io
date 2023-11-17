---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 정의 로딩 애니메이션 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱에서 사용자에게 로딩 상태를 시각적으로 표시하는 것은 사용자 경험을 향상시키는 데 매우 중요합니다. NVActivityIndicatorView는 Swift에서 사용할 수 있는 간단하고 멋진 로딩 애니메이션 라이브러리입니다. 이번 튜토리얼에서는 NVActivityIndicatorView를 이용하여 사용자 정의 로딩 애니메이션을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 애플리케이션에서 로딩 표시를 할 때 사용되는 Swift 라이브러리입니다. 다양한 스타일의 로딩 애니메이션을 제공하며, 사용자가 직접 스타일을 커스터마이징할 수도 있습니다.

## 시작하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 프로젝트에 해당 라이브러리를 추가해야 합니다. Cocoapods를 사용하여 NVActivityIndicatorView를 설치하려면 `Podfile`에 다음과 같이 추가하고 터미널에서 `pod install`을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## 구현하기

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화하고 애니메이션을 보여줄 뷰에 추가합니다. 이 예제에서는 UIView를 사용합니다.

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .blue, padding: nil)
view.addSubview(loadingView)
```

3. 로딩 애니메이션을 시작하거나 중지합니다. 예를 들어, 버튼을 눌렀을 때 로딩 애니메이션을 시작하고 데이터를 가져온 후에 중지할 수 있습니다.

```swift
@IBAction func startLoadingButtonTapped(_ sender: UIButton) {
    loadingView.startAnimating()
    
    // 로딩 애니메이션과 같이 수행할 작업
    fetchData()
    
    loadingView.stopAnimating()
}
```

4. 사용자 정의 옵션을 설정할 수도 있습니다. 예를 들어, 로딩 애니메이션의 색상과 크기를 변경하려면 다음과 같이 설정합니다.

```swift
loadingView.color = .red
loadingView.frame = CGRect(x: 0, y: 0, width: 100, height: 100)
```

## 결론

이제 NVActivityIndicatorView를 이용하여 사용자 정의 로딩 애니메이션을 구현하는 방법을 알게 되었습니다. 이 라이브러리를 사용하면 앱에 멋진 로딩 표시 기능을 추가할 수 있습니다. 보다 자세한 정보는 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하여 확인하실 수 있습니다.

더 많은 로딩 표시 라이브러리를 살펴보려면 다음 블로그 포스트를 확인해보세요:
- [Lottie를 이용한 로딩 애니메이션 구현하기](link)
- [MBProgressHUD를 이용한 사용자 정의 로딩 애니메이션 구현하기](link)