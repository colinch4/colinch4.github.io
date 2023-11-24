---
layout: post
title: "[swift] SkyFloatingLabelTextField 커스텀 키보드 옵션 추가하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift에서 사용할 수 있는 텍스트 필드 라이브러리입니다. 기본적으로 키보드는 iOS에서 제공되는 표준 키보드를 사용하게 되는데, 때로는 특정한 사용자 요구에 맞게 커스텀 키보드를 사용해야 할 때가 있습니다. 이번 블로그 포스트에서는 SkyFloatingLabelTextField에 커스텀 키보드 옵션을 추가하는 방법에 대해 알아보겠습니다.

## 커스텀 키보드 옵션 추가하기

1. `SkyFloatingLabelTextFieldDelegate`를 구현하는 클래스를 정의합니다.

```swift
import UIKit
import SkyFloatingLabelTextField

class CustomKeyboardDelegate: NSObject, SkyFloatingLabelTextFieldDelegate {
    
    func textFieldDidBeginEditing(_ textField: SkyFloatingLabelTextField) {
        textField.inputView = createCustomKeyboard()
        textField.reloadInputViews()
    }
    
    func createCustomKeyboard() -> UIView {
        // 커스텀 키보드 뷰를 생성하고 설정합니다.
        let customKeyboardView = UIView(frame: CGRect(x: 0, y: 0, width: UIScreen.main.bounds.width, height: 200))
        customKeyboardView.backgroundColor = .white
        
        // 키보드에 필요한 버튼이나 다른 컴포넌트를 추가합니다.
        
        return customKeyboardView
    }
}
```

2. `CustomKeyboardDelegate`를 텍스트 필드의 delegate로 설정합니다.

```swift
let textField = SkyFloatingLabelTextField()
let customKeyboardDelegate = CustomKeyboardDelegate()

textField.delegate = customKeyboardDelegate
```

3. `textFieldDidBeginEditing` 메서드 내에서 커스텀 키보드를 생성하고 텍스트 필드의 `inputView`로 설정합니다. 이후 `reloadInputViews`를 호출하여 키보드를 다시 불러옵니다.

```swift
func textFieldDidBeginEditing(_ textField: SkyFloatingLabelTextField) {
    textField.inputView = createCustomKeyboard()
    textField.reloadInputViews()
}
```

4. `createCustomKeyboard` 메서드를 구현하여 원하는 커스텀 키보드 뷰를 생성하고 반환합니다. 원하는 방식으로 커스텀 키보드를 디자인하고 레이아웃을 구성합니다.

```swift
func createCustomKeyboard() -> UIView {
    // 커스텀 키보드 뷰를 생성하고 설정합니다.
    let customKeyboardView = UIView(frame: CGRect(x: 0, y: 0, width: UIScreen.main.bounds.width, height: 200))
    customKeyboardView.backgroundColor = .white
    
    // 키보드에 필요한 버튼이나 다른 컴포넌트를 추가합니다.
    
    return customKeyboardView
}
```

위와 같이 커스텀 키보드 옵션을 추가하면, `SkyFloatingLabelTextField`에서 원하는 형태의 키보드를 사용할 수 있습니다.

## 결론

이번 블로그 포스트에서는 `SkyFloatingLabelTextField`에 커스텀 키보드 옵션을 추가하는 방법을 알아보았습니다. 커스텀 키보드를 사용하면 사용자 요구에 맞게 텍스트 필드의 입력을 더욱 편리하게 할 수 있습니다.