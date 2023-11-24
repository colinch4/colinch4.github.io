---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 네트워크 통신 처리 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 소개

이번 포스트에서는 Swift에서 네트워크 통신 처리 중에 사용자에게 진행 상태를 표시하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 Swift에서 널리 사용되는 라이브러리로, 네트워크 요청이나 데이터 로딩 등의 작업 중에 진행 상태를 시각적으로 보여줄 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. 프로젝트의 Podfile에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 사용하기 위해 import 문을 작성합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 사용할 뷰 컨트롤러에 UIView 인스턴스를 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .gray, padding: nil)
```

3. 네트워크 통신 작업을 시작할 때, 다음과 같이 activityIndicatorView를 뷰에 추가하고 시작 메소드를 호출합니다.

```swift
self.view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

4. 네트워크 통신 작업이 완료되었을 때, 다음과 같이 activityIndicatorView를 제거하고 애니메이션을 중지시킵니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 사용 예제

아래는 실제로 NVActivityIndicatorView를 사용하여 네트워크 통신 처리 중에 상태를 표시하는 예제 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .gray, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()

        // activityIndicatorView를 뷰에 추가
        self.view.addSubview(activityIndicatorView)
    }

    func loadData() {
        // 데이터 로딩 시작 전에 activityIndicatorView 애니메이션 시작
        activityIndicatorView.startAnimating()

        // 네트워크 통신 작업 수행

        // 데이터 로딩 완료 후에 activityIndicatorView 애니메이션 중지 및 제거
        activityIndicatorView.stopAnimating()
        activityIndicatorView.removeFromSuperview()
    }
}
```

## 결론

Swift에서 NVActivityIndicatorView를 사용하여 네트워크 통신 처리 중에 진행 상태를 표시하는 방법을 알아보았습니다. NVActivityIndicatorView는 간단한 구현으로 진행 상황을 사용자에게 시각적으로 표시할 수 있어 편리합니다. 이를 통해 사용자는 장시간의 작업을 할 때에도 진행 상태를 확인할 수 있으므로 UX를 향상시킬 수 있습니다.

## 참고자료

- [NVActivityIndicatorView 공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)