---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 경험 개선 및 로딩 시간 최적화하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 소개
앱 또는 웹 페이지에서 데이터를 가져오거나 처리할 때, 로딩 시간을 최적화하고 사용자들에게 더 나은 경험을 제공하는 것은 매우 중요합니다. NVActivityIndicatorView는 Swift에서 사용할 수 있는 오픈소스 라이브러리로, 간단한 코드 몇 줄로 로딩 인디케이터를 구현할 수 있습니다.

## 설치
먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그리고 `pod install` 명령어를 실행하여 라이브러리를 프로젝트에 추가합니다.

## 사용법
1. 뷰 컨트롤러에 NVActivityIndicatorView를 추가합니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()
        // NVActivityIndicatorView 인스턴스 생성 및 설정
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100),
                                                        type: .ballPulse,
                                                        color: .blue,
                                                        padding: nil)
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }

    // 로딩 시작 함수
    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    // 로딩 종료 함수
    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
}
```

2. 필요한 곳에서 로딩 시작 및 종료 함수를 호출하면 됩니다.

```swift
func fetchData() {
    startLoading()

    // 데이터 가져오기 로직

    stopLoading()
}
```

## 스타일링
NVActivityIndicatorView는 다양한 스타일을 지원합니다. `type` 파라미터 값을 변경하여 다른 스타일을 사용할 수 있습니다. 예를 들어, `.circleStrokeSpin` 스타일을 사용하려면 다음과 같이 설정합니다.

```swift
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100),
                                                type: .circleStrokeSpin,
                                                color: .blue,
                                                padding: nil)
```

스타일에 대한 더 자세한 정보와 사용 가능한 모든 스타일 목록은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

## 결론
NVActivityIndicatorView를 사용하면 간단한 코드로 로딩 인디케이터를 구현할 수 있습니다. 로딩 시간 최적화와 함께 사용자 경험을 개선하여 앱 또는 웹 페이지의 성능을 향상시킬 수 있습니다.