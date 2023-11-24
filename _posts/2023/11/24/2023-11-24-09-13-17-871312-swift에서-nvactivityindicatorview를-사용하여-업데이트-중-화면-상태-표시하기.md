---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 업데이트 중 화면 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱을 개발할 때, 데이터 업데이트나 작업 처리 중에 사용자에게 로딩 상태를 표시하는 것은 중요합니다. NVActivityIndicatorView는 Swift에서 사용할 수 있는 간편한 라이브러리로, 로딩 인디케이터를 추가하여 화면 상태를 표시하는 데 도움을 줍니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 인디케이터 뷰 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하여 앱의 로딩 상태를 시각적으로 표시할 수 있습니다.

## 설치하기

NVActivityIndicatorView를 설치하기 위해서는 CocoaPods 또는 Carthage를 사용할 수 있습니다. 여기서는 CocoaPods를 사용한 예제를 보여드리겠습니다.

1. `Podfile`을 열고 아래의 코드를 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

2. 터미널을 열고 프로젝트 디렉토리로 이동한 후, 다음 명령어를 실행합니다:

```bash
pod install
```

3. 프로젝트가 성공적으로 설치된 후, `.xcworkspace` 확장자를 가진 Xcode 워크스페이스 파일을 엽니다.

## 사용하기

1. 먼저, NVActivityIndicatorView를 import해야 합니다:

```swift
import NVActivityIndicatorView
```

2. 해당 인디케이터 뷰를 추가할 수 있는 View를 생성합니다. 이 예시에서는 UIViewController의 view를 사용하겠습니다:

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
indicatorView.center = self.view.center
self.view.addSubview(indicatorView)
```

3. 인디케이터 뷰의 스타일을 설정합니다. 여기서는 `.ballPulse` 스타일을 사용하겠습니다:

```swift
indicatorView.type = .ballPulse
```

4. 인디케이터를 시작 및 중지하는 함수를 정의하세요:

```swift
func startLoading() {
    indicatorView.startAnimating()
}

func stopLoading() {
    indicatorView.stopAnimating()
}
```

5. 업데이트가 진행될 때 `startLoading()` 함수를 호출하여 로딩 인디케이터를 시작하고, 업데이트가 완료되면 `stopLoading()` 함수를 호출하여 로딩 인디케이터를 중지합니다.

```swift
startLoading()

// 업데이트 중인 작업 수행

stopLoading()
```

이제, NVActivityIndicatorView를 사용하여 Swift 앱에서 업데이트 중 로딩 상태를 시각적으로 표시할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)