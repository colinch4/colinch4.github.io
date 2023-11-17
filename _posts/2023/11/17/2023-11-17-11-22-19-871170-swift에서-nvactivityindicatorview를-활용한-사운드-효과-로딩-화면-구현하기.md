---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 활용한 사운드 효과 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

로딩 화면은 사용자들이 어떤 작업이 진행 중인지 알 수 있도록 도와주는 중요한 요소입니다. Swift 언어로 iOS 앱을 개발할 때, 사운드 효과와 함께 로딩 화면을 구현하고 싶다면 NVActivityIndicatorView를 사용할 수 있습니다. NVActivityIndicatorView는 많은 다양한 로딩 애니메이션을 제공하며, 이 중에서도 효과적인 사운드 효과와 조합하여 사용할 수 있습니다.

## NVActivityIndicatorView 설치

**1. CocoaPods**를 사용하여 NVActivityIndicatorView를 설치합니다. `Podfile`을 열고 아래와 같이 Pods에 NVActivityIndicatorView를 추가합니다.

```plaintext
pod 'NVActivityIndicatorView'
```

**2. 터미널**에서 `pod install` 명령어를 실행하여 NVActivityIndicatorView를 프로젝트에 설치합니다.

## NVActivityIndicatorView 사용 방법

**1. NVActivityIndicatorView를 초기화**하고 로딩 화면을 표시할 뷰에 추가합니다. 

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .white, padding: nil)
        
        // 로딩 화면을 표시할 뷰에 추가
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }
}
```

**2. 로딩 화면을 시작**하고, 작업이 완료된 후에 로딩 화면을 숨깁니다.

```swift
// 로딩 시작
activityIndicatorView.startAnimating()

// 작업 완료 후 로딩 화면 숨김
// 예를 들어, API 요청이 완료된 후에 숨김
func onAPICallCompleted() {
    activityIndicatorView.stopAnimating()
}
```

위의 예시에서는 `NVActivityIndicatorView`를 초기화하고, 로딩 화면을 표시할 뷰에 추가한 후 `startAnimating()` 메서드를 호출하여 로딩을 시작하고, 작업이 완료된 후에는 `stopAnimating()` 메서드를 호출하여 로딩 화면을 숨깁니다.

## 사운드 효과 추가하기

로딩 화면에 사운드 효과를 추가하기 위해 `AVAudioPlayer`를 사용할 수 있습니다. 

**1. 사운드 파일을 프로젝트에 추가**합니다. Xcode의 프로젝트 네비게이터에서 "Add Files to..."를 선택하고, 사운드 파일을 선택하여 프로젝트에 추가합니다.

**2. `AVAudioPlayer`를 초기화**하고 사운드 파일을 로딩합니다.

```swift
import AVFoundation

class LoadingViewController: UIViewController {
    var audioPlayer: AVAudioPlayer?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // AVAudioPlayer 초기화
        let soundURL = Bundle.main.url(forResource: "loading_sound", withExtension: "mp3")
        audioPlayer = try? AVAudioPlayer(contentsOf: soundURL!)
        audioPlayer?.prepareToPlay()
    }
}
```

**3. 사운드 효과 재생**을 원하는 위치에서 `play()` 메서드를 호출합니다.

```swift
// 로딩 시작
activityIndicatorView.startAnimating()
audioPlayer?.play()

// 작업 완료 후 로딩 화면 숨김
func onAPICallCompleted() {
    activityIndicatorView.stopAnimating()
}
```

위의 예시에서는 `AVAudioPlayer`를 초기화하고, 사운드 파일을 로딩한 후 `play()` 메서드를 호출하여 사운드 효과를 재생합니다. 로딩 화면을 숨길 때 사운드 효과가 끝나지 않았다면 `stop()` 메서드를 호출하여 사운드 효과를 중지할 수도 있습니다.

## 결론

이제 Swift에서 NVActivityIndicatorView를 사용하여 사운드 효과와 함께 로딩 화면을 구현하는 방법을 알아보았습니다. NVActivityIndicatorView를 활용하면 다양한 로딩 애니메이션을 쉽게 구현할 수 있으며, 사운드 효과를 추가하여 사용자들에게 더 나은 사용자 경험을 제공할 수 있습니다.

NVActivityIndicatorView 공식 문서: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)

AVAudioPlayer 공식 문서: [https://developer.apple.com/documentation/avfoundation/avaudioplayer](https://developer.apple.com/documentation/avfoundation/avaudioplayer)