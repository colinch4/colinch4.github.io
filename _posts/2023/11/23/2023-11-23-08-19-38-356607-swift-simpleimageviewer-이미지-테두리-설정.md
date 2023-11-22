---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 테두리 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어 라이브러리를 사용하여 이미지를 표시할 때, 때로는 이미지 주위에 테두리를 추가하고 싶을 수 있습니다. Swift에서 SimpleImageViewer를 사용하여 이미지 테두리를 설정하는 방법에 대해 알아보겠습니다. 

먼저, SimpleImageViewer를 설치합니다. CocoaPods를 사용한다면 Podfile에 다음과 같이 라이브러리를 추가합니다.

```ruby
pod 'SimpleImageViewer'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

이제 이미지를 로드한 후, 테두리를 설정하는 코드를 작성해보겠습니다.

```swift
import SimpleImageViewer

let imageViewer = ImageViewer()
let image = UIImage(named: "example_image")

let imageView = UIImageView(image: image)
imageView.layer.borderWidth = 1 // 테두리 두께 설정
imageView.layer.borderColor = UIColor.black.cgColor // 테두리 색상 설정

imageView.isUserInteractionEnabled = true // 이미지 뷰에 상호 작용 활성화

// 이미지 뷰를 클릭했을 때, 이미지 뷰어로 이미지 표시
imageViewer.show(imageView, in: self)
```

위의 코드에서 `imageView.layer.borderWidth`를 사용하여 테두리의 두께를 설정하고, `imageView.layer.borderColor`를 사용하여 테두리의 색상을 설정합니다. 이후 `imageView.isUserInteractionEnabled`를 true로 설정하여 이미지 뷰에 상호 작용을 활성화합니다.

마지막으로 `imageViewer.show(imageView, in: self)`를 사용하여 이미지 뷰어로 이미지를 표시합니다.

위의 코드를 실행하여 이미지를 로드하고 테두리를 설정해보세요. SimpleImageViewer를 사용하여 이미지의 테두리를 쉽게 추가할 수 있습니다.

참고 문서: [SimpleImageViewer GitHub](https://github.com/Krisiacik/ImageViewer)