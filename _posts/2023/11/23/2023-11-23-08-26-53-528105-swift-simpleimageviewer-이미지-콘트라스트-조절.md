---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 콘트라스트 조절"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 콘트라스트(Contrast)는 이미지의 밝기와 명암 대비를 조절하여 더 선명하고 생동감 있는 이미지를 만들 수 있는 기능입니다. Swift와 SimpleImageViewer를 사용하여 이미지 콘트라스트를 조절하는 방법을 알아보겠습니다.

## 1. SimpleImageViewer 라이브러리 설치

SimpleImageViewer는 Swift로 개발된 간단하고 유연한 이미지뷰어 라이브러리입니다. 이 라이브러리를 사용하면 이미지를 쉽게 표시하고 조작할 수 있습니다. SimpleImageViewer를 설치하기 위해 CocoaPods를 사용합니다. `Podfile`에 다음과 같이 추가합니다.

```swift
pod 'SimpleImageViewer'
```

그리고 터미널에서 다음 명령을 실행하여 라이브러리를 설치합니다.

```bash
pod install
```

## 2. 이미지뷰어 생성

```swift
import SimpleImageViewer

// 이미지를 표시할 이미지뷰 생성
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
imageView.image = UIImage(named: "example")

// 이미지뷰어 생성
let viewer = ImageViewerController(imageViewerConfiguration: ImageViewerConfiguration { config in
    config.imageView = imageView
})

// 뷰어를 보여줄 뷰컨트롤러를 설정
present(viewer, animated: true, completion: nil)
```

위 코드에서 `UIImageView`를 사용하여 이미지뷰를 생성하고, `UIImage(named:)`을 사용하여 이미지를 설정합니다. 그리고 `ImageViewerController`를 생성하고 이미지뷰어에 이미지뷰를 설정합니다. 마지막으로 `present(_:animated:completion:)`을 사용하여 이미지뷰어를 보여줍니다.

## 3. 이미지 콘트라스트 조절

이미지 콘트라스트를 조절하기 위해서는 이미지뷰어에 접근해야 합니다. `ImageViewerController`에는 `containerView` 속성이 있으므로, 이를 사용하여 이미지뷰어에 접근할 수 있습니다.

```swift
let imageViewer = viewer.containerView
```

`imageViewer`는 `ImageViewerContainer` 타입이므로, 이를 `ImageViewerContainer`로 타입 캐스팅하여 `maximumContrast`와 `minimumContrast` 속성을 조절하여 이미지의 콘트라스트를 변경할 수 있습니다.

```swift
if let container = imageViewer as? ImageViewerContainer {
    // 콘트라스트 조절
    container.maximumContrast = 2.0 // 최대 명암 대비 값
    container.minimumContrast = 0.5 // 최소 명암 대비 값
}
```

위 코드에서 `maximumContrast`는 이미지의 최대 명암 대비 값을, `minimumContrast`는 이미지의 최소 명암 대비 값을 의미합니다. 콘트라스트 값을 변경하여 이미지의 선명도와 명암 대비를 조절할 수 있습니다.

## 참고 자료

- SimpleImageViewer 라이브러리 GitHub 저장소: [https://github.com/Krisiacik/SimpleImageViewer](https://github.com/Krisiacik/SimpleImageViewer)