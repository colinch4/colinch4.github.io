---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 페이드 인/아웃 효과"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift를 사용하여 이미지 페이드 인/아웃 효과를 구현하는 방법에 대해 알아보겠습니다. 이미지 페이드 인/아웃 효과는 사용자에게 부드러운 애니메이션을 제공하여 UI를 더욱 흥미롭게 만들어줍니다.

## UIImageView와 애니메이션 속성

UIKit에서 이미지를 표시하는 가장 일반적인 방법은 UIImageView를 사용하는 것입니다. UIImageView는 UIImage를 로드하고 이를 화면에 표시하는 역할을 합니다. UIImageView의 alpha 속성을 사용하여 이미지의 투명도를 조정할 수 있으며, 애니메이션 속성을 사용하여 부드러운 페이드 인/아웃 효과를 구현할 수 있습니다.

## 이미지 페이드 인/아웃 구현

아래는 이미지 페이드 인/아웃 효과를 구현하는 간단한 예제 코드입니다. 코드를 이해하기 위해 먼저 UIImageView와 UIImage 인스턴스를 생성해야 합니다.

```swift
import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 불러오기
        let image = UIImage(named: "example_image")
        
        // ImageView에 이미지 설정
        imageView.image = image
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
        // 이미지 페이드 인 애니메이션 실행
        UIView.animate(withDuration: 1.0, delay: 0.0, options: .curveEaseInOut, animations: {
            self.imageView.alpha = 1.0
        }, completion: nil)
        
        // 이미지 페이드 아웃 애니메이션 실행
        UIView.animate(withDuration: 1.0, delay: 2.0, options: .curveEaseInOut, animations: {
            self.imageView.alpha = 0.0
        }, completion: nil)
    }
}
```

위의 코드에서, `viewDidLoad()` 메서드에서 UIImageView에 이미지를 설정하는 부분이 있습니다. 이미지를 가져와서 UIImageView의 `image` 속성에 할당합니다.

`viewDidAppear()` 메서드에서 이미지 페이드 인/아웃 애니메이션을 실행합니다. `UIView.animate(withDuration:delay:options:animations:completion:)` 메서드를 사용하여 애니메이션을 적용하며, 이미지를 서서히 나타나게 하려면 `imageView.alpha` 값을 1로 설정하고, 이미지를 서서히 사라지게 하려면 `imageView.alpha` 값을 0으로 설정합니다.

애니메이션 속성들은 주어진 시간 동안 이미지의 투명도를 변경하여 페이드 인/아웃 효과를 만들어줍니다. 위의 예제 코드에서는 1초 동안 이미지를 페이드 인 시키고, 2초 후에 1초 동안 이미지를 페이드 아웃 시킵니다.

이제 코드를 실행하면 이미지가 부드럽게 페이드 인/아웃되는 효과를 확인할 수 있습니다.

## 마치며

이번에는 Swift를 사용하여 이미지 페이드 인/아웃 효과를 구현하는 방법에 대해 알아보았습니다. UIImageView와 애니메이션 속성을 활용하여 부드러운 효과를 적용할 수 있습니다. 페이드 인/아웃 효과는 앱의 UI를 더욱 흥미롭게 만들어주는 효과적인 방법입니다.