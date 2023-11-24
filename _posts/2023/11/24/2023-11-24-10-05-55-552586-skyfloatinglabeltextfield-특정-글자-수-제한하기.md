---
layout: post
title: "[swift] SkyFloatingLabelTextField 특정 글자 수 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자가 텍스트를 입력할 수 있는 TextField입니다. 이 TextField를 사용하여 사용자로부터 입력받는 글자 수를 제한하고 싶다면, 다음과 같은 방법을 사용할 수 있습니다.

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
    
    guard let text = textField.text else { return true }

    // 최대 글자 수를 10으로 제한
    let maxLength = 10
    let currentLength = text.count + string.count - range.length
    
    // 텍스트 필드에 입력된 글자 수가 최대 글자 수를 초과한 경우 입력을 막음
    return currentLength <= maxLength
  }
}
```

위의 코드에서는 `SkyFloatingLabelTextField` 객체의 `delegate`를 `ViewController`로 설정하고, `UITextFieldDelegate` 프로토콜을 구현합니다. `shouldChangeCharactersIn` 메서드에서 텍스트 필드에 텍스트가 입력될 때마다 호출되며, 이를 통해 입력된 텍스트의 길이를 제한합니다.

위의 코드는 텍스트 필드에서 입력된 텍스트의 길이가 최대 글자 수를 초과하는 경우 입력을 막습니다. 따라서, 사용자는 최대 글자 수를 초과하는 글자를 입력할 수 없습니다.

이와 같이 `SkyFloatingLabelTextField`를 사용하여 특정 글자 수를 제한하는 방법을 알아보았습니다. 해당 방법을 활용하여 원하는 길이의 텍스트를 입력받을 수 있습니다.

---

## 참고 자료
- [SkyFloatingLabelTextField GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)