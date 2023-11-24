---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 길이에 따라 텍스트 크기 조절하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

![SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField/raw/master/SkyFloatingLabelTextField.gif)

[SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField)는 Swift로 작성된 오픈 소스 라이브러리로, 텍스트 필드에 부가적인 라벨을 제공합니다. 이 라이브러리를 사용하면 사용자가 텍스트를 입력하거나 선택하면 라벨이 위로 올라가서 가독성을 높여줍니다.

이번에는 SkyFloatingLabelTextField를 사용하여 입력된 텍스트의 길이에 따라 텍스트 크기를 조절하는 방법에 대해서 알아보겠습니다.

## Step 1: SkyFloatingLabelTextField 추가하기
먼저, SkyFloatingLabelTextField를 프로젝트에 추가해야 합니다. CocoaPods를 사용하는 경우 `Podfile`에 다음과 같이 추가합니다.
```
pod 'SkyFloatingLabelTextField'
```
그런 다음, 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다.
```
pod install
```

## Step 2: SkyFloatingLabelTextField 생성하기
SkyFloatingLabelTextField를 사용하기 위해 먼저 텍스트 필드를 생성해야 합니다. 다음과 같이 코드를 작성하여 텍스트 필드를 생성합니다.

```swift
import SkyFloatingLabelTextField

let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 50))
```

## Step 3: 입력된 텍스트 길이에 따라 크기 조절하기
이제 입력된 텍스트의 길이에 따라 텍스트 크기를 조절하는 기능을 추가해보겠습니다. TextFieldDelegate를 사용하여 텍스트가 변경되었을 때 호출될 메서드를 구현합니다.

```swift
// TextFieldDelegate를 추가합니다.
class ViewController: UIViewController, UITextFieldDelegate {
  override func viewDidLoad() {
    super.viewDidLoad()
    
    // 텍스트 필드의 delegate를 설정합니다.
    textField.delegate = self
  }

  // TextFieldDelegate 메서드로 텍스트가 변경될 때 호출됩니다.
  func textFieldDidChangeSelection(_ textField: UITextField) {
    // 텍스트 필드의 텍스트 길이를 확인합니다.
    let textLength = textField.text?.count ?? 0
    
    // 텍스트 길이에 따라 텍스트 필드의 폰트 크기를 조절합니다.
    if textLength > 10 {
        textField.font = UIFont.systemFont(ofSize: 20)
    } else {
        textField.font = UIFont.systemFont(ofSize: 16)
    }
  }
}
```

위 예제 코드에서는 `textFieldDidChangeSelection` 메서드를 사용하여 텍스트 필드의 텍스트 변경 시 호출됩니다. 메서드 내부에서는 텍스트의 길이를 확인하고 길이에 따라서 폰트 크기를 조절하고 있습니다.

이제 텍스트 필드에 입력된 텍스트의 길이에 따라 텍스트 크기가 동적으로 변하는 기능을 구현했습니다. 원하는 조건에 맞게 폰트 크기를 변경하고, 앱의 디자인에 맞게 조정할 수 있습니다.

이상으로 SkyFloatingLabelTextField 입력 길이에 따라 텍스트 크기를 조절하는 방법에 대해 알아보았습니다. SkyFloatingLabelTextField는 유용한 기능을 제공하는 라이브러리이며, 다양한 사용 사례에 맞게 활용할 수 있습니다.

참고 자료:
- [SkyFloatingLabelTextField GitHub](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [UITextFieldDelegate Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextfielddelegate)