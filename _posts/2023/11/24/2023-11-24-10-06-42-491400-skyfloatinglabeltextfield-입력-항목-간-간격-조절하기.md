---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 항목 간 간격 조절하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자에게 입력 필드를 제공하는 데 유용한 라이브러리입니다. 이 라이브러리는 입력 필드에 부가적인 라벨을 제공하여 사용자에게 입력 필드의 목적을 알려줍니다. 이번에는 SkyFloatingLabelTextField의 입력 항목 간 간격을 조절하는 방법에 대해 알아보겠습니다.

## SkyFloatingLabelTextField 버전 확인하기
먼저, 프로젝트에 SkyFloatingLabelTextField가 설치되어 있는지 확인해야 합니다. Podfile에 다음과 같이 추가하여 SkyFloatingLabelTextField의 최신 버전을 설치할 수 있습니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

그런 다음, 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 입력 항목 간 간격 조절하기
SkyFloatingLabelTextField는 StackView를 사용하여 입력 필드를 관리합니다. StackView의 속성을 조정하여 입력 항목 간의 간격을 조절할 수 있습니다.

```swift
import UIKit
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var stackView: UIStackView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 입력 항목 간의 간격을 조절합니다.
        stackView.spacing = 10.0
    }
}
```

위의 코드에서 `stackView.spacing` 속성을 원하는 간격으로 조정하면 됩니다. 예를 들어, 10의 값을 주면 입력 항목 간의 간격이 10포인트가 됩니다.

## 추가적인 조정

SkyFloatingLabelTextField는 입력 필드와 라벨 사이의 간격을 자동으로 계산하여 적용합니다. 만약 입력 항목 간의 간격 뿐만 아니라 입력 필드와 라벨 사이의 간격 또한 조정하고 싶다면, 다음과 같이 직접 계산하여 조정할 수 있습니다.

```swift
import UIKit
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var stackView: UIStackView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 입력 필드와 라벨 사이의 간격을 조정합니다.
        for case let textField as SkyFloatingLabelTextField in stackView.arrangedSubviews {
            textField.titleLabelYPadding = -10.0
        }
    }
}
```

위의 코드에서 `titleLabelYPadding` 속성을 조정하여 입력 필드와 라벨 사이의 간격을 조절합니다. 예를 들어, `-10.0`의 값을 주면 입력 필드와 라벨 사이의 간격이 10포인트만큼 좁아집니다.

## 마치며
이제 입력 항목 간의 간격을 조절하는 방법을 알게 되었습니다. SkyFloatingLabelTextField를 사용하여 깔끔하고 사용자 친화적인 입력 필드를 만들어보세요!

---

참고 자료:
- [SkyFloatingLabelTextField GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)