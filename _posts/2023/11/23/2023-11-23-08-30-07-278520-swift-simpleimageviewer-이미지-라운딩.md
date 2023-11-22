---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 라운딩"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지를 원형이나 둥근 모양으로 보여주고 싶다면, Swift의 `SimpleImageViewer`를 사용하여 이를 간단하게 구현할 수 있습니다. 이 블로그 포스트에서는 `SimpleImageViewer`를 사용하여 이미지를 둥근 모양으로 라운딩하는 방법을 안내하겠습니다.

## SimpleImageViewer란?

`SimpleImageViewer`는 Swift에서 이미지를 표시하고 조작하는 강력한 라이브러리입니다. 원하는 모양으로 이미지를 변형하거나 필터링 할 수 있으며, 여러 가지 효과를 적용하여 이미지를 개인화 할 수 있습니다.

## 이미지 둥글게 만들기

1. 먼저 `SimpleImageViewer`를 프로젝트에 추가해야 합니다. 프로젝트의 `Podfile`에 다음과 같이 `SimpleImageViewer`를 추가합니다:

```ruby
pod 'SimpleImageViewer'
```

2. Terminal에서 프로젝트 폴더로 이동한 후, `pod install` 명령어를 실행하여 `SimpleImageViewer`를 설치합니다.

3. 이제 이미지를 둥글게 만들 준비가 되었습니다. 프로젝트의 ViewController 파일을 열고 다음과 같이 코드를 작성합니다:

```swift
import UIKit
import SimpleImageViewer

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지를 둥글게 만들기
        imageView.layer.cornerRadius = imageView.frame.size.width / 2
        imageView.clipsToBounds = true

        // 이미지 뷰어 추가하기
        let imageTapGesture = UITapGestureRecognizer(target: self, action: #selector(showImageViewer))
        imageView.isUserInteractionEnabled = true
        imageView.addGestureRecognizer(imageTapGesture)
    }
    
    @objc func showImageViewer() {
        guard let image = imageView.image else { return }
        let viewer = ImageViewerController(image: image)
        present(viewer, animated: true)
    }
}
```

4. `imageView`의 `layer.cornerRadius`를 설정하여 이미지를 둥글게 만들 수 있습니다. 이 때, `imageView`의 너비를 이용하여 반지름 값을 계산하여 적용합니다.

5. `imageView`에 `UITapGestureRecognizer`를 추가하여 이미지를 탭하면 이미지 뷰어가 열리도록 합니다. `ImageViewerController`를 사용하여 이미지를 표시하는 뷰어를 만들고, 탭 이벤트가 발생하면 해당 뷰어를 표시합니다.

6. 프로젝트를 빌드 및 실행하여 이미지를 선택하면 둥근 모양으로 라운딩된 이미지가 표시되는 것을 확인할 수 있습니다.

## 결론

`SimpleImageViewer`를 사용하여 Swift에서 이미지를 둥글게 만들 수 있었습니다. 이렇게 이미지를 둥글게 만드는 것은 UI 디자인에 활용하기 좋은 기능 중 하나입니다. 다른 모양으로 이미지를 변형하거나 필터링할 수도 있으므로, 필요에 따라 `SimpleImageViewer`를 활용해보세요.