---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용 복사하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 [SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 사용하여 입력한 텍스트 내용을 복사하는 방법에 대해 알아보겠습니다. 

## 복사 기능 구현

```swift
import SkyFloatingLabelTextField

class TextFieldViewController: UIViewController {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // textField 설정
        
        // 우측에 복사 버튼 추가
        let copyButton = UIButton(type: .custom)
        copyButton.setImage(UIImage(systemName: "doc.on.doc"), for: .normal)
        copyButton.addTarget(self, action: #selector(copyText), for: .touchUpInside)
        textField.rightView = copyButton
        textField.rightViewMode = .always
    }
    
    @objc func copyText() {
        guard let text = textField.text else { return }
        // 텍스트 복사
        UIPasteboard.general.string = text
        
        // 복사 완료 메시지 표시
        let alert = UIAlertController(title: "복사 완료", message: "텍스트가 복사되었습니다.", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "확인", style: .default, handler: nil))
        present(alert, animated: true, completion: nil)
    }
}
```

위 코드에서는 `SkyFloatingLabelTextField`를 사용하여 텍스트 입력 필드를 구성합니다. `viewDidLoad()`에서는 텍스트 필드 우측에 복사 버튼을 추가합니다. 복사 버튼은 `doc.on.doc` 이미지를 사용하며, 탭 동작으로 `copyText()` 메서드가 호출되도록 설정합니다.

`copyText()` 메서드에서는 텍스트를 가져와 복사하기 위해 `UIPasteboard.general.string`에 저장합니다. 그리고 복사 완료 메시지를 알림창으로 표시합니다.

## 결론

이렇게 [SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField)와 Swift를 사용하여 입력한 텍스트 내용을 복사하는 기능을 구현할 수 있습니다. 텍스트 필드 우측에 버튼을 추가하여 사용자가 텍스트를 간편하게 복사할 수 있도록 도와줍니다.