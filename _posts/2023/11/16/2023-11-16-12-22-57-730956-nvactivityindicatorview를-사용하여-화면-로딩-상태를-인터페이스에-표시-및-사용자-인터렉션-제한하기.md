---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 인터페이스에 표시 및 사용자 인터렉션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

애플리케이션에서 데이터를 가져오거나 긴 처리 작업을 수행할 때, 사용자에게 로딩 상태를 시각적으로 표시하는 것은 좋은 UX(User Experience)입니다. 이를 위해 NVActivityIndicatorView라는 오픈 소스 라이브러리를 사용하여 화면 로딩 상태를 인터페이스에 표시하고, 사용자의 인터렉션을 제한할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 애플리케이션에서 사용할 수 있는 간단하고 유연한 로딩 인디케이터 라이브러리입니다. 다양한 모양과 스타일의 로딩 인디케이터를 제공하여, 애플리케이션의 디자인에 맞게 로딩 상태를 표시할 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 통해 라이브러리를 설치해야 합니다. 

```swift
// Podfile에 추가
pod 'NVActivityIndicatorView'
```

터미널을 열고 프로젝트 폴더로 이동한 후, 다음 명령어를 실행하여 Cocoapods를 설치합니다.

```bash
pod install
```

## NVActivityIndicatorView 사용법

라이브러리를 설치했다면, 이제 코드에서 NVActivityIndicatorView를 사용하여 화면 로딩 상태를 표시할 수 있습니다. 먼저, ViewController에 NVActivityIndicatorView를 추가하고, 인디케이터의 모양과 스타일을 설정합니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicator: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 인디케이터의 위치와 크기 설정
        let frame = CGRect(x: 0, y: 0, width: 100, height: 100)
        activityIndicator = NVActivityIndicatorView(frame: frame)

        // 인디케이터의 모양과 스타일 설정
        activityIndicator.type = .ballSpinFadeLoader
        activityIndicator.color = UIColor.blue

        // 뷰에 인디케이터 추가
        view.addSubview(activityIndicator)
    }

    // 로딩 상태 표시 및 사용자 인터렉션 제한
    func showLoading() {
        // 화면에 인디케이터 표시
        activityIndicator.startAnimating()

        // 사용자 인터렉션 제한
        view.isUserInteractionEnabled = false
    }

    // 로딩 상태 종료 및 사용자 인터렉션 가능
    func hideLoading() {
        // 화면에서 인디케이터 제거
        activityIndicator.stopAnimating()

        // 사용자 인터렉션 가능
        view.isUserInteractionEnabled = true
    }
}
```

위의 코드에서는 ViewController에 NVActivityIndicatorView 인스턴스를 추가하고, 인디케이터의 모양과 스타일을 설정한 후, 인디케이터를 화면에 추가합니다. showLoading() 함수를 호출하면 화면에 인디케이터가 표시되고, 사용자의 인터렉션을 제한합니다. hideLoading() 함수를 호출하면 인디케이터를 제거하고, 사용자의 인터렉션을 다시 가능하게 합니다.

## 마무리

NVActivityIndicatorView를 사용하여 화면 로딩 상태를 표시하고, 사용자의 인터렉션을 제한하는 방법에 대해 알아보았습니다. 이를 통해 사용자에게 좋은 사용자 경험을 제공할 수 있습니다. NVActivityIndicatorView의 다양한 모양과 스타일을 활용하여 애플리케이션의 디자인에 맞게 로딩 인디케이터를 사용할 수 있습니다.

더 자세한 정보를 원한다면, [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고해보세요.