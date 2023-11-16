---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱을 개발하다 보면 네트워크 요청이나 데이터 로딩 등 시간이 걸리는 작업이 있을 때 사용자에게 로딩 중임을 알려주는 것이 중요합니다. 이를 위해 NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 개발자들이 앱 내에서 로딩 중임을 나타내기 위해 사용할 수 있는 오픈 소스 라이브러리입니다. Circle, Line, Native 등 다양한 스타일과 커스터마이징 옵션을 제공하여 다양한 로딩 애니메이션을 구현할 수 있습니다.

## 설치

NVActivityIndicatorView는 CocoaPods를 통해 손쉽게 설치할 수 있습니다. `Podfile`에 아래와 같이 추가한 후, 터미널에서 `pod install` 명령을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## 사용법

1. `import NVActivityIndicatorView` 문을 통해 라이브러리를 로드합니다.
2. `NVActivityIndicatorView` 인스턴스를 생성하고 원하는 프레임과 스타일을 지정합니다.
3. 로딩 중인 상태를 나타내기 위해 `startAnimating()` 메서드를 호출합니다.
4. 작업이 완료되면 `stopAnimating()` 메서드를 호출하여 애니메이션을 중지합니다.

다음은 간단한 사용 예제입니다:

```swift
import UIKit
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 인스턴스 생성
        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .gray, padding: nil)
        
        // 현재 뷰에 추가
        view.addSubview(activityIndicatorView)

        // 중앙 정렬
        activityIndicatorView.center = view.center
        
        // 로딩 시작
        activityIndicatorView.startAnimating()

        // 3초 후 로딩 중지
        DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
            activityIndicatorView.stopAnimating()
        }
    }
}
```

## 커스터마이징

NVActivityIndicatorView는 다양한 커스터마이징 옵션을 제공합니다. 스타일, 크기, 색상 등을 변경하여 앱에 맞는 로딩 애니메이션을 만들 수 있습니다. 자세한 내용은 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.

## 결론

NVActivityIndicatorView를 사용하면 앱에서 로딩 상태를 시각적으로 표현할 수 있습니다. 이를 통해 사용자에게 작업이 진행 중임을 알리고 UX를 향상시킬 수 있습니다.