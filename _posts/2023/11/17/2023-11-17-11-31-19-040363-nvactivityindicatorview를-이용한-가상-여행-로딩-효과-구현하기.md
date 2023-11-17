---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 가상 여행 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

여행 관련 앱을 개발 중이거나, 다양한 콘텐츠를 로딩할 때 사용자에게 고유한 로딩 효과를 제공하고 싶을 때가 있습니다. 이때 NVActivityIndicatorView 라이브러리를 사용하면 쉽게 여행 로딩 효과를 구현할 수 있습니다.

NVActivityIndicatorView는 미리 정의된 다양한 로딩 효과를 제공하며, Swift에서 사용하기 간편한 API를 제공합니다. 이제 NVActivityIndicatorView를 사용하여 가상 여행 로딩 효과를 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 설치

먼저, NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Cocoapods를 사용하는 경우, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용법

1. `import NVActivityIndicatorView`를 통해 라이브러리를 임포트합니다.

2. `NVActivityIndicatorView` 인스턴스를 생성합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. 효과와 색상을 설정합니다. 여행 로딩 효과를 위해 해당 효과와 색상을 선택합니다:

```swift
activityIndicatorView.type = .ballRotateChase
activityIndicatorView.color = UIColor.blue
```

4. `NVActivityIndicatorView`를 보이게하고 로딩을 시작합니다:

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

5. 로딩이 완료되면 `stopAnimating()`을 호출하여 로딩 효과를 중지합니다:

```swift
activityIndicatorView.stopAnimating()
```

## 예제 코드

이제 NVActivityIndicatorView를 사용하여 가상 여행 로딩 효과를 구현하는 예제 코드를 보여드리겠습니다:

```swift
import NVActivityIndicatorView

class TravelLoadingViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 효과 설정
        activityIndicatorView.type = .ballRotateChase
        activityIndicatorView.color = UIColor.blue

        // 뷰에 추가
        view.addSubview(activityIndicatorView)
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        // 로딩 시작
        activityIndicatorView.startAnimating()

        // 가상 여행 로딩 시뮬레이션 (5초 후에 로딩 완료)
        DispatchQueue.main.asyncAfter(deadline: .now() + 5) {
            self.activityIndicatorView.stopAnimating()
        }
    }
}
```

위의 예제 코드에서는 `TravelLoadingViewController`에서 `viewDidAppear` 메서드를 통해 로딩을 시작하고, 5초 후에 로딩을 종료합니다.

## 마무리

NVActivityIndicatorView를 사용하여 간단한 가상 여행 로딩 효과를 구현하는 방법을 알아보았습니다. NVActivityIndicatorView는 다양한 로딩 효과를 제공하므로, 원하는 효과와 색상을 선택하여 로딩 화면을 꾸밀 수 있습니다.

더 많은 정보를 원하시거나 라이브러리의 다른 기능을 알아보고 싶다면, [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고해보세요.