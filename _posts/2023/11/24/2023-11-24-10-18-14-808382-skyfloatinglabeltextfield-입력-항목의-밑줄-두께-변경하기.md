---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 항목의 밑줄 두께 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 텍스트 입력을 위한 유용한 커스텀 텍스트 필드입니다. 이 텍스트 필드를 사용할 때 밑줄의 두께를 변경하고 싶을 수 있습니다. 이 기능을 구현하는 방법을 알아보겠습니다.

1. SkyFloatingLabelTextField를 프로젝트에 추가합니다. CocoaPods를 사용한다면 Podfile에 다음의 코드를 추가한 뒤, `pod install` 명령어를 실행합니다.

```
pod 'SkyFloatingLabelTextField'
```

2. SkyFloatingLabelTextField를 화면에 추가하고 아웃렛을 설정합니다.

```swift
@IBOutlet weak var myTextField: SkyFloatingLabelTextField!
```

3. viewDidLoad()에서 `underlineThickness` 속성을 사용하여 밑줄의 두께를 변경합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    myTextField.underlineThickness = 2.0
}
```

위 코드에서 `underlineThickness`는 밑줄의 두께를 설정하는 속성입니다. 이 값을 원하는 값으로 변경하여 사용하면 됩니다.

## 추가적인 설정

SkyFloatingLabelTextField에는 다양한 다른 설정 옵션이 있습니다. 필요한 경우 [공식 문서](https://github.com/Skyscanner/SkyFloatingLabelTextField/blob/master/README.md)를 참조하여 원하는 설정을 적용할 수 있습니다.

이제 SkyFloatingLabelTextField의 입력 항목의 밑줄 두께를 변경하는 방법에 대해 알아보았습니다. 이를 통해 iOS 앱의 텍스트 필드를 더욱 다양하게 커스텀할 수 있습니다.