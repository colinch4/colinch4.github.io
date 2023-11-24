---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 유효성 검사 이벤트 감지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift에서 사용할 수 있는 사용자 정의 텍스트 필드입니다. 이 텍스트 필드를 사용하면 입력한 텍스트의 유효성을 검사하고 이벤트를 감지할 수 있습니다.

## 1. SkyFloatingLabelTextField 설정

먼저, SkyFloatingLabelTextField를 설정하는 방법부터 알아보겠습니다. 

```swift
import SkyFloatingLabelTextField

let textField = SkyFloatingLabelTextField()
textField.title = "이름"
textField.placeholder = "이름을 입력하세요"
textField.delegate = self
```

위의 코드에서는 SkyFloatingLabelTextField 객체를 생성하고, 필요한 속성들을 설정하고 있습니다. title, placeholder, delegate 등을 설정하여 원하는 형태의 텍스트 필드를 만들 수 있습니다.

## 2. UITextFieldDelegate를 활용한 이벤트 감지

SkyFloatingLabelTextField에 입력한 텍스트의 유효성을 검사하기 위해서는 UITextFieldDelegate를 활용할 수 있습니다. UITextFieldDelegate는 UITextField 객체의 이벤트를 감지하는데 사용됩니다.

```swift
extension ViewController: UITextFieldDelegate {
    func textFieldDidEndEditing(_ textField: UITextField) {
        if let text = textField.text {
            if text.isEmpty {
                print("텍스트를 입력해주세요")
            } else {
                print("유효한 텍스트입니다: \(text)")
            }
        }
    }
}
```

위의 코드에서는 UITextFieldDelegate 프로토콜을 채택한 ViewController에 textFieldDidEndEditing 메서드를 구현하고 있습니다. 이 메서드는 텍스트 필드에서 편집이 끝난 후 호출되는데, 여기서 입력된 텍스트의 유효성을 검사할 수 있습니다.

이제 SkyFloatingLabelTextField에 입력된 텍스트가 유효한지 여부를 감지할 수 있는 준비가 되었습니다.

## 결론

이렇게 SkyFloatingLabelTextField를 사용하여 입력한 텍스트의 유효성을 감지하는 방법을 알아보았습니다. UITextFieldDelegate를 사용하여 편집이 끝난 후의 이벤트를 감지하고, 입력된 텍스트를 검사하여 원하는 액션을 수행할 수 있습니다.