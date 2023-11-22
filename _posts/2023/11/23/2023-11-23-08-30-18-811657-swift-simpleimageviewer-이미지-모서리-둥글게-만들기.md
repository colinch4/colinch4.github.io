---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 모서리 둥글게 만들기"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift를 사용하여 이미지 뷰어의 이미지 모서리를 둥글게 만드는 방법에 대해 알아보겠습니다.

## UIImageView의 layer 속성 사용하기

UIImageView의 둥글게 만들기 기능을 구현하기 위해서는 UIImageView의 layer 속성을 사용해야 합니다. layer는 UIView의 하위레벨에서 그래픽을 그리는데 사용되며, 모양, 그림자, 애니메이션 등을 쉽게 제어할 수 있습니다.

```swift
let imageView = UIImageView(image: UIImage(named: "exampleImage"))
imageView.layer.cornerRadius = 10
imageView.layer.masksToBounds = true
```

위의 코드에서는 UIImageView를 생성한 후, layer의 cornerRadius 속성을 사용하여 모서리를 둥글게 만들었습니다. cornerRadius 속성에 값을 할당하여 얼마나 둥글게 만들지를 조절할 수 있습니다. 또한, layer의 masksToBounds 속성을 true로 설정하여 이미지를 둥글게 만드는 동시에 내부를 잘라내도록 설정했습니다.

## UIImageView Extension으로 둥글게 만들기 기능 추가하기

같은 기능을 다른 이미지뷰에서도 사용할 수 있도록 하기 위해 UIImageView Extension을 작성해보겠습니다.

```swift
extension UIImageView {
    func makeRounded() {
        self.layer.cornerRadius = self.frame.width / 2
        self.layer.masksToBounds = true
    }
}
```

위의 코드에서는 UIImageView를 확장하여 makeRounded라는 메서드를 추가했습니다. makeRounded 메서드 내에서는 frame의 너비를 이용하여 이미지뷰를 원형으로 만들도록 설정했습니다.

이제 이미지뷰어에서 다음과 같이 makeRounded 메서드를 호출하여 이미지 모서리를 둥글게 만들 수 있습니다.

```swift
let imageView = UIImageView(image: UIImage(named: "exampleImage"))
imageView.makeRounded()
```

## 마무리

지금까지 Swift를 사용하여 이미지 뷰어의 이미지 모서리를 둥글게 만드는 방법에 대해 알아보았습니다. UIImageView의 layer 속성을 활용하여 모서리를 둥글게 만들 수 있으며, UIImageView Extension을 통해 코드를 간결하게 관리할 수도 있습니다. 이를 참고하여 UI를 보다 예쁘게 꾸미는데 활용해보시기 바랍니다.

관련 참고 자료:
- [UIImageView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimageview)
- [CALayer - Apple Developer Documentation](https://developer.apple.com/documentation/quartzcore/calayer)