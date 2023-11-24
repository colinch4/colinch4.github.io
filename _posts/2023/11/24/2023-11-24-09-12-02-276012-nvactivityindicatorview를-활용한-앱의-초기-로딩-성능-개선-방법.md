---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 앱의 초기 로딩 성능 개선 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱의 초기 로딩 성능은 사용자 경험에 큰 영향을 미칩니다. 특히 대용량 파일 또는 네트워크 요청과 같은 작업들이 필요한 경우, 사용자는 기다리는 동안 앱이 지루하거나 느릴 수 있다고 느낄 수 있습니다. 이러한 문제를 해결하기 위해 NVActivityIndicatorView를 사용하여 앱의 초기 로딩 성능을 개선하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift 언어로 작성된 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 앱에서 대기 시간을 시각적으로 나타내는데 사용됩니다. 다양한 스타일과 색상으로 로딩 인디케이터를 커스터마이징할 수 있으며, 간편하게 구현할 수 있습니다.

## NVActivityIndicatorView를 설치하기

NVActivityIndicatorView를 설치하려면 먼저 CocoaPods 또는 Swift Package Manager를 사용하여 프로젝트에 종속성을 추가해야합니다. 

#### CocoaPods를 사용하는 경우

```ruby
pod 'NVActivityIndicatorView'
```

#### Swift Package Manager를 사용하는 경우

Xcode에서 프로젝트를 열고 `File` -> `Swift Packages` -> `Add Package Dependency`를 선택한 다음, `https://github.com/ninjaprox/NVActivityIndicatorView.git`를 입력하여 종속성을 추가합니다.

## NVActivityIndicatorView 사용 방법

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 원하는 위치에 NVActivityIndicatorView의 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. 원하는 스타일과 색상으로 인디케이터를 설정합니다.

```swift
activityIndicatorView.type = .ballSpinFadeLoader
activityIndicatorView.color = UIColor.red
```

4. 인디케이터를 화면에 추가하고, 시작 또는 중지합니다.

```swift
view.addSubview(activityIndicatorView)

// 인디케이터 시작
activityIndicatorView.startAnimating()

// 인디케이터 중지
activityIndicatorView.stopAnimating()
```

5. 필요에 따라 인디케이터의 크기와 위치를 조정할 수 있습니다.

```swift
activityIndicatorView.frame = CGRect(x: view.center.x - 25, y: view.center.y - 25, width: 50, height: 50)
```

## 초기 로딩 성능 개선을 위한 활용 방법

NVActivityIndicatorView를 사용하여 초기 로딩 성능을 개선하려면 다음과 같은 방법을 고려해볼 수 있습니다.

### 1. 네트워크 요청 전 로딩 인디케이터 표시

네트워크 요청이 필요한 작업이 있을 때, 해당 작업을 수행하기 전에 로딩 인디케이터를 화면에 표시합니다. 이렇게하면 사용자는 작업이 진행 중임을 알아차리고 실제 작업이 시작되기를 기다릴 필요가 없습니다.

```swift
activityIndicatorView.startAnimating()
networkRequest(completion: { response in
    activityIndicatorView.stopAnimating()
    // 작업 완료 시 로직 처리
})
```

### 2. 비동기 작업 시 로딩 인디케이터 표시

비동기 작업을 수행할 때는 작업이 시작되는 동안 로딩 인디케이터를 표시하여 사용자에게 진행 중임을 알리는 것이 좋습니다.

```swift
activityIndicatorView.startAnimating()
DispatchQueue.global().async {
    // 비동기 작업 수행
    DispatchQueue.main.async {
        activityIndicatorView.stopAnimating()
        // 작업 완료 시 로직 처리
    }
}
```

### 3. 데이터 로딩 시 로딩 인디케이터 표시

대용량의 데이터를 로딩하는 작업이 있을 때는 사용자에게 작업이 진행 중임을 알리는 로딩 인디케이터를 표시해야 합니다. 이렇게 하면 사용자는 로딩이 계속되고 있는지 알 수 있고, 카드 또는 스피너와 같은 로딩 UI를 통해 진행 상황을 시각적으로 확인할 수 있습니다.

```swift
activityIndicatorView.startAnimating()
loadData(completion: { data in
    activityIndicatorView.stopAnimating()
    // 데이터 로딩 완료 시 로직 처리
})
```

## 결론

NVActivityIndicatorView를 사용하여 앱의 초기 로딩 성능을 개선하는 방법을 알아보았습니다. 이를 활용하여 사용자에게 로딩 중임을 알리고, 사용자 경험을 향상시키는데 도움이 될 것입니다. NVActivityIndicatorView를 사용하여 앱의 초기 로딩을 성능 개선하는 데 성공하세요!

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://ninjaprox.github.io/NVActivityIndicatorView)
- [CocoaPods](https://cocoapods.org/)
- [Swift Package Manager](https://swift.org/package-manager/)