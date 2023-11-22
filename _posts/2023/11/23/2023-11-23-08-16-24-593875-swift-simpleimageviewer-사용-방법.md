---
layout: post
title: "[swift] Swift SimpleImageViewer 사용 방법"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift로 작성된 SimpleImageViewer 라이브러리의 사용 방법을 알아보겠습니다.

### SimpleImageViewer란?

SimpleImageViewer는 이미지 뷰어를 간편하게 구현할 수 있도록 도와주는 Swift 라이브러리입니다. 이 라이브러리를 사용하면 이미지를 로드하고 확대/축소, 드래그 기능을 간단하게 구현할 수 있습니다.

### 설치 방법

SimpleImageViewer는 CocoaPods를 통해 설치할 수 있습니다. 프로젝트의 `Podfile`에 다음 코드를 추가해주세요.

```ruby
pod 'SimpleImageViewer', '~> 1.0.0'
```
저장 후 터미널에서 `pod install` 명령어를 실행합니다. CocoaPods를 사용하여 SimpleImageViewer를 설치할 수 있습니다.

### 사용 방법

1. 먼저, 이미지를 보여줄 UIImageView 인스턴스를 생성합니다.

```swift
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
imageView.image = UIImage(named: "exampleImage")
```

2. SimpleImageViewer 인스턴스를 생성하고, 이미지 뷰어를 추가합니다.

```swift
let imageViewer = ImageViewer()
imageViewer.show(imageView: imageView)
```

이제 이미지 뷰어가 생성되고, 해당 이미지가 표시됩니다. 사용자는 이미지를 확대/축소하거나 드래그하여 이동할 수 있습니다.

### 사용자 지정 옵션

SimpleImageViewer는 사용자가 다양한 옵션을 지정할 수 있도록 제공됩니다. 몇 가지 중요한 옵션은 다음과 같습니다.

- `backgroundColor`: 뷰어의 배경색을 설정합니다.
- `shouldDismissOnTap`: 사용자가 이미지 뷰를 탭할 때 뷰어가 닫히도록 설정합니다.
- `dismissOnSwipe`: 사용자가 이미지를 스와이프하여 뷰어를 닫히도록 설정합니다.

옵션을 사용하려면 SimpleImageViewer 인스턴스 생성 시 `options` 매개변수로 옵션을 설정하면 됩니다.

```swift
let options = ImageViewerOptions(backgroundColor: .black, shouldDismissOnTap: true)
let imageViewer = ImageViewer(options: options)
```

### 참고 자료

- [SimpleImageViewer GitHub 레포지토리](https://github.com/Krisiacik/SimpleImageViewer)

이제 SimpleImageViewer 라이브러리를 사용하여 간단하고 편리한 이미지 뷰어를 만들어보세요!