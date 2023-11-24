---
layout: post
title: "[swift] SkyFloatingLabelTextField 텍스트 및 플레이스홀더 폰트 스타일 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift로 작성된 사용자 정의 가능한 텍스트 필드 라이브러리입니다. 텍스트 필드에는 텍스트와 함께 부가적인 플레이스홀더도 표시할 수 있습니다. 이 라이브러리를 사용하면 텍스트 필드와 플레이스홀더의 폰트 스타일을 사용자가 원하는 대로 변경할 수 있습니다.

SkyFloatingLabelTextField의 텍스트 및 플레이스홀더 폰트 스타일을 변경하는 방법은 다음과 같습니다.

### 1. 폰트 스타일 생성

텍스트와 플레이스홀더에 원하는 폰트 스타일을 적용하기 위해 먼저 UIFontDescriptor 객체를 생성해야 합니다. UIFontDescriptor는 UIFont의 특정 스타일과 속성을 정의합니다. 예를 들어, 폰트 이름, 크기, 굵기, 스타일 등을 지정할 수 있습니다. 

다음은 14pt 크기의 볼드체 시스템 폰트를 생성하는 예제입니다.

```swift
let descriptor = UIFontDescriptor.preferredFontDescriptor(withTextStyle: .body)
let boldFontDescriptor = descriptor.withSymbolicTraits(.traitBold)
let boldFont = UIFont(descriptor: boldFontDescriptor!, size: 14.0)
```

### 2. SkyFloatingLabelTextField에 폰트 스타일 적용

SkyFloatingLabelTextField에 폰트 스타일을 적용하려면, 생성한 폰트를 사용하여 텍스트 필드의 `font` 및 `placeholderFont` 속성을 설정해야 합니다. 

다음은 SkyFloatingLabelTextField에 폰트 스타일을 적용하는 예제입니다.

```swift
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))
textField.font = boldFont // 텍스트 필드의 폰트 스타일 설정
textField.placeholderFont = boldFont // 플레이스홀더의 폰트 스타일 설정
```

### 3. 적용된 폰트 확인

폰트 스타일이 적용되었는지 확인하기 위해 텍스트 필드를 화면에 표시합니다.

```swift
view.addSubview(textField)
```

이제 텍스트 필드가 지정한 폰트 스타일을 적용하여 텍스트와 플레이스홀더를 표시할 것입니다.

위의 코드를 참고하여 SkyFloatingLabelTextField의 텍스트와 플레이스홀더 폰트 스타일을 사용자 정의하세요.

**참고:**

- [SkyFloatingLabelTextField README](https://github.com/Skyscanner/SkyFloatingLabelTextField#Usage)