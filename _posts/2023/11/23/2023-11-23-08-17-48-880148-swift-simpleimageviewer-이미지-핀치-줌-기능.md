---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 핀치 줌 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발하다보면 이미지를 핀치 줌해서 확대/축소하는 기능을 구현해야 할 때가 있습니다. 이번 글에서는 Swift를 사용하여 간단한 이미지 뷰어를 만들고, 이미지 핀치 줌 기능도 함께 구현해보겠습니다.

## 요구사항

이미지 뷰어의 핵심 요구사항은 다음과 같습니다:
1. 이미지를 보여줄 수 있는 이미지 뷰어가 있어야 합니다.
2. 사용자는 핀치 제스처를 통해 이미지를 확대 또는 축소할 수 있어야 합니다.
3. 이미지는 최소 크기와 최대 크기를 설정해야 합니다.
4. 이미지는 제스처에 따라서 화면에 맞춰 회전되어야 합니다.

## 구현 방법

간단한 이미지 뷰어를 만들기 위해 다음과 같은 단계를 따를 수 있습니다:

1. UIViewController를 상속한 CustomViewController를 만듭니다.
2. CustomViewController에 UIImageView를 추가합니다.
3. UIImageView에 UIGestureRecognizerDelegate를 채택하고 제스처 관련 메소드를 구현합니다.
4. 제스처 메소드에서 핀치 제스처를 인식하여 이미지를 확대/축소합니다.
5. 이미지 뷰어에서 이미지를 회전하기 위해 제스처 메소드에서 회전 각도를 계산합니다.

```swift
import UIKit

class CustomViewController: UIViewController, UIGestureRecognizerDelegate {

    var imageView: UIImageView!
    let minZoomScale: CGFloat = 0.5
    let maxZoomScale: CGFloat = 2.0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰 생성
        imageView = UIImageView(frame: view.bounds)
        imageView.contentMode = .scaleAspectFit
        imageView.image = UIImage(named: "sample_image")
        
        // 제스처 인식기 생성
        let pinchGesture = UIPinchGestureRecognizer(target: self, action: #selector(handlePinch(_:)))
        pinchGesture.delegate = self
        imageView.addGestureRecognizer(pinchGesture)
        
        // 이미지 뷰어에 이미지 뷰 추가
        view.addSubview(imageView)
    }
    
    @objc func handlePinch(_ gestureRecognizer: UIPinchGestureRecognizer) {
        guard gestureRecognizer.view != nil else { return }
        
        // 이미지 뷰의 크기 변경
        let scale = gestureRecognizer.scale
        var newScale = imageView.frame.size.width * scale
        
        // 최소/최대 크기 제한
        newScale = max(min(newScale, view.frame.size.width * maxZoomScale), view.frame.size.width * minZoomScale)
        
        // 이미지 뷰의 크기 반영
        imageView.transform = CGAffineTransform(scaleX: newScale/imageView.frame.size.width, y: newScale/imageView.frame.size.height)
        
        // 이미지 뷰가 화면에 가운데 위치하도록 이동
        imageView.center = view.center
    }
    
    func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool {
        return true
    }
}
```

## 사용 예시

이미지 뷰어를 사용하는 예시 코드입니다:
```swift
let customViewController = CustomViewController()
present(customViewController, animated: true, completion: nil)
```

## 결론

Swift를 사용하여 간단한 이미지 뷰어를 만들고 이미지 핀치 줌 기능을 구현하는 방법에 대해 알아보았습니다. 핀치 제스처를 사용하여 이미지를 확대/축소함으로써 사용자에게 더 나은 이미지 뷰어를 제공할 수 있습니다.