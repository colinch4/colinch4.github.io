---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 포커스 변경 이벤트 감지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift에서 사용되는 오픈 소스 라이브러리로, 입력 필드에 라벨이 부착되어 사용자에게 더 나은 사용자 경험을 제공합니다. 이번 포스트에서는 SkyFloatingLabelTextField의 입력 포커스 변경 이벤트를 감지하는 방법에 대해 알아보겠습니다.

### SkyFloatingLabelTextFieldDelegate 사용하기

SkyFloatingLabelTextField에서 입력 포커스 변경 이벤트를 감지하기 위해서는 `SkyFloatingLabelTextFieldDelegate` 프로토콜을 사용해야 합니다. 이 프로토콜은 `textFieldDidBeginEditing` 및 `textFieldDidEndEditing` 함수를 제공합니다.

```swift
class ViewController: UIViewController, SkyFloatingLabelTextFieldDelegate {

    @IBOutlet weak var textField: SkyFloatingLabelTextField!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        textField.delegate = self
    }

    func textFieldDidBeginEditing(_ textField: UITextField) {
        // 입력 포커스가 시작되었을 때 실행되는 코드
        print("텍스트 필드에 포커스가 들어왔습니다.")
    }

    func textFieldDidEndEditing(_ textField: UITextField) {
        // 입력 포커스가 종료되었을 때 실행되는 코드
        print("텍스트 필드에서 포커스가 빠져나갔습니다.")
    }
}
```

위 예제에서는 `ViewController` 클래스가 `SkyFloatingLabelTextFieldDelegate` 프로토콜을 채택하고, `textFieldDidBeginEditing` 및 `textFieldDidEndEditing` 함수를 구현하였습니다. 이렇게 구현된 함수들은 각각 입력 포커스가 시작되거나 종료될 때 실행됩니다.

### 이벤트 처리하기

입력 포커스 변경 이벤트를 감지하여 원하는 작업을 수행할 수 있습니다. 예를 들어, 포커스가 들어왔을 때 텍스트 필드의 배경 색상을 변경하거나, 힌트 텍스트를 숨기는 등의 작업을 할 수 있습니다.

```swift
func textFieldDidBeginEditing(_ textField: UITextField) {
    textField.backgroundColor = UIColor.yellow
    textField.placeholder = ""
}

func textFieldDidEndEditing(_ textField: UITextField) {
    textField.backgroundColor = UIColor.white
    textField.placeholder = "이름을 입력하세요"
}
```

위 예제에서는 포커스가 시작될 때 텍스트 필드의 배경 색상을 노란색으로 변경하고, 힌트 텍스트를 숨깁니다. 포커스가 종료될 때는 배경 색상을 원래대로 돌리고, 힌트 텍스트를 다시 표시합니다.

### 결론

SkyFloatingLabelTextField를 사용하여 입력 포커스 변경 이벤트를 감지하고 이에 따른 작업을 수행하는 것은 매우 간단합니다. `SkyFloatingLabelTextFieldDelegate` 프로토콜을 구현하여 `textFieldDidBeginEditing` 및 `textFieldDidEndEditing` 함수를 사용하면 됩니다. 이를 통해 사용자에게 더 나은 입력 경험을 제공할 수 있습니다.

### 참고 자료

- [SkyFloatingLabelTextField GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [SkyFloatingLabelTextFieldDelegate 프로토콜 문서](https://developer.apple.com/documentation/uikit/uitextfielddelegate)