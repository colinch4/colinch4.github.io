---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 내용 삭제하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 입력 필드에 라벨과 함께 부드러운 애니메이션을 제공하는 좋은 라이브러리입니다. 사용자가 입력한 내용을 삭제하는 방법에 대해 알아보겠습니다.

먼저, SkyFloatingLabelTextField를 프로젝트에 추가해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음 코드를 추가하고 `pod install`을 실행하여 라이브러리를 설치합니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

인터페이스 빌더(XIB 또는 Storyboard)를 사용하는 경우, UITextField 대신 SkyFloatingLabelTextField로 필드를 추가할 수 있습니다. 

그런 다음, 코드에서 해당 필드에 접근하여 입력 내용을 삭제할 수 있습니다. SkyFloatingLabelTextField는 UITextField의 하위 클래스이므로 UITextField의 기능을 그대로 사용할 수 있습니다.

다음은 입력 내용을 삭제하는 예시 코드입니다.

```swift
import SkyFloatingLabelTextField

// SkyFloatingLabelTextField에 접근하여 입력 내용을 삭제하는 함수
func clearTextFieldContent() {
    // textField는 SkyFloatingLabelTextField 인스턴스여야 함
    if let textField = textField as? SkyFloatingLabelTextField {
        textField.text = ""
        textField.selectedTitle = ""
        textField.title = ""
        textField.errorMessage = ""
    }
}
```

위의 코드에서 `clearTextFieldContent()` 함수를 사용하여 입력 내용을 삭제할 수 있습니다. 해당 함수에서 `textField`는 `SkyFloatingLabelTextField` 인스턴스여야 합니다.

함수를 호출하여 입력 필드의 내용을 삭제할 수 있습니다. 예를 들어, 버튼의 액션 메서드에서 `clearTextFieldContent()` 함수를 호출하여 입력 필드의 내용을 삭제할 수 있습니다.

```swift
@IBAction func clearButtonTapped(_ sender: Any) {
    clearTextFieldContent()
}
```

위의 코드는 `clearButtonTapped(_:)` 메서드가 활성화된 버튼을 선택할 때 호출되어 입력 필드의 내용을 삭제합니다.

이제 SkyFloatingLabelTextField의 입력 내용을 삭제하는 방법을 알게 되었습니다. 해당 라이브러리를 사용하면 사용자 친화적인 입력 필드를 쉽게 만들 수 있습니다.

## 참고 자료
- [SkyFloatingLabelTextField GitHub 리포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)