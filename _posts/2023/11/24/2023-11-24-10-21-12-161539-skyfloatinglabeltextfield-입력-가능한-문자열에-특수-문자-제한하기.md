---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열에 특수 문자 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

[![Swift Version](https://img.shields.io/badge/Swift-5.0-orange.svg)](https://swift.org/blog/swift-5-released/)

SkyFloatingLabelTextField는 매우 유용한 사용자 지정 텍스트 필드입니다. 그러나 때로는 사용자가 입력할 수 있는 문자열에 특정 제한을 두고 싶을 수 있습니다. 이 글에서는 SkyFloatingLabelTextField에 입력 가능한 문자열에 특수 문자를 제한하는 방법에 대해 알아보겠습니다.

## 시작하기 전에

이 예제에서는 Swift 5.0 버전과 SkyFloatingLabelTextField 4.0.0 버전을 기준으로 작성되었습니다. SkyFloatingLabelTextField를 설치하기 위해서는 CocoaPods나 Carthage와 같은 의존성 관리 도구를 사용할 수 있습니다. 자세한 사용법은 SkyFloatingLabelTextField GitHub 페이지를 참조하십시오.

## 특수 문자 제한을 위한 코드

아래 예제에서는 사용자가 입력할 수 있는 문자열에 특수 문자를 제한하는 방법을 보여줍니다. 특정 문자를 허용하고 싶다면 `allowedCharacterSet`에 해당 문자들을 추가하면 됩니다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()

        textField.delegate = self
    }
}

extension ViewController: UITextFieldDelegate {

    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 특수 문자를 제외한 알파벳, 숫자, 공백만 입력 가능하도록 설정
        let allowedCharacterSet = CharacterSet(charactersIn: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ").inverted
        let components = string.components(separatedBy: allowedCharacterSet)
        let filteredString = components.joined(separator: "")

        let newString = (textField.text as NSString?).replacingCharacters(in: range, with: filteredString)

        return newString.count <= 20 // 최대 20개의 문자만 입력 가능하도록 설정
    }
}
```

위의 코드는 `SkyFloatingLabelTextField`를 사용하는 `ViewController`에 구현된 예제입니다. `SkyFloatingLabelTextField`의 `delegate`를 설정하고, `shouldChangeCharactersIn` 메서드를 사용하여 입력 가능한 문자열에 특수 문자를 제한하였습니다. 허용되지 않는 문자는 `allowedCharacterSet`에 의해 제거되며, 최대 문자 길이를 제한하기 위해 `return newString.count <= 20`을 추가하였습니다.

## 결론

이 예제에서는 SkyFloatingLabelTextField에 입력 가능한 문자열에 특수 문자를 제한하는 방법에 대해 알아보았습니다. 필요에 따라 `allowedCharacterSet`을 사용하여 특정 문자나 문자열을 추가하거나 수정할 수 있습니다. SkyFloatingLabelTextField의 공식 문서와 레퍼런스를 참조하여 더 많은 기능을 익히실 수 있습니다.

## 참고 자료

- [SkyFloatingLabelTextField GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)