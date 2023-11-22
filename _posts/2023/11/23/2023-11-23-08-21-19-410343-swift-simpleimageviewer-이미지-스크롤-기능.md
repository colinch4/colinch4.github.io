---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 스크롤 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift SimpleImageViewer는 iOS 앱에서 이미지를 스크롤할 수 있는 기능을 제공하는 간단하고 편리한 라이브러리입니다.

## 설치

SimpleImageViewer는 [CocoaPods](https://cocoapods.org/)를 사용하여 설치할 수 있습니다. `Podfile`에 다음 코드를 추가한 후, `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

```swift
pod 'SimpleImageViewer'
```

## 사용법

1. SimpleImageViewer를 import 합니다.

```swift
import SimpleImageViewer
```

2. 이미지를 스크롤할 뷰컨트롤러 인스턴스를 생성합니다.

```swift
let imageViewer = SimpleImageViewerController()
```

3. 이미지를 설정하고 이미지 뷰어를 표시합니다.

```swift
if let myImage = UIImage(named: "myImage.png") {
    imageViewer.image = myImage
    present(imageViewer, animated: true, completion: nil)
}
```

4. 추가적인 설정

- `imageViewer`의 `modalPresentationStyle` 속성을 `fullScreen`으로 설정하여 전체 화면으로 이미지 뷰어를 표시할 수 있습니다.

```swift
imageViewer.modalPresentationStyle = .fullScreen
```

- `imageViewer`의 `dismissCompletion` 클로저를 사용하여 이미지 뷰어가 닫힐 때 수행할 작업을 지정할 수 있습니다.

```swift
imageViewer.dismissCompletion = {
    print("Image viewer dismissed")
}
```

5. 사용자가 특정 이미지를 선택했을 때 추가적인 작업을 수행하고자 하는 경우, `SimpleImageViewerDelegate`를 구현할 수 있습니다. 해당 뷰컨트롤러에서 프로토콜을 채택하고 델리게이트 메서드를 구현합니다.

```swift
class MyViewController: UIViewController, SimpleImageViewerDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()

        imageViewer.delegate = self
    }

    func imageViewerDidDismiss(_ imageViewer: SimpleImageViewerController) {
        print("Image viewer dismissed")
    }
}
```

## 결론

Swift SimpleImageViewer를 사용하면 iOS 앱에서 간편하게 이미지 스크롤 기능을 구현할 수 있습니다. 위의 단계를 따라하면 이미지를 스크롤할 수 있는 이미지 뷰어를 쉽게 구현할 수 있습니다.