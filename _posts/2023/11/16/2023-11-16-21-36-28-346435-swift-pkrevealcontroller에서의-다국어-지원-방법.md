---
layout: post
title: "[swift] Swift PKRevealController에서의 다국어 지원 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---
PKRevealController는 iOS에서 사이드 메뉴를 구현하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 사용자가 앱의 메뉴를 왼쪽 또는 오른쪽에서 나타낼 수 있습니다. 이때, 다국어 지원을 제공하려면 몇 가지 작업을 진행해야 합니다.

## 1. Localizable.strings 파일 생성
다국어 지원을 하기 위해서는 Localizable.strings 파일을 생성해야 합니다. 이 파일은 각 언어별로 해당되는 텍스트를 포함하고 있습니다. 프로젝트 내에 `Localizable.strings` 파일을 생성하고 원하는 언어별로 `Localizable.strings` 파일을 복사하여 붙여넣습니다. 예를 들어, 한국어를 추가하려면 `Localizable.strings(ko)`라는 파일을 생성합니다.

## 2. 다국어 파일 작성
각 언어별 `Localizable.strings` 파일에는 해당 언어로 표시될 텍스트를 포함해야 합니다. 아래와 같이 텍스트 쌍을 추가합니다.

```swift
"Menu" = "메뉴";
"Settings" = "설정";
```

각 언어에 맞게 텍스트를 작성해야 합니다. 예를 들어, 영어로 표시되기를 원하는 경우 다음과 같이 작성할 수 있습니다.

```swift
"Menu" = "Menu";
"Settings" = "Settings";
```

이렇게 작성된 `Localizable.strings` 파일은 각 언어에 맞게 텍스트를 표시하는 데 사용됩니다.

## 3. PKRevealController 변경 사항
PKRevealController를 사용하여 다국어를 지원하려면 다음과 같이 변경하면 됩니다.
1. PKRevealController.m 파일을 엽니다.
2. `awakeFromNib` 메서드 내에서 sideMenuButton의 title을 변경하는 부분을 찾습니다.
3. 변경된 부분을 아래와 같이 수정합니다.
```swift
   self.sideMenuButton.title = NSLocalizedString(@"Menu", @"");
```

변경된 코드에서 `NSLocalizedString` 함수를 사용하여 `Menu` 텍스트를 로컬라이즈된 문자열로 변경합니다. `Menu`는 Localizable.strings 파일에서 해당 언어에 맞는 텍스트로 대체됩니다.

이제 PKRevealController를 사용할 때, 각 언어에 맞는 텍스트를 표시할 수 있습니다.

## 소결
Swift PKRevealController에서 다국어 지원을 위해서는 Localizable.strings 파일을 생성하고, 각 언어별 텍스트를 포함하여 작성해야 합니다. PKRevealController 코드를 수정하여 localizable된 텍스트를 사용하도록 변경하면 간단하게 다국어 지원을 할 수 있습니다.