---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 삭제 이벤트 감지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS에서 유용하게 사용할 수 있는 사용자 정의 텍스트 필드입니다. 이 텍스트 필드에서 입력한 텍스트가 삭제되는 이벤트를 감지하고 싶다면, 아래의 내용을 참고해주세요.

## 1. 델리게이트 설정

먼저, SkyFloatingLabelTextFieldDelegate 프로토콜을 채택한 후 해당 델리게이트를 SkyFloatingLabelTextField 인스턴스에 설정해야 합니다. 아래의 코드는 ViewController 클래스에서 SkyFloatingLabelTextFieldDelegate를 채택하는 예시입니다.

```swift
class ViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {
    // ...
    
    func setupTextField() {
        let textField = SkyFloatingLabelTextField(frame: CGRect(x: 50, y: 100, width: 200, height: 50))
        textField.delegate = self
        
        // 텍스트 필드 설정 코드...
        
        view.addSubview(textField)
    }
    
    // ...
}
```

## 2. 삭제 이벤트 감지하기

SkyFloatingLabelTextFieldDelegate 프로토콜을 채택한 후 아래의 메서드를 구현하면, 입력한 텍스트의 삭제 이벤트를 감지할 수 있습니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    if range.length == 1 && string.isEmpty {
        // 입력한 텍스트가 삭제되는 이벤트 감지
        print("텍스트가 삭제되었습니다.")
    }
    
    return true
}
```

위의 코드에서 `textField(_:shouldChangeCharactersIn:replacementString:)` 메서드의 인자인 `range.length`가 1이고, `string.isEmpty`가 true이면 입력한 텍스트가 삭제되는 이벤트를 감지할 수 있습니다.

## 3. 전체 코드 예시

아래의 코드는 SkyFloatingLabelTextField에서 입력한 텍스트가 삭제되는 이벤트를 감지하여 "텍스트가 삭제되었습니다."를 출력하는 예시입니다.

```swift
import UIKit
import SkyFloatingLabelTextField

class ViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupTextField()
    }
    
    func setupTextField() {
        let textField = SkyFloatingLabelTextField(frame: CGRect(x: 50, y: 100, width: 200, height: 50))
        textField.delegate = self
        
        textField.placeholder = "텍스트 입력"
        textField.tintColor = .blue
        
        view.addSubview(textField)
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        if range.length == 1 && string.isEmpty {
            print("텍스트가 삭제되었습니다.")
        }
        
        return true
    }
}
```

위의 코드를 사용하면 SkyFloatingLabelTextField에서 입력한 텍스트가 삭제될 때마다 "텍스트가 삭제되었습니다."를 출력할 수 있습니다.

텍스트 필드의 설정은 필요에 따라 자유롭게 변경하실 수 있습니다.

## 참고 자료

- [SkyFloatingLabelTextField GitHub Repository](https://github.com/marcelofabri/SkyFloatingLabelTextField)