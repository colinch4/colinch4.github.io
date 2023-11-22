---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 회전 각도 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift에서 `SimpleImageViewer`를 사용하여 이미지를 표시하고 회전 각도를 설정하는 방법을 알아보겠습니다.

## SimpleImageViewer란?

`SimpleImageViewer`는 Swift에서 제공하는 이미지 뷰어 라이브러리입니다. 터치 제스처를 이용하여 이미지를 확대, 축소하고 회전할 수 있습니다.

## 이미지 회전 각도 설정하기

이미지 회전 각도를 설정하려면 `SimpleImageViewer`의 `rotationAngle` 속성을 사용하면 됩니다. 

아래 예제에서는 이미지 뷰를 생성하고 회전 각도를 90도로 설정하는 방법을 보여줍니다.

```swift
import SimpleImageViewer

// 이미지 뷰어 생성
let imageViewer = SimpleImageViewer()

// 이미지 설정
let image = UIImage(named: "myImage")
imageViewer.setImage(image)

// 회전 각도 설정
imageViewer.rotationAngle = 90.0
```

위 예제에서는 `SimpleImageViewer`를 import한 후, 이미지 뷰를 생성하고 이미지를 설정합니다. 그리고 회전 각도를 90도로 설정합니다.

## 참고 자료

- [SimpleImageViewer GitHub 저장소](https://github.com/kiritmodi2702/SimpleImageViewer)

위 예제에서는 간단하게 `SimpleImageViewer`의 `rotationAngle` 속성을 사용하여 이미지의 회전 각도를 설정하는 방법을 설명했습니다. 따라서 원하는 회전 각도를 설정하여 이미지를 표시할 수 있습니다.