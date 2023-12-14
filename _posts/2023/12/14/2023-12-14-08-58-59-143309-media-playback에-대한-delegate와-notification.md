---
layout: post
title: "[ios] Media Playback에 대한 Delegate와 Notification"
description: " "
date: 2023-12-14
tags: [ios]
comments: true
share: true
---

iOS 애플리케이션에서 미디어를 재생하는 동안 특정 이벤트에 대응하기 위해 Delegate 및 Notification을 사용할 수 있습니다. 이를 통해 재생 상태의 변경, 재생이 완료될 때의 작업, 오디오 포커스를 관리하는 등 다양한 작업을 수행할 수 있습니다.

## AVPlayerDelegate
AVPlayerDelegate는 AVPlayer 객체에서 재생 관련 이벤트를 처리하기 위한 프로토콜입니다. AVPlayer 객체가 생성한 후 해당 객체의 delegate 프로퍼티에 할당하여 사용할 수 있습니다. 아래는 AVPlayerDelegate 프로토콜의 주요 메서드들입니다.

### 1. func playerItemDidPlayToEndTime(_ player: AVPlayer)
이 메서드는 재생 중인 아이템이 재생이 끝났을 때 호출됩니다. 이를 통해 재생이 끝나면 다음 동작을 처리할 수 있습니다.

### 2. func player(_ player: AVPlayer, didChangePlaybackState state: AVPlayerPlaybackState)
이 메서드는 재생 상태의 변화를 감지하여 처리할 수 있게 해줍니다. 재생 중, 일시정지, 정지 등의 상태 변경에 따라 적절한 작업을 수행할 수 있습니다.

## NotificationCenter
Notification을 사용하여 미디어 재생과 관련된 이벤트를 수신할 수 있습니다. NotificationCenter를 사용하면 여러 객체에서 특정 이벤트에 대응할 수 있으며, 별도의 Delegate를 지정할 필요가 없습니다.

### 1. Notification.Name.AVPlayerItemDidPlayToEndTime
이 Notification은 AVPlayerItem이 재생을 완료했을 때 발생합니다. 이를 통해 재생이 끝났을 때 필요한 작업을 처리할 수 있습니다.

### 2. Notification.Name.AVPlayerItemTimeJumped
이 Notification은 AVPlayerItem의 재생 시간이 변경됐을 때 발생합니다. 이를 활용하여 재생 시간에 따른 화면 표시 등의 작업을 수행할 수 있습니다.

Delegate와 Notification을 활용하여 미디어 재생과 관련된 이벤트를 적절하게 처리하면 더 효율적이고 유연한 애플리케이션을 개발할 수 있습니다.

## 참고 자료
- [Apple Developer Documentation - AVPlayerDelegate](https://developer.apple.com/documentation/avfoundation/avplayerdelegate)
- [Apple Developer Documentation - NotificationCenter](https://developer.apple.com/documentation/foundation/notificationcenter)

위의 내용은 iOS 애플리케이션에서 미디어 재생과 관련된 Delegate와 Notification에 대한 간략한 소개입니다. Delegate와 Notification을 효과적으로 활용하여 미디어 재생 동작을 제어하고 이벤트에 대응할 수 있습니다.