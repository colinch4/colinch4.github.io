---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 지도 로딩 효과 적용하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

지도 앱에서 사용자가 지도 정보를 로딩할 때 로딩 효과를 적용하면 사용자 경험을 향상시킬 수 있습니다. 이를 위해 Swift에서 NVActivityIndicatorView 라이브러리를 사용하여 지도 로딩 효과를 적용하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 라이브러리 설치하기

먼저, NVActivityIndicatorView 라이브러리를 설치해야 합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다:

```ruby
target 'YourProjectTarget' do
  pod 'NVActivityIndicatorView'
end
```

그런 다음, 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 2. NVActivityIndicatorView를 사용하여 로딩 효과 적용하기

NVActivityIndicatorView를 사용하여 로딩 효과를 적용하려면 다음 단계를 따라야 합니다:

### 2.1 NVActivityIndicatorView 초기화하기

NVActivityIndicatorView를 초기화하려면 다음 코드를 사용합니다:

```swift
import NVActivityIndicatorView

class MapViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let activityIndicatorSize: CGFloat = 60
        let activityIndicatorFrame = CGRect(x: view.bounds.midX - activityIndicatorSize/2, y: view.bounds.midY - activityIndicatorSize/2, width: activityIndicatorSize, height: activityIndicatorSize)
        activityIndicatorView = NVActivityIndicatorView(frame: activityIndicatorFrame, type: .circleStrokeSpin, color: .white, padding: nil)
        activityIndicatorView.backgroundColor = .black
        activityIndicatorView.alpha = 0.5
        activityIndicatorView.layer.cornerRadius = 10
        view.addSubview(activityIndicatorView)
    }
    
    // ...
}
```

### 2.2 로딩 효과 시작 및 종료

로딩 효과를 시작하고 종료하려면 다음 코드를 사용합니다:

```swift
class MapViewController: UIViewController {

    // ...
    
    func startLoading() {
        activityIndicatorView.startAnimating()
    }
    
    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
    
    // ...
}
```

로딩 효과를 적용하려는 시점에 `startLoading()` 함수를 호출하여 로딩 효과를 시작하고, 로딩이 완료되면 `stopLoading()` 함수를 호출하여 로딩 효과를 종료합니다.

## 3. 로딩 효과 적용 예시

지도 로딩 시 로딩 효과를 적용하는 예시입니다:

```swift
class MapViewController: UIViewController {

    // ...
    
    func loadMapData() {
        startLoading()
        
        // 지도 데이터 로딩 및 초기화
        // ...
        
        stopLoading()
    }
    
    // ...
}
```

위 예시에서 `loadMapData()` 함수에서 `startLoading()` 함수를 호출하여 지도 데이터를 로딩할 때 로딩 효과를 시작하고, 로딩이 완료된 후에 `stopLoading()` 함수를 호출하여 로딩 효과를 종료합니다.

## 결론

Swift에서 NVActivityIndicatorView를 사용하여 지도 로딩 효과를 적용하는 방법을 알아보았습니다. 이를 통해 사용자 경험을 향상시킬 수 있고, 지도 앱에 더욱 동적인 요소를 추가할 수 있습니다. 다양한 NVActivityIndicatorView 스타일을 활용하여 원하는 로딩 효과를 구현해보세요!

## 참고 자료

- NVActivityIndicatorView GitHub 레포지토리: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)
- Cocoapods 공식 사이트: [https://cocoapods.org/](https://cocoapods.org/)
- Swift 공식 문서: [https://swift.org/documentation/](https://swift.org/documentation/)