---
layout: post
title: "[swift] SkyFloatingLabelTextField 폰트 크기 조절하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자로부터 입력을 받을 수 있는 텍스트 필드를 제공하는 라이브러리입니다. 이 라이브러리는 iOS 애플리케이션에서 더 나은 사용자 경험을 제공하는 데 도움이 됩니다. 

기본적으로 SkyFloatingLabelTextField는 텍스트 필드의 폰트 크기를 제어할 수 있는 다양한 속성을 제공합니다. 이 글에서는 SkyFloatingLabelTextField의 폰트 크기를 조절하는 방법에 대해 알아보겠습니다.

## 1. 폰트 크기 조절하기

SkyFloatingLabelTextField의 폰트 크기를 조절하기 위해서는 원하는 폰트 크기를 설정하면 됩니다. 다음은 코드를 통해 폰트 크기를 조절하는 예시입니다.

```swift
let textField = SkyFloatingLabelTextField()
textField.font = UIFont.systemFont(ofSize: 20)
```

위의 코드에서 `UIFont.systemFont(ofSize: 20)` 부분은 폰트 크기를 20으로 설정하는 부분입니다. 필요한 폰트 크기에 맞게 값을 조절하면 됩니다.

## 2. 플레이스홀더 폰트 크기 조절하기

SkyFloatingLabelTextField는 플레이스홀더의 폰트 크기를 따로 조절할 수 있습니다. 플레이스홀더 폰트 크기를 조절하려면 다음과 같은 코드를 사용할 수 있습니다.

```swift
textField.placeholderFont = UIFont.systemFont(ofSize: 15)
```

위의 코드에서 `UIFont.systemFont(ofSize: 15)` 부분은 플레이스홀더의 폰트 크기를 15로 설정하는 부분입니다. 필요한 폰트 크기에 맞게 값을 조절하면 됩니다.

## 결론

SkyFloatingLabelTextField를 사용하여 폰트 크기를 조절하는 방법에 대해 알아보았습니다. 위의 예시 코드를 참고하여 원하는 폰트 크기로 텍스트 필드와 플레이스홀더의 폰트 크기를 설정할 수 있습니다. SkyFloatingLabelTextField를 사용하면 iOS 애플리케이션에서 좀 더 세련된 텍스트 입력 환경을 제공할 수 있습니다.

> **참고자료:**  
> - [SkyFloatingLabelTextField GitHub Repository](https://github.com/Skyscanner/SkyFloatingLabelTextField)