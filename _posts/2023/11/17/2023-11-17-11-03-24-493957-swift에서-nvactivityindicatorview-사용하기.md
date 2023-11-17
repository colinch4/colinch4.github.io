---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 사용하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift 언어에서 **NVActivityIndicatorView** 라이브러리를 사용하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 로딩 인디케이터를 제공하는 라이브러리로, 널리 사용되며 사용하기도 매우 쉽습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 로딩 인디케이터 라이브러리입니다. 다양한 스타일과 크기로 로딩 인디케이터를 표시할 수 있으며, 많은 기능과 설정 옵션을 제공합니다.

## 설치

먼저, NVActivityIndicatorView를 설치해야 합니다. `Podfile` 파일에 아래의 코드를 추가하고, 터미널에서 `pod install` 명령어를 실행하여 의존성을 설치합니다.

```swift
pod 'NVActivityIndicatorView'
```

## 사용 방법

1. 먼저, `NVActivityIndicatorView`를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 인디케이터를 초기화합니다. `NVActivityIndicatorView(frame: CGRect(x: x, y: y, width: width, height: height))`와 같이 프레임을 설정하여 초기화할 수 있습니다.

```swift
let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
let activityIndicatorView = NVActivityIndicatorView(frame: frame)
```

3. 원하는 스타일과 크기를 설정합니다. `type` 파라미터로 로딩 인디케이터의 스타일을 선택할 수 있습니다. 예를 들어, .ballSpinFadeLoader로 설정하면 돌아가는 공 로딩 인디케이터가 생성됩니다. `color` 파라미터는 로딩 인디케이터의 색상을 설정합니다.

```swift
activityIndicatorView.type = .ballSpinFadeLoader
activityIndicatorView.color = .blue
activityIndicatorView.startAnimating()
```

4. 화면에 로딩 인디케이터를 추가합니다.

```swift
self.view.addSubview(activityIndicatorView)
```

5. 로딩 인디케이터를 제거하려면 `stopAnimating()` 메서드를 호출합니다.

```swift
activityIndicatorView.stopAnimating()
```

## 예제

아래는 로딩 인디케이터를 사용하는 간단한 예제입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))

    override func viewDidLoad() {
        super.viewDidLoad()

        // 설정
        activityIndicatorView.type = .ballSpinFadeLoader
        activityIndicatorView.color = .blue

        // 화면에 추가
        self.view.addSubview(activityIndicatorView)
    }

    @IBAction func startButtonPressed(_ sender: UIButton) {
        // 로딩 시작
        activityIndicatorView.startAnimating()
    }

    @IBAction func stopButtonPressed(_ sender: UIButton) {
        // 로딩 중지
        activityIndicatorView.stopAnimating()
    }
}
```

위의 예제에서는 버튼을 누를 때마다 로딩 인디케이터가 시작하거나 중지되도록 구현되어 있습니다.

이제 Swift에서 NVActivityIndicatorView를 사용하는 방법을 알게 되었습니다. 이 라이브러리는 앱의 사용자 경험을 향상시키기 위해 로딩 인디케이터를 사용하는 데 적합합니다. 자세한 설정 옵션과 스타일에 대해서는 공식 문서를 참조해주세요.
 
## 참고 자료

- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView#usage)
- [스위프트 공식 홈페이지](https://swift.org/)
- [코코아포드 공식 홈페이지](https://cocoapods.org/)