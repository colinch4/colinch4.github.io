---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 포커스 스타일 애니메이션 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

![SkyFloatingLabelTextField](https://raw.githubusercontent.com/Skyscanner/SkyFloatingLabelTextField/master/SkyFloatingLabelTextField.gif)

## 소개

SkyFloatingLabelTextField는 Swift로 작성된 라이브러리로, 입력 필드에 부가적인 기능들을 제공합니다. 이 라이브러리는 입력 필드와 그에 해당하는 라벨의 스타일과 애니메이션을 설정할 수 있게 해줍니다. 

이 글에서는 SkyFloatingLabelTextField를 사용하여 입력 포커스 스타일 애니메이션을 설정하는 방법을 알아보겠습니다.

## 설정하기

1. 먼저, [SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField) 라이브러리를 프로젝트에 추가합니다. 

2. SkyFloatingLabelTextField를 선언하고 적절한 프로퍼티들을 설정합니다. 예를 들어, 다음과 같이 설정할 수 있습니다.

```swift
let textField = SkyFloatingLabelTextField()
textField.placeholder = "이름"
textField.title = "이름"
textField.tintColor = .black
textField.selectedTitleColor = .blue
textField.lineColor = .gray
textField.selectedLineColor = .blue
```

이 코드에서, `textField`는 라벨과 연결된 입력 필드를 나타냅니다. `title`은 입력 필드 위에 표시되는 라벨의 텍스트를 설정하고, `tintColor`은 입력 필드의 색상을 설정합니다.

3. 입력 포커스에 따라 스타일을 변경하기 위해 `textField`의 `textFieldDidBeginEditing` 메서드를 구현합니다. 

```swift
func textFieldDidBeginEditing(_ textField: UITextField) {
    textField.selectedTitleColor = .green
    textField.selectedLineColor = .green
}
```

위의 코드에서, `textFieldDidBeginEditing` 메서드는 입력 포커스가 시작될 때마다 호출됩니다. 이 메서드 내에서 `selectedTitleColor`와 `selectedLineColor` 프로퍼티를 변경하여 입력 포커스 시에 표시되는 라벨의 스타일을 설정할 수 있습니다.

4. 선택이 해제되거나 다른 입력 필드를 선택한 경우에도 스타일을 변경할 수 있도록 `textFieldDidEndEditing` 메서드를 구현합니다.

```swift
func textFieldDidEndEditing(_ textField: UITextField) {
    textField.selectedTitleColor = .blue
    textField.selectedLineColor = .blue
}
```

이제, 입력 포커스가 시작되면 표시되는 라벨의 스타일이 변경되며, 선택이 해제되면 원래의 스타일로 돌아갑니다.

## 마무리

SkyFloatingLabelTextField를 사용하면 입력 필드의 스타일과 애니메이션을 쉽게 설정할 수 있습니다. 이번 글에서는 입력 포커스 스타일 애니메이션을 설정하는 방법을 소개했습니다. 추가적으로 다양한 기능들을 사용해보고 자신만의 스타일을 만들어보세요.

더 자세한 정보는 [공식 GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참조하세요.