---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 포커스 이벤트 감지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 개요
SkyFloatingLabelTextField는 Swift 언어로 작성된 텍스트 입력 필드 컴포넌트입니다. 이 컴포넌트는 텍스트 필드에 라벨이 부착되어 있어 사용자에게 입력 내용을 알려주는 역할을 합니다. 이번에는 SkyFloatingLabelTextField에서 입력 포커스 이벤트를 감지하는 방법에 대해 알아보겠습니다.

## SkyFloatingLabelTextFieldDelegate 사용하기
SkyFloatingLabelTextFieldDelegate 프로토콜을 사용하여 입력 포커스 이벤트를 감지할 수 있습니다. 아래와 같이 클래스에서 해당 프로토콜을 구현해야 합니다.

```swift
class ViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {
    // ...
    
    func viewDidLoad() {
        super.viewDidLoad()
        
        let textField = SkyFloatingLabelTextField(frame: CGRect(x: 100, y: 100, width: 200, height: 40))
        textField.delegate = self
        
        // ...
    }
    
    // 입력 포커스가 변경될 때 호출되는 메서드
    func textFieldDidBeginEditing(_ textField: UITextField) {
        // 포커스가 들어온 텍스트 필드에 대한 동작 구현
        print("포커스가 들어왔습니다.")
    }
    
    func textFieldDidEndEditing(_ textField: UITextField) {
        // 포커스가 나간 텍스트 필드에 대한 동작 구현
        print("포커스가 나갔습니다.")
    }
    
    // ...
}
```

SkyFloatingLabelTextFieldDelegate 프로토콜을 구현하고, textFieldDidBeginEditing(_:), textFieldDidEndEditing(_:), 등의 메서드를 구현하면 해당 메서드가 입력 포커스가 변경될 때 호출됩니다. 필요에 따라 각각의 메서드에서 특정 동작을 처리하면 됩니다.

## 참고 자료
- [SkyFloatingLabelTextField GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)