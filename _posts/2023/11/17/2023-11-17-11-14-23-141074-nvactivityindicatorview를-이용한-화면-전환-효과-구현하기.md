---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 화면 전환 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이 글에서는 iOS 앱에서 NVActivityIndicatorView를 사용하여 화면 전환 효과를 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 인디케이터를 보여주기 위한 라이브러리입니다. 다양한 스타일의 인디케이터를 제공하며, 사용자에게 로딩 중임을 알리는 데 유용합니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 설치해야 합니다. 터미널을 열고 다음 명령어를 실행하세요.

```
$ sudo gem install cocoapods
```

Podfile을 만들기 위해 프로젝트 폴더로 이동한 후 다음 명령어를 실행하세요.

```
$ pod init
```

Podfile에 다음 줄을 추가하세요.

```
pod 'NVActivityIndicatorView'
```

그리고 다음 명령어를 실행하여 Cocoapods에서 라이브러리를 설치하세요.

```
$ pod install
```

## NVActivityIndicatorView 사용하기

1. 우선, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화하고 뷰에 추가합니다. 앱이 로딩 중임을 나타내기 위해 보여줄 화면에 다음과 같은 코드를 추가하세요.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .white, padding: nil)
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위 코드에서 `type` 매개변수를 통해 사용할 인디케이터의 스타일을 선택할 수 있습니다. `.ballSpinFadeLoader`는 하나의 공이 회전하는 스타일입니다.

3. 화면 전환 완료 후에는 NVActivityIndicatorView를 제거해야 합니다. 다음 코드를 사용하여 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 예제

아래 예제는 버튼을 터치했을 때 화면 전환 효과를 적용하는 예제입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .white, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }

    @IBAction func buttonTapped(_ sender: UIButton) {
        activityIndicatorView.startAnimating()
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            self.activityIndicatorView.stopAnimating()
            self.performSegue(withIdentifier: "showNextScreen", sender: nil)
        }
    }

    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "showNextScreen" {
            // 다음 화면으로 전환하기 전에 필요한 작업을 수행합니다.
        }
    }
}
```

위 예제에서는 버튼을 터치하면 화면 전환과 함께 인디케이터가 화면에 표시됩니다. 2초 후에 인디케이터가 중지되고 다음 화면으로 전환됩니다.

## 참고 자료

- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)
- [Cocoapods](https://cocoapods.org/)