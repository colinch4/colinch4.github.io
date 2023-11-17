---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 의사 소통 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift 프로그래밍 언어를 사용하여 NVActivityIndicatorView를 이용한 의사 소통 로딩 효과를 추가하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 애플리케이션에서 사용할 수 있는 사용자 정의 로딩 효과를 제공하는 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 로딩 스타일과 색상을 제공하여 애플리케이션의 로딩 화면을 보다 흥미롭고 시각적으로 매력적으로 만들 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods를 설치해야 합니다. 다음과 같은 명령어를 터미널에 입력하여 CocoaPods를 설치하세요.

```shell
$ gem install cocoapods
```

프로젝트의 Podfile에 NVActivityIndicatorView를 추가하세요. Podfile을 열고 다음과 같은 내용을 추가하고 저장하세요.

```ruby
pod 'NVActivityIndicatorView'
```

터미널에서 다음 명령어를 실행하여 NVActivityIndicatorView를 설치하세요.

```shell
$ pod install
```

## NVActivityIndicatorView 사용하기

1. Storyboard에서 NVActivityIndicatorView를 추가할 뷰 컨트롤러를 선택하세요.
2. Identity Inspector에서 Custom Class를 선택하고 NVActivityIndicatorView로 설정하세요.
3. Attributes Inspector에서 원하는 스타일과 색상 등을 설정하세요.
4. IBOutlet으로 NVActivityIndicatorView를 연결하세요.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    @IBOutlet weak var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 효과를 시작하기 전에 필요한 설정을 진행합니다.
        activityIndicatorView.type = .ballClipRotateMultiple
        activityIndicatorView.color = UIColor.red
        activityIndicatorView.startAnimating()
    }
    
    // 로딩 효과를 중지하려면 아래의 코드를 사용합니다.
    // activityIndicatorView.stopAnimating()
}
```

NVActivityIndicatorView를 사용하여 의사 소통 로딩 효과를 추가하는 방법에 대해 알아보았습니다. 이제 애플리케이션에 더 개성 있는 로딩 화면을 추가할 수 있습니다.

더 많은 스타일과 설정 옵션에 대해서는 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.