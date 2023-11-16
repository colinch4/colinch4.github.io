---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 효과 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 많은 다양한 스피너 애니메이션을 제공하는 오픈 소스 라이브러리입니다. 이 라이브러리를 사용하면 앱에서 로딩, 작업 진행 등을 나타내기 위한 효과적인 애니메이션을 구현할 수 있습니다.

## NVActivityIndicatorView 설치하기

1. `CocoaPods`를 사용하여 NVActivityIndicatorView를 프로젝트에 추가합니다. `Podfile`에 다음과 같이 라이브러리를 추가합니다.
```
pod 'NVActivityIndicatorView'
```

2. 터미널에서 프로젝트 디렉토리로 이동한 후, 다음 명령어를 실행하여 라이브러리를 설치합니다.
```
pod install
```

3. 설치가 완료되면 `.xcworkspace` 파일을 열어서 프로젝트를 실행합니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 사용하기 위해서는 먼저 `NVActivityIndicatorViewDelegate`를 구현해야 합니다. 해당 프로토콜은 애니메이션이 시작되거나 종료될 때 호출되는 메소드를 정의합니다.

```swift
class ViewController: UIViewController, NVActivityIndicatorViewDelegate {
    // ...
}
```

2. NVActivityIndicatorView를 사용할 View를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScale, color: .red, padding: .none)
```

위의 코드에서 `frame`은 View의 크기와 위치를 설정하는 부분입니다. `type`은 애니메이션 모양을 결정하는 부분입니다. 여러 가지 애니메이션 타입을 사용할 수 있으며, 필요에 따라 설정합니다. `color`는 애니메이션의 색상을 설정하는 부분입니다. `padding`은 애니메이션과 View 경계 간의 여백을 설정하는 부분입니다.

3. View를 화면에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

위의 코드에서 `addSubview`를 사용하여 생성한 View를 화면에 추가합니다. `center`를 사용하여 해당 View를 화면의 가운데로 위치시킵니다.

4. 애니메이션을 시작하고 종료하는 메소드를 구현합니다.

```swift
func startAnimating() {
    activityIndicatorView.startAnimating()
}

func stopAnimating() {
    activityIndicatorView.stopAnimating()
}
```

위의 코드에서 `startAnimating`은 애니메이션을 시작하는 메소드입니다. `stopAnimating`은 애니메이션을 종료하는 메소드입니다.

5. 애니메이션을 시작하거나 종료해보세요.

```swift
startAnimating()

// 애니메이션이 끝난 후에는 다음과 같이 종료할 수 있습니다.
stopAnimating()
```

NVActivityIndicatorView를 사용하여 앱에 효과적인 애니메이션을 설정할 수 있습니다. 여러 가지 옵션을 통해 원하는 스피너 애니메이션을 사용하고, 색상과 위치를 조정할 수 있습니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인하실 수 있습니다.