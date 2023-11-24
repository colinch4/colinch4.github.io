---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 애니메이션 효과 예시"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서 NVActivityIndicatorView는 로딩 인디케이터에 사용되는 애니메이션 효과를 구현하는 유용한 도구입니다. 이를 이용하여 앱의 로딩 화면 등에 다양한 애니메이션 효과를 부여할 수 있습니다.

NVActivityIndicatorView는 Cocoapods를 통해 설치할 수 있습니다. 먼저, Podfile에 다음과 같이 추가해주세요:

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드 및 설치합니다.

이제 애니메이션을 적용할 뷰컨트롤러에 다음과 같이 코드를 작성해보겠습니다:

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicator: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 액티비티 인디케이터 초기화
        activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .blue, padding: nil)
        activityIndicator.center = self.view.center
        
        self.view.addSubview(activityIndicator)
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        // 액티비티 인디케이터 시작
        activityIndicator.startAnimating()
        
        // 로딩 시간이 지난 후 액티비티 인디케이터 종료
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            self.activityIndicator.stopAnimating()
        }
    }
}
```

위 코드에서는 `NVActivityIndicatorView`를 `ViewController` 안에 추가하였습니다. `viewDidLoad`에서 `NVActivityIndicatorView`를 초기화하고, `viewDidAppear`에서 액티비티 인디케이터를 시작하고 3초 후에 종료하도록 설정하였습니다.

여러분은 `type` 매개변수를 통해 다양한 애니메이션 효과를 선택할 수 있습니다. `color` 매개변수를 통해 원하는 색상을 지정할 수도 있습니다.

이제 코드를 실행하면 액티비티 인디케이터가 화면 중앙에서 시작되고 3초 후에 종료됩니다.

더 많은 애니메이션 효과와 커스터마이징 옵션을 알아보려면 [NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)의 공식 GitHub 페이지를 참조해주세요.