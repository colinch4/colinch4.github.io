---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 딜레이 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS에서 간단한 로딩 애니메이션을 구현하기 위한 라이브러리입니다. 이 라이브러리를 사용하여 애니메이션에 딜레이를 추가하는 방법에 대해 알아보겠습니다.

먼저, NVActivityIndicatorView를 프로젝트에 추가합니다. CocoaPods를 사용하는 경우, Podfile에 다음 줄을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

이제 NVActivityIndicatorView를 사용하기 위해 `import NVActivityIndicatorView` 구문을 작성합니다.

```swift
import NVActivityIndicatorView
```

애니메이션을 표시할 뷰 컨트롤러에서 NVActivityIndicatorView를 초기화하고 설정합니다. 딜레이를 적용할 경우 애니메이션이 표시되기 전에 잠시 멈추도록 설정해야 합니다.

```swift
class ViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 애니메이션을 표시할 뷰 크기와 위치를 설정합니다.
        let frame = CGRect(x: 0, y: 0, width: 100, height: 100)
        activityIndicatorView = NVActivityIndicatorView(frame: frame)

        // 사용할 애니메이션 유형을 선택합니다.
        // .ballRotateChase 애니메이션 예시입니다.
        let animationType = NVActivityIndicatorType.ballRotateChase
        activityIndicatorView.type = animationType

        // 애니메이션 딜레이를 설정합니다. 여기서는 2초로 설정하겠습니다.
        let delay: TimeInterval = 2
        activityIndicatorView.startAnimatingWithDelay(delay)

        // 뷰에 애니메이션 뷰를 추가합니다.
        view.addSubview(activityIndicatorView)
    }
}
```

이제 다음과 같이 애니메이션 딜레이가 적용된 NVActivityIndicatorView를 사용할 수 있습니다. 애니메이션이 시작되기 전에 2초 동안 딜레이가 발생합니다.

```swift
let delay: TimeInterval = 2
activityIndicatorView.startAnimatingWithDelay(delay)
```


이제 NVActivityIndicatorView를 사용하여 애니메이션에 딜레이를 설정하는 방법에 대해 알게 되었습니다. 이를 통해 앱의 로딩 화면 등에서 사용자에게 공간적 또는 시간적으로 여유를 줄 수 있습니다.

더 많은 NVActivityIndicatorView의 사용 방법은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.