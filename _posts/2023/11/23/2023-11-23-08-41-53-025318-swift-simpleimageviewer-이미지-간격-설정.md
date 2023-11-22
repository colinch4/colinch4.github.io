---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 간격 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift SimpleImageViewer는 iOS 앱에서 이미지를 간단하게 표시할 수 있는 사용하기 쉬운 라이브러리입니다. 이번에는 Swift SimpleImageViewer에서 이미지 간격을 설정하는 방법에 대해 알아보겠습니다.

## 1. SimpleImageViewer 설치하기

먼저, SimpleImageViewer를 사용하기 위해 Cocoapods를 통해 라이브러리를 설치해야 합니다. Podfile에 다음과 같은 내용을 추가합니다.

```swift
pod 'SimpleImageViewer'
```

설치를 위해 터미널을 열고 다음 명령어를 실행합니다.

```shell
pod install
```

## 2. 이미지 간격 설정하기

SimpleImageViewer에서 이미지 간격을 설정하려면 ImageViewerController 인스턴스를 생성한 후 `spacing` 속성을 설정하면 됩니다. 이미지 간격은 포인트로 지정할 수 있습니다.

```swift
import SimpleImageViewer

let imageViewer = ImageViewerController(images: [...])
imageViewer.spacing = 10.0
```

위의 예시에서 `imageViewer`는 ImageViewerController의 인스턴스이며, 이미지 간격을 10포인트로 설정하고 있습니다. `images`는 표시할 이미지 배열입니다. 이 배열에 필요한 이미지 URL 또는 UIImage 객체를 전달할 수 있습니다.

## 3. 이미지 간격 설정 적용하기

ImageViewerController 인스턴스를 생성하고 이미지 간격을 설정한 후, 이를 표시하기 위해 현재 UIViewController에 추가해야 합니다.

```swift
present(imageViewer, animated: true, completion: nil)
```

위의 코드는 이미지 뷰어를 현재 UIViewController에서 모달 형태로 표시합니다.

## 결론

Swift SimpleImageViewer를 사용하면 iOS 앱에서 이미지를 간편하게 표시할 수 있습니다. 이번 글에서는 이미지 간격을 설정하는 방법에 대해 알아보았습니다. SimpleImageViewer의 다양한 기능을 활용하여 앱에 깔끔하고 사용자 친화적인 이미지 뷰어를 구성할 수 있습니다.

## 참고 자료
- [SimpleImageViewer GitHub Repository](https://github.com/jessedc/SimpleImageViewer)