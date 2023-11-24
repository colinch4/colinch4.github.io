---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 유효성 검사하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 사용자로부터 입력을 받을 때 사용하는 UITextField의 서브클래스입니다. 이 컴포넌트를 사용하여 입력 필드에 유효성 검사를 적용하는 방법을 알아보겠습니다.

## 1. SkyFloatingLabelTextField 설치하기

SkyFloatingLabelTextField를 사용하기 위해서는 먼저 해당 라이브러리를 설치해야 합니다. Cocoapods를 사용한다면, Podfile에 다음과 같은 내용을 추가하고 `pod install` 명령어를 실행하세요.

```swift
pod 'SkyFloatingLabelTextField'
```

## 2. SkyFloatingLabelTextField 사용하기

SkyFloatingLabelTextField를 사용하려면, 먼저 클래스를 import하고 인스턴스를 생성해야 합니다. 

```swift
import SkyFloatingLabelTextField
```

다음은 SkyFloatingLabelTextField를 생성하고 뷰에 추가하는 예제입니다.

```swift
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 20, y: 100, width: 200, height: 50))
textField.placeholder = "이름"
self.view.addSubview(textField)
```

## 3. 유효성 검사 적용하기

SkyFloatingLabelTextField를 사용하여 입력 필드에 유효성 검사를 적용하려면, UITextFieldDelegate 프로토콜을 구현해야 합니다. 이를 위해 클래스에 UITextFieldDelegate를 추가하고, 해당 메서드를 구현합니다.

```swift
class ViewController: UIViewController, UITextFieldDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let textField = SkyFloatingLabelTextField(frame: CGRect(x: 20, y: 100, width: 200, height: 50))
        textField.placeholder = "이름"
        textField.delegate = self
        self.view.addSubview(textField)
    }
    
    func textFieldDidEndEditing(_ textField: UITextField) {
        guard let text = textField.text else {
            return
        }
        
        if text.isEmpty {
            textField.errorMessage = "이름을 입력해주세요."
        } else {
            textField.errorMessage = ""
        }
    }
}
```

위의 코드에서 `textFieldDidEndEditing` 메서드는 사용자가 입력을 끝냈을 때 호출되며, 입력값이 비어있을 경우 에러 메시지를 표시합니다. 반대로 입력값이 존재할 경우 에러 메시지를 제거합니다.

## 결론

SkyFloatingLabelTextField를 사용하면 입력 필드에 유효성 검사를 쉽게 적용할 수 있습니다. UITextFieldDelegate를 구현하여 필요한 유효성 검사 로직을 추가하면 됩니다. 이를 통해 사용자로부터 올바른 데이터를 입력받을 수 있습니다.

---

참고 링크:
- [SkyFloatingLabelTextField 라이브러리 GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)