---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 모서리 둥글게 처리"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 픽셀 값을 모서리를 둥글게 처리하는 것은 시각적인 요소를 부드럽게 만들어주어 UI의 디자인을 개선하는 데 도움이 됩니다. 이번 게시물에서는 Swift에서 SimpleImageViewer를 사용하여 이미지의 픽셀 값을 모서리를 둥글게 처리하는 방법을 알아보겠습니다.

## 1. SimpleImageViewer 설치하기

SimpleImageViewer는 Swift에서 이미지를 간단하게 표시하고 처리할 수 있는 라이브러리입니다. CocoaPods를 사용하여 프로젝트에 간단하게 설치할 수 있습니다. 다음 명령어를 사용하여 Podfile을 열고 내용을 추가합니다.

```swift
pod 'SimpleImageViewer'
```

그런 다음, 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다.

```bash
pod install
```

## 2. 이미지뷰 생성하기

이제 UIViewController에 SimpleImageViewer를 사용하기 위해 UIImageView를 만들어야 합니다. 다음과 같이 UIImageView를 생성하고 원하는 이미지를 설정합니다.

```swift
import SimpleImageViewer

class ViewController: UIViewController {
    @IBOutlet weak var imageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let image = UIImage(named: "example_image")
        imageView.image = image
    }
}
```

위 예제에서는 `example_image`라는 이미지 파일을 사용하고 있습니다. 원하는 이미지를 사용하기 위해 해당 이미지 파일을 프로젝트에 추가해주세요.

## 3. 모서리를 둥글게 처리하기

이제 SimpleImageViewer를 사용하여 이미지의 픽셀 값을 모서리를 둥글게 처리해보겠습니다. UIImageView의 layer의 cornerRadius 속성을 사용하여 모서리를 둥글게 만들 수 있습니다. 이를 위해 다음과 같은 코드를 추가합니다.

```swift
import SimpleImageViewer

class ViewController: UIViewController {
    @IBOutlet weak var imageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let image = UIImage(named: "example_image")
        imageView.image = image

        imageView.layer.cornerRadius = 10
        imageView.clipsToBounds = true
    }
}
```

위 코드에서 `cornerRadius` 속성의 값으로 숫자를 변경하여 모서리의 둥글기 정도를 조절할 수 있습니다. `clipsToBounds` 속성은 이미지의 모서리를 벗어난 부분을 자르는 옵션입니다.

## 마무리

이제 SimpleImageViewer를 사용하여 이미지의 픽셀 값을 모서리를 둥글게 처리하는 방법을 알게 되었습니다. UI의 디자인을 개선하기 위해 이 요소를 활용해보세요. 이 문서에서는 Swift로의 설명을 기반으로 하였으며, 다른 프로그래밍 언어에서도 유사한 방법을 사용할 수 있습니다.

더 자세한 내용은 다음 링크를 참조하세요:
- [SimpleImageViewer](https://github.com/ningo/SimpleImageViewer)