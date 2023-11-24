---
layout: post
title: "[swift] SkyFloatingLabelTextField 에러 메시지 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자가 입력한 값의 유효성을 검사하고 에러 메시지를 표시하는 기능을 제공합니다. 이 기능을 사용하려면 몇 가지 단계를 따라야 합니다.

### 1. SkyFloatingLabelTextFieldDelegate 채택하기

SkyFloatingLabelTextFieldDelegate 프로토콜을 채택하여 해당 델리게이트 메소드를 구현해야 합니다.

```swift
class ViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {
    // ...
}
```

### 2. 에러 메시지 정의하기

에러 메시지를 정의하기 위해 커스텀 메소드를 추가해야 합니다. 이 메소드는 필드의 유효성을 검사하고 에러 메시지를 반환합니다.

```swift
func validateTextFieldValue(textField: SkyFloatingLabelTextField) -> String? {
    if textField.text?.isEmpty ?? false {
        return "필수 입력값입니다."
    }
    return nil
}
```

### 3. 에러 메시지 표시하기

오류 메시지를 표시하기 위해 아래의 코드를 사용할 수 있습니다. 이 코드는 필드를 검사하고, 유효하지 않은 경우 에러 메시지를 표시합니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    guard let skyTextField = textField as? SkyFloatingLabelTextField else {
        return true
    }
    
    let newString = (skyTextField.text as NSString?)?.replacingCharacters(in: range, with: string) ?? string
    let errorMessage = validateTextFieldValue(textField: skyTextField)
    
    // 에러 메시지 설정
    skyTextField.errorMessage = errorMessage
    
    return true
}
```

위의 코드를 실행하면 사용자가 올바르지 않은 입력을 하거나 필드를 빈 채로 두었을 경우, 에러 메시지가 텍스트 필드의 하단에 표시됩니다.

위의 단계를 따라서 SkyFloatingLabelTextField에서 에러 메시지를 표시할 수 있습니다. 이를 통해 사용자가 올바른 입력을 하도록 안내할 수 있습니다.

### 참고 자료

- [SkyFloatingLabelTextField GitHub 리포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)