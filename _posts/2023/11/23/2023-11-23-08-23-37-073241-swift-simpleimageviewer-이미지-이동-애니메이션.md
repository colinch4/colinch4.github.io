---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 이동 애니메이션"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift를 사용하여 이미지 뷰어를 개발할 때, 이미지 이동 애니메이션을 추가하는 방법에 대해 알아보겠습니다.

## 1. SimpleImageViewer 구현하기

먼저, SimpleImageViewer 클래스를 구현해야 합니다. 이 클래스는 이미지를 표시하고 이동 애니메이션을 처리하는 역할을 합니다.

```swift
import UIKit

class SimpleImageViewer: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    
    var images: [UIImage] = []
    var currentIndex: Int = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰 설정
        imageView.contentMode = .scaleAspectFit
        imageView.image = images[currentIndex]
        
        // 제스처 추가
        let swipeLeftGesture = UISwipeGestureRecognizer(target: self, action: #selector(swipeLeft))
        swipeLeftGesture.direction = .left
        view.addGestureRecognizer(swipeLeftGesture)
        
        let swipeRightGesture = UISwipeGestureRecognizer(target: self, action: #selector(swipeRight))
        swipeRightGesture.direction = .right
        view.addGestureRecognizer(swipeRightGesture)
    }
    
    @objc func swipeLeft() {
        // 이미지 왼쪽으로 이동
        if currentIndex < images.count - 1 {
            currentIndex += 1
            animateImageTransition()
        }
    }
    
    @objc func swipeRight() {
        // 이미지 오른쪽으로 이동
        if currentIndex > 0 {
            currentIndex -= 1
            animateImageTransition()
        }
    }
    
    func animateImageTransition() {
        UIView.transition(with: imageView, duration: 0.3, options: .transitionCrossDissolve, animations: {
            self.imageView.image = self.images[self.currentIndex]
        }, completion: nil)
    }
}
```

위 코드에서는 우선 `SimpleImageViewer` 클래스를 선언하고, `UIImageView`를 생성해 이미지를 표시할 준비를 합니다. 

`viewDidLoad` 메서드에서 `UIImageView`를 설정하고 이미지를 첫 번째 이미지로 설정합니다. 

또한 `UISwipeGestureRecognizer`를 이용하여 왼쪽으로 스와이프하면 `swipeLeft` 메서드가 호출되며 이미지를 왼쪽으로 이동시키고, 오른쪽으로 스와이프하면 `swipeRight` 메서드가 호출되며 이미지를 오른쪽으로 이동시킵니다.

`animateImageTransition` 메서드에서는 이미지 뷰의 페이드 애니메이션을 처리합니다.

## 2. SimpleImageViewer 사용하기

다음은 `SimpleImageViewer` 클래스를 사용하는 방법입니다.

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
    }

    @IBAction func showImageViewer(_ sender: Any) {
        // 이미지 뷰어 인스턴스 생성
        let imageViewer = SimpleImageViewer()
        
        // 이미지 설정
        imageViewer.images = [
            UIImage(named: "image1")!,
            UIImage(named: "image2")!,
            UIImage(named: "image3")!
        ]
        
        // 이미지 뷰어 모달로 표시
        present(imageViewer, animated: true, completion: nil)
    }
}
```

위 코드에서 `ViewController` 클래스에서 `showImageViewer` 메서드가 호출될 때, `SimpleImageViewer` 인스턴스를 생성한 후 이미지를 설정합니다.

그리고 `present` 메서드를 사용하여 이미지 뷰어를 모달로 표시합니다.

## 결론

이렇게 Swift를 사용하여 간단한 이미지 뷰어를 구현하고 이미지 이동 애니메이션을 추가하는 방법을 알아보았습니다. 이를 활용하여 사용자에게 다양한 이미지를 보여줄 수 있는 멋진 앱을 만들어보세요!

## 참고 자료
- [Apple Developer Documentation](https://developer.apple.com/documentation/)
- [SwiftUI Tutorial](https://developer.apple.com/tutorials/swiftui)