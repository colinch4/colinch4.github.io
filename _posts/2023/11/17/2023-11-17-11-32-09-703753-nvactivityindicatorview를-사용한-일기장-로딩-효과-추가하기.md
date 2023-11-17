---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 일기장 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

일기장 앱에 로딩 효과를 추가하고 싶다면, NVActivityIndicatorView 라이브러리를 사용할 수 있습니다. NVActivityIndicatorView는 다양한 스타일의 로딩 인디케이터를 제공하여 앱의 로딩 상태를 시각적으로 표시할 수 있습니다.

## 1. NVActivityIndicatorView 설치하기

먼저, CocoaPods를 사용하여 NVActivityIndicatorView를 프로젝트에 설치해야 합니다. 프로젝트 디렉토리의 Podfile에 다음과 같이 NVActivityIndicatorView를 추가해주세요.


```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 의존성을 설치합니다.

```
pod install
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 다음과 같이 코드를 작성해보겠습니다.

```swift
import NVActivityIndicatorView

class DiaryViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView?

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 인디케이터 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .gray, padding: nil)
        activityIndicatorView?.center = view.center

        // 화면에 추가
        if let activityIndicatorView = activityIndicatorView {
            view.addSubview(activityIndicatorView)
        }

        // 로딩 시작
        startLoading()
    }

    func startLoading() {
        // 로딩 인디케이터 애니메이션 시작
        activityIndicatorView?.startAnimating()

        // 네트워크 요청 등 로딩이 필요한 작업 실행
        // ...

        // 로딩 완료 후 로딩 인디케이터 숨기고 애니메이션 중지
        activityIndicatorView?.stopAnimating()
        activityIndicatorView?.isHidden = true
    }
}
```

위의 코드에서는 DiaryViewController 클래스에서 NVActivityIndicatorView를 사용하는 예제입니다. viewDidLoad()에서 로딩 인디케이터를 초기화하고 화면에 추가하고, startLoading() 메소드에서 로딩 애니메이션을 시작하고 필요한 작업을 실행한 후 로딩 완료시 숨기고 중지합니다.

## 3. 로딩 효과 변경하기

로딩 효과의 스타일을 변경하고 싶다면, NVActivityIndicatorView에서 제공하는 다양한 스타일을 선택할 수 있습니다. 예를 들어, .lineScalePulseOut 효과를 사용하려면 다음과 같이 코드를 변경해주세요.

```swift
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .lineScalePulseOut, color: .gray, padding: nil)
```

코드에서 type 매개변수를 변경하여 원하는 스타일을 선택할 수 있습니다. 자세한 스타일 목록은 NVActivityIndicatorView의 공식 문서를 참조해주세요.

## 결론

이제 NVActivityIndicatorView를 사용하여 일기장 앱에 로딩 효과를 추가할 수 있습니다. NVActivityIndicatorView는 다양한 스타일의 로딩 인디케이터를 제공하므로, 앱의 디자인과 잘 어울리는 효과를 선택하여 사용해보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)