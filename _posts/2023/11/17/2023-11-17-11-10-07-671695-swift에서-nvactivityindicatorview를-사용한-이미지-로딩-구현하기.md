---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 이미지 로딩 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이미지 로딩은 iOS 앱 개발에서 중요한 요소 중 하나입니다. 사용자가 앱에서 이미지를 로딩할 때 로딩 표시기를 표시하여 사용자 경험을 향상시킬 수 있습니다. 이를 위해 NVActivityIndicatorView를 사용하여 이미지 로딩 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 사용자 정의 로딩 표시기를 구현하기 위한 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 스타일과 색상의 로딩 표시기를 제공하며, 사용하기 쉬운 API를 제공합니다.

## NVActivityIndicatorView 설치하기

CocoaPods를 사용하여 NVActivityIndicatorView를 설치할 수 있습니다. 

1. `Podfile` 파일을 열고, 아래의 코드를 추가합니다:
   ```ruby
   pod 'NVActivityIndicatorView'
   ```
2. 터미널에서 `pod install` 명령을 실행합니다.

## NVActivityIndicatorView를 사용한 이미지 로딩 구현하기
```swift
import NVActivityIndicatorView

class ImageLoaderViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 표시기 설정
        activityIndicatorView.type = .ballScaleRippleMultiple
        activityIndicatorView.color = .gray
        activityIndicatorView.center = view.center
        activityIndicatorView.startAnimating()
        view.addSubview(activityIndicatorView)
        
        // 이미지 로드
        loadImage()
    }
    
    func loadImage() {
        // 이미지 로딩 시작
        DispatchQueue.global().async {
            let imageURL = URL(string: "https://example.com/image.jpg")
            guard let imageData = try? Data(contentsOf: imageURL!) else {
                return
            }
            
            // 이미지 로딩 후 처리
            DispatchQueue.main.async {
                self.imageView.image = UIImage(data: imageData)
                self.activityIndicatorView.stopAnimating()
                self.activityIndicatorView.removeFromSuperview()
            }
        }
    }
}
```

위의 코드는 NVActivityIndicatorView를 사용하여 이미지 로딩을 구현한 예시입니다. `NVActivityIndicatorView` 객체를 생성하고, 로딩 표시기의 모양과 색상을 설정한 후 `view.addSubview()`를 통해 화면에 추가합니다. 이후 이미지를 비동기적으로 로드하는 `loadImage()` 메서드를 호출하고, 이미지 로딩이 완료되면 메인 스레드에서 이미지를 표시하고 로딩 표시기를 중지 및 제거합니다.

위의 예시 코드에서 `https://example.com/image.jpg`는 실제 이미지 URL로 대체되어야 합니다. 

## 결론

NVActivityIndicatorView를 사용하여 Swift에서 이미지 로딩 표시기를 구현하는 방법을 알아보았습니다. 이를 통해 앱의 사용자 경험을 향상시킬 수 있으며, 다양한 스타일의 로딩 표시기를 사용할 수 있습니다.

참고 링크:
- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)
- [CocoaPods](https://cocoapods.org/)