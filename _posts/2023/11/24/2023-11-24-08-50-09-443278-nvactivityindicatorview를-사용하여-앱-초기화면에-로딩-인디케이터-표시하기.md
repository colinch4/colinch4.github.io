---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 앱 초기화면에 로딩 인디케이터 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱의 초기화면에서 로딩 인디케이터를 표시하여 사용자에게 앱이 작업을 수행하고 있음을 시각적으로 알려줄 수 있습니다. 이를 위해 `NVActivityIndicatorView` 라이브러리를 사용하여 로딩 인디케이터를 구현할 수 있습니다.

## NVActivityIndicatorView란?

`NVActivityIndicatorView`는 다양한 스타일의 로딩 인디케이터를 제공하는 Swift 라이브러리입니다. 많은 인디케이터 스타일과 커스터마이징 옵션을 제공하여 다양한 디자인 요구에 맞게 사용할 수 있습니다.

## NVActivityIndicatorView 설치하기

`NVActivityIndicatorView`는 CocoaPods를 통해 설치할 수 있습니다. `Podfile`에 아래와 같이 추가한 후, `pod install` 명령을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

1. `NVActivityIndicatorView`의 인스턴스를 초기화합니다. 보여줄 스타일과 크기를 선택할 수 있습니다.

```swift
import NVActivityIndicatorView

let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .white, padding: 0)
```

2. 로딩 인디케이터를 위치시킬 뷰에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

3. 로딩 인디케이터를 가운데 정렬하기 위해 Auto Layout을 설정합니다.

```swift
activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false
activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
```

4. 로딩 인디케이터를 시작하고 멈추는 메소드를 정의합니다.

```swift
func startLoading() {
    activityIndicatorView.startAnimating()
}

func stopLoading() {
    activityIndicatorView.stopAnimating()
}
```

5. 로딩 인디케이터를 필요한 곳에서 시작 및 정지합니다. 예를 들어, 앱 초기화면에 로딩 인디케이터를 표시하려면 `viewDidAppear` 메소드에서 시작하고, 데이터 로딩이 완료된 후에 정지합니다.

```swift
override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)
    startLoading()
    
    // 데이터 로딩 완료 후
    stopLoading()
}
```

## 커스터마이징하기

`NVActivityIndicatorView`는 다양한 커스터마이징 옵션을 제공합니다. 예를 들어, 인디케이터의 색상과 크기, 애니메이션 속도 등을 변경할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.

## 결론

`NVActivityIndicatorView`를 사용하면 앱 초기화면에 로딩 인디케이터를 쉽게 구현할 수 있습니다. 사용자에게 앱이 작업 중임을 시각적으로 알려줌으로써 더 나은 사용자 경험을 제공할 수 있습니다.

**참고 자료:**
- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)