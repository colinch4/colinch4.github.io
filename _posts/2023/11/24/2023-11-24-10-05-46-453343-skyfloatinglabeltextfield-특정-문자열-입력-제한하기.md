---
layout: post
title: "[swift] SkyFloatingLabelTextField 특정 문자열 입력 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 SwiftUI에서 사용할 수 있는 커스텀 텍스트 필드 라이브러리입니다. 이 라이브러리를 사용하면 기본 텍스트 필드보다 더 많은 커스터마이징이 가능하며, 부드러운 애니메이션과 함께 사용자 친화적인 디자인을 구현할 수 있습니다.

하지만 때로는 사용자가 입력하는 문자열을 특정 제한 조건에 맞게 제어해야하는 경우가 있습니다. 예를 들어, 사용자가 숫자만 입력하도록 제한하거나, 특정 문자열의 길이를 제한하는 등의 요구사항이 있을 수 있습니다.

이번 포스트에서는 SkyFloatingLabelTextField에서 입력되는 문자열을 제한하는 방법에 대해 알아보겠습니다.

## 1. Delegate를 구현하기

SkyFloatingLabelTextField에서 문자열 입력을 제한하려면 UITextFieldDelegate를 구현해야합니다. UITextFieldDelegate를 구현하면 입력된 문자열을 제어하고, 필요한 경우 오류 메세지를 표시할 수 있습니다.

```swift
class MyViewController: UIViewController, UITextFieldDelegate {
    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 입력 제한 로직 구현
        return true
    }
}
```

위의 예제에서는 MyViewController가 UITextFieldDelegate를 구현하고 있습니다. 또한, SkyFloatingLabelTextField의 delegate 속성을 MyViewController로 지정하고 있습니다. 이를 통해 문자열 입력 시 delegate 메서드가 호출되도록 설정할 수 있습니다.

## 2. 입력 제한 로직 구현하기

textField(_:shouldChangeCharactersIn:replacementString:) 메서드를 사용하여 입력 제한 로직을 구현할 수 있습니다. 이 메서드는 textField에 문자열이 입력될 때마다 호출되며, 이 메서드에서 입력된 문자열을 필터링하여 원하는 제한 조건에 맞지 않는 경우 입력을 막을 수 있습니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    let currentText = textField.text ?? ""
    let newText = (currentText as NSString).replacingCharacters(in: range, with: string)
    
    // 특정 문자만 입력 가능하도록 제한하는 예제
    let allowedCharacters = CharacterSet(charactersIn: "0123456789")
    let characterSet = CharacterSet(charactersIn: string)
    return allowedCharacters.isSuperset(of: characterSet) && newText.count <= 10
}
```

위의 예제에서는 입력되는 문자열이 "0123456789"에 포함된 문자인지 확인하고, newText의 길이가 10 이하인지 확인하여 입력을 제어하고 있습니다. 이 예제에서는 숫자만 입력 가능하도록 제한하고 있습니다.

## 3. 오류 메시지 표시하기

입력된 문자열이 특정 제한 조건을 만족하지 않는 경우, 사용자에게 오류 메시지를 표시할 수 있습니다. 이는 SkyFloatingLabelTextField의 errorMessage 속성을 이용하여 구현할 수 있습니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    let currentText = textField.text ?? ""
    let newText = (currentText as NSString).replacingCharacters(in: range, with: string)
    
    // 특정 문자만 입력 가능하도록 제한하는 예제
    let allowedCharacters = CharacterSet(charactersIn: "0123456789")
    let characterSet = CharacterSet(charactersIn: string)
    
    if allowedCharacters.isSuperset(of: characterSet) && newText.count <= 10 {
        textField.errorMessage = nil
        return true
    } else {
        textField.errorMessage = "숫자만 입력 가능하며, 10자 이하로 입력해주세요."
        return false
    }
}
```

위의 예제에서는 입력된 문자열이 특정 제한 조건을 만족하지 않는 경우, textField의 errorMessage에 오류 메시지를 설정하고, 입력을 막고 있습니다.

이제 SkyFloatingLabelTextField에서 문자열 입력을 특정 조건에 맞게 제어하는 방법에 대해 알아보았습니다. 사용자에게 친숙한 UI와 함께 문자열 입력을 제한할 수 있기 때문에, 사용자 경험을 향상시키는데 큰 도움이 될 것입니다.

## 참고 자료

- [SkyFloatingLabelTextField 라이브러리](https://github.com/Skyscanner/SkyFloatingLabelTextField)