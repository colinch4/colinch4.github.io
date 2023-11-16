---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 로딩 화면 디자인 및 사용자 경험 개선하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

원활한 사용자 경험을 제공하기 위해 앱 내에 로딩 화면을 추가하는 것은 중요합니다. 이번 글에서는 iOS 앱 개발을 위한 NVActivityIndicatorView 라이브러리를 활용하여 로딩 화면을 디자인하고, 사용자 경험을 개선하는 방법을 알아봅니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS용 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 애니메이션을 제공하여 앱에 다양한 로딩 화면을 구현할 수 있도록 도와줍니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 CocoaPods를 설치해야합니다. 프로젝트의 Podfile에 다음과 같은 내용을 추가합니다.

```
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 `pod install` 명령을 실행하여 라이브러리를 프로젝트에 설치합니다.

## 로딩 화면 디자인하기

NVActivityIndicatorView를 사용하여 로딩 화면을 디자인하는 방법은 간단합니다. 먼저, ViewController에 NVActivityIndicatorView를 추가하기 위해 `import NVActivityIndicatorView`를 추가합니다.

```swift
import NVActivityIndicatorView
```

그런 다음 NVActivityIndicatorView의 인스턴스를 만들어 원하는 위치에 추가하고 원하는 스타일로 설정합니다. 아래는 로딩 화면을 추가하는 예제 코드입니다.

```swift
class LoadingViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 인디케이터 스타일 설정
        let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
        activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballScaleRippleMultiple, color: .gray, padding: nil)

        // 로딩 인디케이터 위치 설정
        activityIndicatorView.center = view.center

        // 로딩 인디케이터를 뷰에 추가
        view.addSubview(activityIndicatorView)
    }

    // 로딩 화면 보이기
    func showLoadingScreen() {
        activityIndicatorView.startAnimating()
    }

    // 로딩 화면 숨기기
    func hideLoadingScreen() {
        activityIndicatorView.stopAnimating()
    }
}
```

위의 예제 코드에서는 NVActivityIndicatorView의 스타일을 `.ballScaleRippleMultiple`로 설정하고, 색상은 `.gray`로 지정했습니다. 로딩 화면을 보여주고 숨기기 위해 `showLoadingScreen()`과 `hideLoadingScreen()` 메서드를 사용할 수 있습니다.

## 사용자 경험 개선하기

로딩 화면을 도입하여 사용자 경험을 개선하는 방법은 여러 가지가 있습니다. 몇 가지 예시를 살펴보겠습니다.

1. 네트워크 요청 시 로딩 화면 표시: 사용자가 어떠한 요청을 하거나 데이터를 불러올 때 로딩 화면을 표시하여 사용자가 작업이 진행 중임을 알 수 있도록 합니다.

2. 장기간 작업 시 로딩 화면 표시: 데이터를 긴 시간 동안 처리해야하는 경우, 사용자의 대기 시간 동안 로딩 화면을 표시하여 대기 상태임을 알립니다.

3. 진행률 표시: 긴 작업이 진행되는 경우, NVActivityIndicatorView를 이용하여 진행률을 표시할 수도 있습니다. 진행률바나 퍼센티지를 함께 표시하여 사용자가 작업이 진행되고 있는지 확인할 수 있습니다.

## 결론

NVActivityIndicatorView 라이브러리를 사용하여 로딩 화면을 디자인하고, 사용자 경험을 개선하는 방법을 알아보았습니다. 로딩 화면을 도입함으로써 사용자가 작업의 진행 상태를 알 수 있고, 원활한 사용자 경험을 제공할 수 있습니다. 이러한 기법을 활용하여 앱의 사용성을 높이세요.

> 참고: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)