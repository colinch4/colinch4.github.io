---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 캡션 스타일 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어는 사용자에게 이미지를 보여주는 데 사용되는 매우 유용한 도구입니다. Swift에서는 SimpleImageViewer 라이브러리를 사용하여 간단하고 효과적인 이미지 뷰어를 만들 수 있습니다. 이번 예시에서는 SimpleImageViewer를 사용하여 이미지 캡션의 스타일을 설정하는 방법을 알아보겠습니다.

## 필수 준비물
- Xcode가 설치된 Mac 컴퓨터
- SimpleImageViewer 라이브러리

## 라이브러리 설치
1. Xcode를 열고 프로젝트를 선택합니다.
2. 프로젝트 내부에서 `File` > `Swift Packages` > `Add Package Dependency...`를 선택합니다.
3. 패키지 관리자 창에서 `https://github.com/Krisiacik/ImageViewer.swift`를 입력하고 확인을 누릅니다.
4. 원하는 버전을 선택하고 `Add Package`를 클릭합니다.

## 이미지 캡션 스타일 설정

먼저, SimpleImageViewer를 사용하여 이미지 뷰어를 생성해야 합니다. 이미지 뷰어를 생성한 뒤에는 캡션 라벨의 스타일을 변경할 수 있습니다.

```swift
import UIKit
import SimpleImageViewer

class ViewController: UIViewController {
    
    // ...

    func showImageViewer() {
        let imageViewer = ImageViewerController(imageUrls: ["image1.jpg", "image2.jpg", "image3.jpg"])
        present(imageViewer, animated: true, completion: nil)
        
        // 캡션 라벨 스타일 설정
        imageViewer.captionLabel.textAlignment = .center
        imageViewer.captionLabel.textColor = .white
        imageViewer.captionLabel.font = UIFont.boldSystemFont(ofSize: 16)
        imageViewer.captionLabel.backgroundColor = .black
    }
    
    // ...
}
```
위의 코드에서 `imageViewer.captionLabel` 을 사용하여 캡션 라벨의 스타일을 변경할 수 있습니다. `textAlignment`을 사용하여 텍스트 정렬을 설정하고 `textColor`를 사용하여 텍스트 색상을 변경할 수 있습니다. 또한, `font`를 사용하여 텍스트의 글꼴을 설정하고 `backgroundColor`를 사용하여 캡션 라벨의 배경색을 변경할 수 있습니다.

이제 이미지 뷰어가 표시될 때 캡션 라벨의 스타일이 설정된 것을 확인할 수 있습니다.

## 결론

SimpleImageViewer를 사용하여 이미지 캡션 스타일을 설정하는 방법을 알아보았습니다. 이를 통해 사용자는 이미지 뷰어의 캡션 라벨을 자신의 앱에 맞게 사용자 정의할 수 있습니다. 추가로 필요한 스타일 변경은 SimpleImageViewer의 다른 속성들을 활용하여 쉽게 구현할 수 있습니다.

## 참고 자료

- [SimpleImageViewer 라이브러리](https://github.com/Krisiacik/ImageViewer.swift)