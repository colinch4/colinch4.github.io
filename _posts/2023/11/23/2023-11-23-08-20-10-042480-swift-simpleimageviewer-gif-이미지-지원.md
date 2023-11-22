---
layout: post
title: "[swift] Swift SimpleImageViewer GIF 이미지 지원"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift로 간단한 이미지 뷰어를 만들고 GIF 이미지를 지원하는 방법에 대해 알아보겠습니다.

## SimpleImageViewer 구성하기

먼저, SimpleImageViewer를 구성하기 위해 `UIImageView`를 사용합니다. SimpleImageViewer는 이미지를 화면에 표시하는 역할을 합니다. 

```swift
import UIKit

class SimpleImageViewer: UIImageView {

    // 이미지를 로드하여 보여주는 메소드
    func load(image: UIImage) {
        self.image = image
    }
}
```

위의 코드에서 `load(image:)` 메소드는 이미지를 받아와서 `UIImageView`에 설정해줍니다.

## GIF 이미지 지원하기

GIF 이미지를 지원하기 위해서는 `UIImage+GIF.swift` 파일을 추가해야 합니다. 해당 파일을 내려받거나 직접 작성하여 프로젝트에 추가합니다.

```swift
import UIKit
import ImageIO

extension UIImage {

    public class func gifImageWithData(data: NSData) -> UIImage? {
        guard let source = CGImageSourceCreateWithData(data, nil) else {
            print("Invalid source")
            return nil
        }
        
        var images = [UIImage]()
        let count = CGImageSourceGetCount(source)
        
        for i in 0..<count {
            if let cgImage = CGImageSourceCreateImageAtIndex(source, i, nil) {
                let image = UIImage(cgImage: cgImage)
                images.append(image)
            }
        }
        
        return UIImage.animatedImage(with: images, duration: totalDuration(source: source))
    }
    
    public class func totalDuration(source: CGImageSource) -> TimeInterval {
        let count = CGImageSourceGetCount(source)
        var duration: TimeInterval = 0
        
        for i in 0..<count {
            if let properties = CGImageSourceCopyPropertiesAtIndex(source, i, nil) as? NSDictionary,
               let gifProperties = properties[kCGImagePropertyGIFDictionary] as? NSDictionary,
               let frameDuration = gifProperties[kCGImagePropertyGIFDelayTime] as? NSNumber {
                duration += frameDuration.doubleValue
            }
        }
        
        return duration
    }
}

```

위의 확장(extension) 코드를 통해 `UIImage` 클래스에 GIF 이미지 지원 기능을 추가합니다. 

SimpleImageViewer의 `load(image:)` 메소드를 다음과 같이 수정하여 GIF 이미지를 지원하도록 합니다.

```swift
extension SimpleImageViewer {
    func load(gifData: Data) {
        if let gifImage = UIImage.gifImageWithData(data: gifData) {
            self.image = gifImage
        } else {
            print("Failed to load GIF image")
        }
    }
}
```

## GIF 이미지 뷰어 사용하기

이제 GIF 이미지 뷰어를 사용해보겠습니다. 먼저, SimpleImageViewer를 인스턴스화하고 `load(gifData:)` 메소드를 사용하여 GIF 이미지를 로드합니다.

```swift
let imageView = SimpleImageViewer()
let gifData = // GIF 이미지 데이터

imageView.load(gifData: gifData)
```

위의 예제 코드에서 `gifData`는 로드할 GIF 이미지의 데이터를 나타냅니다. `load(gifData:)` 메소드를 호출하여 GIF 이미지를 로드한 후 `imageView`에 표시합니다.

## 결론

이렇게 Swift로 간단한 이미지 뷰어를 만들고 GIF 이미지를 지원하는 방법을 알아보았습니다. GIF 이미지를 지원하는 기능은 유용하게 활용될 수 있으니 필요한 경우 이를 활용해보세요!

## 참고 자료

- [iOS: Loading and Displaying Animated GIFs](https://www.appcoda.com/animated-gif-nsdata/)