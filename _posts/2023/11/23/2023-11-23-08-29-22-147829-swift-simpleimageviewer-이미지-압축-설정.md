---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 압축 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift SimpleImageViewer은 간단하고 편리한 이미지 뷰어입니다. 하지만 대용량의 이미지를 로드하는 경우 메모리 부족 문제가 발생할 수 있습니다. 이를 해결하기 위해서 이미지 압축 설정을 사용할 수 있습니다. 

## 이미지 압축 설정 방법

1. 이미지 뷰어 사용을 위한 `SimpleImageViewer` 인스턴스를 생성합니다.
```swift
let imageViewer = SimpleImageViewer()
```
2. `imageViewer`의 `compressionQuality` 속성을 이용하여 이미지 압축 품질을 설정할 수 있습니다.
```swift
imageViewer.compressionQuality = 0.5 // 압축 품질을 50%로 설정
```
압축 품질은 0에서 1 사이의 값을 가지며, 1에 가까울수록 이미지 품질이 좋아집니다. 따라서, 값이 작을수록 압축이 강하게 이루어집니다.

3. 이미지를 로드할 때 `imageViewer`의 `loadImage` 메서드를 이용하여 이미지를 압축 적용하여 로드할 수 있습니다.
```swift
imageViewer.loadImage(imageURL, completion: { image in
    // 압축 적용된 이미지를 사용하는 코드
})
```
위의 코드에서 `imageURL`은 로드할 이미지의 URL이고, `completion` 클로저는 이미지 로드가 완료된 후 실행되는 코드입니다.

## 참고 자료
- [SimpleImageViewer GitHub 레포지토리](https://github.com/simpleviewinc/SimpleImageViewer)