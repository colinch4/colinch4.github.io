---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 활용하기 - 도시 가이드 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift 프로그래밍 언어를 사용하여 NVActivityIndicatorView를 활용하여 도시 가이드 앱의 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 화면을 구현하기 위한 오픈 소스 라이브러리입니다. 이 라이브러리는 많은 다양한 스타일의 로딩 인디케이터를 제공하여 사용자에게 진행 중임을 시각적으로 표시할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods을 설치해야 합니다. 터미널에서 다음 명령을 실행하여 CocoaPods을 설치하세요:

```
$ sudo gem install cocoapods
```

다음으로, 프로젝트의 `Podfile`에 NVActivityIndicatorView를 추가하고 Cocoapods을 통해 라이브러리를 설치합니다. `Podfile`에 다음 내용을 추가하세요:

```
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령을 실행하여 라이브러리를 설치합니다:

```
$ pod install
```

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 사용할 Swift 파일로 이동합니다.
2. 해당 파일의 상단에 `import NVActivityIndicatorView`를 추가합니다.
3. 다음과 같이 NVActivityIndicatorView 인스턴스를 생성합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
```

- `frame`: 로딩 인디케이터의 프레임을 설정합니다.
- `type`: 로딩 인디케이터의 스타일을 설정합니다. 다양한 스타일을 사용할 수 있습니다.
- `color`: 로딩 인디케이터의 색상을 설정합니다.
- `padding`: 로딩 인디케이터의 패딩을 설정합니다. 필요하지 않은 경우 `nil`로 설정할 수 있습니다.

4. 로딩 인디케이터를 추가할 뷰에 다음과 같이 인디케이터를 addSubview합니다:

```swift
view.addSubview(activityIndicatorView)
```

5. 로딩 화면을 시작하려면 다음과 같이 `startAnimating` 메서드를 호출합니다:

```swift
activityIndicatorView.startAnimating()
```

6. 로딩 화면을 종료하려면 다음과 같이 `stopAnimating` 메서드를 호출합니다:

```swift
activityIndicatorView.stopAnimating()
```

## 예제 코드

다음은 NVActivityIndicatorView를 활용하여 도시 가이드 로딩 화면을 구현하는 예제 코드입니다:

```swift
import UIKit
import NVActivityIndicatorView

class GuideViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addSubview(activityIndicatorView)
    }

    func showLoadingScreen() {
        activityIndicatorView.startAnimating()
    }

    func hideLoadingScreen() {
        activityIndicatorView.stopAnimating()
    }
}
```

위의 코드에서 `showLoadingScreen` 메서드를 호출하여 로딩 화면을 시작하고, `hideLoadingScreen` 메서드를 호출하여 로딩 화면을 종료할 수 있습니다.

## 마무리

이제 NVActivityIndicatorView를 사용하여 도시 가이드 로딩 화면을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 앱의 사용자 경험을 향상시키고 진행 중 상태를 시각적으로 표시할 수 있습니다. 참고로 NVActivityIndicatorView에 대한 자세한 내용은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 확인해보세요.