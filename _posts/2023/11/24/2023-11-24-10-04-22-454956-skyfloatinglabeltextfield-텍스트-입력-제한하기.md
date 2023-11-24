---
layout: post
title: "[swift] SkyFloatingLabelTextField 텍스트 입력 제한하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 소개
SkyFloatingLabelTextField는 iOS 앱에서 사용자에게 텍스트를 입력받을 때 사용되는 텍스트 필드입니다. 텍스트 필드에 입력할 수 있는 제약을 설정하여 사용자의 입력을 제한하는 방법을 알아보겠습니다.

## 텍스트 입력 제한 방법

### 1. 최대 글자 수 제한하기
```swift
textField.maxLength = 10
```
위의 코드는 `textField`에 입력할 수 있는 최대 글자 수를 10으로 제한하는 예시입니다. 사용자가 10자를 초과하여 입력하려고 하면 입력이 제한됩니다.

### 2. 특정 문자만 입력 가능하도록 제한하기
```swift
textField.allowedCharacterSet = CharacterSet(charactersIn: "0123456789")
```
위의 코드는 `textField`에 입력할 수 있는 문자를 0부터 9까지의 숫자만 입력 가능하도록 제한하는 예시입니다. 다른 문자를 입력하려고 하면 입력이 제한됩니다.

### 3. 특정 패턴에 맞게 입력되도록 제한하기
```swift
textField.formatPattern = "###-####-####"
```
위의 코드는 `textField`에 입력할 수 있는 패턴을 ###-####-####와 같이 제한하는 예시입니다. 사용자가 해당 패턴에 맞지 않는 문자를 입력하려고 하면 입력이 제한됩니다.

### 4. 특정 문자열에 포함되는지 체크하여 입력 제한하기
```swift
if let text = textField.text, text.contains("금지단어") {
    // 금지단어가 포함된 경우
    textField.text = ""
}
```
위의 코드는 `textField`에 금지단어가 포함되어 있는지 체크하여 입력을 제한합니다. 만약 금지단어가 포함되어 있다면, 텍스트 필드의 텍스트를 비웁니다.

## 결론
SkyFloatingLabelTextField를 사용하면 텍스트 입력을 제한하는 다양한 방법을 구현할 수 있습니다. 위에서 소개한 방법들을 활용하여 앱의 사용자 인터페이스를 보다 유연하게 제어해보세요.

## 참고 자료
- [SkyFloatingLabelTextField GitHub Repo](https://github.com/Skyscanner/SkyFloatingLabelTextField)