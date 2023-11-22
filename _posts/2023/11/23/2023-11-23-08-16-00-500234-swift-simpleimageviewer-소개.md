---
layout: post
title: "[swift] Swift SimpleImageViewer 소개"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---
[SimpleImageViewer](https://github.com/KrisUng/SimpleImageViewer)는 Swift로 작성된 간단한 이미지 뷰어 라이브러리입니다. 이 라이브러리를 사용하면 애플리케이션에서 이미지를 간편하게 보여줄 수 있습니다.

## 기능
SimpleImageViewer는 다음과 같은 기능을 제공합니다:
- 이미지 URL이나 파일 경로를 통해 이미지를 로드할 수 있음
- 이미지 확대/축소, 이동 가능
- 이미지 스와이프로 다음/이전 이미지로 이동 가능

## 사용법
SimpleImageViewer를 사용하려면 먼저 이 라이브러리를 프로젝트에 추가해야 합니다. Cocoapods를 사용한다면 Podfile에 다음과 같이 추가해주세요:
```ruby
pod 'SimpleImageViewer', :git => 'https://github.com/KrisUng/SimpleImageViewer.git'
```

다음은 간단한 예제 코드입니다:

```swift
import SimpleImageViewer

// 이미지 뷰어를 생성하고 초기화
let imageViewer = ImageViewer()

// 이미지 로드
let imageURL = URL(string: "https://example.com/image.jpg")
imageViewer.loadImage(imageURL)

// 이미지 뷰어를 현재 표시되는 뷰에 추가
imageViewer.show(from: self)
```

위 예제 코드에서는 SimpleImageViewer를 초기화하고 이미지를 로드한 다음, 현재 화면에 이미지를 표시합니다. 이 외에도 이미지 확대/축소, 스와이프로 다음/이전 이미지로 이동하는 등 다양한 기능을 사용할 수 있습니다.

## 참고 자료
- [SimpleImageViewer GitHub 레포지토리](https://github.com/KrisUng/SimpleImageViewer)