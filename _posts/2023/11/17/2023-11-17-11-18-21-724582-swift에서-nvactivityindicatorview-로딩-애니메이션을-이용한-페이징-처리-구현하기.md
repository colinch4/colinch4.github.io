---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 로딩 애니메이션을 이용한 페이징 처리 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 소개

페이징 처리는 앱에서 많은 양의 데이터를 로드할 때 사용되는 일반적인 기술입니다. 이러한 처리를 보여주기 위해 사용자에게 로딩 상태를 시각적으로 알려주는 로딩 애니메이션을 함께 구현할 수 있습니다. 이 글에서는 Swift 프로그래밍 언어로 NVActivityIndicatorView로딩 애니메이션을 이용해 페이징 처리를 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 로딩 상태를 나타내기 위한 UI 컴포넌트입니다. 다양한 스타일의 로딩 애니메이션을 제공하며, 간단한 코드만으로 구현할 수 있습니다.

## 구현

### 1. NVActivityIndicatorView 추가

처음으로 프로젝트에 NVActivityIndicatorView를 추가해야 합니다. 이를 위해 CocoaPods을 사용할 수 있습니다. `Podfile`에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 의존성을 설치합니다:

```bash
$ pod install
```

### 2. NVActivityIndicatorView 초기화

로딩 애니메이션을 사용할 뷰 컨트롤러에서 NVActivityIndicatorView를 초기화합니다. 다음과 같은 코드를 추가합니다:

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50),
                                                        type: .ballScaleRippleMultiple,
                                                        color: .gray,
                                                        padding: nil)
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }

    // ...
}
```

### 3. 페이징 처리

로딩 애니메이션을 사용하여 페이징 처리를 구현하기 위해 해당 기능을 호출하는 함수 내부에서 NVActivityIndicatorView의 상태를 제어해야 합니다. 예를 들어, 페이징 데이터를 로드하는 버튼을 눌렀을 때 애니메이션을 시작하고, 데이터가 완전히 로드되면 애니메이션을 중지하는 방식으로 구현할 수 있습니다. 다음은 간단한 예시입니다:

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50),
                                                        type: .ballScaleRippleMultiple,
                                                        color: .gray,
                                                        padding: nil)
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }

    // 페이징 처리 함수
    func loadMoreData() {
        // 로딩 애니메이션 시작
        activityIndicatorView.startAnimating()

        // 페이징 데이터 로드
        fetchData { [weak self] result in
            // 데이터 처리 후 애니메이션 중지
            self?.activityIndicatorView.stopAnimating()
        }
    }

    // ...
}
```

## 결론

이제 Swift에서 NVActivityIndicatorView를 사용하여 로딩 애니메이션과 함께 페이징 처리를 구현하는 방법을 알게 되었습니다. NVActivityIndicatorView는 간단하게 초기화하고 사용할 수 있기 때문에 편리하게 로딩 상태를 나타낼 수 있습니다. 이를 통해 사용자 경험을 개선하고 데이터 로딩 과정을 시각적으로 보여줄 수 있습니다.

## 참고 자료

- NVActivityIndicatorView GitHub 리포지토리: [링크](https://github.com/ninjaprox/NVActivityIndicatorView)