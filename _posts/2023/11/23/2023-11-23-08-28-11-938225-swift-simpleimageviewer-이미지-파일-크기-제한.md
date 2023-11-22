---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 파일 크기 제한"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 파일을 로딩하고 표시하는 Swift SimpleImageViewer의 기능 중 하나는 이미지 파일 크기를 제한하는 것입니다. 이 기능을 사용하면 앱에서 특정 크기보다 큰 이미지를 표시하지 않을 수 있습니다. 이 글에서는 Swift SimpleImageViewer를 사용하여 이미지 파일 크기를 제한하는 방법을 알아보겠습니다.

## 1. 이미지 파일 크기 제한 설정하기

SimpleImageViewer에서 이미지 파일 크기를 제한하기 위해서는 `maxImageSize`라는 속성을 사용해야 합니다. 이 속성은 바이트 단위로 이미지 파일의 최대 허용 크기를 나타냅니다.

```swift
// 이미지 파일 크기 제한 설정 예시
let viewer = SimpleImageViewer()
viewer.maxImageSize = 5 * 1024 * 1024 // 5MB
```

위의 예시에서 `maxImageSize`를 5MB로 설정하였습니다. 이렇게 설정하면 5MB보다 큰 이미지 파일은 로딩되지 않고 표시되지 않습니다.

## 2. 이미지 파일 크기 확인하기

SimpleImageViewer는 이미지 파일을 로딩하기 전에 파일 크기를 확인합니다. 파일의 크기가 `maxImageSize`보다 큰 경우 이미지 로딩을 취소합니다. 따라서 이미지 파일을 불러올 때마다 크기를 확인하는 것은 성능상 비효율적일 수 있습니다.

```swift
// 이미지 파일 크기 확인 예시
let fileURL = URL(fileURLWithPath: "image.jpg")
let fileSize = try? fileURL.resourceValues(forKeys: [.fileSizeKey]).fileSize
if let fileSize = fileSize, fileSize > viewer.maxImageSize {
    print("이미지 파일 크기가 제한을 초과하여 로딩할 수 없습니다.")
} else {
    // 이미지 파일 로딩 및 표시
    viewer.loadImage(fileURL)
}
```

위의 예시에서는 `fileURL`을 통해 이미지 파일의 크기(`fileSize`)를 확인한 후, `maxImageSize`와 비교하여 제한을 초과하는 경우에는 이미지 파일 로딩을 취소하고 그렇지 않은 경우에는 이미지를 로딩하여 표시합니다.

## 3. 추가적인 고려 사항

- `maxImageSize`를 설정할 때 주의할 점은 사용하는 기기의 메모리 한계를 고려해야 합니다. 큰 이미지를 로딩하면 메모리 부족 문제가 발생할 수 있으므로 적절한 크기로 제한해야 합니다.
- 사용자 경험을 개선하기 위해 이미지 파일 크기 제한에 대한 안내나 경고 메시지를 추가할 수 있습니다.

## 참고 자료

- [Swift SimpleImageViewer GitHub Repository](https://github.com/simple-swift/SimpleImageViewer)