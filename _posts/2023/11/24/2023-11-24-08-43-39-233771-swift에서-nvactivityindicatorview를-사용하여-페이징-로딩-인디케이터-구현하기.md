---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 페이징 로딩 인디케이터 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱에서 페이징 기능을 구현할 때 사용자에게 로딩 중임을 알려주기 위해 로딩 인디케이터를 표시하는 것이 일반적입니다. Swift에서는 NVActivityIndicatorView 라이브러리를 사용하여 간단하게 로딩 인디케이터를 구현할 수 있습니다.

이번 블로그 포스트에서는 NVActivityIndicatorView를 사용하여 페이징 로딩 인디케이터를 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 인디케이터를 구현하기 위한 오픈소스 라이브러리입니다. 이 라이브러리는 여러 가지 다양한 스타일의 인디케이터를 제공하며, 쉽게 커스터마이징할 수 있습니다. 또한 Swift와 Objective-C 모두에서 사용할 수 있습니다.

## NVActivityIndicatorView 설치하기

우선 CocoaPods를 통해 NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Podfile에 다음과 같이 추가한 후, `pod install` 명령어를 실행하세요.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

1. 먼저, `import NVActivityIndicatorView`를 사용하여 NVActivityIndicatorView를 가져옵니다.

2. 인디케이터를 표시할 UIView의 인스턴스를 생성합니다. 

```swift
let containerView = UIView()
```

3. 다음으로, NVActivityIndicatorView를 초기화 합니다. 인디케이터의 스타일과 크기를 설정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .white, padding: nil)
```

4. 인디케이터를 containerView에 추가하고, containerView를 원하는 위치에 추가합니다.

```swift
containerView.addSubview(activityIndicatorView)
containerView.center = CGPoint(x: view.bounds.width / 2, y: view.bounds.height / 2)
view.addSubview(containerView)
```

5. 원하는 시점에 `startAnimating()` 메소드를 호출하여 인디케이터를 시작합니다.

```swift
activityIndicatorView.startAnimating()
```

6. 작업이 완료되면 `stopAnimating()` 메소드를 호출하여 인디케이터를 정지합니다.

```swift
activityIndicatorView.stopAnimating()
```

7. 필요에 따라 인디케이터의 스타일이나 색상 등을 커스터마이징할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView) 페이지를 참조하세요.

이제 Swift에서 NVActivityIndicatorView를 사용하여 페이징 로딩 인디케이터를 구현할 수 있습니다. 사용자에게 로딩 중임을 알려주기 위해 NVActivityIndicatorView를 적극적으로 활용해 보세요!

---

**참고 자료:**

- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)
- [Swift](https://swift.org/)