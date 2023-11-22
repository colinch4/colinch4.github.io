---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 사이즈 변경 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어는 대부분의 앱에서 매우 중요한 역할을 합니다. 이미지를 로드하고 표시하기 위해 많은 라이브러리와 프레임워크가 있지만, 간단하게 이미지를 로드하고 사이즈를 조정하는 기능을 가진 Swift SimpleImageViewer를 만들어보겠습니다.

## 준비하기

먼저 프로젝트에 `SimpleImageViewer.swift`라는 이름의 새로운 Swift 파일을 생성합니다. 그리고 다음과 같은 코드를 복사하여 붙여넣습니다.

```swift
import UIKit

class SimpleImageViewer: UIImageView {
    
    override var image: UIImage? {
        get { return super.image }
        set {
            super.image = newValue
            resizeImage()
        }
    }
    
    private func resizeImage() {
        guard let image = self.image else { return }
        
        let targetSize = CGSize(width: 200, height: 200) // 원하는 이미지 사이즈
        let scaledSize = image.size.scaleAspectFit(withinSize: targetSize)
        
        UIGraphicsBeginImageContextWithOptions(scaledSize, false, 0.0)
        image.draw(in: CGRect(origin: .zero, size: scaledSize))
        let resizedImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        
        super.image = resizedImage
    }
}

extension CGSize {
    func scaleAspectFit(withinSize targetSize: CGSize) -> CGSize {
        let widthRatio = targetSize.width / self.width
        let heightRatio = targetSize.height / self.height
        
        let scaleRatio = min(widthRatio, heightRatio)
        
        return CGSize(
            width: self.width * scaleRatio,
            height: self.height * scaleRatio
        )
    }
}
```

`SimpleImageViewer`라는 클래스는 `UIImageView`를 상속받아 이미지 사이즈를 변환하는 기능을 추가한 클래스입니다. `image` 프로퍼티가 설정될 때마다 `resizeImage()` 메서드가 호출되어 이미지 사이즈가 조정됩니다.

`resizeImage()` 메서드는 원하는 이미지 사이즈를 `targetSize` 변수에 지정한 후 `scaleAspectFit(withinSize:)` 확장 메서드를 사용하여 이미지를 조정합니다. 조정한 이미지는 `resizedImage` 변수에 저장되고, 이를 `super.image`에 할당하여 이미지가 화면에 보이도록 합니다.

`scaleAspectFit(withinSize:)` 확장 메서드는 현재 이미지의 비율을 유지하면서 지정한 크기로 조정하는 역할을 합니다.

## 사용하기

뷰 컨트롤러에 `SimpleImageViewer` 인스턴스를 추가하고 이미지를 로드해보겠습니다.

```swift
import UIKit

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let imageView = SimpleImageViewer(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
        imageView.contentMode = .scaleAspectFit
        imageView.image = UIImage(named: "example_image")
        
        view.addSubview(imageView)
    }
}
```

`SimpleImageViewer`를 사용하기 위해 해당 클래스의 인스턴스를 생성하고 이미지를 설정합니다. 이미지는 `UIImage(named:)`를 사용하여 불러온 다음, `imageView.image`에 할당합니다.

## 결과 확인하기

이제 앱을 빌드하여 실행해보면, 이미지가 지정한 사이즈로 조정되어 보일 것입니다. `SimpleImageViewer`가 이미지를 로드하고 자동으로 사이즈를 조정하는 기능을 가지고 있습니다.

## 결론

위의 방법을 사용하여 간단한 이미지 뷰어를 만들어보았습니다. `SimpleImageViewer` 클래스를 사용하여 이미지 사이즈 조정 기능을 손쉽게 구현할 수 있습니다. 이 코드를 활용하여 이미지 뷰어를 개선하거나 다른 기능을 추가할 수도 있습니다.

참고 자료:
- [UIKit - UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)
- [UIKit - UIImage](https://developer.apple.com/documentation/uikit/uiimage)