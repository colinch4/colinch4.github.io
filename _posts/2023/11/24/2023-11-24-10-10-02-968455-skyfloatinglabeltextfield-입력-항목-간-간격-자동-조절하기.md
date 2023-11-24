---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 항목 간 간격 자동 조절하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 글에서는 iOS 앱 개발 시 자주 사용되는 SkyFloatingLabelTextField의 입력 항목 간 간격 조절에 대해 알아보겠습니다.

SkyFloatingLabelTextField는 텍스트 입력 필드와 그 위에 있는 라벨이 함께 있는 커스텀 뷰입니다. 사용자가 텍스트를 입력하면 라벨이 위로 올라가서 입력 내용을 표시해주는 효과를 가지고 있습니다.

## 문제 상황

기본적으로 SkyFloatingLabelTextField는 입력 필드와 라벨 사이에 4포인트의 간격을 가지고 있습니다. 그러나 때로는 이 간격이 좁아서 사용자가 입력 내용을 올바르게 읽지 못할 수 있습니다. 입력 항목 간의 간격을 자동으로 조절하여 사용자가 쉽게 입력할 수 있도록 해야 합니다.

## 해결 방법

SkyFloatingLabelTextField의 입력 항목 간 간격을 자동으로 조절하기 위해 아래와 같은 코드를 사용할 수 있습니다.

```swift
extension SkyFloatingLabelTextField {
    open override func textRect(forBounds bounds: CGRect) -> CGRect {
        let rect = super.textRect(forBounds: bounds)
        return rect.insetBy(dx: 0, dy: 8)
    }

    open override func editingRect(forBounds bounds: CGRect) -> CGRect {
        let rect = super.editingRect(forBounds: bounds)
        return rect.insetBy(dx: 0, dy: 8)
    }
}
```

위 코드는 SkyFloatingLabelTextField를 상속받아서 `textRect(forBounds:)`와 `editingRect(forBounds:)` 메서드를 오버라이드합니다. 각각의 메서드는 입력 필드의 프레임을 조정하여 입력 항목 간의 간격을 조절합니다. 

인셋 값을 조정하여 입력 필드와 라벨 사이의 원하는 간격을 설정할 수 있습니다. 위 예제 코드에서는 8포인트의 간격을 설정하였습니다.

## 사용 예제

```swift
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))
textField.placeholder = "이름"
textField.title = "이름"
textField.font = UIFont.systemFont(ofSize: 14)

// 입력 항목 간 간격 설정
textField.spaceBetweenTextFieldAndLabel = 8

self.view.addSubview(textField)
```

위 예제 코드에서는 `textField.spaceBetweenTextFieldAndLabel` 속성을 사용하여 입력 필드와 라벨 사이의 간격을 설정할 수 있습니다. 값을 조정하여 원하는 간격으로 설정할 수 있습니다.

## 결론

이번 글에서는 SkyFloatingLabelTextField의 입력 항목 간 간격을 자동으로 조절하는 방법에 대해 알아보았습니다. 입력 필드와 라벨 사이의 간격을 조정하여 사용자가 편리하게 입력할 수 있도록 해줍니다. 이 기능을 사용하여 사용자 인터페이스를 개선하고 사용자 경험을 향상시킬 수 있습니다.

참고 링크:
- [SkyFloatingLabelTextField 소스 코드](https://github.com/Skyscanner/SkyFloatingLabelTextField)