---
layout: post
title: "[swift] SkyFloatingLabelTextField 키보드 리턴키 동작 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 SkyFloatingLabelTextField를 사용해서 키보드의 리턴키 동작을 설정하는 방법에 대해 알아보겠습니다.

SkyFloatingLabelTextField는 iOS에서 자주 사용되는 폼 입력 컨트롤입니다. 사용자가 텍스트를 입력할 때 동적으로 레이블이 움직이는 효과를 주어 사용성을 높일 수 있습니다.

## 1. SkyFloatingLabelTextField 라이브러리 설치하기

먼저, SkyFloatingLabelTextField를 프로젝트에 추가해야 합니다. 

1. Cocoapods를 사용하는 경우, Podfile에 다음과 같이 추가합니다:
```ruby
pod 'SkyFloatingLabelTextField'
```

2. 수동으로 라이브러리를 다운로드해서 추가하는 경우, 공식 GitHub 저장소에서 최신 버전을 다운로드하고 프로젝트에 추가합니다.

## 2. 키보드 리턴키 동작 설정하기

SkyFloatingLabelTextField의 리턴키 동작을 설정하려면 UITextFieldDelegate 프로토콜을 구현해야 합니다. UITextFieldDelegate를 구현한 클래스에서 다음 메서드를 구현합니다:

```swift
func textFieldShouldReturn(_ textField: UITextField) -> Bool {
    textField.resignFirstResponder() // 키보드를 닫습니다.

    // 원하는 동작을 수행합니다.

    return true
}
```

위 예제에서는 textField.resignFirstResponder()를 호출하여 키보드를 닫고, 원하는 동작을 수행하도록 구현되어 있습니다. 원하는 동작을 수행하는 코드를 추가하면 됩니다.

## 3. SkyFloatingLabelTextField에 UITextFieldDelegate 설정하기

SkyFloatingLabelTextField에 UITextFieldDelegate를 설정하여 리턴키 동작을 처리할 수 있도록 해야 합니다. SkyFloatingLabelTextField의 delegate 속성을 UITextFieldDelegate로 설정합니다:

```swift
textField.delegate = self
```

위의 코드에서 self는 UITextFieldDelegate를 구현한 클래스를 가리킵니다.

## 마무리

이제 SkyFloatingLabelTextField를 사용하여 키보드의 리턴키 동작을 설정하는 방법에 대해 알아봤습니다. UITextFieldDelegate 프로토콜을 구현하여 textFieldShouldReturn 메서드에서 키보드 동작을 처리할 수 있습니다.