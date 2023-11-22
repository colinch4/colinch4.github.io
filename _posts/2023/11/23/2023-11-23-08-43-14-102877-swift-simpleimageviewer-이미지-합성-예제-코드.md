---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 합성 예제 코드"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

## 소개
이 예제 코드는 Swift를 사용하여 이미지 합성을 수행하기 위한 간단한 ImageViewer를 구현하는 방법을 보여줍니다. 이 예제 코드를 사용하여 이미지를 로드하고 합성하여 결과 이미지를 보여줄 수 있습니다.

## 요구 사항
이 예제 코드를 실행하기 위해서는 다음이 필요합니다:
- Swift 5.0 이상
- Xcode 11.0 이상

## 구현
다음은 간단한 이미지 합성을 위한 예제 코드입니다.

```swift
import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let image1 = UIImage(named: "image1")
        let image2 = UIImage(named: "image2")
        
        let size = CGSize(width: image1!.size.width, height: image1!.size.height)
        
        UIGraphicsBeginImageContextWithOptions(size, false, 0.0)
        
        image1?.draw(in: CGRect(x: 0, y: 0, width: size.width, height: size.height))
        image2?.draw(in: CGRect(x: 0, y: 0, width: size.width, height: size.height), blendMode: .normal, alpha: 0.5)
        
        let newImage = UIGraphicsGetImageFromCurrentImageContext()
        
        UIGraphicsEndImageContext()
        
        imageView.image = newImage
    }
}
```

위의 코드는 UIViewController를 사용하여 간단한 ImageViewer를 구현합니다. `ViewController` 클래스는 Storyboard에서 IBOutlet으로 연결된 `imageView` 속성을 가지고 있습니다. 

`viewDidLoad` 메서드에서는 이미지 파일 `image1`과 `image2`를 로드한 후, 이미지를 합성하기 위해 `UIGraphicsBeginImageContextWithOptions` 메서드를 사용하여 새로운 그래픽 컨텍스트를 생성합니다. 이후, `image1`과 `image2`를 원하는 위치에 그리고, 알파 값을 조절하여 합성된 이미지를 생성합니다.

마지막으로, 그래픽 컨텍스트를 정리하고 합성된 이미지를 `imageView`에 할당하여 결과 이미지를 표시합니다.

## 실행
위의 예제 코드를 실행하려면 먼저 `image1`과 `image2`라는 이름의 이미지 파일을 프로젝트에 추가해야 합니다.

## 결론
이 예제 코드를 사용하여 Swift로 이미지 합성을 수행하는 간단한 ImageViewer를 구현하는 방법을 배웠습니다. 이를 활용하여 이미지 합성에 대한 다양한 기능을 추가할 수 있습니다.