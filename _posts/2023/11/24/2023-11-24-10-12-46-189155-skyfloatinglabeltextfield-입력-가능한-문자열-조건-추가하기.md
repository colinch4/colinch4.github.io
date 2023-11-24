---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열 조건 추가하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 텍스트 필드를 구현하기 위해 많이 사용되는 라이브러리 중 하나입니다. 이 라이브러리를 사용하면 화려한 효과와 함께 텍스트 필드를 만들 수 있습니다.

하지만, 때로는 사용자가 입력할 수 있는 문자열을 제한하고 싶을 때가 있습니다. 예를 들어, 특정 문자나 숫자만 입력 가능하도록 제한하고 싶다면 어떻게 해야 할까요? 이번 포스트에서는 SkyFloatingLabelTextField에 입력 가능한 문자열 조건을 추가하는 방법을 알아보겠습니다.

## 1. Delegate 사용하기

SkyFloatingLabelTextField에 입력 가능한 문자열 조건을 추가하려면 먼저 UITextFieldDelegate 프로토콜을 채택하고 해당 메서드를 구현해야 합니다. 아래의 예제 코드를 참고하세요.

```swift
class ViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()

        textField.delegate = self
    }

    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 입력 가능한 문자열 조건 확인하기
        let allowedCharacterSet = CharacterSet(charactersIn: "0123456789")
        let replacementStringCharacterSet = CharacterSet(charactersIn: string)
        return allowedCharacterSet.isSuperset(of: replacementStringCharacterSet)
    }
}
```

위의 코드에서 `shouldChangeCharactersIn` 메서드는 텍스트 필드에 새로운 문자열이 입력되기 전에 호출됩니다. 해당 메서드에서는 입력 가능한 문자열의 조건을 확인한 후, `true` 또는 `false`를 반환합니다. 이를 통해 허용되지 않은 문자열이 입력되지 않도록 제어할 수 있습니다.

여기에서 `allowedCharacterSet`은 입력 가능한 문자열로 구성된 CharacterSet을 생성합니다. 위의 예제 코드에서는 "0123456789" 문자열을 입력할 수 있는 조건으로 설정되어 있습니다. 이후 `replacementStringCharacterSet`을 생성하여 새로 입력된 문자열이 `allowedCharacterSet`에 포함되는지 확인합니다. 이렇게 입력 가능한 문자열 조건을 확인하고, `true`를 반환하면 입력을 허용하고, `false`를 반환하면 입력을 거부합니다.

## 2. 사용자 피드백 제공하기

입력 가능한 문자열 조건을 추가하면 사용자가 실시간으로 입력한 문자열을 확인할 수 있습니다. 이를 통해 사용자에게 피드백을 제공하여 올바른 입력을 유도할 수 있습니다. 아래의 예제 코드에서는 SkyFloatingLabelTextField의 bottomLine의 색상을 사용자 입력에 따라 변경하는 방법을 보여줍니다.

```swift
class ViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()

        textField.delegate = self

        // 초기 피드백 색상 설정
        textField.bottomLineColor = .red
    }

    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 입력 가능한 문자열 조건 확인하기
        let allowedCharacterSet = CharacterSet(charactersIn: "0123456789")
        let replacementStringCharacterSet = CharacterSet(charactersIn: string)
        let isValid = allowedCharacterSet.isSuperset(of: replacementStringCharacterSet)

        // 입력한 문자열에 따라 피드백 색상 변경하기
        if isValid {
            textField.bottomLineColor = .green
        } else {
            textField.bottomLineColor = .red
        }

        return isValid
    }
}
```

위의 코드에서 `bottomLineColor` 속성을 사용하여 bottomLine의 색상을 변경합니다. 입력 가능한 문자열일 경우 녹색, 그렇지 않을 경우 빨강색으로 설정되어 있습니다. 이를 통해 사용자가 입력한 문자열의 유효성을 즉시 확인할 수 있습니다.

## 결론

이번 포스트에서는 SkyFloatingLabelTextField에 입력 가능한 문자열 조건을 추가하는 방법에 대해 알아보았습니다. UITextFieldDelegate 프로토콜의 메서드를 활용하여 입력 가능한 문자열 조건을 확인하고, 사용자에게 피드백을 제공할 수 있습니다. 이를 통해 사용자 입력의 유효성을 보다 쉽게 관리할 수 있습니다.

해당 내용은 아래의 공식 문서를 참고하여 작성되었습니다.

- [SkyFloatingLabelTextField - GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [UITextInputTraits - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextinputtraits)

이상으로 SkyFloatingLabelTextField에 입력 가능한 문자열 조건을 추가하는 방법에 대해 알아보았습니다. 감사합니다.