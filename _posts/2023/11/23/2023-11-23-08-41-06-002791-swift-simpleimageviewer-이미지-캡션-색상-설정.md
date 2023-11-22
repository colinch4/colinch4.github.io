---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 캡션 색상 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

# 개요
Swift SimpleImageViewer라는 라이브러리는 간단하고 편리한 이미지 뷰어 기능을 제공합니다. 이 라이브러리를 사용하여 이미지를 보여줄 때, 이미지 캡션의 색상을 설정하는 방법에 대해 알아보겠습니다.

# 단계 1: 라이브러리 설치
SimpleImageViewer 라이브러리를 사용하기 위해서는 먼저 CocoaPods를 통해 라이브러리를 설치해야 합니다. Podfile에 다음과 같이 추가한 후, 터미널에서 `pod install` 명령을 실행합니다.

```bash
platform :ios, '9.0'
use_frameworks!

target 'YourApp' do
  pod 'SimpleImageViewer'
end
```

# 단계 2: 이미지 캡션 색상 설정
SimpleImageViewer는 이미지와 관련된 정보를 보여주는 캡션을 제공합니다. 이 캡션의 색상을 설정하기 위해서는 SimpleImageViewerConfig 클래스의 captionTextColor 속성을 사용합니다.

```swift
import SimpleImageViewer

let config = SimpleImageViewerConfig()

// 이미지 캡션 텍스트 색상 설정
config.captionTextColor = .red

// 이미지 뷰어 생성
let viewer = ImageViewerController(config: config, imageUrls: imageUrls, initialIndex: 0)

// 이미지 뷰어 표시
present(viewer, animated: true, completion: nil)
```

위의 예제에서 captionTextColor 속성을 사용하여 캡션 텍스트의 색상을 설정합니다. 이 예제에서는 캡션 텍스트의 색상을 빨강으로 설정했습니다.

# 참고
- SimpleImageViewer GitHub 저장소: [링크](https://github.com/nashysolutions/SimpleImageViewer)

이제 Swift SimpleImageViewer를 사용하면서 이미지 캡션의 색상을 설정하는 방법을 알게 되었습니다. 이를 활용하여 더욱 멋진 이미지 뷰어를 구현해 보세요.