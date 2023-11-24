---
layout: post
title: "[swift] SkyFloatingLabelTextField 플레이스홀더 텍스트 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발하다 보면 UITextField가 너무 단조롭고 지루하다고 생각할 때가 있습니다. SkyFloatingLabelTextField는 플레이스홀더 텍스트가 위로 올라가면서 더욱 독특한 느낌을 주는 커스텀 텍스트 필드입니다.

이번에는 SkyFloatingLabelTextField의 플레이스홀더 텍스트를 변경하는 방법에 대해 알아보겠습니다.

## 1. SkyFloatingLabelTextField 설치하기

먼저, SkyFloatingLabelTextField를 프로젝트에 설치해야 합니다. CocoaPods를 사용하는 경우 `Podfile`에 다음과 같이 추가합니다:

```swift
pod 'SkyFloatingLabelTextField'
```

그리고 터미널에서 `pod install`을 실행하여 라이브러리를 설치합니다.

## 2. 플레이스홀더 텍스트 변경하기

SkyFloatingLabelTextField의 인스턴스를 만들고 플레이스홀더 텍스트를 변경하기 위해 다음과 같이 코드를 작성합니다:

```swift
import SkyFloatingLabelTextField

// SkyFloatingLabelTextField 인스턴스 생성
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 50))

// 플레이스홀더 텍스트 설정
textField.placeholder = "이름"

// 플레이스홀더 텍스트 색상 설정
textField.placeholderColor = .lightGray

// 플레이스홀더 텍스트 폰트 설정
textField.placeholderFont = UIFont.systemFont(ofSize: 14)

// 플레이스홀더 텍스트 애니메이션 설정
textField.animationType = .float
```

위의 코드에서 `textField.placeholder`를 원하는 텍스트로 변경하시면 됩니다. 다른 속성도 동일한 방식으로 설정하실 수 있습니다.

## 마무리

이제 SkyFloatingLabelTextField를 사용하여 플레이스홀더 텍스트를 변경하는 방법에 대해 알아보았습니다. 원하는 텍스트로 변경하여 iOS 앱을 더욱 독특하게 만들어보세요.

## 참고 자료

- [SkyFloatingLabelTextField GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)