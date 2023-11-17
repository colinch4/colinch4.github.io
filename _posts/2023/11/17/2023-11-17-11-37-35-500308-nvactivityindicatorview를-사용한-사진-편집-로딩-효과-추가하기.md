---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 사진 편집 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요
이번 튜토리얼에서는 NVActivityIndicatorView를 사용하여 사진 편집 로딩 효과를 추가하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 로딩 중에 사용자에게 시각적인 피드백을 제공하는 데에 도움이 되는 라이브러리입니다.

## NVActivityIndicatorView 설치하기
먼저, NVActivityIndicatorView를 프로젝트에 설치해야합니다. `Podfile`에 다음과 같은 코드를 추가하고 `pod install` 명령어를 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기
1. NVActivityIndicatorView를 사용할 뷰 컨트롤러 또는 뷰에 import 문을 추가하세요.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView의 인스턴스를 생성합니다. 로딩 효과를 보여줄 위치와 스타일을 설정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: UIColor.gray, padding: nil)
```

3. 로딩 효과를 보여줄 위치에 NVActivityIndicatorView를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
```

4. 로딩 효과를 멈추고 제거할 때는 다음 코드를 사용합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 예제 코드
다음은 NVActivityIndicatorView를 사용하여 사진 편집 로딩 효과를 추가하는 예제 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class PhotoEditorViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: UIColor.gray, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()

        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)

        activityIndicatorView.startAnimating()
        // 사진 편집 로직 실행
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)

        activityIndicatorView.stopAnimating()
        activityIndicatorView.removeFromSuperview()
    }
}
```

## 결론
NVActivityIndicatorView를 사용하여 사진 편집 로딩 효과를 추가하는 방법을 알아보았습니다. 이제 사용자에게 로딩 중임을 시각적으로 표시하여 더 나은 사용자 경험을 제공할 수 있습니다.

## 참고 자료
- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://ninjaprox.github.io/NVActivityIndicatorView/)