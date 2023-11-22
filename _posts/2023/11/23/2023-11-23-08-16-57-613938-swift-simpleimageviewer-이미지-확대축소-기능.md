---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 확대/축소 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어는 사용자가 이미지를 확대하거나 축소할 수 있는 기능을 가진 앱이나 웹 페이지에서 자주 사용됩니다. Swift에서는 `UIScrollView`와 `UIImageView`를 이용하여 간단한 이미지 뷰어를 만들 수 있습니다.

## 1. UIScrollView 설정

먼저, 이미지 뷰어를 만들기 위해 `UIScrollView`를 설정해야 합니다. 

```swift
import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var scrollView: UIScrollView!
    var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 스크롤 뷰 설정
        scrollView.delegate = self
        scrollView.minimumZoomScale = 1.0
        scrollView.maximumZoomScale = 6.0
        
        // 이미지 뷰 설정
        imageView = UIImageView(image: UIImage(named: "image.jpg"))
        imageView.contentMode = .scaleAspectFit
        scrollView.addSubview(imageView)
        
        // 이미지 뷰의 제약 조건 설정
        imageView.translatesAutoresizingMaskIntoConstraints = false
        imageView.topAnchor.constraint(equalTo: scrollView.topAnchor).isActive = true
        imageView.leadingAnchor.constraint(equalTo: scrollView.leadingAnchor).isActive = true
        imageView.trailingAnchor.constraint(equalTo: scrollView.trailingAnchor).isActive = true
        imageView.bottomAnchor.constraint(equalTo: scrollView.bottomAnchor).isActive = true
    }
}
```

## 2. UIScrollViewDelegate 구현

이어서, 이미지 뷰어를 확대 또는 축소하기 위해 `UIScrollViewDelegate`를 구현해야 합니다.

```swift
extension ViewController: UIScrollViewDelegate {
    func viewForZooming(in scrollView: UIScrollView) -> UIView? {
        return imageView
    }
}
```

## 3. 앱 실행

위의 코드를 실행하면 이미지가 보이는 UIScrollView가 만들어집니다. 사용자는 두 손가락을 사용하여 이미지를 확대하거나 축소할 수 있습니다.

## 결론

이것은 Swift에서 간단한 이미지 뷰어를 만드는 방법에 대한 예시입니다. UIScrollView와 UIImageView를 조합하여 이미지를 확대하고 축소할 수 있는 기능을 구현할 수 있습니다. 추가적으로, UIImagePicker 등을 사용하여 사용자가 이미지를 선택할 수 있도록 확장할 수 있습니다.

*참고: [Apple Developer Documentation - UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview), [Apple Developer Documentation - UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)*