---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UITextField에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

`UITextField`는 iOS 앱에서 텍스트를 입력받을 수 있는 UI 컴포넌트입니다. 이 컴포넌트를 사용할 때, 사용자가 텍스트 필드를 터치할 때마다 원하는 동작을 처리하고 싶을 수 있습니다. 이를 위해 `UIResponder` 프로토콜의 메서드를 사용하여 터치 이벤트를 처리할 수 있습니다.

## UIResponder 개요
`UIResponder`는 iOS에서 이벤트를 처리할 수 있는 추상 클래스입니다. `UIResponder`를 상속받은 클래스는 사용자의 터치 이벤트를 받을 수 있고, 필요한 작업을 수행할 수 있습니다. `UIResponder`를 상속받은 클래스는 `canBecomeFirstResponder` 메서드를 오버라이드하여 터치 이벤트를 받을 수 있는지를 결정할 수 있습니다.

## UITextField에서 UIResponder 사용하기
UITextField에서 UIResponder를 사용하여 터치 이벤트를 처리하려면 다음과 같은 단계를 따를 수 있습니다.

1. `UITextFieldDelegate` 프로토콜을 구현한 클래스를 정의합니다.
2. 해당 클래스에서 `UITextField` 인스턴스의 delegate를 설정합니다.
3. UIResponder 메서드를 오버라이드하여 사용자의 터치 이벤트를 처리합니다.

```swift
class MyTextFieldDelegate: NSObject, UITextFieldDelegate {

    func textFieldDidBeginEditing(_ textField: UITextField) {
        // 텍스트 필드가 편집 상태로 전환될 때 호출됩니다.
        // 원하는 작업을 수행합니다.
    }

    func textFieldDidEndEditing(_ textField: UITextField) {
        // 텍스트 필드의 편집이 종료될 때 호출됩니다.
        // 원하는 작업을 수행합니다.
    }

    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        // 리턴 키를 눌렀을 때 호출됩니다.
        // 원하는 작업을 수행하고, 키보드를 내릴지 결정합니다.
        return true
    }
}

let myTextField = UITextField()
let delegate = MyTextFieldDelegate()
myTextField.delegate = delegate
```

위의 예제에서는 `MyTextFieldDelegate` 클래스가 `UITextFieldDelegate` 프로토콜을 구현하고 있습니다. 이 클래스의 인스턴스를 `UITextField` 인스턴스의 delegate로 설정하면 해당 텍스트 필드의 터치 이벤트를 처리할 수 있습니다.

`UITextFieldDelegate`의 메서드 중 일부인 `textFieldDidBeginEditing`, `textFieldDidEndEditing`, `textFieldShouldReturn`은 텍스트 필드의 편집이 시작될 때, 종료될 때, 또는 리턴 키를 눌렀을 때 호출됩니다. 이 메서드들을 오버라이드하여 원하는 동작을 구현할 수 있습니다.

참고 자료:
- [UITextFieldDelegate - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextfielddelegate)
- [UIResponder - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiresponder)
- [UITextField - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextfield)