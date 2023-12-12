---
layout: post
title: "[swift] Swift AVPlayerViewController를 이용한 비디오 재생"
description: " "
date: 2023-12-12
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발하다 보면 동영상을 재생해야 하는 경우가 많이 있습니다. AVPlayerViewController는 iOS에서 비디오를 재생할 때 유용한 컨트롤러 중 하나입니다. 이를 이용하여 약간의 코드로 동영상을 간단히 재생할 수 있습니다. 
이번에는 AVPlayerViewController를 이용한 Swift 코드 예제를 통해 어떻게 동영상을 재생하는지 알아보겠습니다.

## AVPlayerViewController 만들기
AVPlayerViewController를 이용하여 동영상을 재생하려면 AVKit 프레임워크를 import해야 합니다.

```swift
import AVKit
import AVFoundation
```

## AVPlayerViewController 초기화 및 비디오 재생
AVPlayerViewController를 초기화하고 비디오를 재생하는 예제 코드는 다음과 같습니다.

```swift
if let videoURL = URL(string: "video_url_here") {
    let player = AVPlayer(url: videoURL)
    let playerController = AVPlayerViewController()
    playerController.player = player
    present(playerController, animated: true) {
        player.play()
    }
}
```

위 코드에서는 AVPlayerViewController를 초기화하고, 비디오의 URL을 이용하여 AVPlayer를 만든 다음, AVPlayerViewController에 해당 player를 설정한 후 화면에 보여주는 과정을 보여줍니다.

이제 위의 코드를 이용해서 간단한 동영상 재생 기능을 구현할 수 있습니다. AVPlayerViewController는 사용자에게 동영상 재생을 위한 기본적인 인터페이스를 제공하여 개발자가 별도의 인터페이스를 구현하지 않아도 됩니다.

AVPlayerViewController를 이용하면 코드를 간단하게 유지하면서도 동영상을 손쉽게 재생할 수 있습니다. 이를 통해 앱의 사용자 경험을 향상시키고 동영상 관련 기능을 더 쉽게 구현할 수 있습니다.

## 결론
이번 포스트에서는 AVPlayerViewController를 이용하여 Swift로 동영상을 재생하는 방법에 대해 알아보았습니다. AVPlayerViewController를 활용하면 간단한 코드로 동영상 재생 기능을 구현할 수 있으며, 이를 통해 앱의 사용자 경험을 향상시킬 수 있습니다. 
AVPlayerViewController를 사용하여 동영상을 재생하는 방법에 익숙해지면 다양한 동영상 처리 기능을 추가하여 보다 다채로운 앱을 개발할 수 있을 것입니다.

[참고 자료]
- [AVPlayerViewController 공식 문서 (Apple Developer)](https://developer.apple.com/documentation/avkit/avplayerviewcontroller)
- [AVPlayerViewController 클래스 레퍼런스 (Apple Developer)](https://developer.apple.com/documentation/avkit/avplayerviewcontroller)