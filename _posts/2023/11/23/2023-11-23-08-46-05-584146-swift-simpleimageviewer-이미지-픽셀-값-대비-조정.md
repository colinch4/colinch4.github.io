---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 대비 조정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 픽셀 값 대비 조정은 이미지를 더 선명하고 더 동적으로 보이게 만드는 데 도움이 됩니다. 이렇게 조정된 이미지를 보는 방법 중 하나는 간단한 이미지 뷰어를 사용하는 것입니다. 이 블로그 게시물에서는 Swift를 사용하여 간단한 이미지 뷰어를 만들고, 이미지 픽셀 값 대비 조정을 적용하는 방법을 알아보겠습니다.

## 참고 자료
- [AppCoda - How to Build a Simple Image Viewer App in Swift](https://www.appcoda.com/simple-image-viewer-app-swift/)

## 라이브러리 가져오기

먼저, 이미지 픽셀 값 대비 조정을 쉽게 구현할 수 있는 `CoreImage` 라이브러리를 가져와야 합니다. 이를 위해 `import CoreImage` 문을 추가합니다.

```swift
import CoreImage
```

## 이미지 뷰어 만들기

간단한 이미지 뷰어를 만들기 위해 `UIImageView`와 `UIPanGestureRecognizer`를 사용합니다. `UIImageView`는 이미지를 표시하기 위한 뷰이고, `UIPanGestureRecognizer`는 이미지를 드래그하여 화면을 이동하는 기능을 추가하기 위해 사용됩니다.

```swift
class SimpleImageViewer: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    private var originalPosition: CGPoint!
    private var scale: CGFloat = 1
    private var lastScale: CGFloat = 1

    override func viewDidLoad() {
        super.viewDidLoad()

        let panGestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePan))
        imageView.addGestureRecognizer(panGestureRecognizer)

        let pinchGestureRecognizer = UIPinchGestureRecognizer(target: self, action: #selector(handlePinch))
        imageView.addGestureRecognizer(pinchGestureRecognizer)

        let doubleTapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(handleDoubleTap))
        doubleTapGestureRecognizer.numberOfTapsRequired = 2
        imageView.addGestureRecognizer(doubleTapGestureRecognizer)
    }

    @objc func handlePan(_ gestureRecognizer: UIPanGestureRecognizer) {
        let translation = gestureRecognizer.translation(in: imageView.superview)
        imageView.transform = imageView.transform.translatedBy(x: translation.x, y: translation.y)
        gestureRecognizer.setTranslation(CGPoint.zero, in: imageView.superview)
    }

    @objc func handlePinch(_ gestureRecognizer: UIPinchGestureRecognizer) {
        guard gestureRecognizer.view != nil else { return }

        if gestureRecognizer.state == .began || gestureRecognizer.state == .changed {
            let newScale = gestureRecognizer.scale
            guard scale * newScale >= 1 else { return }
            lastScale = newScale
            imageView.transform = imageView.transform.scaledBy(x: newScale, y: newScale)
            gestureRecognizer.scale = 1
        }
    }

    @objc func handleDoubleTap(_ gestureRecognizer: UITapGestureRecognizer) {
        if scale == 1 {
            originalPosition = imageView.center
            UIView.animate(withDuration: 0.5, animations: {
                self.imageView.transform = CGAffineTransform(scaleX: 2, y: 2)
                self.imageView.center = self.view.center
            })
            scale = 2
        } else {
            UIView.animate(withDuration: 0.5, animations: {
                self.imageView.transform = .identity
                self.imageView.center = self.originalPosition
            })
            scale = 1
        }
    }
}
```

## 이미지 픽셀 값 대비 조정

이미지 픽셀 값 대비 조정을 위해 `CoreImage`의 `CIColorControls` 필터를 사용할 수 있습니다. 이 필터를 사용하여 이미지의 밝기, 대비, 채도 등을 조정할 수 있습니다.

```swift
extension SimpleImageViewer {

    func applyContrastFilter(to image: UIImage, contrast: Float) -> UIImage? {
        let context = CIContext(options: nil)
        let inputImage = CIImage(image: image)
        
        guard let filter = CIFilter(name: "CIColorControls") else { return nil }
        filter.setValue(inputImage, forKey: kCIInputImageKey)
        filter.setValue(contrast, forKey: kCIInputContrastKey)
        
        guard let outputImage = filter.outputImage else { return nil }
        guard let cgImage = context.createCGImage(outputImage, from: outputImage.extent) else { return nil }
        
        return UIImage(cgImage: cgImage)
    }
}
```

`applyContrastFilter` 메서드는 입력 이미지와 대비 값을 받아 해당 이미지에 대비 필터를 적용한 다음, 결과 이미지를 반환합니다.

## 이미지 뷰어에 이미지 로드 및 대비 조정 적용하기

이미지 뷰어의 `viewDidLoad` 메서드에서 이미지 파일을 로드하고, 대비 조정을 적용합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // 이미지 로드
    guard let image = UIImage(named: "example.jpg") else { return }
    imageView.image = image

    // 대비 조정 적용
    guard let contrastAdjusted = applyContrastFilter(to: image, contrast: 2.0) else { return }
    imageView.image = contrastAdjusted
}
```

`example.jpg`는 프로젝트 내에 있는 이미지 파일의 이름으로 대체해야 합니다.

## 결론

Swift를 사용하여 이미지 픽셀 값 대비 조정을 적용하는 간단한 이미지 뷰어를 만들었습니다. CoreImage 라이브러리를 사용하여 이미지에 대비 필터를 적용하고, 이미지를 드래그하거나 축소 확대할 수 있도록 기능을 추가했습니다. 이를 통해 이미지를 더 선명하게 보이도록 조정할 수 있습니다.

위에서 제시한 예시 코드는 기본적인 템플릿으로 사용할 수 있습니다. 필요에 따라 추가적인 기능이나 UI 요소를 구현하여 더 다양한 이미지 처리 기능을 제공할 수도 있습니다.