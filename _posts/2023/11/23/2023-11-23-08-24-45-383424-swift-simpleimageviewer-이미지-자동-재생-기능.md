---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 자동 재생 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어는 사용자가 이미지를 간편하게 볼 수 있는 기능을 제공합니다. 이번에는 Swift로 개발된 SimpleImageViewer에 이미지 자동 재생 기능을 추가하는 방법을 알아보겠습니다.

## 필요한 라이브러리 설치

SimpleImageViewer가 이미 설치되어 있다면 건너뛰어도 됩니다. 만약 설치되어 있지 않다면, 다음 명령어를 사용하여 설치합니다.

```swift
pod 'SimpleImageViewer'
```

## 이미지 자동 재생 기능 추가하기

1. SimpleImageViewer를 import 합니다.

```swift
import SimpleImageViewer
```

2. UIImageView에 탭 제스처를 설정하여 이미지가 선택되었을 때 호출되는 함수를 작성합니다.

```swift
let imageViewer = ImageViewerController()
    
@objc func imageTapped(sender: UITapGestureRecognizer) {
    guard let imageView = sender.view as? UIImageView else { return }
    
    if let image = imageView.image {
        imageViewer.setImageInputs([ImageSource(image: image)])
    }
    
    present(imageViewer, animated: true, completion: nil)
}
```

3. 이미지 뷰에 탭 제스처를 추가하고, 해당 제스처가 발생하면 `imageTapped` 함수를 호출합니다.

```swift
let imageView = UIImageView()

override func viewDidLoad() {
    super.viewDidLoad()
    
    // 이미지 뷰에 탭 제스처 추가
    let tapGesture = UITapGestureRecognizer(target: self, action: #selector(imageTapped))
    imageView.addGestureRecognizer(tapGesture)
    imageView.isUserInteractionEnabled = true
}
```

## 이미지 자동 재생 기능 설정하기

1. `imageViewer.setImageInputs`를 사용하여 이미지를 설정합니다.

```swift
let image1 = UIImage(named: "image1")
let image2 = UIImage(named: "image2")
let image3 = UIImage(named: "image3")

// 이미지 뷰어에 이미지 입력 설정
imageViewer.setImageInputs([
    ImageSource(image: image1!),
    ImageSource(image: image2!),
    ImageSource(image: image3!)
])
```

2. 이미지 자동 재생 간격을 설정합니다. (단위: 초)

```swift
imageViewer.slideshowInterval = 3.0
```

3. 자동 재생 시작을 설정합니다.

```swift
imageViewer.autoPlay = true
```

## 실행 결과

위와 같이 코드를 작성하면, 이미지 뷰어가 이미지를 자동으로 재생합니다. 사용자가 이미지를 탭하면 크게 볼 수 있고, 설정된 간격에 따라 이미지가 자동으로 변경됩니다.

## 결론

Swift SimpleImageViewer에 이미지 자동 재생 기능을 추가하는 방법을 알아보았습니다. 이미지 뷰어를 사용하여 사용자가 편리하게 이미지를 감상할 수 있도록 UI를 개선할 수 있습니다. 참고하여 원하는 기능을 추가해보세요.