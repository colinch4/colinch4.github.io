---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 캡션 배경 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift를 사용하여 간단한 이미지 뷰어를 만들고, 이미지 캡션의 배경을 설정하는 방법에 대해 알아보겠습니다.

### 이미지 뷰어 생성

우선, `SimpleImageViewer` 클래스를 생성하고, 해당 클래스에 이미지 뷰와 캡션 라벨을 추가합니다. 다음은 해당 클래스의 초기화 메서드입니다.

```swift
import UIKit

class SimpleImageViewer: UIView {
    private let imageView: UIImageView = UIImageView()
    private let captionLabel: UILabel = UILabel()

    override init(frame: CGRect) {
        super.init(frame: frame)
        setupViews()
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    private func setupViews() {
        // 이미지 뷰 설정
        imageView.contentMode = .scaleAspectFit
        imageView.translatesAutoresizingMaskIntoConstraints = false
        addSubview(imageView)
        NSLayoutConstraint.activate([
            imageView.topAnchor.constraint(equalTo: topAnchor),
            imageView.leadingAnchor.constraint(equalTo: leadingAnchor),
            imageView.trailingAnchor.constraint(equalTo: trailingAnchor),
            imageView.heightAnchor.constraint(equalTo: heightAnchor, multiplier: 0.8)
        ])

        // 캡션 라벨 설정
        captionLabel.font = UIFont.boldSystemFont(ofSize: 16)
        captionLabel.textAlignment = .center
        captionLabel.translatesAutoresizingMaskIntoConstraints = false
        addSubview(captionLabel)
        NSLayoutConstraint.activate([
            captionLabel.topAnchor.constraint(equalTo: imageView.bottomAnchor, constant: 10),
            captionLabel.leadingAnchor.constraint(equalTo: leadingAnchor),
            captionLabel.trailingAnchor.constraint(equalTo: trailingAnchor)
        ])
    }
}
```

### 캡션 배경 설정

이제 `SimpleImageViewer` 클래스에 캡션 배경을 설정할 수 있는 메서드를 추가하겠습니다. 아래의 `setCaptionBackground` 메서드는 주어진 색상을 사용하여 캡션 라벨의 배경을 설정하는 역할을 합니다.

```swift
extension SimpleImageViewer {
    func setCaptionBackground(color: UIColor) {
        captionLabel.backgroundColor = color
    }
}
```

### 사용 예시

위에서 작성한 `SimpleImageViewer` 클래스를 사용하여 이미지 뷰어를 만들고, 캡션 배경을 설정해보겠습니다.

```swift
let imageViewer = SimpleImageViewer(frame: CGRect(x: 0, y: 0, width: 300, height: 400))
imageViewer.imageView.image = UIImage(named: "example_image")
imageViewer.captionLabel.text = "Example Caption"
imageViewer.setCaptionBackground(color: UIColor.yellow)
```

위의 예시 코드에서 `setCaptionBackground` 메서드를 사용하여 캡션 배경을 노란색으로 설정하였습니다.

### 마무리

이제 Swift로 간단한 이미지 뷰어를 만들고, 이미지 캡션의 배경을 설정하는 방법에 대해 알아보았습니다. 이를 통해 더 다양한 기능을 추가하여 실제 앱에서 이미지 뷰어를 구현해볼 수 있습니다.

---

참고: 

- [UIKit Documentation](https://developer.apple.com/documentation/uikit)
- [Swift Programming Language Guide](https://docs.swift.org/swift-book/)