---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현하고 사용자 인터랙션 제어하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

현대의 모바일 앱은 사용자에게 빠르고 반응적인 경험을 제공하기 위해 로딩 상태를 시각적으로 표시해야 합니다. 이를 위해 NVActivityIndicatorView 라이브러리를 사용하여 화면 로딩 상태를 표시하고 사용자 인터랙션을 제어하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS 앱의 화면 로딩 상태를 나타내기 위한 라이브러리입니다. 이 라이브러리는 다양한 스타일과 색상의 인디케이터를 제공하여 개발자가 로딩 상태를 시각적으로 나타낼 수 있습니다.

## NVActivityIndicatorView 설치하기

1. Cocoapods를 사용하여 NVActivityIndicatorView를 설치합니다. `Podfile`에 다음과 같은 내용을 추가합니다.

```
pod 'NVActivityIndicatorView'
```

2. 터미널을 열고 프로젝트 폴더로 이동한 뒤, 다음 명령어를 실행합니다.

```
pod install
```

3. 설치가 완료되면 Xcode에서 프로젝트를 다시 엽니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 상태를 표시할 뷰를 생성합니다.

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
```

3. 로딩 인디케이터 스타일을 선택합니다. NVActivityIndicatorView는 다양한 스타일을 제공하므로, 필요에 따라 적절한 스타일을 선택할 수 있습니다. 예를 들어, `.ballSpinFadeLoader` 스타일을 선택하려면 다음과 같이 설정합니다.

```swift
loadingView.type = .ballSpinFadeLoader
```

4. 로딩 인디케이터 색상을 지정합니다. 기본값은 회색입니다.

```swift
loadingView.color = .red
```

5. 로딩 인디케이터를 화면에 표시합니다.

```swift
loadingView.startAnimating()
```

6. 로딩 인디케이터를 숨기고 사용자 인터랙션을 가능하게 하려면 다음과 같이 설정합니다.

```swift
loadingView.stopAnimating()
```

## 예제 코드

다음은 `NVActivityIndicatorView`를 사용하여 화면 로딩 상태를 표시하고 사용자 인터랙션을 제어하는 예제 코드입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))

    override func viewDidLoad() {
        super.viewDidLoad()
        // 로딩 인디케이터 스타일 설정
        loadingView.type = .ballSpinFadeLoader
        // 로딩 인디케이터 색상 설정
        loadingView.color = .red
        // 로딩 인디케이터를 뷰에 추가
        view.addSubview(loadingView)
    }

    func startLoading() {
        // 로딩 인디케이터 표시
        loadingView.startAnimating()
        // 사용자 인터랙션 제어
        view.isUserInteractionEnabled = false
    }

    func stopLoading() {
        // 로딩 인디케이터 숨김
        loadingView.stopAnimating()
        // 사용자 인터랙션 제어 해제
        view.isUserInteractionEnabled = true
    }

    // 사용 예시
    func fetchData() {
        startLoading()
        // 데이터 가져오기
        // ...
        stopLoading()
    }
}
```

위의 예제 코드에서는 `ViewController` 클래스에 메소드 `startLoading()`과 `stopLoading()`을 추가하여 로딩 인디케이터를 표시하고 사용자 인터랙션을 제어합니다. `fetchData()` 메소드 예시를 통해 데이터를 가져오는 동안 로딩 인디케이터를 표시합니다.

## 결론

NVActivityIndicatorView를 사용하여 화면 로딩 상태를 표시하고 사용자 인터랙션을 제어하는 방법에 대해 알아보았습니다. 이 라이브러리는 간편하게 화면 로딩 상태를 시각적으로 나타낼 수 있어 사용자 경험을 향상시키는 데 도움이 됩니다. 또한 다양한 스타일과 색상의 인디케이터를 제공하므로, 앱의 디자인에 맞게 알맞은 스타일을 선택할 수 있습니다.