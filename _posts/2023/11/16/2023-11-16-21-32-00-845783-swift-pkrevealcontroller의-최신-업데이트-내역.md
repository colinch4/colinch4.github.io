---
layout: post
title: "[swift] Swift PKRevealController의 최신 업데이트 내역"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift PKRevealController는 iOS 앱에서 햄버거 메뉴 기능을 제공하는 라이브러리입니다. 이 라이브러리는 앱의 사용자 인터페이스를 향상시키고 사용자가 좀 더 편리하게 앱을 사용할 수 있도록 도와줍니다. 최근에 Swift PKRevealController에는 몇 가지 중요한 업데이트가 이루어졌습니다. 이제 해당 업데이트 내용에 대해 알아보겠습니다.

## v2.0.0: 메이저 업데이트

- Swift 5를 지원하도록 업데이트되었습니다.
- iOS 13의 다크 모드와 호환되도록 향상되었습니다.
- Xcode 11과의 완벽한 호환성을 제공합니다.
- 최소한의 메모리 사용량을 위해 성능을 최적화했습니다.
- 버그 수정 및 일반적인 개선 사항이 포함되어 있습니다.

예제 코드:

```swift
import PKRevealController

class ViewController: PKRevealController {
    override func viewDidLoad() {
        super.viewDidLoad()
        // 햄버거 메뉴 구성 요소 추가 및 설정
        let menuViewController = MenuViewController()
        let mainViewController = MainViewController()
        
        self.setLeftViewController(menuViewController)
        self.setMainViewController(mainViewController)
    }
}
```

업데이트된 Swift PKRevealController에 대한 자세한 내용은 [공식 GitHub 레포지토리](https://github.com/pkluz/PKRevealController)에서 확인할 수 있습니다.