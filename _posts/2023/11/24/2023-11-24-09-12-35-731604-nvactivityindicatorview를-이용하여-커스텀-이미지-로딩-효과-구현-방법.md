---
layout: post
title: "[swift] NVActivityIndicatorView를 이용하여 커스텀 이미지 로딩 효과 구현 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 기술 블로그에서는 앱에서 커스텀 이미지 로딩 효과를 구현하는 방법에 대해 알아보겠습니다. 이를 위해 NVActivityIndicatorView 라이브러리를 사용할 것입니다. NVActivityIndicatorView는 로딩 스피너를 쉽게 구현할 수 있도록 도와주는 Swift 기반의 라이브러리입니다.

## 1. NVActivityIndicatorView 설치

먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. 이를 위해 CocoaPods를 사용하겠습니다. `Podfile`에 아래와 같이 추가해주세요.

```
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 2. 이미지 로딩 효과 구현

### 2.1 NVActivityIndicatorView 인스턴스 생성

이미지 로딩 효과를 보여주기 위해, NVActivityIndicatorView의 인스턴스를 생성합니다. 이 때 스피너의 크기와 색상을 설정할 수 있습니다. 아래는 예시 코드입니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let spinnerSize: CGFloat = 50
        let spinnerColor: UIColor = .red
        
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: spinnerSize, height: spinnerSize),
                                                        type: .ballScaleRippleMultiple,
                                                        color: spinnerColor,
                                                        padding: nil)
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }
}
```

### 2.2 로딩 효과 시작 및 중지

로딩 효과를 시작하고 중지하기 위해, 다음 함수를 추가합니다.

```swift
class LoadingViewController: UIViewController {
    // ...

    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
}
```

### 2.3 이미지 로딩 시 로딩 효과 사용

이제 이미지 로딩 시에 로딩 효과를 사용할 수 있습니다. 예를 들어, Alamofire를 사용하여 이미지를 다운로드하는 경우, 아래와 같이 구현할 수 있습니다.

```swift
import Alamofire
import NVActivityIndicatorView

class ImageViewController: UIViewController {
    var imageView: UIImageView!
    var loadingViewController: LoadingViewController!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
        view.addSubview(imageView)
        imageView.center = view.center
        
        loadingViewController = LoadingViewController()
        addChild(loadingViewController)
        view.addSubview(loadingViewController.view)
        
        loadImage()
    }
    
    func loadImage() {
        loadingViewController.startLoading()
        
        let imageUrl = URL(string: "https://example.com/image.jpg")
        
        Alamofire.request(imageUrl!).response { response in
            if let data = response.data {
                let image = UIImage(data: data)
                self.imageView.image = image
            }
            
            self.loadingViewController.stopLoading()
        }
    }
}
```

이제 앱에서 이미지를 불러올 때마다 NVActivityIndicatorView를 사용하여 커스텀 이미지 로딩 효과를 볼 수 있습니다.

## 요약

이번 기술 블로그에서는 NVActivityIndicatorView를 사용하여 커스텀 이미지 로딩 효과를 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 손쉽게 로딩 스피너를 구현할 수 있으며, 앱의 사용자 경험을 향상시킬 수 있습니다.

더 자세한 내용은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 확인해주세요.