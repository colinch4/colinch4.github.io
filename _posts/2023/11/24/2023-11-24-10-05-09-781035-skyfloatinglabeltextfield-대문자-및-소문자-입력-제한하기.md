---
layout: post
title: "[swift] SkyFloatingLabelTextField 대문자 및 소문자 입력 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서 SkyFloatingLabelTextField를 사용하여 대문자와 소문자 입력을 제한하는 방법에 대해 알아보겠습니다.

이 예제에서는 SkyFloatingLabelTextField를 사용하여 대문자와 소문자만 입력할 수 있는 텍스트 필드를 만들어보겠습니다. 

## 1. SkyFloatingLabelTextField 설정

먼저, SkyFloatingLabelTextField를 사용하기 위해 프로젝트에 해당 라이브러리를 추가하고, 필요한 파일을 import 해줍니다.

```swift
import SkyFloatingLabelTextField
```

## 2. 대문자 및 소문자 입력 제한

SkyFloatingLabelTextField에 대문자와 소문자 입력 제한을 설정하기 위해 UITextFieldDelegate를 구현해야 합니다. 아래의 코드를 참고하여 구현해보세요.

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    
    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        guard let textFieldText = textField.text,
              let rangeOfTextToReplace = Range(range, in: textFieldText) else {
            return false
        }
        
        let substringToReplace = textFieldText[rangeOfTextToReplace]
        let count = textFieldText.count - substringToReplace.count + string.count
        
        // 대문자와 소문자만 입력 가능하도록 제한
        let regex = try! NSRegularExpression(pattern: "^[a-zA-Z]*$")
        let matches = regex.matches(in: string, range: NSRange(0..<string.utf16.count))
        
        return matches.count > 0 && count <= 10 // 최대 10자 제한
    }
    
    // 다른 필요한 메소드들을 추가로 구현할 수 있습니다.
}
```

위의 예제에서는 `textField(_:shouldChangeCharactersIn:replacementString:)` 메소드를 구현하여 대문자와 소문자만 입력할 수 있도록 제약 조건을 설정했습니다. 정규식을 사용하여 입력한 문자열이 영문자만으로 이루어져 있는지 확인하고, 최대 글자 수 제한도 설정하였습니다.

## 3. 결과 확인

위의 코드를 사용하여 대문자와 소문자만 입력할 수 있는 SkyFloatingLabelTextField를 만들었습니다. 프로젝트를 실행하여 해당 텍스트 필드에 입력해보세요.

이제 SkyFloatingLabelTextField에서는 영문 대문자와 소문자만 입력할 수 있으며, 최대 글자 수도 제한됩니다.

## 참고 자료

- [SkyFloatingLabelTextField GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [UITextFiledDelegate - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextfielddelegate)

이제 대문자 및 소문자 입력 제한을 구현하는 데 필요한 코드를 알게 되었습니다. 위의 예제를 참고하여 프로젝트에 적용해보세요.