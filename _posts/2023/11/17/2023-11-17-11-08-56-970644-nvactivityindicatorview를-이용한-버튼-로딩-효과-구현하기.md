---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 버튼 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

![](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Demo.gif)

안녕하세요! 이번에는 Swift에서 버튼 로딩 효과를 구현하는 방법을 알려드리려고 합니다. NVActivityIndicatorView는 iOS 앱에서 로딩 효과를 구현할 수 있는 오픈 소스 라이브러리입니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. 프로젝트의 Podfile에 다음과 같이 추가합니다.

```
pod 'NVActivityIndicatorView'
```

그런 다음, 터미널을 열고 프로젝트의 디렉터리로 이동한 후, 다음 명령어를 실행하여 설치합니다.

```
pod install
```

## NVActivityIndicatorView 적용

먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

로딩 효과를 적용할 버튼을 생성합니다. 버튼의 액션 메서드에서 로딩 효과를 시작하고, 작업이 완료된 후에 로딩 효과를 종료합니다.

```swift
class ViewController: UIViewController {

    @IBOutlet weak var button: UIButton!

    override func viewDidLoad() {
        super.viewDidLoad()
        // 버튼 스타일을 커스텀 스타일로 지정
        button.backgroundColor = UIColor.blue
        button.setTitleColor(UIColor.white, for: .normal)
    }

    @IBAction func buttonClicked(_ sender: UIButton) {
        // 버튼 클릭 시 로딩 효과 시작
        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 30, height: 30), type: .ballClipRotateMultiple, color: UIColor.white, padding: nil)
        activityIndicatorView.center = sender.center
        sender.addSubview(activityIndicatorView)
        activityIndicatorView.startAnimating()

        // 작업이 완료된 후 로딩 효과 종료 예시
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            activityIndicatorView.stopAnimating()
            activityIndicatorView.removeFromSuperview()
        }
    }
}
```

위의 코드에서는 `NVActivityIndicatorView`를 이용하여 로딩 효과를 구현하고 있습니다. `NVActivityIndicatorView`의 `type` 속성을 조정하여 원하는 형태의 로딩 효과를 선택할 수 있습니다. `color` 속성을 이용하여 로딩 효과의 색상을 설정할 수 있습니다.

## 요약

NVActivityIndicatorView를 이용하면 Swift에서 간단하게 버튼 로딩 효과를 구현할 수 있습니다. 설치와 적용 방법을 알아보았는데요, 여러분도 NVActivityIndicatorView를 사용하여 앱에 멋진 로딩 효과를 추가해보세요!

## 참고자료
- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)