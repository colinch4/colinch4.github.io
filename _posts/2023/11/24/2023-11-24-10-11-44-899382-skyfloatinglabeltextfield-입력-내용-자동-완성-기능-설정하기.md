---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 내용 자동 완성 기능 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 유저가 입력한 내용을 보다 시각적으로 표현해주는 커스텀 텍스트 필드입니다. 이번에는 SkyFloatingLabelTextField에 자동 완성 기능을 추가하는 방법에 대해 알아보겠습니다.

## 1. 자동 완성 데이터 준비하기

먼저, 자동 완성 기능을 제공하기 위해 필요한 데이터를 준비해야 합니다. 보통은 배열이나 딕셔너리 등의 데이터 구조를 사용합니다. 예를 들어, 카테고리명을 자동 완성 기능으로 제공하려면 아래와 같이 데이터를 구성할 수 있습니다.

```swift
let categories = ["Apple", "Banana", "Orange", "Pineapple"]
```

## 2. SkyFloatingLabelTextField 설정하기

SkyFloatingLabelTextField를 설정하여 자동 완성 기능을 구현할 수 있습니다. 코드 예시는 아래와 같습니다.

```swift
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))

// 자동 완성 기능을 제공할 데이터를 설정합니다.
textField.autoCompleteDataSource = categories

// 자동 완성 기능 활성화를 설정합니다.
textField.autoCompleteEnabled = true

// 자동 완성 기능에서 보여질 결과 개수를 설정합니다. 기본값은 5입니다.
textField.maximumAutoCompleteCount = 10

// 자동 완성 기능에서 결과를 보여줄 때 사용하는 셀의 클래스를 설정합니다. 기본값은 `AutoCompleteTableViewCell`입니다.
textField.cellHeight = 40
```

위 코드에서 `textField.autoCompleteDataSource`에 자동 완성 기능을 제공할 데이터를 설정해야 합니다. 그리고 `textField.autoCompleteEnabled`를 true로 설정하여 자동 완성 기능을 활성화합니다. `textField.maximumAutoCompleteCount`로 자동 완성 결과에서 보여질 최대 개수를 지정할 수 있습니다.

## 3. 자동 완성 기능 처리하기

SkyFloatingLabelTextField에서 자동 완성 기능 처리를 위해 아래 메서드를 구현할 수 있습니다.

```swift
func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
    // 현재 입력한 텍스트를 가져옵니다.
    let currentText = (textField.text as NSString?)?.replacingCharacters(in: range, with: string) ?? ""
    
    // 자동 완성 기능을 제공할 데이터를 가져옵니다.
    let autoCompleteData = categories.filter { $0.localizedCaseInsensitiveContains(currentText) }
    
    // 자동 완성 기능을 처리합니다.
    textField.autoCompleteStrings = autoCompleteData
    
    return true
}

func textFieldShouldReturn(_ textField: UITextField) -> Bool {
    // 자동 완성 결과 중 선택한 값을 가져와 처리합니다.
    if let selectedValue = textField.autoCompleteSelectedItem {
        // 선택한 값을 텍스트 필드에 설정합니다.
        textField.text = selectedValue
    }
    
    // 키보드를 숨깁니다.
    textField.resignFirstResponder()
    
    return true
}
```

위 코드에서 `textField(_:shouldChangeCharactersIn:replacementString:)` 메서드는 유저가 텍스트를 입력할 때마다 호출됩니다. 이 메서드에서는 현재 입력된 텍스트를 가져와 `autoCompleteDataSource`에서 일치하는 결과를 필터링하여 `autoCompleteStrings`에 대입하여 자동 완성 결과를 보여줍니다.

`textFieldShouldReturn` 메서드는 리턴 키가 눌렸을 때 호출되며, 선택한 자동 완성 값을 텍스트 필드에 설정합니다. 그리고 키보드를 숨깁니다.

## 참고 링크

- [SkyFloatingLabelTextField GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [SkyFloatingLabelTextField 사용법](https://medium.com/@hydroponics1111/skyfloatinglabeltextfield-55f6a3fd0fb7)