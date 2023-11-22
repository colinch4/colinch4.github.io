---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 캡션 위치 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 캡션은 이미지를 설명하고 추가 정보를 제공하는 데 사용됩니다. SimpleImageViewer는 사용하기 쉬운 이미지 뷰어 라이브러리로, 이미지에 캡션을 추가하기 위한 다양한 옵션을 제공합니다.

## 이미지 캡션 위치 설정하기

SimpleImageViewer를 사용하여 이미지 캡션의 위치를 설정하려면 다음 단계를 따르세요.

1. SimpleImageViewer를 프로젝트에 추가합니다. (CocoaPods를 사용하는 경우 `pod 'SimpleImageViewer'`를 Podfile에 추가한 후 `pod install`을 실행합니다.)
2. 적절한 위치에서 `SimpleImageViewer`를 import 합니다.
   ```swift
   import SimpleImageViewer
   ```
3. `SimpleImageViewer`의 `configuration` 객체를 생성하고, `captionStyle`을 사용하여 원하는 캡션 위치를 설정합니다. 일반적으로 `captionAlignment` 속성을 사용하여 캡션의 가로 위치를 조정하고, `captionVerticalAlignment` 속성을 사용하여 캡션의 세로 위치를 조정할 수 있습니다.
   ```swift
   let configuration = ImageViewerConfiguration { config in
       config.captionStyle = .bottom // 캡션을 이미지 하단에 표시합니다.
       config.captionAlignment = .center // 캡션을 가운데로 정렬합니다.
       config.captionVerticalAlignment = .bottom // 캡션을 이미지 하단으로 정렬합니다.
   }
   ```
4. 이미지를 보여줄 때, `configuration` 객체를 사용하여 `ImageViewerController`를 초기화하고 캡션을 설정합니다.
   ```swift
   let imageViewer = ImageViewerController(imageURL: imageURL, configuration: configuration)
   imageViewer.caption = "이미지 설명" // 캡션을 설정합니다.
   self.present(imageViewer, animated: true, completion: nil)
   ```

위의 예제에서는 `captionStyle`을 `.bottom`으로 설정하여 캡션을 이미지의 하단에 표시하였습니다. `captionAlignment`과 `captionVerticalAlignment`을 사용하여 캡션을 원하는 위치로 조정할 수 있습니다.

자세한 내용은 [SimpleImageViewer GitHub 레포지토리](https://github.com/Isuru-Nanayakkara/SimpleImageViewer)를 참조하십시오.