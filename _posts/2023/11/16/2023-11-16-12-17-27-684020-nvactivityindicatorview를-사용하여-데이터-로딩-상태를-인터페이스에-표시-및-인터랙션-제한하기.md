---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 인터페이스에 표시 및 인터랙션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

데이터를 로딩하는 동안 사용자에게 로딩 상태를 시각적으로 표시하는 것은 사용자 경험을 향상시키는 중요한 부분입니다. NVActivityIndicatorView는 iOS 애플리케이션에서 데이터 로딩 상태를 인터페이스에 표시하는 데 도움을 주는 유용한 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS용 로딩 인디케이터(loading indicator)입니다. 다양한 스타일과 커스터마이징 옵션을 제공하여 로딩 화면을 다양하게 만들 수 있습니다.

## 설치

NVActivityIndicatorView를 설치하려면 CocoaPods 또는 Carthage를 사용할 수 있습니다. 본 예제에서는 CocoaPods를 사용하도록 하겠습니다.

```swift
pod 'NVActivityIndicatorView'
```

설치가 완료되면 프로젝트 파일에서 `import NVActivityIndicatorView`를 추가해야 합니다.

## 사용 방법

먼저 NVActivityIndicatorView의 인스턴스를 생성합니다. 이를 위해 인디케이터의 크기와 색상을 지정할 수 있습니다. 다음은 인디케이터를 생성하는 예시입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScaleRipple, color: .white, padding: nil)
```

인디케이터의 크기와 색상을 앱의 디자인에 맞게 조정하세요.

다음으로, 인디케이터를 화면에 추가하고 시작하는 메소드를 만듭니다. 이 메소드는 데이터 로딩이 시작될 때 호출되어 사용자에게 로딩 상태를 시각적으로 보여줍니다.

```swift
func showLoadingIndicator() {
    // 인디케이터를 parentView에 추가합니다.
    parentView.addSubview(activityIndicatorView)
    
    // 인디케이터를 화면 중앙에 위치시킵니다.
    activityIndicatorView.center = parentView.center
    
    // 애니메이션을 시작합니다.
    activityIndicatorView.startAnimating()
    
    // 화면의 인터랙션을 제한합니다.
    parentView.isUserInteractionEnabled = false
}
```

위의 코드에서 `parentView`는 인디케이터가 표시될 부모 뷰입니다. `showLoadingIndicator` 메소드는 데이터 로딩이 시작될 때 호출하면 됩니다. 인디케이터를 parentView에 추가하고 화면 중앙에 위치시킨 다음, 애니메이션을 시작합니다. 마지막으로, `isUserInteractionEnabled` 속성을 false로 설정하여 화면의 인터랙션을 제한합니다.

로딩이 완료되면 인디케이터를 제거하고 인터랙션을 다시 활성화해주어야 합니다. 다음은 로딩이 완료되었을 때 호출되는 메소드를 추가하는 예시입니다.

```swift
func hideLoadingIndicator() {
    // 인디케이터를 제거합니다.
    activityIndicatorView.removeFromSuperview()
    
    // 화면의 인터랙션을 다시 활성화합니다.
    parentView.isUserInteractionEnabled = true
}
```

로딩이 완료되면 `hideLoadingIndicator` 메소드를 호출하여 인디케이터를 제거하고 인터랙션을 활성화합니다.

## 마무리

NVActivityIndicatorView를 사용하면 데이터 로딩 상태를 인터페이스에 표시하고 인터랙션을 제한할 수 있습니다. 이를 통해 사용자에게 로딩이 진행 중임을 시각적으로 안내하고 사용자 경험을 높일 수 있습니다. NVActivityIndicatorView의 다양한 스타일과 커스터마이징 옵션을 활용하여 앱의 로딩 인디케이터를 개선해보세요.

더 자세한 정보는 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하십시오.

**참고 자료:**
- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)