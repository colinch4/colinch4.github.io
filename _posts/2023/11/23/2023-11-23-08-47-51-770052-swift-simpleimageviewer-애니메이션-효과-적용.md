---
layout: post
title: "[swift] Swift SimpleImageViewer 애니메이션 효과 적용"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift에서 애니메이션 효과를 사용하여 이미지 뷰어를 만드는 방법을 알아보겠습니다. SimpleImageViewer는 이미지를 확대 및 축소하고 스와이프하여 다음 또는 이전 이미지로 이동할 수 있는 간단한 이미지 뷰어입니다.

## 애니메이션 효과를 위한 준비

이미지를 확대 및 축소하기 위해서는 `UIScrollView`를 사용합니다. 따라서, 이미지 뷰어를 담을 `UIScrollView`를 생성합니다.

```swift
let scrollView = UIScrollView(frame: view.bounds)
scrollView.backgroundColor = .black
view.addSubview(scrollView)
```

또한, 이미지 뷰어의 축소 상태에서 확대되었을 때 효과를 주기 위해 `UIScrollViewDelegate` 프로토콜을 구현합니다. 

```swift
extension ViewController: UIScrollViewDelegate {
    func viewForZooming(in scrollView: UIScrollView) -> UIView? {
        return imageView
    }
    
    func scrollViewDidZoom(_ scrollView: UIScrollView) {
        updateImageViewConstraints()
    }
}
```

## 이미지 로딩 및 확대/축소

이미지 뷰어에 이미지를 로딩하고 확대/축소하는 방법은 다음과 같습니다.

```swift
func loadImage(image: UIImage) {
    imageView.removeFromSuperview()
    
    scrollView.contentSize = image.size
    scrollView.delegate = self
    
    imageView = UIImageView(image: image)
    imageView.contentMode = .scaleAspectFit
    imageView.isUserInteractionEnabled = true
    scrollView.addSubview(imageView)
    
    updateImageViewConstraints()
}

func updateImageViewConstraints() {
    let imageSize = imageView.image?.size ?? CGSize.zero
    
    let scrollViewSize = scrollView.bounds.size
    let widthScale = scrollViewSize.width / imageSize.width
    let heightScale = scrollViewSize.height / imageSize.height
    let minScale = min(widthScale, heightScale)
    
    scrollView.minimumZoomScale = minScale
    scrollView.maximumZoomScale = 3.0
    scrollView.zoomScale = minScale
    
    imageView.frame = CGRect(x: 0, y: 0, width: imageSize.width * scrollView.zoomScale, height: imageSize.height * scrollView.zoomScale)
    scrollView.contentSize = imageView.frame.size
}
```

위 코드에서 `loadImage` 함수는 이미지를 로딩하여 이미지 뷰어에 추가하는 역할을 합니다. `updateImageViewConstraints` 함수는 이미지 뷰어의 사이즈와 줌 스케일을 업데이트합니다.

## 스와이프 제스처 추가하기

다음과 이전 이미지로 이동하기 위해 스와이프 제스처를 추가합니다.

```swift
extension ViewController {
    func setupSwipeGesture() {
        let swipeLeft = UISwipeGestureRecognizer(target: self, action: #selector(showNextImage))
        swipeLeft.direction = .left
        imageView.addGestureRecognizer(swipeLeft)
        
        let swipeRight = UISwipeGestureRecognizer(target: self, action: #selector(showPreviousImage))
        swipeRight.direction = .right
        imageView.addGestureRecognizer(swipeRight)
    }
    
    @objc func showNextImage() {
        // 다음 이미지 보여주기
    }
    
    @objc func showPreviousImage() {
        // 이전 이미지 보여주기
    }
}
```

위 코드에서 `showNextImage` 함수와 `showPreviousImage` 함수는 각각 다음 이미지와 이전 이미지를 보여주는 로직을 구현해야합니다.

## 결론

이렇게 Swift를 사용하여 SimpleImageViewer에 애니메이션 효과를 적용하는 방법을 알아보았습니다. `UIScrollView`를 사용하여 이미지를 확대 및 축소하고, 스와이프 제스처를 추가하여 다음 또는 이전 이미지로 이동할 수 있도록 구현할 수 있습니다.

더 자세한 내용은 [Apple 공식 문서][apple-docs]를 참고하시기 바랍니다.

[apple-docs]: https://developer.apple.com/documentation/uikit/uiscrollview