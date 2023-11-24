---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트 가져오기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 입력 필드에 부가적인 기능을 제공하는 라이브러리입니다. 이 라이브러리를 사용하면 입력 필드에 플레이스홀더 텍스트와 함께 라벨이 표시되며, 사용자의 입력에 따라 라벨이 위로 올라가거나 텍스트 필드의 상태를 표시할 수 있습니다.

SkyFloatingLabelTextField에서 입력된 텍스트를 가져오는 방법은 간단합니다. `text` 속성을 사용하여 현재 입력된 텍스트 값을 가져올 수 있습니다.

아래 예제는 SkyFloatingLabelTextField에서 입력한 텍스트를 가져오는 방법을 보여줍니다.

```swift
import SkyFloatingLabelTextField

// SkyFloatingLabelTextField 인스턴스 생성
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))

// 텍스트 필드에 입력된 텍스트 가져오기
let inputText = textField.text
print("입력된 텍스트: \(inputText ?? "")")
```

위 예제에서는 `SkyFloatingLabelTextField` 인스턴스를 생성한 후 `text` 속성을 사용하여 입력된 텍스트 값을 가져와 출력합니다.

SkyFloatingLabelTextField를 사용하면 입력 필드에 부가적인 기능을 쉽게 추가할 수 있습니다. 자세한 내용은 [공식 GitHub 저장소](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참조하시기 바랍니다.