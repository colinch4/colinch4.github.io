---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 버튼 클릭 시 로딩 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift에서 NVActivityIndicatorView 라이브러리를 사용하여 버튼 클릭 시 로딩 표시하는 방법을 알아보겠습니다.

## 1. NVActivityIndicatorView 라이브러리 설치하기

우선 NVActivityIndicatorView 라이브러리를 설치해야 합니다. `Podfile`에 다음과 같이 추가한 뒤 `pod install` 명령어를 실행해주세요.

```swift
pod 'NVActivityIndicatorView'
```

## 2. NVActivityIndicatorView 인스턴스 생성하기

로딩 표시를 하기 위해 먼저 NVActivityIndicatorView 인스턴스를 생성해야 합니다. UIViewController의 원하는 위치에 다음과 같이 코드를 추가해주세요.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballClipRotate, color: .gray, padding: nil)
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }

    // ...
}
```

`NVActivityIndicatorView`의 `frame`과 `type`, `color` 등을 적절히 설정하여 로딩 표시의 모양을 원하는 대로 만들 수 있습니다.

## 3. 버튼 클릭 시 로딩 표시하기

이제 버튼을 클릭할 때마다 로딩 표시를 할 수 있도록 코드를 추가해보겠습니다. 다음은 버튼을 클릭할 때 `startAnimating()` 메서드를 호출하여 로딩을 시작하고, 작업이 완료되면 `stopAnimating()` 메서드를 호출하여 로딩을 종료하는 예제입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    // ...

    @IBAction func buttonTapped(_ sender: UIButton) {
        activityIndicatorView.startAnimating()

        // 네트워크 요청이나 긴 작업을 수행하는 코드 작성

        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            self.activityIndicatorView.stopAnimating()

            // 작업 완료 후 수행해야 할 코드 작성
        }
    }

    // ...
}
```

위 예제에서는 `startAnimating()` 메서드를 호출하여 로딩을 시작하고, 2초 후에 `stopAnimating()` 메서드를 호출하여 로딩을 종료하도록 처리하였습니다.

## 마무리

이제 NVActivityIndicatorView를 사용하여 Swift에서 버튼 클릭 시 로딩 표시하는 방법을 알아보았습니다. NVActivityIndicatorView는 다양한 로딩 표시 스타일을 제공하기 때문에 필요에 따라 적절한 스타일을 선택하여 사용할 수 있습니다.

더 자세한 사용법은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.