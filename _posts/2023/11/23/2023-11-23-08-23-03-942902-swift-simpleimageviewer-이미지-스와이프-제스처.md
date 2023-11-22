---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 스와이프 제스처"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

## 소개

이미지 스와이프 제스처는 사용자가 이미지를 스와이프하여 다른 이미지로 전환할 수 있는 기능을 제공합니다. Swift 언어를 사용하여 간단한 이미지 뷰어를 만들어 보겠습니다.

## 구현

### 이미지 뷰어 생성

```swift
import UIKit

class SimpleImageViewer: UIViewController {
    
    var images: [UIImage] = []
    var currentImageIndex = 0
    
    private var imageView: UIImageView!
    private var swipeGestureRecognizer: UISwipeGestureRecognizer!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupImageView()
        setupSwipeGestureRecognizer()
    }
    
    private func setupImageView() {
        imageView = UIImageView(frame: view.bounds)
        imageView.contentMode = .scaleAspectFit
        imageView.image = images[currentImageIndex]
        view.addSubview(imageView)
    }
    
    private func setupSwipeGestureRecognizer() {
        swipeGestureRecognizer = UISwipeGestureRecognizer(target: self, action: #selector(handleSwipeGesture(_:)))
        swipeGestureRecognizer.direction = [.left, .right]
        imageView.addGestureRecognizer(swipeGestureRecognizer)
        imageView.isUserInteractionEnabled = true
    }
    
    @objc private func handleSwipeGesture(_ gestureRecognizer: UISwipeGestureRecognizer) {
        if gestureRecognizer.direction == .left {
            showNextImage()
        } else if gestureRecognizer.direction == .right {
            showPreviousImage()
        }
    }
    
    private func showNextImage() {
        if currentImageIndex < images.count - 1 {
            currentImageIndex += 1
            imageView.image = images[currentImageIndex]
        }
    }
    
    private func showPreviousImage() {
        if currentImageIndex > 0 {
            currentImageIndex -= 1
            imageView.image = images[currentImageIndex]
        }
    }
}
```

### 이미지 뷰어 사용

```swift
let images: [UIImage] = [UIImage(named: "image1"), UIImage(named: "image2"), UIImage(named: "image3")]        
let imageViewer = SimpleImageViewer()
imageViewer.images = images

// 이미지 뷰어를 현재 화면 위에 모달로 표시
present(imageViewer, animated: true, completion: nil)
```

## 결과

위의 코드를 실행하면 이미지 스와이프 제스처를 사용하여 다음 이미지 또는 이전 이미지로 전환할 수 있는 이미지 뷰어가 생성됩니다.

## 결론

이번 포스트에서는 Swift를 사용하여 이미지 스와이프 제스처를 구현하는 방법을 알아보았습니다. 사용자가 이미지를 스와이프하여 다른 이미지로 전환할 수 있도록 하는 기능은 이미지 뷰어를 개발할 때 매우 유용하게 사용될 수 있습니다.

더 많은 기능을 추가하여 사용자 친화적인 이미지 뷰어를 개발해보세요!