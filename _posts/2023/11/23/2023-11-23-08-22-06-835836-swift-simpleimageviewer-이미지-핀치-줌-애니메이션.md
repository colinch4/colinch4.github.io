---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 핀치 줌 애니메이션"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

![Swift](https://www.gstatic.com/devrel-devsite/v0717acb297ad06549ccdb10ce16719e3db01a6b841f9e140273b573644d07f8e/developers/images/touchicon-180.png)

이번 튜토리얼에서는 Swift를 사용하여 간단한 이미지 뷰어를 만드는 방법을 알아보겠습니다. 이 이미지 뷰어는 사용자가 이미지를 핀치해서 줌인하고 줌아웃할 수 있는 애니메이션 효과가 있습니다.

## 준비하기

### 1. 프로젝트 생성하기

Xcode를 열고 새로운 Swift 프로젝트를 생성합니다.

### 2. 이미지 추가하기

프로젝트 내에 사용할 이미지를 추가합니다. 이미지는 `Assets.xcassets` 폴더 내에 추가하거나 `Assets.xcassets` 파일이 없다면 프로젝트 폴더 내에 직접 이미지 파일을 추가할 수도 있습니다.

## 코드 작성하기

### 1. 이미지 뷰어 화면 구성하기

Storyboard에서 `ViewController`를 선택하고 `UIImageView`를 추가합니다. 이 `UIImageView`는 이미지를 보여주는 역할을 수행할 것입니다. Auto Layout을 사용하여 `UIImageView`를 적절한 위치와 크기로 조정합니다.

### 2. 제스처 인식기 추가하기

`ViewController` 파일을 열고 `viewDidLoad()` 메서드 내에 다음 코드를 추가하여 이미지 뷰어에 제스처 인식기를 추가합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    let pinchGestureRecognizer = UIPinchGestureRecognizer(target: self, action: #selector(handlePinch(_:)))
    imageView.addGestureRecognizer(pinchGestureRecognizer)
    imageView.isUserInteractionEnabled = true
}
```

### 3. 핀치 줌 애니메이션 구현하기

`ViewController` 파일에 다음 코드로 핀치 줌 애니메이션을 처리하는 `handlePinch()` 메서드를 작성합니다.

```swift
@objc func handlePinch(_ gestureRecognizer: UIPinchGestureRecognizer) {
    guard let view = gestureRecognizer.view else { return }
    
    if gestureRecognizer.state == .began || gestureRecognizer.state == .changed {
        view.transform = view.transform.scaledBy(x: gestureRecognizer.scale, y: gestureRecognizer.scale)
        gestureRecognizer.scale = 1.0
    } else if gestureRecognizer.state == .ended {
        UIView.animate(withDuration: 0.3, delay: 0, options: .curveEaseInOut, animations: {
            view.transform = CGAffineTransform.identity
        }, completion: nil)
    }
}
```

## 실행하기

이제 앱을 빌드해서 실행해보세요. 이미지 뷰어에 핀치를 사용하여 줌인하고 줌아웃하는 애니메이션이 작동하는 것을 확인할 수 있습니다.

## 마무리하며

위의 튜토리얼에서는 Swift를 사용하여 간단한 이미지 뷰어를 만드는 방법을 알아보았습니다. 핀치 제스처를 사용하여 이미지를 줌인하고 줌아웃하는 애니메이션 효과를 추가했습니다. 이러한 기술을 응용하여 더 복잡한 이미지 뷰어를 구축할 수도 있습니다.

더 자세한 내용은 [SwiftUI 공식 문서](https://developer.apple.com/documentation/swiftui)를 참조하시기 바랍니다.