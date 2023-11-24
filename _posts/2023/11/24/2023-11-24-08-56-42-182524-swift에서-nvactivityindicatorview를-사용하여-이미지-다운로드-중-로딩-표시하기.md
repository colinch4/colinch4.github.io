---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 이미지 다운로드 중 로딩 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 개요
이미지 다운로드 시 사용자에게 로딩 상태를 보여주는 로딩 표시기가 필요한 경우, NVActivityIndicatorView를 사용할 수 있습니다. 이 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 이미지 다운로드 중 로딩 표시하는 방법에 대해서 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 Swift에서 사용할 수 있는 로딩 표시기 라이브러리입니다. 다양한 로딩 스타일과 색상을 제공하며, 쉽게 사용할 수 있습니다.

## 설치하기
NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods을 통해 라이브러리를 설치해야 합니다. Podfile에 다음과 같이 추가해주세요.

```
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 설치해주세요.

```
$ pod install
```

## 사용하기
1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화합니다. 이때 프레임의 크기와 로딩 스타일을 지정할 수 있습니다.

```swift
let loadingIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .blue, padding: nil)
```

3. 이미지 다운로드 시작 전에 로딩 표시기를 추가합니다.

```swift
view.addSubview(loadingIndicator)
loadingIndicator.startAnimating()
```

4. 이미지 다운로드가 완료되면 로딩 표시기를 제거합니다.

```swift
loadingIndicator.stopAnimating()
loadingIndicator.removeFromSuperview()
```

## 예제 코드
다음은 이미지 다운로드 중 로딩 표시를 구현하는 예제 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let loadingIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .blue, padding: nil)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        view.addSubview(loadingIndicator)
        loadingIndicator.center = view.center
        
        startImageDownload()
    }
    
    func startImageDownload() {
        loadingIndicator.startAnimating()
        
        // 이미지 다운로드 로직 구현
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            self.loadingIndicator.stopAnimating()
            self.loadingIndicator.removeFromSuperview()
            
            // 이미지 다운로드가 완료되면 처리할 로직
        }
    }
}
```

## 결론
이미지 다운로드 중에 사용자에게 로딩 상태를 보여주는 로딩 표시기는 사용자 경험을 개선하는 데 큰 도움이 됩니다. Swift에서 NVActivityIndicatorView를 사용하면 쉽게 로딩 표시기를 구현할 수 있습니다.