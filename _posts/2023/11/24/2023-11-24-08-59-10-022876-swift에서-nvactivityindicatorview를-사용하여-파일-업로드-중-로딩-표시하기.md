---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 파일 업로드 중 로딩 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 파일 업로드 중 로딩 표시를 할 수 있는 NVActivityIndicatorView를 사용하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 파일 업로드, 네트워크 작업 등 앱 내에서 긴 작업을 수행할 때 사용자에게 로딩 표시를 보여주는 데 사용됩니다. 이는 사용자 경험을 향상시키고, 앱이 응답하지 않는 것처럼 느껴지는 것을 방지합니다.

## 설치

NVActivityIndicatorView는 CocoaPods로 설치할 수 있습니다. Podfile에 아래 코드를 추가해주세요.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 아래 명령어를 실행하여 CocoaPods를 설치해주세요.

```
$ pod install
```

## 사용법

1. 먼저, NVActivityIndicatorView를 import 해주세요.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화하고, 원하는 크기와 스타일을 설정해주세요. 코드는 아래와 같습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballScaleRippleMultiple, color: .blue)
```

3. NVActivityIndicatorView를 화면에 추가하고 애니메이션을 시작합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

4. 파일 업로드가 완료되면, 애니메이션을 중지하고 NVActivityIndicatorView를 화면에서 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 예시 코드

아래는 NVActivityIndicatorView를 사용하여 파일 업로드 중 로딩 표시를 하는 예시 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class UploadViewController: UIViewController {

   let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballScaleRippleMultiple, color: .blue)

   func uploadFile() {
       view.addSubview(activityIndicatorView)
       activityIndicatorView.startAnimating()

       // 파일 업로드 로직

       activityIndicatorView.stopAnimating()
       activityIndicatorView.removeFromSuperview()
   }

}
```

이제 NVActivityIndicatorView를 사용하여 Swift에서 파일 업로드 중에 로딩 표시를 할 수 있습니다.

참고: [NVActivityIndicatorView 공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)