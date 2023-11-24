---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 내용 자동 저장하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

iOS 앱 개발에서 사용되는 SkyFloatingLabelTextField는 입력 필드에 부드러운 애니메이션과 함께 라벨을 표시하는 텍스트 필드입니다. 사용자가 입력한 내용을 임시로 저장하여, 다음에 앱을 실행할 때도 이전에 입력한 내용을 보여주고 싶다면 어떻게 해야 할까요? 

이번 기술 블로그에서는 SkyFloatingLabelTextField를 사용하여 입력 내용을 자동으로 저장하고 불러오는 방법을 소개하겠습니다.

## 1. UserDefault를 통한 저장

SkyFloatingLabelTextField의 입력 내용을 저장하기 위해 UserDefault를 사용할 수 있습니다. UserDefault는 iOS 앱에서 작은 데이터를 저장하는 데 유용한 인터페이스입니다.

먼저, 입력 내용을 저장할 Key를 정의합니다. 예를 들어, "username"이라는 키를 사용하도록 하겠습니다.

```swift
let key = "username"
```

그런 다음 `SkyFloatingLabelTextField`의 `text` 속성을 `UserDefaults`에 저장합니다.

```swift
UserDefaults.standard.set(textField.text, forKey: key)
```

## 2. 저장된 내용 불러오기

앱을 실행할 때 저장된 내용을 불러와 `SkyFloatingLabelTextField`에 다시 표시하려면, 다음과 같이 `viewDidLoad` 메소드에서 저희가 저장한 `UserDefaults`를 다시 불러와야 합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    if let savedText = UserDefaults.standard.string(forKey: key) {
        textField.text = savedText
    }
}
```

## 3. 입력 필드 값 감지

만약 입력 필드의 값이 변경될 때마다 저장하고 싶다면, `textFieldDidChange` 메소드를 사용할 수 있습니다.

```swift
@objc func textFieldDidChange(_ textField: UITextField) {
    UserDefaults.standard.set(textField.text, forKey: key)
}
```

이제 `textFieldDidChange` 메소드를 `SkyFloatingLabelTextField`의 `editingChanged` 이벤트와 연결하면, 사용자의 입력이 변경될 때마다 값을 저장할 수 있습니다.

```swift
textField.addTarget(self, action: #selector(textFieldDidChange(_:)), for: .editingChanged)
```

이제 SkyFloatingLabelTextField의 입력 내용을 자동으로 저장하고 불러올 수 있습니다. 이를 통해 사용자는 이전에 입력한 내용을 다음에도 쉽게 찾아볼 수 있으며, 더 나은 사용자 경험을 제공할 수 있습니다.

더 자세한 사용 방법에 대해서는 [공식 문서](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참조하시기 바랍니다.

이번 기술 블로그에서는 Swift의 SkyFloatingLabelTextField를 사용하여 입력 내용을 자동으로 저장하는 방법을 알아보았습니다. 많은 사용자의 편의를 위해 이와 같은 기능을 구현해 보세요!