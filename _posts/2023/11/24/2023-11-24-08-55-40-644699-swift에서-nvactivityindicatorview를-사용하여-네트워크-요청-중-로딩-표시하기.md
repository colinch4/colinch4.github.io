---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 네트워크 요청 중 로딩 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift 언어에서 NVActivityIndicatorView를 사용하여 네트워크 요청 중 로딩 표시하는 방법을 알아보겠습니다. NVActivityIndicatorView는 iOS 앱에서 로딩 인디케이터를 쉽게 구현할 수 있는 오픈 소스 라이브러리입니다.

## 1. NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 사용하기 위해 Cocoapods를 이용해 프로젝트에 라이브러리를 설치해야 합니다. `Podfile` 파일을 열고 다음과 같이 `NVActivityIndicatorView` 라이브러리를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

설치 후에는 터미널에서 `pod install` 명령을 실행하여 라이브러리를 다운로드하고 프로젝트에 추가합니다.

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하여 로딩 표시를 구현하는 방법은 다음과 같습니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 인디케이터 속성 설정
        let size = CGSize(width: 50, height: 50)
        let color = UIColor.blue

        // 인디케이터 뷰 생성
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(origin: CGPoint(x: view.frame.midX - size.width / 2, y: view.frame.midY - size.height / 2), size: size), type: .circleStrokeSpin, color: color, padding: nil)
        activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false

        // 화면에 추가
        view.addSubview(activityIndicatorView)

        // 제약 조건 설정
        NSLayoutConstraint.activate([
            activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])

        // 네트워크 요청 시작 시 로딩 표시
        activityIndicatorView.startAnimating()

        // 네트워크 요청 완료 시 로딩 표시 중지
        activityIndicatorView.stopAnimating()
    }
}
```

위의 코드에서는 먼저 `NVActivityIndicatorView`의 속성을 설정하고, 해당 속성을 사용하여 로딩 인디케이터 뷰를 생성합니다. 그리고 화면에 추가하고 제약 조건을 설정한 뒤, 네트워크 요청 시작 시 `startAnimating()`을 호출하여 로딩 표시를 시작하고, 요청 완료 시 `stopAnimating()`을 호출하여 로딩 표시를 중지합니다.

## 3. 결과 확인하기

앱을 실행하면 화면 중앙에 로딩 인디케이터가 표시되는 것을 확인할 수 있습니다. 네트워크 요청을 시작하면 로딩 인디케이터가 돌아가며 작업이 진행되고, 요청이 완료되면 로딩 인디케이터가 사라집니다.

## 결론

이번 글에서는 Swift에서 NVActivityIndicatorView를 사용하여 네트워크 요청 중 로딩 표시하는 방법을 알아보았습니다. NVActivityIndicatorView는 간단하게 로딩 인디케이터를 구현할 수 있어 유용합니다. 필요에 따라 인디케이터의 크기, 색상 등을 설정하여 원하는 스타일로 커스터마이즈할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)