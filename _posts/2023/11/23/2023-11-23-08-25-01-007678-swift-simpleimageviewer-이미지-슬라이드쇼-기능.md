---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 슬라이드쇼 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이 글에서는 Swift를 사용하여 간단한 이미지 뷰어와 슬라이드쇼 기능을 구현하는 방법을 알아보겠습니다.

## 개요
이미지 슬라이드쇼 기능은 여러 개의 이미지를 자동으로 전환하면서 보여주는 기능을 의미합니다. 이를 위해 `UIImageView`와 `Timer`를 사용하여 이미지를 보여주고 전환하는 로직을 구현할 것입니다. 

## 프로젝트 설정
먼저, Xcode에서 Swift 프로젝트를 생성하고, 이미지 파일들을 프로젝트에 추가합니다. 이미지 파일들은 Assets.xcassets에 추가하거나 프로젝트 파일 시스템에 직접 추가할 수 있습니다.

## 이미지 뷰어 구현하기
먼저, 이미지를 보여주기 위한 `UIImageView`를 UI에 추가해야 합니다. 스토리보드로 인터페이스를 구성하거나 코드로 `UIImageView`를 생성할 수 있습니다. 

```swift
import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰어 초기화
        imageView.image = UIImage(named: "image1") // 첫 번째 이미지로 초기화
    }
}
```

위 코드는 `UIImageView`를 추가하고 첫 번째 이미지로 초기화하는 예제입니다.

## 슬라이드쇼 기능 추가하기
이제 타이머를 사용하여 이미지를 전환하는 슬라이드쇼 기능을 추가하겠습니다.

```swift
import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    
    let images = ["image1", "image2", "image3"] // 전환할 이미지 파일 이름들
    var currentIndex = 0 // 현재 보여지고 있는 이미지 인덱스
    var timer: Timer? // 슬라이드쇼 타이머
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰어 초기화
        imageView.image = UIImage(named: images[currentIndex]) // 첫 번째 이미지로 초기화
        
        // 슬라이드쇼 시작
        startSlideshow()
    }
    
    func startSlideshow() {
        timer = Timer.scheduledTimer(timeInterval: 2.0, target: self, selector: #selector(nextImage), userInfo: nil, repeats: true)
    }
    
    @objc func nextImage() {
        currentIndex = (currentIndex + 1) % images.count // 다음 이미지 인덱스 계산
        imageView.image = UIImage(named: images[currentIndex]) // 다음 이미지로 전환
    }
    
    func stopSlideshow() {
        timer?.invalidate()
        timer = nil
    }
}
```

위 코드는 슬라이드쇼 기능을 추가한 예제입니다. `images` 배열에 전환할 이미지 파일 이름들을 저장하고, 타이머를 사용하여 `nextImage` 메소드를 일정 시간마다 실행하여 이미지를 전환합니다. `startSlideshow` 메소드에서 타이머를 시작하고, `stopSlideshow` 메소드에서 타이머를 중지시킵니다.

## 결론
이제 Swift를 사용하여 간단한 이미지 뷰어와 슬라이드쇼 기능을 구현하는 방법을 알아보았습니다. 이를 응용하여 다양한 이미지 뷰어 및 슬라이드쇼 앱을 개발할 수 있습니다.

## 참고 자료
- [Swift 공식 문서](https://docs.swift.org/swift-book/)
- [Apple Developer Documentation](https://developer.apple.com/documentation/)