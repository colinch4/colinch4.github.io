---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 그리기 샘플 코드"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift로 이미지 뷰어를 만드는 간단한 예제 코드를 소개하겠습니다. UIImageView를 사용하여 이미지를 그리는 방법을 알아보겠습니다.

## UIImageView 생성하기

먼저, UIImageView를 생성하여 이미지를 그릴 준비를 합니다. 아래의 코드를 참고해주세요.

```swift
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
imageView.contentMode = .scaleAspectFill
view.addSubview(imageView)
```

위 코드에서는 200x200 크기의 UIImageView를 생성하고, 이미지를 채우기 위해 `contentMode`를 `.scaleAspectFill`로 설정합니다. 마지막으로 `addSubview`를 사용하여 imageView를 화면에 추가합니다.

## 이미지 설정하기

이미지를 설정하기 위해서는 `UIImage` 객체를 생성하여 UIImageView에 할당해야 합니다. 아래의 코드를 참고해주세요.

```swift
let image = UIImage(named: "example_image")
imageView.image = image
```

위 코드에서는 프로젝트에 있는 "example_image"라는 이름의 이미지를 가져와 `UIImage` 객체로 생성합니다. 그리고 생성한 이미지를 `imageView.image`에 할당하여 이미지를 설정합니다. 

## 주의사항

위 예제 코드에서는 이미지의 크기가 `200x200`로 고정되어 있으며, 프로젝트 내에 있는 "example_image" 이미지를 사용하고 있습니다. 

만약에 코드를 실행시켜보려면, 미리 프로젝트에 "example_image" 이미지를 추가해주세요.

이제 위 예제 코드를 참고하여 자신만의 이미지 뷰어를 만들어보세요!

## 참고 자료

- [UIImageView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimageview)
- [UIImage - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimage)