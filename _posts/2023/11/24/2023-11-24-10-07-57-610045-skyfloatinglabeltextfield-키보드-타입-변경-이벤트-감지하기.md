---
layout: post
title: "[swift] SkyFloatingLabelTextField 키보드 타입 변경 이벤트 감지하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift 언어로 작성된 유명한 텍스트 필드 라이브러리입니다. 이 라이브러리는 사용자가 입력하는 텍스트를 표시하고, 키보드 타입을 제어하는데 사용할 수 있습니다. 이번 블로그 포스트에서는 SkyFloatingLabelTextField에서 키보드 타입 변경 이벤트를 감지하는 방법에 대해 알아보겠습니다.

## 1. UITextFieldDelegate 채택하기

SkyFloatingLabelTextField는 UITextField를 상속한 클래스이므로 UITextFieldDelegate 프로토콜을 채택하여 키보드 타입 변경 이벤트를 감지할 수 있습니다. 먼저 UITextFieldDelegate 프로토콜을 채택하기 위해 클래스 정의에 다음과 같이 추가합니다.

```swift
class ViewController: UIViewController, UITextFieldDelegate {
  // ...
}
```

## 2. delegate 설정하기

다음으로 SkyFloatingLabelTextField 인스턴스를 생성한 후 delegate를 설정해야 합니다. 일반적으로는 `viewDidLoad` 메서드에서 설정하는 것이 좋습니다.

```swift
override func viewDidLoad() {
  super.viewDidLoad()

  let textField = SkyFloatingLabelTextField()
  textField.delegate = self

  // ...
}
```

## 3. textField(_:shouldChangeCharactersIn:replacementString:) 메서드 구현하기

이제 UITextFieldDelegate 프로토콜의 `textField(_:shouldChangeCharactersIn:replacementString:)` 메서드를 구현하여 키보드 타입 변경 이벤트를 감지할 수 있습니다. 해당 메서드는 사용자가 텍스트를 입력, 삭제 또는 변경할 때마다 호출됩니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
  // 키보드 타입 변경 이벤트 처리
  // ...

  return true
}
```

## 4. 키보드 타입 변경 이벤트 처리하기

`textField(_:shouldChangeCharactersIn:replacementString:)` 메서드 내에서 키보드 타입 변경 이벤트를 처리합니다. 예를 들어, 사용자가 텍스트 필드에 숫자를 입력하고 있다면 숫자 키패드를 보여주고, 문자를 입력하고 있다면 일반 키보드를 보여줄 수 있습니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
  if let text = textField.text,
     let textRange = Range(range, in: text) {
    
    let updatedText = text.replacingCharacters(in: textRange, with: string)

    if updatedText.isEmpty {
      textField.keyboardType = .default
    } else if updatedText.isNumeric() {
      textField.keyboardType = .numberPad
    } else {
      textField.keyboardType = .default
    }
  }

  return true
}
```

## 5. 사용자 정의 함수 추가하기

코드에서 `updatedText.isNumeric()` 함수가 사용되었는데, 이 함수는 사용자 정의하셔서 숫자 여부를 판단하는 로직을 추가하면 됩니다.

```swift
extension String {
  func isNumeric() -> Bool {
    return Double(self) != nil
  }
}
```

이제 SkyFloatingLabelTextField에서 키보드 타입 변경 이벤트를 감지하고, 해당 이벤트에 대해 특정 동작을 수행할 수 있습니다.

이 블로그 포스트에서는 SkyFloatingLabelTextField를 예시로 들었지만, UITextFieldDelegate 프로토콜을 채택하는 다른 텍스트 필드에서도 동일한 방법으로 키보드 타입 변경 이벤트를 감지할 수 있습니다.

## 참고 자료

- [SkyFloatingLabelTextField GitHub 저장소](https://github.com/Skyscanner/SkyFloatingLabelTextField)