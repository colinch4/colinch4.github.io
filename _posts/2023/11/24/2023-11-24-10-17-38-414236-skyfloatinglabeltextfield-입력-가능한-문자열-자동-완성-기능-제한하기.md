---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열 자동 완성 기능 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS에서 자주 사용되는 텍스트 필드 컴포넌트입니다. 이 컴포넌트는 사용자에게 입력 도움을 주기 위해 자동 완성 기능을 제공합니다. 하지만 때로는 입력 가능한 문자열을 제한하고 싶을 때가 있을 수 있습니다. 이번 포스트에서는 SkyFloatingLabelTextField에서 입력 가능한 문자열 자동 완성 기능을 제한하는 방법에 대해 알아보겠습니다.

## 1. UITextFieldDelegate를 구현하기

SkyFloatingLabelTextField의 입력을 제한하기 위해서는 UITextFieldDelegate를 구현해야 합니다. UITextFieldDelegate는 UITextField에서 발생하는 이벤트를 처리하기 위한 프로토콜입니다.

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        textField.delegate = self
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 입력 가능한 문자열을 제한하는 로직을 구현합니다.
        return true
    }
}
```

위의 예제에서는 ViewController가 UITextFieldDelegate를 구현하고 있으며, textField:shouldChangeCharactersIn:replacementString: 메서드를 구현하고 있습니다.

## 2. 입력 가능한 문자열 제한 로직 구현하기

textField:shouldChangeCharactersIn:replacementString: 메서드에서 입력 가능한 문자열을 제한하는 로직을 구현합니다. 예를 들어, 알파벳 대문자와 숫자만 입력 가능하도록 제한하고 싶다면 아래와 같이 구현할 수 있습니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    let allowedCharacterSet = CharacterSet(charactersIn: "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    let range = string.rangeOfCharacter(from: allowedCharacterSet.inverted)
    return range == nil
}
```

위의 예제에서는 allowedCharacterSet라는 허용된 문자 집합(CharacterSet)을 정의하고, 입력된 문자열(string)에 허용된 문자 집합을 적용하여 range를 계산합니다. range가 nil인 경우 허용된 문자열이 입력된 것이므로 true를 반환하고, 그렇지 않은 경우 false를 반환하여 입력을 제한합니다.

## 3. SkyFloatingLabelTextField에 UITextFieldDelegate 설정하기

마지막으로, SkyFloatingLabelTextField에 UITextFieldDelegate를 설정하여 입력을 제한하는 로직을 적용합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    textField.delegate = self
}
```

위의 예제에서는 viewDidLoad 메서드에서 textField의 delegate를 ViewController로 설정하고 있습니다. 이렇게 하면 TextField에서 발생하는 이벤트를 ViewController에서 처리할 수 있습니다.

이제 SkyFloatingLabelTextField에서 입력 가능한 문자열 자동 완성 기능을 제한할 수 있습니다. 만약 특정한 문자 범위를 제한하고 싶다면, allowedCharacterSet를 원하는 문자 집합으로 수정하면 됩니다.

관련 레퍼런스:
- [UITextFieldDelegate - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextfielddelegate)
- [CharacterSet - Apple Developer Documentation](https://developer.apple.com/documentation/foundation/characterset)