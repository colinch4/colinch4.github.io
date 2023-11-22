---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 채도 조절"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 SimpleImageViewer를 사용하여 이미지의 채도를 조절하는 방법에 대해 알아보겠습니다. SimpleImageViewer는 이미지를 간단히 보여주는 기능을 제공하는 라이브러리입니다.

## 1. SimpleImageViewer 설치

SimpleImageViewer를 사용하기 위해 먼저 CocoaPods를 사용하여 설치해야 합니다. Podfile에 아래와 같이 추가해주세요.

```ruby
pod 'SimpleImageViewer'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 설치를 완료해주세요.

## 2. 채도 조절 기능 추가하기

우선 SimpleImageViewer를 사용하여 이미지를 보여줄 ViewController를 만들어주세요. 그리고 이미지를 보여줄 UIImageView를 추가해주세요.

```swift
import UIKit
import SimpleImageViewer

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 이미지를 로드하여 UIImageView에 설정합니다.
        imageView.image = UIImage(named: "your_image_name")
        
        // 이미지를 클릭할 때 채도 조절 기능을 추가합니다.
        imageView.isUserInteractionEnabled = true
        let gestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(showImageWithSaturation))
        imageView.addGestureRecognizer(gestureRecognizer)
    }

    @objc func showImageWithSaturation() {
        // SimpleImageViewer를 사용하여 이미지를 보여줍니다.
        let configuration = ImageViewerConfiguration { config in
            let imageView = config.imageView
            imageView.image = self.imageView.image
            imageView.contentMode = .scaleAspectFit
            
            // 채도 조절 슬라이더를 추가합니다.
            let saturationSlider = UISlider()
            saturationSlider.minimumValue = 0
            saturationSlider.maximumValue = 2
            saturationSlider.value = 1
            saturationSlider.addTarget(self, action: #selector(self.handleSaturationSliderChange(_:)), for: .valueChanged)
            
            let sliderContainer = UIStackView(arrangedSubviews: [saturationSlider])
            sliderContainer.axis = .vertical
            sliderContainer.spacing = 10
            
            config.footerView = sliderContainer
        }
        
        let imageViewerController = ImageViewerController(configuration: configuration)
        present(imageViewerController, animated: true)
    }

    @objc func handleSaturationSliderChange(_ sender: UISlider) {
        // 이미지 채도를 조절합니다.
        let saturation = sender.value
        imageView.image = imageView.image?.withSaturation(saturation: saturation)
    }
}
```

위의 코드에서 `your_image_name` 부분을 원하는 이미지의 이름으로 변경해주세요. 채도 조절 기능은 이미지를 클릭했을 때 실행되며, 이미지를 화면에 보여주고 채도 조절 슬라이더를 추가합니다. 채도 슬라이더의 `handleSaturationSliderChange` 메서드에서 이미지의 채도를 조절합니다.

## 3. 실행하기

위의 코드를 작성한 후에 앱을 실행해보세요. 이미지를 클릭하면 채도 조절 슬라이더가 나타나고, 슬라이더를 조절하여 이미지의 채도를 조절할 수 있습니다.

이번에는 Swift SimpleImageViewer를 사용하여 이미지의 채도를 조절하는 방법에 대해 알아보았습니다. SimpleImageViewer를 사용하면 이미지를 보여주고 다양한 기능을 추가할 수 있습니다. 추가적인 기능이나 자세한 사용법은 SimpleImageViewer의 공식 문서를 참고하시면 됩니다.

- [SimpleImageViewer GitHub](https://github.com/kentya6/SimpleImageViewer)

만약 이미지 보기 기능이 필요할 때는 SimpleImageViewer를 사용해보세요. 간단하게 이미지를 보여주며 다양한 기능을 추가할 수 있어 개발자들에게 유용한 라이브러리입니다.