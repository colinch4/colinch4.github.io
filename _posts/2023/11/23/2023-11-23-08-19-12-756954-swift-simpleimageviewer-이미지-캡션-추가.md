---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 캡션 추가"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift SimpleImageViewer는 이미지 뷰어 라이브러리로, 이미지를 터치하여 확대 / 축소하고 스와이프하여 다음 이미지로 이동할 수 있는 기능을 제공합니다. 이 라이브러리를 사용하면 이미지에 캡션을 추가하여 더 많은 정보를 전달할 수 있습니다.

### 라이브러리 설치

SimpleImageViewer를 사용하기 위해 먼저 라이브러리를 설치해야 합니다. CocoaPods를 사용하면 간단하게 설치할 수 있습니다. Podfile에 다음과 같이 추가합니다:

```swift
pod 'SimpleImageViewer', '~> 1.0'
```

그리고 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

### 이미지 캡션 추가

SimpleImageViewer를 사용하여 이미지를 보여주고 캡션을 추가하는 방법은 다음과 같습니다.

```swift
import SimpleImageViewer

class MyImageViewController: UIViewController {
    private let images = [UIImage(named: "image1"), UIImage(named: "image2"), UIImage(named: "image3")]
    private let captions = ["첫 번째 이미지", "두 번째 이미지", "세 번째 이미지"]

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let imageViewer = SimpleImageViewerController()
        
        for (index, image) in images.enumerated() {
            let imageView = UIImageView(image: image)
            imageView.contentMode = .scaleAspectFit
            
            let caption = captions[index]
            let captionLabel = UILabel()
            captionLabel.text = caption
            captionLabel.textAlignment = .center
            
            let item = GalleryItem.image { $0(imageView) }
            item.imageViewSetter = { [weak self] imageView in
                self?.setImage(imageView, index: index)
            }
            item.textLabelSetter = { [weak self] label in
                self?.setLabel(label, caption: caption)
            }
            
            imageViewer.addItem(item)
        }
        
        present(imageViewer, animated: true, completion: nil)
    }
    
    private func setImage(_ imageView: UIImageView, index: Int) {
        imageView.image = images[index]
    }
    
    private func setLabel(_ label: UILabel, caption: String) {
        label.text = caption
    }
}
```

위의 코드에서는 `images` 배열에 이미지들을, `captions` 배열에 캡션들을 저장합니다. `viewDidLoad`에서는 SimpleImageViewer 인스턴스를 생성하고, 각각의 이미지와 캡션을 포함한 이미지 뷰와 캡션 라벨을 생성하여 `imageViewer`에 추가합니다.

`item.imageViewSetter` 클로저에서는 이미지 뷰의 이미지를 설정하는 로직을 구현하고, `item.textLabelSetter` 클로저에서는 캡션 라벨의 텍스트를 설정하는 로직을 구현합니다.

마지막으로 `imageViewer`를 present하여 이미지 뷰어를 표시합니다.

### 캡션 스타일링

위의 코드에서는 캡션 텍스트를 `captionLabel`에 단순히 설정했지만, 필요에 따라 캡션에 스타일링을 적용할 수 있습니다. 예를 들어, 캡션 텍스트를 진하게 표시하고 폰트 크기를 조정하려면 다음과 같이 수정할 수 있습니다:

```swift
let captionLabel = UILabel()
captionLabel.text = caption
captionLabel.textAlignment = .center
captionLabel.font = UIFont.boldSystemFont(ofSize: 16)
```

### 참고 자료

- [SimpleImageViewer GitHub 저장소](https://github.com/hirohisa/ImageScrollView)
- [CocoaPods](https://cocoapods.org/)
- [UILabel Documentation](https://developer.apple.com/documentation/uikit/uilabel)