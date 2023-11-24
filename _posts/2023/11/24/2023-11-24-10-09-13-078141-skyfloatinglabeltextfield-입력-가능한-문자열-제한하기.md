---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자에게 입력 가능한 텍스트를 제공하는 데 사용되는 도구 입니다. 사용자가 입력하는 텍스트에 대해 제한을 두고 싶을 때, 다양한 방법 중 하나는 UITextFieldDelegate 메서드를 사용하는 것입니다. 이를 통해 입력 가능한 문자열의 길이를 제한할 수 있습니다.

다음은 입력 가능한 문자열의 길이를 제한하는 방법에 대한 예시 코드 입니다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        textField.delegate = self
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        // 입력 가능한 최대 길이 설정
        let maxLength = 10
        
        // 현재 입력된 텍스트와 새로 입력되는 텍스트 조합
        let currentText = textField.text ?? ""
        let newText = (currentText as NSString).replacingCharacters(in: range, with: string)
        
        // 입력 가능한 최대 길이 보다 긴지 체크
        return newText.count <= maxLength
    }
}
```

위의 코드에서는 UITextFieldDelegate 프로토콜을 준수하기 위해 ViewController에서 UITextFieldDelegate를 상속받습니다. 그리고 viewDidLoad() 메서드에서 textField의 delegate를 ViewController로 설정합니다.

textField(_:shouldChangeCharactersIn:replacementString:) 메서드는 사용자가 텍스트를 입력할 때 호출됩니다. 이 메서드를 사용하여 사용자가 입력한 텍스트를 현재 입력된 텍스트와 조합하여 새로운 텍스트를 만들고, 이 새로운 텍스트의 길이가 입력 가능한 최대 길이인 maxLength보다 작거나 같은지 체크합니다. 그리고 이 결과를 반환하여 입력 가능 여부를 결정합니다.

이제 사용자는 textField에 입력할 수 있는 문자열의 길이가 제한된 상태에서 텍스트를 입력할 수 있습니다.

참고 문서:
- [SkyFloatingLabelTextField GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [UITextFieldDelegate 메서드](https://developer.apple.com/documentation/uikit/uitextfielddelegate)