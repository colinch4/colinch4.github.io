---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 팀프로젝트 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 블로그에서는 NVActivityIndicatorView 라이브러리를 사용하여 스위프트(Swift)로 작성된 팀프로젝트에 로딩 효과를 추가하는 방법을 알아보겠습니다.

## 1. NVActivityIndicatorView 소개

NVActivityIndicatorView는 로딩 효과를 쉽게 구현할 수 있도록 도와주는 오픈 소스 라이브러리입니다. 다양한 스타일과 색상의 로딩 애니메이션을 제공하며, 간단한 코드로 적용할 수 있습니다.

Github 링크: [NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)

## 2. NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods를 이용하여 프로젝트에 라이브러리를 추가해야 합니다.

Podfile에 다음과 같은 내용을 추가합니다:

```
pod 'NVActivityIndicatorView'
```

그리고 터미널을 열고 프로젝트 경로에서 `pod install`을 실행하여 라이브러리를 설치합니다.

## 3. NVActivityIndicatorView 사용 방법

### 3.1 뷰 컨트롤러에 NVActivityIndicatorView 추가

로딩 효과를 보여줄 뷰 컨트롤러에 NVActivityIndicatorView를 추가해야합니다. 먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

다음으로, NVActivityIndicatorView를 생성하고 원하는 스타일과 색상을 설정합니다. 예를 들어, 아래와 같이 설정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 50, height: 50),
    type: .ballSpinFadeLoader,
    color: .blue,
    padding: nil
)
```

위 코드에서는 너비(width)와 높이(height)가 50인 크기의 NVActivityIndicatorView를 생성하고, .ballSpinFadeLoader 스타일을 사용하며, 파란색으로 표시됩니다.

### 3.2 로딩 효과 보여주기

로딩 효과를 보여주기 위해서는 다음과 같이 시작 및 중지 메서드를 호출해야 합니다.

```swift
// 로딩 효과 시작
activityIndicatorView.startAnimating()

// 로딩 효과 중지
activityIndicatorView.stopAnimating()
```

로딩 효과를 보여주고자하는 시점에 `startAnimating()`을 호출하여 로딩 효과를 시작하고, 로딩이 완료되면 `stopAnimating()`을 호출하여 로딩 효과를 중지합니다.

### 3.3 NVActivityIndicatorView 위치 설정

NVActivityIndicatorView를 원하는 위치에 배치하려면, `activityIndicatorView`의 `center` 속성을 설정하면 됩니다.

예를 들어, 화면 중앙에 배치하고자 한다면 아래와 같이 설정할 수 있습니다.

```swift
activityIndicatorView.center = view.center
```

위 코드에서 `view.center`는 뷰 컨트롤러의 중앙 위치를 나타냅니다.

## 4. 프로젝트에 NVActivityIndicatorView 적용하기

프로젝트에 NVActivityIndicatorView를 적용하기 위해서는 먼저 위에서 작성한 코드를 참고하여 뷰 컨트롤러에서 NVActivityIndicatorView를 생성하고 위치를 설정합니다.

그리고 원하는 시점에 로딩 효과를 시작하여 데이터 로딩 중임을 사용자에게 알려줍니다. 데이터 로딩이 완료되었을 때 로딩 효과를 중지하면 됩니다.

```swift
class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // NVActivityIndicatorView 생성 및 위치 설정
        activityIndicatorView = NVActivityIndicatorView(
            frame: CGRect(x: 0, y: 0, width: 50, height: 50),
            type: .ballSpinFadeLoader,
            color: .blue,
            padding: nil
        )
        activityIndicatorView.center = view.center
        
        // 뷰에 추가
        view.addSubview(activityIndicatorView)
    }

    func startDataLoading() {
        // 로딩 효과 시작
        activityIndicatorView.startAnimating()
        
        // 데이터 로딩 코드 작성
        // ...
        
        // 로딩 완료 후 로딩 효과 중지
        activityIndicatorView.stopAnimating()
    }

}
```

이제 위와 같이 작성하면 팀프로젝트에 NVActivityIndicatorView를 쉽게 적용할 수 있습니다.

## 5. 마무리

이번 블로그에서는 NVActivityIndicatorView를 사용하여 팀프로젝트에 로딩 효과를 추가하는 방법을 알아보았습니다. NVActivityIndicatorView는 간단한 설정으로 다양한 로딩 애니메이션을 제공하여 사용자에게 더 나은 사용자 경험을 제공할 수 있습니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.