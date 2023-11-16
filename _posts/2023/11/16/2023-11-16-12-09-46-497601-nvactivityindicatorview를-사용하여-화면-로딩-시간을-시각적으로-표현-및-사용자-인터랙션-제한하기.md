---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 시간을 시각적으로 표현 및 사용자 인터랙션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

많은 앱에서 화면이 로딩되는 동안 사용자에게 로딩 중임을 알리는 시각적인 피드백이 필요합니다. 이를 위해, 우리는 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 만들 수 있습니다. NVActivityIndicatorView는 많은 다양한 로딩 스타일과 애니메이션을 제공하여 개발자가 원하는 디자인에 맞게 로딩 인디케이터를 커스터마이징할 수 있는 기능을 제공합니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS 앱의 라이브러리입니다. 이 라이브러리는 화면에 로딩 인디케이터를 표시하는 데 사용됩니다. 스피너의 스타일과 애니메이션은 매우 다양하며, 개발자는 직접 스타일을 설정하거나 커스텀 애니메이션을 만들 수도 있습니다.

## 설치하기

NVActivityIndicatorView는 CocoaPods을 사용하여 설치할 수 있습니다. Podfile에 다음과 같은 줄을 추가하고 `pod install` 명령을 실행하여 설치합니다.

```swift
pod 'NVActivityIndicatorView'
```

## 사용하기

1. 먼저, `import NVActivityIndicatorView` 구문을 사용하여 NVActivityIndicatorView를 가져옵니다.
2. 원하는 ViewController에서 NVActivityIndicatorView를 인스턴스화합니다.
3. 로딩 시작 및 종료 메소드를 사용하여 로딩 인디케이터를 표시하고 숨깁니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicator: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 인스턴스화
        activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .gray, padding: nil)
        activityIndicator.center = view.center
        view.addSubview(activityIndicator)
    }

    func startLoading() {
        // 로딩 시작
        activityIndicator.startAnimating()

        // 사용자 인터랙션 제한
        view.isUserInteractionEnabled = false
    }

    func stopLoading() {
        // 로딩 종료
        activityIndicator.stopAnimating()

        // 사용자 인터랙션 활성화
        view.isUserInteractionEnabled = true
    }

    // 이하 코드는 로딩 인디케이터를 표시/숨기기 위한 액션 메소드 예시

    @IBAction func startButtonTapped(_ sender: UIButton) {
        startLoading()
    }

    @IBAction func stopButtonTapped(_ sender: UIButton) {
        stopLoading()
    }

}
```

위 예제에서는 `ballSpinFadeLoader` 타입의 로딩 인디케이터를 사용하고 있습니다. 타입을 변경하거나 원하는 스타일과 색상으로 커스터마이징 할 수 있습니다.

이제 NVActivityIndicatorView를 사용하여 화면 로딩 시간 동안 사용자에게 시각적인 피드백을 제공할 수 있고, 동시에 사용자 인터랙션을 제한할 수 있게 되었습니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하십시오.