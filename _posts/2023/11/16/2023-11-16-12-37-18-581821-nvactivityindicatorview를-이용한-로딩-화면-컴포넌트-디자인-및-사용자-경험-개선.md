---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 로딩 화면 컴포넌트 디자인 및 사용자 경험 개선"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

로딩 화면은 앱이 데이터를 가져오거나 처리하는 동안 사용자에게 진행 상태를 시각적으로 알려주는 중요한 요소입니다. 이번에는 NVActivityIndicatorView를 사용하여 로딩 화면 컴포넌트를 디자인하고 사용자 경험을 개선하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS용 로딩 화면 컴포넌트입니다. 많은 스타일의 로딩 인디케이터를 제공하며, 간편한 인터페이스를 통해 로딩 상태를 설정하고 관리할 수 있습니다.

## 2. NVActivityIndicatorView 설치

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. 프로젝트의 Podfile에 다음 라인을 추가하고, 터미널에서 `pod install`을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## 3. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 먼저 `NVActivityIndicatorViewable` 프로토콜을 채택해야 합니다. 이 프로토콜은 로딩 화면을 표시하는 데 필요한 기능을 제공합니다. 아래는 사용 예시입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController, NVActivityIndicatorViewable {
    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 화면 표시
        startAnimating()

        // 데이터 가져오기 등의 작업 수행

        // 로딩 화면 종료
        stopAnimating()
    }
}
```

위의 예시에서 `startAnimating()` 메서드를 호출하여 로딩 화면을 표시하고, 작업이 완료된 후 `stopAnimating()` 메서드로 로딩 화면을 종료합니다.

## 4. 로딩 인디케이터 스타일 설정

NVActivityIndicatorView는 다양한 로딩 인디케이터 스타일을 제공합니다. 원하는 스타일로 변경하려면 `NVActivityIndicatorType` 열거형 값을 설정하면 됩니다. 아래는 몇 가지 인디케이터 스타일의 예시입니다.

```swift
NVActivityIndicatorType.circleStrokeSpin
NVActivityIndicatorType.ballBeat
NVActivityIndicatorType.lineScale
```

다음 예시는 로딩 인디케이터 스타일을 설정하는 방법입니다.

```swift
NVActivityIndicatorView.DEFAULT_TYPE = .circleStrokeSpin
```

## 5. 커스텀 로딩 화면 디자인

NVActivityIndicatorView는 미리 정의된 스타일을 제공하지만, 앱의 디자인에 맞게 커스텀 로딩 화면을 디자인할 수도 있습니다. `NVActivityIndicatorViewable` 프로토콜을 채택한 클래스에서 `activityIndicatorView` 속성을 통해 인디케이터 뷰에 직접 접근할 수 있습니다.

```swift
class CustomViewController: UIViewController, NVActivityIndicatorViewable {
    override func viewDidLoad() {
        super.viewDidLoad()

        // 커스텀 인디케이터 뷰를 추가
        let customIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulseSync, color: .red)
        customIndicatorView.center = view.center
        view.addSubview(customIndicatorView)

        // 커스텀 인디케이터 뷰를 사용해서 로딩 화면 표시
        startAnimating(nil, style: .custom(customIndicatorView))
    }
}
```

위의 예시는 커스텀 인디케이터 뷰를 추가하여 로딩 화면을 디자인하는 방법을 보여줍니다.

## 6. 결과

NVActivityIndicatorView를 사용하여 로딩 화면 컴포넌트를 디자인하고 사용자 경험을 개선했습니다. 로딩 인디케이터 스타일을 선택하거나 커스텀 디자인을 적용하여 앱의 로딩 화면을 더욱 직관적이고 매력적으로 만들 수 있습니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.