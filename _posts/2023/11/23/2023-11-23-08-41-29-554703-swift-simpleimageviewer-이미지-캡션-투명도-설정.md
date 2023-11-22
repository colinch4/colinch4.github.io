---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 캡션 투명도 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이전에 [Swift SimpleImageViewer](https://github.com/michaelhenry/SimpleImageViewer)를 사용하여 이미지 뷰어를 만들었는데, 이때 이미지 캡션의 투명도를 조절하고자 합니다. 캡션을 투명하게 하여 이미지를 더욱 강조하고 싶은 경우 유용합니다. 

## Step 1: SimpleImageViewer 가져오기

먼저, SimpleImageViewer 라이브러리를 프로젝트에 추가합니다. 이를 위해서는 [CocoaPods](https://cocoapods.org/)를 사용할 수 있습니다. Podfile에 다음 코드를 추가합니다:

```ruby
pod 'SimpleImageViewer'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## Step 2: 캡션 투명도 설정하기

SimpleImageViewer는 이미지와 캡션을 렌더링하기 위해 `CaptionView`를 사용합니다. 캡션의 투명도를 조절하려면 `CaptionView`를 커스터마이즈 해야합니다.

```swift
import SimpleImageViewer

class CustomCaptionView: CaptionView {
    override func setup() {
        super.setup()
        self.backgroundColor = UIColor.black.withAlphaComponent(0.5) // 투명도 조절
        self.textColor = UIColor.white // 캡션 텍스트 색상 지정
    }
}

// SimpleImageViewer를 초기화할 때 다음과 같이 사용합니다.
let configuration = ImageViewerConfiguration { config in
    config.customCaptionView = CustomCaptionView.self
}
let imageViewer = ImageViewerController(configuration: configuration)
```

위의 코드에서, `CustomCaptionView` 클래스는 `CaptionView`를 상속받아 투명도와 텍스트 색상을 조절합니다. `backgroundColor` 속성을 사용하여 캡션의 투명도를 조절할 수 있습니다. 위의 코드에서는 검은색 배경에 0.5의 투명도를 지정하였습니다. `textColor` 속성을 사용하여 캡션 텍스트의 색상을 지정할 수도 있습니다.

## 결론

SimpleImageViewer를 사용하여 이미지 뷰어를 만들 때, 이미지 캡션의 투명도를 조절하는 방법을 알아보았습니다. 위의 단계를 따라가면 캡션 투명도를 원하는 대로 설정할 수 있습니다. 이를 통해 이미지 뷰어를 더욱 개인화하고 다양한 스타일을 적용할 수 있습니다.