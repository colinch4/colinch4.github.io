---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트의 글자 수 제약 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

`SkyFloatingLabelTextField`는 iOS 앱에서 사용자에게 텍스트 입력을 위한 텍스트 필드를 제공하는 라이브러리입니다. 이 라이브러리를 사용하여 입력한 텍스트의 글자 수에 제약을 설정하는 방법에 대해 알아보겠습니다.

## 1. SkyFloatingLabelTextField 설치하기

먼저, `SkyFloatingLabelTextField`를 설치해야 합니다. 설치하기 전에, Cocoapods를 사용하여 라이브러리를 관리하는 방법을 알고 있어야 합니다.

```bash
pod 'SkyFloatingLabelTextField'
```
설치한 후에는 `import SkyFloatingLabelTextField`로 라이브러리를 가져와 사용할 수 있습니다.

## 2. 글자 수 제약 설정하기

다음은 `SkyFloatingLabelTextField`에서 입력한 텍스트의 글자 수 제약을 설정하는 예제입니다.

```swift
let textField = SkyFloatingLabelTextField()
textField.maxCharacterLimit = 10 // 최대 글자 수를 10으로 설정

// 글자 수 제약이 설정되면 자동으로 텍스트 필드의 오른쪽 하단에 글자 수 카운터가 표시됩니다.
// 만약 이 기능을 끄고 싶다면 다음 코드를 추가할 수 있습니다.
textField.showCounterLabel = false
```

위의 예제에서는 `maxCharacterLimit` 속성을 사용하여 최대 글자 수를 10으로 설정하고 있습니다. 이렇게 설정하면 사용자가 10자 이상의 텍스트를 입력하려고 할 때 텍스트 필드의 내용이 수정되지 않습니다. 또한, `showCounterLabel` 속성을 `false`로 설정하여 글자 수 카운터를 숨길 수도 있습니다.

## 3. 추가적인 옵션 설정하기

`SkyFloatingLabelTextField`에는 글자 수 제약 설정 외에도 다양한 옵션을 설정할 수 있습니다. 몇 가지 예를 들어보면 다음과 같습니다.

- `errorColor`: 잘못된 값이 입력되었을 때 텍스트 필드를 강조 표시하는 색상을 설정합니다.
- `lineColor`: 텍스트 필드의 밑줄 색상을 설정합니다.
- `selectedLineColor`: 텍스트 필드가 활성화된 상태에서의 밑줄 색상을 설정합니다.
- `placeholderColor`: 텍스트 필드의 플레이스홀더 텍스트 색상을 설정합니다.
- `disabledColor`: 텍스트 필드가 비활성화된 상태일 때의 색상을 설정합니다.

이 외에도 더 많은 옵션이 제공되므로, [공식 문서](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참고하여 자세한 내용을 확인할 수 있습니다.

이제 `SkyFloatingLabelTextField`를 사용하여 입력한 텍스트의 글자 수 제약을 설정하는 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 텍스트 입력 기능이 있는 앱을 개발할 때 유용하게 사용할 수 있습니다.