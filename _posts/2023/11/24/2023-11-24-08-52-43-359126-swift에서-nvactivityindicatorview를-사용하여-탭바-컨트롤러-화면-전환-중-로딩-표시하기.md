---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 탭바 컨트롤러 화면 전환 중 로딩 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

iOS 애플리케이션에서 탭바 컨트롤러를 사용할 때, 화면 전환 중에 로딩 상태를 표시하는 것은 사용자 경험을 향상시키는 좋은 방법입니다. 이를 위해 NVActivityIndicatorView라는 라이브러리를 사용하여 로딩 인디케이터를 쉽게 구현할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift에서 로딩 인디케이터를 구현하기 위한 간단하고 유연한 라이브러리입니다. 여러 가지 스타일의 로딩 인디케이터를 제공하며, 색상, 크기, 속도 등을 조절할 수 있습니다.

## 설치

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. `Podfile`에 다음 항목을 추가하고 `pod install` 명령어를 실행합니다.

```ruby
pod 'NVActivityIndicatorView', '~> 5.1.1'
```

## 사용 방법

1. 먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 인디케이터를 표시할 뷰를 생성합니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
```

- `frame`: 인디케이터 뷰의 위치와 크기를 지정합니다.
- `type`: 인디케이터의 스타일을 선택합니다.
- `color`: 인디케이터의 색상을 선택합니다.
- `padding`: 인디케이터 내부의 여백을 지정합니다. 있을 경우에만 지정하고, 없으면 `nil`로 설정합니다.

3. 뷰 계층에 인디케이터를 추가합니다.

```swift
view.addSubview(indicatorView)
```

4. 인디케이터를 시작하거나 중지하는 메서드를 구현합니다.

```swift
func startLoading() {
    indicatorView.startAnimating()
    // 화면 전환 중 로딩 상태를 표시하기 위해 추가 작업 수행
}

func stopLoading() {
    indicatorView.stopAnimating()
    // 로딩 상태를 해제하기 위한 추가 작업 수행
}
```

위의 메서드를 화면 전환 중에 호출하여 로딩 인디케이터를 시작하고 중지할 수 있습니다.

5. 탭바 컨트롤러 화면 전환 중에 로딩 상태를 표시하기 위해 다음과 같이 사용할 수 있습니다.

```swift
class ViewController: UIViewController {
    let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()

        // 인디케이터 뷰를 뷰 계층에 추가
        view.addSubview(indicatorView)
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        // 화면 전환 시작 전에 로딩 인디케이터를 시작
        startLoading()

        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            // 3초 후에 화면 전환 완료되었다고 가정
            self.stopLoading()
        }
    }

    func startLoading() {
        indicatorView.startAnimating()
        // 화면 전환 중 로딩 상태를 표시하기 위해 추가 작업 수행
    }

    func stopLoading() {
        indicatorView.stopAnimating()
        // 로딩 상태를 해제하기 위한 추가 작업 수행
    }
}
```

위의 예제에서는 `ViewController`에서 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 구현하고, `viewDidAppear` 메서드에서 화면 전환 발생을 가정하고 로딩 인디케이터를 시작하고 중지하는 방법을 보여줍니다.

이제 NVActivityIndicatorView를 사용하여 탭바 컨트롤러 화면 전환 중에 로딩 인디케이터를 표시할 수 있습니다.

## 참고 자료
- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)