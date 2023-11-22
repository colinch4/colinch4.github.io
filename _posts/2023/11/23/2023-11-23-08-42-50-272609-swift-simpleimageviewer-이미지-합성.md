---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 합성"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 합성은 Swift에서 매우 일반적인 작업 중 하나입니다. 단순하게 이미지를 합성하여 새로운 이미지를 만들 수 있습니다. 이번 예제에서는 Swift를 사용하여 앱에서 사용자가 선택한 이미지를 합성하는 방법을 살펴보겠습니다.

## 프로젝트 설정

1. Xcode에서 새로운 프로젝트를 생성합니다.
2. 적절한 이름을 지정하고 iOS 앱을 선택합니다.
3. 프로젝트를 생성한 후, Assets.xcassets에 이미지를 추가합니다. 이 예제에서는 `background.png`와 `overlay.png`라는 두 개의 이미지를 사용합니다.

## SimpleImageViewer 클래스 만들기

1. 새로운 Swift 파일을 생성합니다.
2. 다음 코드로 `SimpleImageViewer` 클래스를 만듭니다:

```swift
import UIKit

class SimpleImageViewer {
    
    static func compositeImages(backgroundImage: UIImage, overlayImage: UIImage) -> UIImage? {
        UIGraphicsBeginImageContextWithOptions(backgroundImage.size, false, 0.0)
        
        backgroundImage.draw(in: CGRect(x: 0, y: 0, width: backgroundImage.size.width, height: backgroundImage.size.height))
        overlayImage.draw(in: CGRect(x: 0, y: 0, width: backgroundImage.size.width, height: backgroundImage.size.height))
        
        let compositeImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        
        return compositeImage
    }
    
}
```

위의 코드에서 `compositeImages` 메서드는 주어진 `backgroundImage`와 `overlayImage`를 합성하여 새로운 이미지를 생성합니다. 합성된 이미지는 `compositeImage`로 반환됩니다.

## 뷰 컨트롤러에서 SimpleImageViewer 사용하기

1. 적절한 뷰 컨트롤러를 엽니다.
2. 이미지를 합성하기 위해 뷰 컨트롤러에 UIImageView를 추가합니다. 이 예제에서는 `backgroundImageView`라는 이름의 이미지 뷰를 사용합니다.
3. 뷰 컨트롤러의 viewDidLoad 메서드에 다음 코드를 추가합니다:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    let backgroundImage = UIImage(named: "background")
    let overlayImage = UIImage(named: "overlay")
    
    if let compositeImage = SimpleImageViewer.compositeImages(backgroundImage: backgroundImage, overlayImage: overlayImage) {
        backgroundImageView.image = compositeImage
    }
}
```

위의 코드에서는 `backgroundImage`와 `overlayImage`를 로드한 다음, `compositeImages` 메서드를 사용하여 이미지를 합성합니다. 합성된 이미지는 `backgroundImageView`에 표시됩니다.

## 결과

이미지 합성이 성공적으로 이루어지면, 앱에서 사용자에게 합성된 이미지가 표시됩니다.

여기까지 Swift를 사용하여 이미지를 합성하는 방법을 알아보았습니다. 이미지 합성은 다양한 앱에서 유용하게 사용될 수 있으므로, 앱의 요구 사항에 맞게 이 코드를 수정하거나 확장할 수도 있습니다.