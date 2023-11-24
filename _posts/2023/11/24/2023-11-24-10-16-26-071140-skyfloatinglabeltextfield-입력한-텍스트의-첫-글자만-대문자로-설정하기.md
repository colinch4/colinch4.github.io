---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트의 첫 글자만 대문자로 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

```swift
import UIKit
import SkyFloatingLabelTextField

class ViewController: UIViewController {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 텍스트 필드의 대문자 변환 설정
        textField.autocapitalizationType = .words
    }
    
    @IBAction func capitalizeFirstLetter(_ sender: Any) {
        guard let text = textField.text else { return }
        
        // 첫 글자를 대문자로 변환
        let capitalizedText = text.prefix(1).capitalized + text.dropFirst()
        
        // 텍스트 필드에 적용
        textField.text = capitalizedText
    }
}
```

위 코드에서, `SkyFloatingLabelTextField`을 사용하여 사용자의 입력을 받을 수 있습니다. `viewDidLoad()` 함수에서 `autocapitalizationType` 속성을 `.words`로 설정하여, 텍스트 필드에 입력한 단어의 첫 글자를 자동으로 대문자로 변환할 수 있습니다.

또한, `capitalizeFirstLetter()` 함수를 통해 텍스트 필드의 첫 글자를 대문자로 변환하여 보여줄 수 있습니다. 함수 내에서는 `text`의 첫 글자를 `capitalized` 함수를 이용하여 대문자로 변환하고, `dropFirst()` 함수를 이용하여 첫 글자를 제외한 나머지 텍스트를 가져옵니다. 이렇게 변환된 텍스트를 다시 `textField.text`에 할당하여 텍스트 필드에 보여줄 수 있습니다.

이제 첫 글자를 대문자로 변환하는 기능을 구현할 수 있는 `SkyFloatingLabelTextField`를 사용할 수 있습니다. 참고 코드와 함께 시도해보세요!