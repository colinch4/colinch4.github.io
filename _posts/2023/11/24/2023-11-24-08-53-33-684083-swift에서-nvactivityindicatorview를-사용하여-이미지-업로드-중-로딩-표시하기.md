---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 이미지 업로드 중 로딩 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이미지를 업로드하는 동안 사용자에게 로딩 상태를 표시하는 것은 앱의 사용자 경험을 향상시키는 중요한 요소입니다.
그 중 하나는 `NVActivityIndicatorView`라는 라이브러리를 사용하여 로딩 표시를 구현하는 것입니다.

## `NVActivityIndicatorView`란?

`NVActivityIndicatorView`는 iOS 앱에서 로딩 인디케이터를 표시하기 위한 간단한 Swift 라이브러리입니다. 이 라이브러리는 다양한 스타일과 색상의 로딩 인디케이터를 제공하며, 애니메이션될 수 있습니다.

## `NVActivityIndicatorView` 설치하기

`NVActivityIndicatorView`를 사용하기 위해 먼저 CocoaPods를 사용하여 프로젝트에 라이브러리를 설치해야 합니다. Podfile에 다음과 같이 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그런 다음 터미널을 열고 다음 명령을 실행합니다.

```bash
pod install
```

## `NVActivityIndicatorView` 사용하기

다음은 `NVActivityIndicatorView`를 사용하여 이미지 업로드 중 로딩 표시를 구현하는 예제 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ImageUploadViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .white, padding: nil)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 인디케이터 스타일 및 색상 설정
        activityIndicatorView.type = .ballScaleRippleMultiple
        activityIndicatorView.color = .white
        
        // 로딩 인디케이터 뷰를 화면에 추가
        view.addSubview(activityIndicatorView)
        
        // 로딩 인디케이터가 화면 중앙에 배치되도록 설정
        activityIndicatorView.center = view.center
    }

    func uploadImage() {
        // 이미지 업로드 중 로딩 인디케이터 표시
        activityIndicatorView.startAnimating()

        // 이미지 업로드 로직 작성
        // ...

        // 업로드 완료 후 로딩 인디케이터 숨기기
        activityIndicatorView.stopAnimating()
    }

}
```

위의 예제 코드에서 `NVActivityIndicatorView` 객체를 생성한 다음, 원하는 스타일과 색상을 설정합니다. 그리고 로딩 인디케이터를 뷰에 추가한 후, 업로드 도중에 `startAnimating()`을 호출하여 로딩 표시를 시작하고, 업로드가 완료되면 `stopAnimating()`을 호출하여 로딩 표시를 중지합니다.

이와 같은 방식으로 `NVActivityIndicatorView`를 사용하여 이미지 업로드 중 로딩 표시를 구현할 수 있습니다.

더 많은 사용법과 스타일에 대한 자세한 내용은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하십시오.