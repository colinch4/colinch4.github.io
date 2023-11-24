---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트의 글자 수 카운트하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자에게 입력 필드에 대한 힌트를 제공하고 입력된 텍스트가 있는 경우 플로팅 레이블을 표시하는 기능을 제공하는 유용한 라이브러리입니다. 이 라이브러리를 사용하여 입력한 텍스트의 글자 수를 카운트하는 방법에 대해 알아보겠습니다.

먼저, `UITextFieldDelegate` 프로토콜을 채택한 후, 해당 델리게이트 메서드를 구현해야합니다. 이를 위해 아래와 같이 코드를 작성해보세요.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController, UITextFieldDelegate {
    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        textField.delegate = self
    }

    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        guard let text = textField.text else { return true }
        let newText = (text as NSString).replacingCharacters(in: range, with: string)
        let characterCount = newText.count
        
        // 글자 수를 표시하거나 다른 작업을 수행할 수 있습니다.
        print("글자 수: \(characterCount)")
        
        return true
    }
}
```

위의 코드에서 `ViewController`는 `UITextFieldDelegate` 프로토콜을 채택하고, `textField:shouldChangeCharactersIn:replacementString` 메서드를 구현합니다. 이 메서드는 사용자가 텍스트 필드에 입력하거나 삭제할 때마다 호출되며, 입력된 텍스트의 길이를 계산하여 출력합니다.

`shouldChangeCharactersIn` 메서드에서 `text` 속성을 통해 현재 텍스트 필드의 텍스트에 액세스한 다음, `NSString`의 `replacingCharacters(in:with:)` 메서드를 사용하여 새로운 텍스트를 얻습니다. 그런 다음 `count` 속성을 사용하여 새로운 텍스트의 길이를 계산합니다. 이 길이를 사용하여 원하는 작업(예: 레이블에 글자 수 표시 또는 다른 로직 수행)을 수행할 수 있습니다.

위의 코드에서는 간단히 콘솔에 글자 수를 출력했지만, 실제 애플리케이션에서는 알맞은 위치에 이 코드를 적용해야합니다.

이제 SkyFloatingLabelTextField를 사용하여 입력한 텍스트의 글자 수를 카운트하는 방법을 알게 되었습니다. 이를 활용하여 사용자가 입력한 텍스트에 대한 다양한 유효성 검사 또는 조건부 동작을 구현할 수 있습니다.

참고 링크:
- [SkyFloatingLabelTextField GitHub 리포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)