---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 로딩 화면 디자인 및 사용자 피드백 개선 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

로딩 화면은 앱에서 사용자 경험을 개선하기 위해 중요한 부분입니다. NVActivityIndicatorView라는 Swift 기반의 개발자 도구를 사용하면 로딩 화면을 구현하는 것이 간단해집니다. 이번 블로그 글에서는 NVActivityIndicatorView를 사용하여 로딩 화면을 디자인하는 방법과 사용자 피드백을 개선하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 화면을 표시하기 위한 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 사용자가 더 나은 사용자 경험을 느낄 수 있도록 도와줍니다.

## 설치하기

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음과 같은 내용을 추가해주세요.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치해주세요.

```bash
pod install
```

## 사용하기

NVActivityIndicatorView를 사용하여 로딩 화면을 디자인하는 방법은 매우 간단합니다. 아래 코드에 따라 로딩 화면을 추가할 수 있습니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 인디케이터 생성
        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)

        // 인디케이터를 화면 중앙에 위치시키기 위해 오토레이아웃 설정
        activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(activityIndicatorView)

        NSLayoutConstraint.activate([
            activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])

        // 인디케이터 실행
        activityIndicatorView.startAnimating()
    }

}
```

위 코드에서는 로딩 인디케이터를 생성하고, 화면 중앙에 위치시키기 위해 오토레이아웃 제약을 설정한 뒤 실행시킵니다. 로딩이 끝나면 `stopAnimating()` 함수를 호출하여 인디케이터를 중지시킬 수 있습니다.

## 사용자 피드백 개선하기

로딩 화면은 사용자에게 현재 작업이 진행 중임을 알리는 역할을 합니다. 높은 사용성을 위해 몇 가지 사용자 피드백 개선 방법을 적용해보겠습니다.

### 1. 로딩 메시지 표시

로딩 화면에 작업의 진행 상태 또는 어떤 작업이 진행 중인지에 대한 메시지를 함께 표시하면 사용자가 작업이 마무리되길 기다리는 동안 더 나은 사용자 경험을 제공할 수 있습니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 인디케이터 생성
        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)

        // 인디케이터를 화면 중앙에 위치시키기 위해 오토레이아웃 설정
        activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(activityIndicatorView)

        // 메시지 레이블 생성
        let messageLabel = UILabel()
        messageLabel.text = "로딩 중..."
        messageLabel.textColor = .gray
        messageLabel.textAlignment = .center
        messageLabel.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(messageLabel)

        NSLayoutConstraint.activate([
            activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
            messageLabel.topAnchor.constraint(equalTo: activityIndicatorView.bottomAnchor, constant: 16),
            messageLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor)
        ])

        // 인디케이터 실행
        activityIndicatorView.startAnimating()
    }

}
```

위 코드에서는 로딩 메시지를 표시하기 위해 UILabel을 생성하고, 이를 인디케이터 아래에 배치합니다. 메시지는 작업의 진행 상태에 맞게 업데이트할 수 있습니다.

### 2. 로딩 화면 디자인 수정

NVActivityIndicatorView는 다양한 로딩 인디케이터 스타일을 제공합니다. 로딩 화면의 디자인을 수정하여 인디케이터를 더욱 매력적으로 표현할 수 있습니다. 아래는 스타일을 변경하여 로딩 화면에 다양한 효과를 적용하는 예입니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 인디케이터 생성. 다른 스타일로 변경해보세요.
        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .orbit, color: .gray, padding: nil)

        // 인디케이터를 화면 중앙에 위치시키기 위해 오토레이아웃 설정
        activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(activityIndicatorView)

        NSLayoutConstraint.activate([
            activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])

        // 인디케이터 실행
        activityIndicatorView.startAnimating()
    }

}
```

위 코드에서는 `type: .orbit`으로 스타일을 변경하여 Orbit 스타일의 인디케이터를 사용하도록 설정하였습니다. 다른 스타일을 사용해보고 어떤 것이 앱에 가장 잘 어울리는지 확인해보세요.

## 결론

NVActivityIndicatorView를 사용하여 로딩 화면을 디자인하고 사용자 피드백을 개선하는 방법에 대해 알아보았습니다. 로딩 화면은 앱의 사용자 경험을 향상시키기 위해 필수적인 요소 중 하나입니다. NVActivityIndicatorView를 통해 로딩 화면을 손쉽게 구현할 수 있으므로, 앱에 로딩 화면을 추가하여 사용자에게 더 나은 경험을 제공해보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)