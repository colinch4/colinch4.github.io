---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 화질 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift의 SimpleImageViewer을 사용하여 이미지를 로드하고 표시하는 경우, 이미지의 화질을 설정할 수 있습니다. 이미지 화질을 설정하면, 메모리와 성능 측면에서 유리한 옵션을 선택할 수 있습니다.

## 1. 이미지 화질 옵션

SimpleImageViewer에는 이미지 화질을 조절하는 몇 가지 옵션이 있습니다.

### 1.1 lowQualityMode

```swift
viewer.lowQualityMode = true
```

`lowQualityMode`를 `true`로 설정하면, 이미지가 로드될 때 낮은 화질로 보여집니다. 이 옵션은 이미지 로드 속도를 향상시키는 데 도움이 됩니다. 

### 1.2 imageScalingMode

```swift
viewer.imageScalingMode = .aspectFit
```

`imageScalingMode`는 이미지의 크기와 화면 사이즈에 맞게 이미지를 스케일링합니다. 예를 들어 `.aspectFit`을 사용하면, 이미지가 화면에 맞게 비율을 유지하면서 축소됩니다. 

### 1.3 imageContentMode

```swift
viewer.imageContentMode = .scaleAspectFill
```

`imageContentMode`는 이미지의 크기와 뷰의 크기를 맞춰 이미지를 표시하는 방식을 정의합니다. `.scaleAspectFill`은 이미지를 뷰에 꽉 채우는데, 이미지 비율이 유지되지 않을 수 있습니다.

## 2. 이미지 화질 설정 예제

다음은 SimpleImageViewer를 사용하여 이미지를 화면에 표시하고 이미지 화질을 설정하는 예제 코드입니다.

```swift
import SimpleImageViewer

func showImage() {
    let imageViewer = ImageViewer()
    
    // 이미지 화질 설정
    imageViewer.lowQualityMode = true
    imageViewer.imageScalingMode = .aspectFit
    imageViewer.imageContentMode = .scaleAspectFill
    
    // 이미지 로드 및 표시
    let url = URL(string: "https://example.com/image.jpg")
    imageViewer.showImage(withURL: url)
}
```

위의 예제에서는 `lowQualityMode`를 활성화하여 이미지 로드 속도를 향상시켰습니다. `imageScalingMode`와 `imageContentMode`을 사용하여 이미지를 화면에 적절히 표시했습니다.

## 3. 참고 자료

- [SimpleImageViewer GitHub 페이지](https://github.com/kaushlendrar/simple-image-viewer)