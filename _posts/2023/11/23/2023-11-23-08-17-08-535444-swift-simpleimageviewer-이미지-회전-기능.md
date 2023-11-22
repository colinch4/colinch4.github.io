---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 회전 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번 블로그 포스트에서는 Swift로 간단한 이미지 뷰어 앱에 이미지 회전 기능을 추가하는 방법을 알아보겠습니다.

## 1. 이미지 뷰어 앱 구성

먼저, 이미지 뷰어 앱을 구성하기 위해 다음과 같은 요소가 필요합니다.

### 1.1 UIImageView

UIImageView는 이미지를 보여주는 뷰입니다. 앱에서 이미지를 표시하기 위해 UIImageView를 사용합니다.

```swift
let imageView = UIImageView()
```

### 1.2 Rotate Button

회전 기능을 제어하기 위한 버튼이 필요합니다. 이 버튼을 눌렀을 때 이미지가 시계 방향으로 90도 회전될 수 있도록 구현할 것입니다.

```swift
let rotateButton = UIButton()
// 버튼에 회전 액션 추가
rotateButton.addTarget(self, action: #selector(rotateImage), for: .touchUpInside)
```

### 1.3 이미지 회전 기능 구현

이제 이미지 회전 기능을 구현해보겠습니다. 회전은 CGAffineTrasnform을 사용하여 이미지의 회전 각도를 조절하는 방식으로 진행됩니다.

```swift
var rotation: CGFloat = 0.0 // 현재 이미지 회전 각도

@objc func rotateImage() {
    rotation += .pi / 2 // 90도 회전
    imageView.transform = CGAffineTransform(rotationAngle: rotation)
}
```

여기서 `rotation` 변수는 현재 이미지의 회전 각도를 저장하는 역할을 합니다. `rotateImage` 함수는 버튼을 누를 때마다 `rotation` 값에 90도를 더해주고, `CGAffineTransform`을 사용하여 이미지 뷰에 회전 효과를 적용합니다.

## 2. 실행 결과

위의 구현을 완료한 뒤, 앱을 실행하고 이미지를 로드한 다음 회전 버튼을 눌러보세요. 이미지가 90도씩 시계 방향으로 회전할 것입니다.

![](https://example.com/image.png)

## 3. 마무리

이제 Swift로 간단한 이미지 뷰어 앱에 이미지 회전 기능을 추가하는 방법을 배웠습니다. 여러분은 이 기능을 활용하여 이미지 뷰어 앱을 개발하거나 이미지 회전 기능을 다른 앱에 추가할 수 있습니다.

더 많은 정보와 예제 코드는 [Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimageview)를 참고하십시오.