---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 밑줄 색상 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자에게 텍스트를 입력받는데 도움을 주는 유용한 라이브러리입니다. 이 라이브러리를 사용하여 입력한 텍스트의 밑줄 색상을 변경하는 방법을 알아보겠습니다.

우선, SkyFloatingLabelTextField을 프로젝트에 추가합니다. CocoaPods를 사용하는 경우, Podfile에 다음과 같이 라이브러리를 추가합니다:

```ruby
pod 'SkyFloatingLabelTextField'
```

모듈을 불러온 다음, 새로운 SkyFloatingLabelTextField 인스턴스를 만듭니다:

```swift
import SkyFloatingLabelTextField

let textField = SkyFloatingLabelTextField()
```

텍스트 필드의 밑줄 색상을 변경하기 위해선, textField.bottomLineColor 속성을 설정해주어야 합니다. 하지만 이 속성은 textField.textColor 속성이 변경되거나 사용자 입력이 끝났을 때에만 업데이트되므로, 사용자 입력이 끝나지 않았을 때도 즉시 업데이트하려면 다음과 같이 해야합니다:

```swift
textField.addTarget(self, action: #selector(textFieldDidChange(_:)), for: .editingChanged)

@objc func textFieldDidChange(_ textField: SkyFloatingLabelTextField) {
    textField.bottomLineColor = .red
}
```

이렇게 하면 사용자가 텍스트를 입력할 때마다 밑줄 색상이 빨간색으로 변경됩니다.

위의 코드에서 .red 대신 다른 UIColor를 사용하여 원하는 색상으로 변경할 수 있습니다.

마지막으로, 텍스트 필드의 밑줄 색상을 디폴트로 되돌리기 위해, 다음과 같이 속성을 초기값으로 재설정합니다:

```swift
textField.bottomLineColor = UIColor.init(red: 0.6, green: 0.6, blue: 0.6, alpha: 1)
```

이제 SkyFloatingLabelTextField에 입력한 텍스트의 밑줄 색상을 변경하는 방법을 알게 되었습니다. 이를 응용하여 사용자에게 보다 직관적인 UI를 제공할 수 있습니다.

## 참고 자료
- [SkyFloatingLabelTextField GitHub 페이지](https://github.com/Skyscanner/SkyFloatingLabelTextField)