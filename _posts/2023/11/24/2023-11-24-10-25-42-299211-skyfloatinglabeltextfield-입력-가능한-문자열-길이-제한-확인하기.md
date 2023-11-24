---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 가능한 문자열 길이 제한 확인하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서 사용하는 SkyFloatingLabelTextField는 입력 가능한 문자열의 길이를 제한하는 기능을 제공합니다. 이 기능을 사용하여 사용자가 입력한 문자열의 길이를 제한하고, 최대 입력 가능한 길이를 초과하는 경우에 대한 처리를 할 수 있습니다.

## SkyFloatingLabelTextField의 사용법

SkyFloatingLabelTextField를 사용하기 위해서는 먼저 해당 라이브러리를 프로젝트에 추가해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음과 같이 추가합니다.

```swift
pod 'SkyFloatingLabelTextField'
```

SkyFloatingLabelTextField를 사용하려는 파일에서 다음과 같이 import 문을 추가합니다.

```swift
import SkyFloatingLabelTextField
```

이제 SkyFloatingLabelTextField를 사용할 준비가 되었습니다.

## 문자열 길이 제한하기

SkyFloatingLabelTextField를 사용하여 문자열의 길이를 제한하려면 다음과 같이 코드를 작성합니다.

```swift
let textField = SkyFloatingLabelTextField()
textField.maxLength = 10
```

위의 예시에서는 `textField`라는 인스턴스를 생성하고, `maxLength` 속성을 10으로 설정하여 최대 10글자까지 입력 가능하도록 제한하였습니다.

## 입력 길이 확인하기

사용자가 입력한 문자열의 길이를 확인하려면 `textField`의 `text` 속성을 사용합니다. 다음은 입력한 문자열의 길이가 제한된 최대 길이를 초과하는지 확인하는 예시입니다.

```swift
let inputText = textField.text ?? ""
if inputText.count > textField.maxLength {
    print("입력 가능한 최대 길이를 초과하였습니다.")
}
```

위의 예시에서는 `inputText` 변수에 `textField`에 입력된 문자열을 가져온 다음, 해당 문자열의 길이가 `textField`의 `maxLength` 속성보다 큰지 확인하고, 초과하는 경우에는 메시지를 출력합니다.

## 참고 자료

- SkyFloatingLabelTextField GitHub 저장소: [https://github.com/Skyscanner/SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField)