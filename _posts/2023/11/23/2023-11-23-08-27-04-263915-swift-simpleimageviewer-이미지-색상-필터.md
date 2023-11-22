---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 색상 필터"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift를 사용하여 이미지를 색상 필터링하는 방법에 대해 알아보겠습니다. 이미지 색상 필터링은 이미지에 다양한 효과를 줄 수 있는 좋은 방법 중 하나입니다.

## 필요한 라이브러리 가져오기

먼저, 이미지 색상 필터링을 위해 `UIKit` 라이브러리를 가져와야 합니다.

```swift
import UIKit
```

## 이미지 색상 필터 적용하기

이미지 색상 필터를 적용하려면 `UIImage` 클래스의 `withRenderingMode` 메서드를 사용해야 합니다. 다음은 이를 사용하는 간단한 코드 예시입니다.

```swift
let originalImage = UIImage(named: "image.jpg") // 원본 이미지
let filteredImage = originalImage?.withRenderingMode(.alwaysTemplate) // 필터 적용된 이미지
```

위의 코드에서 `image.jpg`는 필터를 적용할 원본 이미지의 경로입니다. `withRenderingMode` 메서드에 `alwaysTemplate` 매개변수를 전달하여 필터 적용된 이미지를 생성합니다.

## 이미지 색상 변경하기

필터 적용된 이미지의 색상을 변경하려면 `tintColor` 속성을 사용해야 합니다. 이를 사용하여 이미지의 색상을 원하는 대로 변경할 수 있습니다.

```swift
let color = UIColor.red // 원하는 색상
filteredImage?.withTintColor(color)
```

위의 코드에서 `UIColor.red`는 이미지에 적용할 원하는 색상입니다. `withTintColor` 메서드를 사용하여 필터 적용된 이미지의 색상을 변경할 수 있습니다.

## 이미지 뷰에 표시하기

마지막으로, 이미지 색상 필터를 적용하고 변경한 이미지를 이미지 뷰에 표시하는 방법입니다.

```swift
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200)) // 이미지 뷰 생성
imageView.image = filteredImage // 필터 적용된 이미지 설정
imageView.tintColor = UIColor.red // 이미지 색상 변경
```

위의 코드에서 `UIImageView` 클래스를 사용하여 이미지 뷰를 생성합니다. 이미지 뷰의 `image` 속성에 필터 적용된 이미지를 설정하고, `tintColor` 속성에 이미지의 색상을 변경하는 코드를 추가합니다.

## 참고 자료

- [UIImage - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimage)
- [UIImageView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimageview)