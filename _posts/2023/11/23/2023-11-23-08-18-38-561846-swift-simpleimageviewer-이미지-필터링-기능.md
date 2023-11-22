---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 필터링 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 필터링은 이미지에 특정 효과를 적용하여 시각적인 표현을 변경하는 기능입니다. 이번 기사에서는 Swift 언어를 사용하여 SimpleImageViewer 앱에 이미지 필터링 기능을 추가하는 방법을 알아보겠습니다.

### 필요한 라이브러리 추가하기

이미지 필터링을 위해서는 Core Image 프레임워크를 사용해야 합니다. 프로젝트의 `Info.plist`에 다음 키를 추가하여 Core Image 사용 권한을 요청해야 합니다.

```xml
<key>NSCameraUsageDescription</key>
<string>Camera permission needed to apply filters.</string>
```

또한, Core Image를 사용하기 위해 `import CoreImage` 문을 추가해야 합니다.

### 이미지 필터링 기능 추가하기

SimpleImageViewer 앱에 이미지 필터링 기능을 추가하기 위해 다음 단계를 따라 진행합니다.

1. 이미지를 로드합니다.
```swift
guard let image = UIImage(named: "exampleImage.jpg") else { return }
```

2. `CIImage`로 변환합니다.
```swift
guard let ciImage = CIImage(image: image) else { return }
```

3. 필터를 선택하고 설정합니다.
```swift
let filter = CIFilter(name: "CISepiaTone")
filter?.setValue(ciImage, forKey: kCIInputImageKey)
filter?.setValue(0.8, forKey: kCIInputIntensityKey)
```

4. 필터를 적용합니다.
```swift
guard let filteredImage = filter?.outputImage else { return }
```

5. 출력 이미지를 `UIImage`로 변환합니다.
```swift
let context = CIContext(options: nil)
guard let finalImage = context.createCGImage(filteredImage, from: filteredImage.extent) else { return }
let filterAppliedImage = UIImage(cgImage: finalImage)
```

6. 필터가 적용된 이미지를 화면에 표시합니다.
```swift
imageView.image = filterAppliedImage
```

### 다양한 필터 적용하기

Core Image는 다양한 종류의 필터를 제공합니다. `CIFilter`의 `name` 속성을 변경하여 각 필터를 적용할 수 있습니다. 예를 들어, 세피아 톤 필터를 적용한 후에는 다음과 같은 코드로 모자이크 필터로 변경할 수 있습니다.

```swift
filter = CIFilter(name: "CIPixellate")
filter?.setValue(ciImage, forKey: kCIInputImageKey)
filter?.setValue(20, forKey: kCIInputScaleKey)
```

### 결과 확인하기

이미지 필터링 기능이 추가된 SimpleImageViewer 앱을 실행해보세요. 이미지를 로드한 후, 다양한 필터를 적용해보면서 결과를 확인할 수 있습니다.

### 결론

Swift를 사용하여 SimpleImageViewer 앱에 이미지 필터링 기능을 추가하는 방법을 배웠습니다. Core Image 프레임워크를 사용하여 이미지 로드, 필터 선택 및 설정, 필터 적용, 출력 이미지 변환까지 다양한 작업을 수행할 수 있습니다. 이미지 필터링은 사용자에게 시각적인 표현을 변경하는 다양한 경험을 제공할 수 있으며, 이를 통해 앱의 사용자들에게 더욱 흥미로운 기능을 제공할 수 있습니다.

### 참고 자료
- [SwiftUI Image Effects](https://developer.apple.com/tutorials/swiftui/interfacing-with-uikit)
- [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/filter/ci/CISepiaTone)