---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 표시하고 사용자 인터랙션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱 개발 중에는 데이터 불러오기, 파일 업로드 등의 작업으로 인해 사용자는 잠시 동안 대기해야 할 때가 있습니다. 이러한 경우에는 화면에 로딩 상태를 표시하여 사용자에게 작업이 진행 중임을 알려주는 것이 좋습니다. NVActivityIndicatorView는 로딩 상태를 표시하기 위한 강력한 라이브러리 중 하나입니다. 이번 글에서는 NVActivityIndicatorView를 사용하여 화면 로딩 상태를 표시하고 사용자 인터랙션을 제한하는 방법을 알아보겠습니다.

## 1. NVActivityIndicatorView 도입하기

먼저, 프로젝트에 NVActivityIndicatorView를 추가해야 합니다. 이를 위해 CocoaPods를 사용하는 것이 가장 일반적인 방법입니다. 다음 명령어를 터미널에 입력하여 CocoaPods를 설치합니다.

```
$ sudo gem install cocoapods
```

Podfile 파일을 프로젝트 폴더에 생성한 후 아래 코드를 추가합니다.

```
platform :ios, '9.0'
use_frameworks!

target 'YourApp' do
  pod 'NVActivityIndicatorView'
end
```

터미널에서 다음 명령어를 실행하여 NVActivityIndicatorView를 설치합니다.

```
$ pod install
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하여 화면 로딩 상태 표시를 위한 간단한 단계를 설명하겠습니다.

### 2.1 NVActivityIndicatorView 인스턴스 생성하기

먼저, 화면에 NVActivityIndicatorView를 추가하기 위해 인스턴스를 생성해야 합니다. 이를 위해 다음의 코드를 사용할 수 있습니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicator: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballClipRotate, color: .white, padding: nil)
        activityIndicator.center = view.center
        view.addSubview(activityIndicator)
    }

    // ...
}
```

### 2.2 로딩 상태 표시 및 인터랙션 제한하기

로딩 상태를 표시하고 사용자의 인터랙션을 제한하려면 다음과 같은 코드를 사용할 수 있습니다.

```swift
func startLoading() {
    activityIndicator.startAnimating()
    view.isUserInteractionEnabled = false
}

func stopLoading() {
    activityIndicator.stopAnimating()
    view.isUserInteractionEnabled = true
}
```

`startLoading` 함수를 호출하면 NVActivityIndicatorView가 로딩 상태를 표시하고, `stopLoading` 함수를 호출하면 로딩을 중지합니다. `view.isUserInteractionEnabled`를 설정하여 사용자의 인터랙션을 제한하거나 원래대로 되돌릴 수 있습니다.

## 3. 마무리

이제 NVActivityIndicatorView를 사용하여 화면 로딩 상태를 표시하고 사용자의 인터랙션을 제한하는 방법을 배웠습니다. 이러한 기능을 추가하여 사용자 경험을 향상시킬 수 있으며, 앱의 완성도를 높일 수 있습니다.

더 자세한 내용은 [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.