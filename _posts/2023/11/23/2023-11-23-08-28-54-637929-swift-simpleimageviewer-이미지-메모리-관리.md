---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 메모리 관리"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift를 사용하여 iOS 앱을 개발할 때, 이미지 메모리 관리는 중요한 과제 중 하나입니다. 특히, 이미지 뷰어에서는 많은 이미지를 동시에 로드하고 표시해야 하므로 메모리 관리가 더욱 중요합니다. 이 글에서는 Swift를 사용하여 간단한 이미지 뷰어를 개발하면서 이미지 메모리 관리에 대해 살펴보겠습니다.

## 1. 이미지 로드 및 표시

가장 먼저, 이미지 뷰어에서 이미지를 로드하고 표시하는 코드부터 살펴보겠습니다. 다음은 Swift에서 UIImageView를 사용하여 이미지를 로드하고 표시하는 코드입니다.

```swift
import UIKit

class ImageViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!

    func loadImage(withURL imageURL: URL) {
        DispatchQueue.global().async {
            if let imageData = try? Data(contentsOf: imageURL) {
                let image = UIImage(data: imageData)
                DispatchQueue.main.async {
                    self.imageView.image = image
                }
            }
        }
    }
    
    // 이미지를 로드하고 표시하는 다른 코드들...
}
```

위의 코드에서는 `loadImage(withURL:)` 메소드를 사용하여 이미지를 로드하고 표시합니다. 이 메소드는 비동기적으로 이미지 데이터를 다운로드하고, 메인 큐에서 이미지를 설정합니다.

## 2. 이미지 메모리 관리

하지만 위의 코드는 메모리 관리 측면에서 문제가 있을 수 있습니다. 만약, 이미지가 많이 로드되고 메모리에 남아있는 경우, 앱의 성능 문제와 메모리 부족 문제를 야기할 수 있습니다. 따라서, 이미지 메모리 관리를 위한 몇 가지 방법을 알아보겠습니다.

### 2.1. 이미지 캐싱

이미지 캐싱은 이미지를 로드한 후, 메모리에 저장하여 다음에 다시 사용할 때 로드 시간을 단축시키는 기술입니다. iOS에서는 NSCache 클래스를 사용하여 메모리 캐시를 구현할 수 있습니다. 다음은 이미지 캐싱을 추가한 코드입니다.

```swift
import UIKit

class ImageViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    
    let imageCache = NSCache<NSString, UIImage>()

    func loadImage(withURL imageURL: URL) {
        DispatchQueue.global().async {
            if let cachedImage = self.imageCache.object(forKey: imageURL.absoluteString as NSString) {
                DispatchQueue.main.async {
                    self.imageView.image = cachedImage
                }
            } else if let imageData = try? Data(contentsOf: imageURL) {
                let image = UIImage(data: imageData)
                self.imageCache.setObject(image, forKey: imageURL.absoluteString as NSString)
                DispatchQueue.main.async {
                    self.imageView.image = image
                }
            }
        }
    }
    
    // 이미지를 로드하고 표시하는 다른 코드들...
}
```

위의 코드에서는 `imageCache`라는 NSCache 인스턴스를 추가하여 이미지를 캐싱합니다. 이미지를 로드할 때, 먼저 캐시에 이미지가 있는지 확인하고, 있다면 캐시된 이미지를 표시합니다. 그렇지 않은 경우에만 이미지를 다운로드하고 캐시에 저장합니다.

### 2.2. 메모리 경고 감지

iOS는 메모리 경고를 감지할 수 있는 기능을 제공합니다. 이를 활용하여 메모리 부족 상황에서 이미지를 해제할 수 있습니다. 다음은 메모리 경고를 감지하고 이미지를 해제하는 코드입니다.

```swift
import UIKit

class ImageViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    
    let imageCache = NSCache<NSString, UIImage>()

    func loadImage(withURL imageURL: URL) {
        DispatchQueue.global().async {
            if let cachedImage = self.imageCache.object(forKey: imageURL.absoluteString as NSString) {
                DispatchQueue.main.async {
                    self.imageView.image = cachedImage
                }
            } else if let imageData = try? Data(contentsOf: imageURL) {
                let image = UIImage(data: imageData)
                self.imageCache.setObject(image, forKey: imageURL.absoluteString as NSString)
                DispatchQueue.main.async {
                    self.imageView.image = image
                }
                
                // 메모리가 부족한 경우 해제
                NotificationCenter.default.addObserver(forName: UIApplication.didReceiveMemoryWarningNotification, object: nil, queue: OperationQueue.main) { _ in
                    self.imageCache.removeAllObjects()
                }
            }
        }
    }
    
    // 이미지를 로드하고 표시하는 다른 코드들...
}
```

위의 코드에서는 `UIApplication.didReceiveMemoryWarningNotification` 노티피케이션을 사용하여 메모리 경고를 감지하고, 메모리가 부족한 경우 캐시된 이미지를 모두 해제합니다.

## 3. 결론

Swift를 사용하여 iOS 앱에서 이미지 메모리 관리를 제대로 해야합니다. 이 글에서는 이미지 캐싱과 메모리 경고 감지를 통해 이미지 메모리 관리를 개선하는 방법을 알아보았습니다. 앱의 성능과 메모리 사용량을 최적화하기 위해 이러한 방법들을 적절히 활용해보세요.

## 참고 자료

- [NSCache - Apple Developer Documentation](https://developer.apple.com/documentation/foundation/nscache)
- [Entering the background - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_background/entering_the_background)