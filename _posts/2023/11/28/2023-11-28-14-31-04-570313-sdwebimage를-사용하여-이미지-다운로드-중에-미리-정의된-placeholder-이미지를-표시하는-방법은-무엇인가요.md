---
layout: post
title: "[swift] SDWebImage를 사용하여 이미지 다운로드 중에 미리 정의된 placeholder 이미지를 표시하는 방법은 무엇인가요?"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

```swift
import SDWebImage

// 이미지를 다운로드할 ImageView 정의하기
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))

// Placeholder 이미지 설정하기
let placeholderImage = UIImage(named: "placeholder")

// SDWebImage를 사용하여 이미지 다운로드 및 표시하기
imageView.sd_setImage(with: URL(string: "https://example.com/image.jpg"), placeholderImage: placeholderImage)
```

위의 코드에서 `UIImage(named: "placeholder")` 부분은 사용할 Placeholder 이미지의 이름을 지정해야 합니다. Placeholder 이미지는 다운로드 중에 표시될 임시 이미지로 사용됩니다. SDWebImage는 원격 이미지를 다운로드하여 표시할 때, 다운로드가 완료될 때까지 이 Placeholder 이미지를 표시합니다. 다운로드가 완료되면 원격 이미지로 교체됩니다.

참고로, 위의 코드에서 `https://example.com/image.jpg` 부분은 실제 이미지 URL로 대체되어야 합니다. 이 코드는 SDWebImage를 사용하여 ImageView에서 비동기적으로 이미지를 다운로드하고 표시하는 기본적인 방법을 보여줍니다.

SDWebImage에 대한 자세한 사용법과 다양한 기능에 대해서는 [공식 문서](https://github.com/SDWebImage/SDWebImage)를 참고하시기 바랍니다.