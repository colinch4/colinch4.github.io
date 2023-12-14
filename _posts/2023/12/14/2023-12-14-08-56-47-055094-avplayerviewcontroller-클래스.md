---
layout: post
title: "[ios] AVPlayerViewController 클래스"
description: " "
date: 2023-12-14
tags: [ios]
comments: true
share: true
---

`AVPlayerViewController`는 iOS 애플리케이션에서 비디오를 재생하기 위한 시각적 사용자 인터페이스를 제공하는 클래스입니다. 이 클래스는 `AVKit` 프레임워크에 포함되어 있으며, 비디오 컨텐츠를 손쉽게 재생하고 제어할 수 있도록 도와줍니다.

## 주요 기능
`AVPlayerViewController` 클래스의 주요 기능은 다음과 같습니다:
- 비디오 재생 제어 버튼을 포함한 기본 비디오 인터페이스 제공
- 비디오의 재생, 일시 정지, 재개, 스크럽(위치 이동) 등의 기능을 포함
- 화면을 회전할 때의 자동 조정 기능

## 사용 예시
`AVPlayerViewController`를 사용하여 비디오를 재생하는 예시 코드는 다음과 같습니다:

```swift
import AVKit
import AVFoundation

// 비디오 파일의 URL
let videoURL = URL(string: "http://www.example.com/video.mp4")

// AVPlayer 인스턴스 생성
let player = AVPlayer(url: videoURL)

// AVPlayerViewController 인스턴스 생성
let playerViewController = AVPlayerViewController()
playerViewController.player = player

// 화면에 표시
present(playerViewController, animated: true) {
    player.play()
}
```

위의 예시 코드에서는 `AVPlayer`를 생성하고, 해당 player를 `AVPlayerViewController`에 할당한 후 화면에 표시하는 과정을 보여줍니다.

`AVPlayerViewController` 클래스를 사용하면 더 나은 비디오 재생 경험을 제공하고, 사용자가 비디오를 손쉽게 제어할 수 있도록 도와줍니다.

자세한 내용은 [Apple Developer Documentation](https://developer.apple.com/documentation/avkit/avplayerviewcontroller)를 참고하세요.

# References
- [Apple Developer Documentation - AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller)