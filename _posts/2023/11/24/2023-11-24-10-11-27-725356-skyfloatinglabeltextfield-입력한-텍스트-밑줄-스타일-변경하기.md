---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 밑줄 스타일 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 개발에서 자주 사용되는 UI 컴포넌트 중 하나입니다. 보다 편리하고 사용자 친화적인 텍스트 입력 경험을 제공하기 위해 개발되었습니다. 이 컴포넌트는 텍스트 필드에 입력한 내용을 표시하는 라벨과 함께 입력한 텍스트에 아래에 줄을 그어줍니다.

만약 SkyFloatingLabelTextField의 입력한 텍스트 밑줄 스타일을 변경하고 싶다면, 아래의 단계를 따라해보세요.

## 단계 1: SkyFloatingLabelTextFieldDelegate 설정

SkyFloatingLabelTextField를 사용하기 위해 먼저 delegate를 설정해야 합니다. ViewController 클래스에서 `UITextFieldDelegate`를 상속하고, 다음과 같이 delegate를 설정 해봅시다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var myTextField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()

        myTextField.delegate = self
    }

    // ...
}
```

## 단계 2: Delegate 메소드 구현

`UITextFieldDelegate` 프로토콜을 구현하고, `textFieldDidBeginEditing` 메소드를 사용하여 텍스트 필드가 편집될 때 밑줄의 스타일을 변경해줄 수 있습니다. 아래의 예제는 텍스트 필드가 편집될 때 밑줄 색상을 빨간색으로 변경해주는 코드입니다.

```swift
func textFieldDidBeginEditing(_ textField: UITextField) {
    if let floatingTextField = textField as? SkyFloatingLabelTextField {
        floatingTextField.lineColor = .red
    }
}
```

위의 코드에서 `lineColor` 속성을 변경하여 밑줄의 색상을 원하는 색으로 설정할 수 있습니다. 다른 스타일 변경을 원하는 경우에는 해당 속성을 사용하여 변경하면 됩니다.

## 단계 3: 다른 스타일 변경

SkyFloatingLabelTextField에서 변경 가능한 다른 밑줄 스타일 속성은 아래와 같습니다.

- `lineColor`: 밑줄 색상 지정
- `selectedLineColor`: 선택된 상태에서의 밑줄 색상 지정
- `lineHeight`: 밑줄의 높이 조절
- `selectedLineHeight`: 선택된 상태에서의 밑줄의 높이 조절

위의 속성을 사용하여 원하는 스타일을 설정할 수 있습니다.

## 마무리
위의 단계를 따라하면 SkyFloatingLabelTextField의 입력한 텍스트의 밑줄 스타일을 변경할 수 있습니다. 다양한 속성을 사용하여 밑줄의 색상, 높이 등을 원하는 대로 변경할 수 있으니 필요에 맞게 설정해보세요.

더 자세한 내용은 [SkyFloatingLabelTextField library GitHub repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참고하십시오.