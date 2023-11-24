---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 포커스 해제 이벤트 감지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift로 개발된 사용자 정의 텍스트 필드입니다. 입력 포커스가 해제되는 이벤트를 감지하고 해당 이벤트에 대한 동작을 수행하려면 UITextFieldDelegate 프로토콜을 구현해야 합니다.

먼저, 해당 컨트롤러에 UITextFieldDelegate 프로토콜을 추가해야 합니다. 이를 위해 컨트롤러의 클래스 선언 부분에 UITextFieldDelegate를 추가하겠습니다.

```swift
class YourViewController: UIViewController, UITextFieldDelegate {
    // ...
}
```

이제 UITextFieldDelegate 프로토콜의 textFieldDidEndEditing(_:) 메서드를 구현하여 입력 포커스가 해제되는 이벤트를 감지할 수 있습니다.

```swift
func textFieldDidEndEditing(_ textField: UITextField) {
    if let floatingLabelTextField = textField as? SkyFloatingLabelTextField {
        // 입력 포커스 해제 이벤트에 대한 동작 수행
        // 예를 들어, 입력값 유효성 검사 등을 수행할 수 있습니다.
    }
}
```

textFieldDidEndEditing(_:) 메서드는 텍스트 필드가 편집 모드에서 벗어날 때 자동으로 호출되는 메서드입니다. 이를 활용하여 입력 포커스 해제 이벤트를 감지하고 원하는 동작을 수행할 수 있습니다.

이제 SkyFloatingLabelTextField에서 입력 포커스 해제 이벤트를 감지하는 방법에 대해 알게 되었습니다. 필요한 경우 위의 코드를 사용하여 입력 포커스 해제 이벤트에 대한 원하는 동작을 구현하면 됩니다.

더 자세한 내용은 [SkyFloatingLabelTextField 공식 GitHub 저장소](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참조하시기 바랍니다.