---
layout: post
title: "[swift] Swift SimpleImageViewer 투명 이미지 지원"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

![SimpleImageViewer](https://example.com/simpleimageviewer.png)

Swift SimpleImageViewer는 이미지를 쉽게 보여주는 간단한 이미지 뷰어 라이브러리입니다. 이 라이브러리를 사용하면 이미지를 확대, 축소, 이동하는 등의 작업을 손쉽게 할 수 있습니다.

그러나 기존의 SimpleImageViewer는 투명 이미지를 지원하지 않아서 배경이 투명한 이미지를 올리면 제대로 표시되지 않는 문제가 발생합니다. 이 문제를 해결하기 위해, 투명 이미지를 지원하는 업데이트된 버전을 제공하고자 합니다.

## 투명 이미지 지원하는 SimpleImageViewer 사용하기

먼저, SimpleImageViewer 라이브러리를 프로젝트에 추가합니다. CocoaPods를 사용하신다면, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'SimpleImageViewer'
```

다음으로, 해당 이미지 뷰어 라이브러리를 사용할 뷰 컨트롤러에서 다음과 같이 코드를 작성합니다.

```swift
import SimpleImageViewer

class MyViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    var imageViewer: ImageViewer?

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let tapGesture = UITapGestureRecognizer(target: self, action: #selector(showImageViewer))
        imageView.isUserInteractionEnabled = true
        imageView.addGestureRecognizer(tapGesture)
    }
    
    @objc func showImageViewer() {
        guard let image = imageView.image else {
            return
        }
        
        imageViewer = ImageViewer(originImage: image, animation: .fade(0.3), backgroundStyle: .blurred(.light), swipeToDismissEnabled: true)
        present(imageViewer!, animated: true, completion: nil)
    }
}
```

위의 코드에서 `imageViewer` 변수는 이미지 뷰어를 나타냅니다. `showImageViewer` 메서드는 이미지 뷰를 탭했을 때 호출되고, 해당 이미지를 보여줍니다.

## 투명 이미지 지원 설정하기

SimpleImageViewer를 수정하여 투명 이미지를 지원하도록 수정해보겠습니다. 

해당 라이브러리의 `ImageViewerController` 클래스를 열어서 `viewDidLoad` 메서드를 다음과 같이 수정합니다.

```swift
open override func viewDidLoad() {
    super.viewDidLoad()
    setupImageView()
}

private func setupImageView() {
    imageView = UIImageView(frame: view.frame)
    imageView.contentMode = .scaleAspectFit
    imageView.image = backgroundStyle.makeBackgroundImage(size: view.frame.size)
    imageView.translatesAutoresizingMaskIntoConstraints = false
    view.addSubview(imageView)
    
    imageView.leadingAnchor.constraint(equalTo: view.leadingAnchor).isActive = true
    imageView.trailingAnchor.constraint(equalTo: view.trailingAnchor).isActive = true
    imageView.topAnchor.constraint(equalTo: view.topAnchor).isActive = true
    imageView.bottomAnchor.constraint(equalTo: view.bottomAnchor).isActive = true
}
```

해당 코드는 `UIImageView`를 사용하여 배경 이미지를 표시합니다. `makeBackgroundImage` 메서드는 배경 스타일에 따라 적절한 이미지를 생성하는 역할을 합니다. 이렇게 수정된 코드를 컴파일하고 테스트하면, 이제 투명 이미지도 제대로 표시되는 것을 확인할 수 있습니다.

## 결론

이제 SimpleImageViewer를 사용하여 투명 이미지도 제대로 표시해줄 수 있는 이미지 뷰어를 구현할 수 있습니다. 위의 내용을 참고하여 원하는 대로 이미지 뷰어를 커스터마이징해보세요. SimpleImageViewer GitHub 저장소를 참고하시면 더 많은 기능과 사용 예제를 확인할 수 있습니다.

## 참고 자료

- [SimpleImageViewer GitHub 저장소](https://github.com/simpleintegrated/simple-image-viewer)