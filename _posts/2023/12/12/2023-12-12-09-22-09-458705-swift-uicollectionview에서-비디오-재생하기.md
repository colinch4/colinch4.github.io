---
layout: post
title: "[swift] Swift UICollectionView에서 비디오 재생하기"
description: " "
date: 2023-12-12
tags: [swift]
comments: true
share: true
---

UICollectionView는 여러 아이템을 그리드나 사용자 지정 레이아웃으로 나란히 배치하여 표시할 수 있는 iOS 앱의 중요한 컴포넌트입니다. UICollectionView를 사용하여 비디오를 표시하고 재생하기 위해서는 몇 가지 단계를 거쳐야 합니다.

## UICollectionView에 비디오 표시하기

UICollectionView의 셀에 비디오를 표시하려면 먼저 셀 디자인을 만들고, 비디오 파일을 로드하여 비디오 뷰에 표시해야 합니다. 비디오 뷰를 만들기 위해서는 AVPlayerLayer를 사용할 수 있습니다.

```swift
import AVKit

class VideoCell: UICollectionViewCell {
    var player: AVPlayer?
    var playerLayer: AVPlayerLayer?

    override func awakeFromNib() {
        super.awakeFromNib()

        let videoURL = URL(fileURLWithPath: "video.mp4")
        player = AVPlayer(url: videoURL)
        playerLayer = AVPlayerLayer(player: player)
        playerLayer?.frame = bounds
        contentView.layer.addSublayer(playerLayer!)
        player?.play()
    }
}
```

위 코드에서는 VideoCell이라는 컬렉션 뷰 셀을 만들고, 해당 셀이 표시될 때 비디오를 재생할 수 있도록 AVPlayer 및 AVPlayerLayer를 사용합니다.

## 비디오 컨트롤 구현하기

비디오를 재생하기 위해서는 사용자가 재생, 일시정지, 탐색 등을 할 수 있는 컨트롤이 필요합니다. 이를 위해 AVPlayerViewController를 사용하여 비디오 컨트롤러를 구현할 수 있습니다.

```swift
import AVKit

class VideoViewController: UIViewController {
    var player: AVPlayer?

    override func viewDidLoad() {
        super.viewDidLoad()

        let videoURL = URL(fileURLWithPath: "video.mp4")
        player = AVPlayer(url: videoURL)

        let playerViewController = AVPlayerViewController()
        playerViewController.player = player
        present(playerViewController, animated: true) {
            playerViewController.player?.play()
        }
    }
}
```

위 코드에서는 AVPlayerViewController를 사용하여 비디오를 표시하고, 사용자가 비디오를 재생할 수 있도록 합니다.

## 결론

Swift를 사용하여 UICollectionView에서 비디오를 재생하는 방법에 대해 알아보았습니다. UICollectionView를 사용하여 여러 개의 비디오를 효율적으로 표시하고 재생할 수 있습니다. 필요에 따라 사용자 지정 컨트롤러를 추가하여 비디오 플레이어를 제어할 수 있습니다.

더 많은 정보를 원하시면 [AVKit Framework](https://developer.apple.com/documentation/avkit)를 참조하세요.