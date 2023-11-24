---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 내용을 복사하기 전 확인하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

`SkyFloatingLabelTextField`는 iOS 앱에서 사용되는 텍스트 필드 컴포넌트입니다. 이 텍스트 필드에서 사용자가 입력한 내용을 복사하기 전에 확인하는 방법에 대해 알아보겠습니다.

## 1. UITextFieldDelegate를 구현하기

`SkyFloatingLabelTextField`는 `UITextFieldDelegate` 프로토콜을 구현하여 텍스트 필드의 이벤트를 처리할 수 있습니다. 우선, 해당 프로토콜을 구현하기 위해 다음과 같이 클래스를 선언합니다.

```swift
class ViewController: UIViewController, UITextFieldDelegate {
    // ...
}
```

## 2. shouldChangeCharactersIn 메서드 사용하기

`UITextFieldDelegate` 프로토콜의 `shouldChangeCharactersIn` 메서드를 사용하여 텍스트 필드의 내용이 변경될 때마다 확인하는 로직을 작성합니다. 다음은 이를 구현하는 예제 코드입니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    // 변경된 텍스트
    let updatedText = (textField.text as NSString?)?.replacingCharacters(in: range, with: string) ?? ""
    
    // 변경된 텍스트를 확인하는 로직 추가
    if shouldCopyText(updatedText) {
        // 텍스트 복사하기
        UIPasteboard.general.string = updatedText
    }
    
    return true
}

func shouldCopyText(_ text: String) -> Bool {
    // 텍스트를 확인하는 로직을 작성합니다.
    // 예를 들어, 특정 조건을 만족할 때만 복사하도록 설정할 수 있습니다.
    // 이 예제에서는 텍스트의 길이가 5 이상인 경우에만 복사하도록 설정합니다.
    return text.count >= 5
}
```

위의 코드에서 `shouldCopyText(_:)` 메서드는 변경된 텍스트를 확인하는 로직을 작성하는 부분입니다. 이 예제에서는 텍스트의 길이가 5 이상인 경우에만 복사하도록 설정하였습니다. 따라서 입력된 텍스트가 5글자 이상인 경우에는 사용자가 복사 버튼을 누르지 않아도 자동으로 복사가 이루어집니다.

## 3. UITextFieldDelegate 설정하기

마지막으로, `SkyFloatingLabelTextField`의 delegate를 설정하여 사용자의 입력을 감지할 수 있도록 합니다. 뷰 컨트롤러에서 `viewDidLoad` 메서드 내에서 다음과 같이 설정합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // 텍스트 필드의 delegate 설정
    textField.delegate = self
}
```

위의 코드에서 `textField`는 `SkyFloatingLabelTextField`의 인스턴스를 나타냅니다.

이제, 사용자가 `SkyFloatingLabelTextField`에 텍스트를 입력하고 다른 곳으로 이동하거나 입력 내용을 변경하면, 입력 내용이 복사되기 전에 확인하는 로직이 실행됩니다.