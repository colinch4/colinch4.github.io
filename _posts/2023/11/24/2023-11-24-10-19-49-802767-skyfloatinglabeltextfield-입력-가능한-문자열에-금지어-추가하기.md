---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열에 금지어 추가하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

# [Swift] SkyFloatingLabelTextField 입력 가능한 문자열에 금지어 추가하기

Swift를 사용하여 iOS 애플리케이션을 개발하다보면 사용자가 입력하는 문자열에 제한을 두고 싶을 때가 있습니다. 이번 포스트에서는 SkyFloatingLabelTextField를 사용하여 입력 가능한 문자열에 금지어를 추가하는 방법에 대해 알아보겠습니다.

## SkyFloatingLabelTextField 소개

SkyFloatingLabelTextField는 iOS에서 사용자가 텍스트를 입력하는 데 사용되는 텍스트 필드입니다. 이를 사용하면 텍스트 필드에 플레이스홀더, 부가적인 타이틀과 함께 스타일링된 텍스트 입력 상자를 만들 수 있습니다. 텍스트 필드에 금지어를 추가하여 사용자가 허용된 문자열만 입력할 수 있도록 할 수 있습니다.

## 금지어 제한 추가하기

첫째로, SkyFloatingLabelTextField를 프로젝트에 추가합니다. 이를 위해서는 Swift Package Manager 또는 CocoaPods를 사용할 수 있습니다. 자세한 추가 방법은 SkyFloatingLabelTextField의 공식 문서를 참조하시기 바랍니다.

텍스트 필드를 만든 후, 입력 가능한 문자열에 제한을 두고 싶다면 `UITextFieldDelegate`를 구현하여 사용자가 입력하는 텍스트를 제한할 수 있습니다. 다음은 금지어를 제한하는 예제입니다.

```swift
extension ViewController: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        guard let text = textField.text else { return true }
        
        // 금지어 배열 예시
        let forbiddenWords = ["금지어1", "금지어2", "금지어3"]
        
        let newText = (text as NSString).replacingCharacters(in: range, with: string)
        
        // 금지어가 입력되었는지 확인
        for word in forbiddenWords {
            if newText.contains(word) {
                return false
            }
        }
        
        return true
    }
}
```

위의 예제에서는 `textField(_:shouldChangeCharactersIn:replacementString:)` 메서드를 사용하여 사용자가 텍스트 필드에 문자를 입력할 때마다 호출됩니다. `newText` 변수를 사용하여 새로운 텍스트와 기존 텍스트를 비교하고, 금지어가 포함되어 있는지를 확인하는 루프를 실행합니다. 금지어가 포함되어 있다면 `false`를 반환하여 입력을 제한하고, 그렇지 않으면 `true`를 반환하여 허용합니다.

## 정리

이제 SkyFloatingLabelTextField를 사용하여 입력 가능한 문자열에 금지어를 추가하는 방법에 대해 알아보았습니다. 사용자가 원치 않는 문자열을 입력하지 못하도록 제한함으로써 애플리케이션의 보안과 품질을 향상시킬 수 있습니다.

자세한 내용은 SkyFloatingLabelTextField의 공식 문서를 참조하십시오.

---
**참고 자료:**
- [SkyFloatingLabelTextField - GitHub](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [UITextFieldDelegate - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextfielddelegate)