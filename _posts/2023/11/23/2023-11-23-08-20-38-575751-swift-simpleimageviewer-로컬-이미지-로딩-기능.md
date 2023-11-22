---
layout: post
title: "[swift] Swift SimpleImageViewer 로컬 이미지 로딩 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

## 소개
이번 글에서는 Swift SimpleImageViewer를 사용하여 로컬 이미지를 로딩하는 방법에 대해 알아보겠습니다. SimpleImageViewer는 편리한 이미지 뷰어 라이브러리로, 이미지를 간단하게 로딩하고 확대/축소할 수 있습니다.

## SimpleImageViewer 설치

SimpleImageViewer를 사용하기 위해선 CocoaPods를 통해 프로젝트에 라이브러리를 추가해야 합니다. Podfile에 다음을 추가한 뒤, `pod install` 명령어를 실행해주세요.

```swift
pod 'SimpleImageViewer', '~> 1.2'
```

## 로컬 이미지 로딩하기

1. `UIImageView` 객체를 생성합니다.

```swift
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
```

2. 로컬 이미지 파일을 `UIImage` 객체로 로딩합니다.

```swift
guard let image = UIImage(named: "image_name") else {
    return
}
```

3. `SimpleImageViewer` 라이브러리를 사용하여 이미지를 로딩하고 보여줍니다.

```swift
let imageViewController = ImageViewerController(image: image)
present(imageViewController, animated: true, completion: nil)
```

## 추가 기능 설정하기

SimpleImageViewer는 몇 가지 추가 기능을 제공합니다.

### 배경 터치시 닫기

뷰어 배경을 터치했을 때 뷰어를 닫고자 한다면, `ImageViewerController` 객체의 `dismissOnBackgroundTap` 속성을 `true`로 설정합니다.

```swift
imageViewController.dismissOnBackgroundTap = true
```

### 이미지 터치시 확대/축소

이미지를 터치했을 때 확대/축소하고 싶다면, `ImageViewerController` 객체의 `shouldZoomAfterTap` 속성을 `true`로 설정합니다.

```swift
imageViewController.shouldZoomAfterTap = true
```

## 결론

이제 SimpleImageViewer를 사용하여 로컬 이미지를 로딩하는 방법을 알아보았습니다. SimpleImageViewer를 사용하면 간단하게 이미지를 로딩하고 확대/축소할 수 있어 유용합니다. 추가 기능으로 배경 터치시 뷰어를 닫거나 이미지 터치시 확대/축소를 설정할 수 있으니, 필요에 따라 활용해보시기 바랍니다.

## 참고
- [SimpleImageViewer GitHub 레포지토리](https://github.com/Krisiacik/SimpleImageViewer)

```