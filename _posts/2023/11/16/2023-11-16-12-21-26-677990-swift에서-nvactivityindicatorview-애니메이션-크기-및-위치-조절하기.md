---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기 및 위치 조절하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 애니메이션을 표시하는 데 사용되는 라이브러리입니다. 이 라이브러리를 사용하면 다양한 유형의 애니메이션을 사용할 수 있으며, 그 크기와 위치를 조절할 수도 있습니다. 이번 블로그 게시물에서는 Swift에서 NVActivityIndicatorView 애니메이션의 크기와 위치를 조절하는 방법을 알아보겠습니다.

## 1. NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 설치해야 합니다. 이를 위해 프로젝트의 `Podfile`에 다음과 같은 내용을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

설정 파일에 대한 변경사항을 적용하기 위해 터미널에서 다음 명령어를 실행합니다.

```shell
$ pod install
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 다음과 같이 import 문을 추가합니다.

```swift
import NVActivityIndicatorView
```

그런 다음, 애니메이션을 표시할 뷰 컨트롤러에 NVActivityIndicatorView를 추가합니다.

```swift
class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 인스턴스 생성
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .blue, padding: nil)

        // 뷰 컨트롤러에 애니메이션 뷰를 추가
        self.view.addSubview(activityIndicatorView)

        // 애니메이션 시작
        activityIndicatorView.startAnimating()
    }
}
```

위의 예제에서는 애니메이션의 크기를 50x50으로 설정하였고, 스타일은 `circleStrokeSpin`으로 설정하였습니다. 또한, 색상은 파란색으로 설정하였습니다.

## 3. 애니메이션 위치 조절하기

NVActivityIndicatorView의 위치를 조절하는 방법에는 여러 가지가 있습니다. 예를 들어, 애니메이션 뷰를 수평 및 수직 중앙에 위치시키려면 다음과 같이 코드를 변경할 수 있습니다.

```swift
let screenWidth = UIScreen.main.bounds.width
let screenHeight = UIScreen.main.bounds.height

let xPosition = (screenWidth - 50) / 2 // 50x50으로 설정한 애니메이션의 크기를 고려하여 위치 계산
let yPosition = (screenHeight - 50) / 2

activityIndicatorView.frame = CGRect(x: xPosition, y: yPosition, width: 50, height: 50)
```

위 코드를 적용하면 애니메이션이 화면의 중앙에 위치하게 됩니다.

## 결론

이제 Swift에서 NVActivityIndicatorView 애니메이션의 크기와 위치를 조절하는 방법을 알게 되었습니다. 이를 통해 더욱 유연한 애니메이션 효과를 구현할 수 있을 것입니다. 좀 더 자세한 설정 방법과 옵션에 대해서는 [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.