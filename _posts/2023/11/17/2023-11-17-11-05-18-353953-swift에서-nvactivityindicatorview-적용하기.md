---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 적용하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 로딩 인디케이터를 쉽게 구현할 수 있는 NVActivityIndicatorView를 소개하고, 적용하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 다양한 모양의 로딩 인디케이터를 제공하며, 간단한 코드로 적용할 수 있습니다. 

## NVActivityIndicatorView 설치하기

1. Cocoapods를 사용하여 NVActivityIndicatorView를 설치할 수 있습니다. Podfile에 다음과 같이 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

2. Terminal을 열고 해당 프로젝트의 폴더로 이동한 후, 다음 명령어를 실행하여 라이브러리를 설치합니다.

```shell
$ pod install
```

3. 설치가 완료되면, 프로젝트를 열고 `import NVActivityIndicatorView`를 추가하여 라이브러리를 사용할 준비를 합니다.

## NVActivityIndicatorView 사용하기

1. 먼저, 인디케이터를 표시하고 싶은 View를 생성합니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
```

2. 인디케이터의 크기와 모양, 색상 등을 설정합니다. 여기서는 `ballSpinFadeLoader` 모양과 파란색을 설정했습니다.

3. 원하는 타이밍에 인디케이터를 표시하고 숨길 수 있습니다.

```swift
indicatorView.startAnimating() // 인디케이터 표시
indicatorView.stopAnimating() // 인디케이터 숨김
```

4. 인디케이터를 표시할 때, 특정 View 위에 배치하고 싶다면 해당 View에 인디케이터를 추가해야 합니다.

```swift
view.addSubview(indicatorView)
```

## 예제 코드

다음은 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 표시하는 간단한 예제 코드입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addSubview(indicatorView)
    }
    
    @IBAction func startButtonTapped(_ sender: UIButton) {
        indicatorView.startAnimating()
    }
    
    @IBAction func stopButtonTapped(_ sender: UIButton) {
        indicatorView.stopAnimating()
    }
}
```

## 결론

이제 Swift에서 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 쉽게 적용할 수 있게 되었습니다. NVActivityIndicatorView의 다양한 모양과 옵션을 사용하여 앱 사용자에게 더 나은 사용자 경험을 제공해보세요!