---
layout: post
title: "[swift] SkyFloatingLabelTextField 텍스트 변경 이벤트 감지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## SkyFloatingLabelTextField 텍스트 변경 이벤트 감지하기

SkyFloatingLabelTextField는 사용자에게 입력 필드에 대한 라벨과 힌트를 제공합니다. 이 기능을 통해 텍스트를 변경할 때마다 특정 이벤트를 감지하고자 하는 경우가 있을 수 있습니다.

```swift
import SkyFloatingLabelTextField

class ViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 텍스트 필드의 델리게이트 설정
        textField.delegate = self

        // 텍스트 변경 이벤트를 감지할 수 있도록 addTarget을 사용하여 textFieldDidChange 메서드를 등록
        textField.addTarget(self, action: #selector(textFieldDidChange(_:)), for: .editingChanged)
    }

    @objc func textFieldDidChange(_ textField: UITextField) {
        // 텍스트 필드의 내용이 변경되었을 때 호출되는 메서드
        if let text = textField.text {
            print("입력된 텍스트: \(text)")
        }
    }
    
    // UITextFieldDelegate를 구현한 경우 키보드의 "완료" 버튼을 누르면 호출되는 메서드
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder() // 키보드 감추기
        return true
    }
}
```

위의 예제에서는 SkyFloatingLabelTextField의 텍스트 값이 변경될 때마다 `textFieldDidChange(_:)` 메서드가 호출됩니다. 해당 메서드 내부에서 텍스트 필드의 입력된 텍스트를 가져와 출력합니다.

또한, `textFieldShouldReturn(_:)` 메서드를 사용하면 키보드의 "완료" 버튼을 누를 때 키보드를 감출 수 있습니다.

이를 활용하여 SkyFloatingLabelTextField의 텍스트 변경 이벤트를 감지하고 필요한 동작을 수행할 수 있습니다.

## 참고 자료
- [SkyFloatingLabelTextField 공식 Github](https://github.com/Skyscanner/SkyFloatingLabelTextField)