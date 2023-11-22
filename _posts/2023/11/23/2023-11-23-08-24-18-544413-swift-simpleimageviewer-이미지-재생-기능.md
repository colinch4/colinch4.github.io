---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 재생 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift SimpleImageViewer는 iOS 앱에서 이미지를 간편하게 보여주는 뷰어 기능을 제공합니다. 이 뷰어에 이미지 재생 기능을 추가해 보겠습니다.

## 프로젝트 설정

1. SimpleImageViewer 라이브러리를 설치합니다. Cocoapods를 사용한다면 Podfile에 다음을 추가합니다.

```swift
pod 'SimpleImageViewer'
```

2. 이후 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 이미지 재생 기능 추가하기

1. SimpleImageViewer를 import 합니다.

```swift
import SimpleImageViewer
```

2. 이미지 뷰어를 생성하고 이미지를 보여주기 위한 버튼을 추가합니다.

```swift
@IBOutlet weak var imageView: UIImageView!

@IBAction func showImageViewer(_ sender: UIButton) {
    let imageViewer = ImageViewerController(images: [imageView.image!])
    present(imageViewer, animated: true)
}
```

3. 이미지 뷰어를 초기화하고 버튼을 연결합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    let tapGesture = UITapGestureRecognizer(target: self, action: #selector(showImageViewer(_:)))
    imageView.isUserInteractionEnabled = true
    imageView.addGestureRecognizer(tapGesture)
}
```

4. 앱을 실행하고 이미지를 터치하면 이미지 뷰어가 열리고 이미지를 스와이프하여 재생할 수 있습니다.

## 결론

이제 SimpleImageViewer를 사용하여 iOS 앱에서 이미지를 재생할 수 있는 기능을 추가해보았습니다. 이를 응용하여 복잡한 이미지 뷰어를 구현할 수도 있습니다. 더 자세한 내용은 [SimpleImageViewer GitHub 페이지](https://github.com/asfedorov/ImageViewerController)를 참고하시기 바랍니다.