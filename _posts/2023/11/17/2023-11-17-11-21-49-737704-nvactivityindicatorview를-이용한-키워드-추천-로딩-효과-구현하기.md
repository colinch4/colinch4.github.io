---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 키워드 추천 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 NVActivityIndicatorView 라이브러리를 사용하여 키워드 추천 로딩 효과를 구현하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 iOS 앱에서 로딩 효과를 쉽게 추가할 수 있도록 도와주는 오픈소스 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift 언어로 작성된 iOS 뷰 컴포넌트 라이브러리로, 다양한 로딩 효과를 제공합니다. 이 라이브러리는 미리 정의된 다양한 로딩 애니메이션 스타일을 제공하며, 적용하기 쉽고 커스터마이징할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. 프로젝트의 Podfile에 다음과 같이 추가해주세요:

```bash
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령을 실행하여 라이브러리를 설치해주세요:

```bash
pod install
```

## NVActivityIndicatorView 사용하기

### 1. 뷰 컨트롤러에 NVActivityIndicatorView 추가하기

먼저, 키워드 추천 로딩 효과를 보여줄 뷰 컨트롤러에 NVActivityIndicatorView를 추가해야 합니다. 뷰 컨트롤러의 viewDidLoad() 메서드에서 다음 코드를 이용하여 NVActivityIndicatorView를 추가합니다:

```swift
import NVActivityIndicatorView

class RecommendationViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 초기화 및 프레임 설정
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScaleRippleMultiple, color: .blue, padding: nil)

        // 뷰에 NVActivityIndicatorView 추가
        self.view.addSubview(activityIndicatorView)

        // NVActivityIndicatorView 중앙 정렬
        activityIndicatorView.center = self.view.center
    }
}
```

### 2. 로딩 효과 시작 및 정지하기

다음으로, 로딩 효과를 시작하고 정지하는 메서드를 추가해야 합니다. 아래 코드를 이용하여 로딩 효과를 시작하고 정지하는 메서드를 구현합니다:

```swift
extension RecommendationViewController {

    // 로딩 효과 시작
    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    // 로딩 효과 정지
    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
}
```

### 3. 키워드 추천 로딩 효과 적용하기

이제 로딩 효과를 적용할 시점에 startLoading() 메서드를 호출하여 로딩 효과를 시작하고, 로딩이 완료되었을 때 stopLoading() 메서드를 호출하여 로딩 효과를 정지하면 됩니다. 예를 들어, 키워드 추천 API를 호출하는 과정에서 다음과 같이 적용할 수 있습니다:

```swift
func getRecommendations() {
    startLoading()

    // 키워드 추천 API 호출 및 데이터 처리 로직 작성
    // ...

    // 작업이 완료된 후 로딩 효과 정지
    stopLoading()
}
```

## 마무리

이렇게 NVActivityIndicatorView를 사용하여 키워드 추천 로딩 효과를 구현할 수 있습니다. NVActivityIndicatorView를 사용하면 로딩 효과를 쉽게 추가할 수 있으며, 다양한 로딩 애니메이션 스타일을 활용할 수 있습니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.