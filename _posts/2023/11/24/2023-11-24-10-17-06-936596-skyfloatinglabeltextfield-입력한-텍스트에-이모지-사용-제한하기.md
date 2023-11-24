---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트에 이모지 사용 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이모지를 입력할 수 없도록 텍스트 필드를 제한하려면 Swift에서 SkyFloatingLabelTextField을 사용할 수 있습니다. 이 텍스트 필드는 이쁜 디자인과 함께 사용자가 텍스트를 입력하는 동안 레이블이 위로 올라가는 효과를 제공합니다.

## SkyFloatingLabelTextField 설정하기

먼저, SkyFloatingLabelTextField을 설치하고 프로젝트에 추가해야합니다. [CocoaPods](https://cocoapods.org/)를 사용한다면 `Podfile`에 다음과 같이 추가하고 `pod install`을 실행해주세요.

```ruby
pod 'SkyFloatingLabelTextField'
```

프로젝트에서 필요한 파일을 import 해주세요.

```swift
import SkyFloatingLabelTextField
```

SkyFloatingLabelTextField을 생성하고 텍스트 필드의 속성을 설정해야합니다.

```swift
let textField = SkyFloatingLabelTextField()
textField.placeholder = "이모지를 입력할 수 없습니다."
textField.delegate = self // 필요한 경우 delegate를 설정해주세요
```

## 이모지 사용 제한 코드 추가하기

SkyFloatingLabelTextField의 delegate를 설정한 경우, `shouldChangeCharactersIn` 메서드를 사용하여 사용자가 입력한 텍스트에 이모지가 있는지 확인하고 제한할 수 있습니다. 이 메서드는 사용자가 텍스트를 입력, 수정 또는 삭제할 때마다 호출됩니다.

```swift
extension ViewController: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        guard let text = textField.text else { return true }
        
        // 입력한 텍스트에 이모지가 있는지 확인
        let containsEmoji = text.containsEmoji
        
        // 이모지가 있으면 입력을 제한
        if containsEmoji {
            // 이모지가 있음을 사용자에게 알리는 방법 (예시: 경고창 표시)
            let alert = UIAlertController(title: "이모지 사용 제한", message: "이모지는 사용할 수 없습니다.", preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "확인", style: .default, handler: nil))
            present(alert, animated: true, completion: nil)
        }
        
        return !containsEmoji
    }
}
```

`containsEmoji` 메서드는 입력한 텍스트에 이모지가 있는지를 확인하는 확장 기능입니다.

```swift
extension String {
    var containsEmoji: Bool {
        return unicodeScalars.contains { CharacterSet.emojiCharacters.contains($0) }
    }
}
```

이제 사용자가 이모지를 입력하면 경고창이 표시되고 이모지가 입력되지 않습니다.

## 결론

SkyFloatingLabelTextField을 사용하여 사용자가 입력한 텍스트에 이모지 사용을 제한하는 방법을 알아보았습니다. 이를 통해 안전하고 제한된 텍스트 입력을 구현할 수 있습니다.