---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 내용 임시 저장하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField은 iOS에서 쉽게 사용할 수 있는 텍스트 필드 라이브러리입니다. 사용자가 텍스트 필드에 입력한 내용을 임시로 저장하고 다른 화면으로 전달해야하는 경우가 있습니다. 이번 포스트에서는 SkyFloatingLabelTextField에서 입력한 내용을 임시로 저장하는 방법에 대해 알아보겠습니다.

## 단일 뷰 컨트롤러 내에서 데이터 저장하기

만약 SkyFloatingLabelTextField가 있는 단일 뷰 컨트롤러에서 입력된 데이터를 임시로 저장하고 다른 메소드에서 사용해야한다면, 다음과 같이 변수를 선언하여 저장할 수 있습니다.

```swift
var temporaryData: String?
```

SkyFloatingLabelTextField의 delegate 메소드를 활용하여 사용자가 입력한 내용을 temporaryData에 저장할 수 있습니다.

```swift
extension ViewController: UITextFieldDelegate {
    func textFieldDidEndEditing(_ textField: UITextField) {
        if let text = textField.text {
            temporaryData = text
        }
    }
}
```

사용자가 입력을 완료하면 `textFieldDidEndEditing` 메소드가 호출되며, 해당 메소드 내에서 입력된 내용을 temporaryData에 저장합니다.

## 다른 뷰 컨트롤러로 데이터 전달하기

SkyFloatingLabelTextField에서 입력한 내용을 다른 뷰 컨트롤러로 전달해야하는 경우에도 위와 비슷한 방식으로 데이터를 저장하고 전달할 수 있습니다.

첫 번째 뷰 컨트롤러에서 데이터를 저장하기 위해 마찬가지로 변수를 선언합니다.

```swift
var temporaryData: String?
```

데이터를 다른 뷰 컨트롤러로 전달하기 위해 UIStoryboardSegue의 prepare 메소드를 사용합니다. 이 메소드는 Segue가 실행되기 전에 호출되며, 다른 뷰 컨트롤러로 데이터를 전달하는 역할을 합니다.

```swift
override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
    if segue.identifier == "showNextViewController" {
        if let nextVC = segue.destination as? NextViewController {
            nextVC.receivedData = temporaryData
        }
    }
}
```

위의 코드에서 "showNextViewController"는 Segue의 identifier입니다. 이것은 Storyboard에서 Segue에 지정한 identifier와 동일해야 합니다. 두 번째 if 조건문에서 다음 뷰 컨트롤러의 receivedData 변수에 temporaryData를 전달합니다.

## 결론

SkyFloatingLabelTextField를 사용하여 입력된 데이터를 임시로 저장하고 다른 화면으로 전달하는 방법에 대해 알아보았습니다. 단일 뷰 컨트롤러 내에서 데이터를 저장하는 방법과 다른 뷰 컨트롤러로 데이터를 전달하는 방법을 설명하였습니다. 이를 통해 사용자의 입력을 효과적으로 관리할 수 있고, 데이터의 일관성과 유효성을 유지할 수 있습니다.

---

#### 참고 링크

- [SkyFloatingLabelTextField 라이브러리](https://github.com/Skyscanner/SkyFloatingLabelTextField)
- [UITextFieldDelegate 문서](https://developer.apple.com/documentation/uikit/uitextfielddelegate)