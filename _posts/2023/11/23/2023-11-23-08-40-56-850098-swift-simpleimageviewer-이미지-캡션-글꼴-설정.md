---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 캡션 글꼴 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift SimpleImageViewer는 이미지를 캡션과 함께 표시하는 간단한 이미지 뷰어 라이브러리입니다. 이 라이브러리를 사용하여 이미지 캡션의 글꼴을 설정하는 방법에 대해 알아보겠습니다.

## 글꼴 설정하기

SimpleImageViewer에서 이미지 캡션에 사용되는 글꼴은 `captionFont` 속성을 통해 설정할 수 있습니다. 이 속성은 `UIFont` 객체를 받으며, 원하는 글꼴과 글꼴 크기를 지정할 수 있습니다.

```swift
import SimpleImageViewer

let viewer = ImageViewer()

// 글꼴 설정
let font = UIFont(name: "Helvetica", size: 16)!
viewer.captionFont = font
```

위의 예제에서는 "Helvetica" 글꼴을 사용하고 글꼴 크기는 16으로 설정하였습니다.

## 참고 자료

- [SimpleImageViewer GitHub 저장소](https://github.com/Krisiacik/SimpleImageViewer)

이제 SimpleImageViewer를 사용하여 이미지 캡션의 글꼴을 설정하는 방법을 알게 되었습니다. 원하는 글꼴과 글꼴 크기를 설정하여 캡션을 보다 시각적으로 개성있게 표현해보세요!