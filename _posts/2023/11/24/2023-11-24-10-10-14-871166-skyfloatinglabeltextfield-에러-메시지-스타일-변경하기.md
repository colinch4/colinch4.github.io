---
layout: post
title: "[swift] SkyFloatingLabelTextField 에러 메시지 스타일 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

[Swift](https://swift.org/)로 iOS 앱을 개발하는 경우, 사용자의 입력을 받는 텍스트 필드는 필수적인 요소입니다. 그리고 [SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField) 라이브러리는 텍스트 입력을 받을 때 부각된 라벨을 제공하여 사용자 경험을 향상시킬 수 있는 좋은 선택입니다.

하지만 때로는 입력이 유효하지 않을 때 에러 메시지를 보여주고 싶을 수 있습니다. SkyFloatingLabelTextField에서는 기본적으로 한 줄의 텍스트로 에러 메시지를 표시합니다. 그러나 이 에러 메시지의 스타일을 변경하는 방법을 알려드리겠습니다.

### 에러 메시지 스타일 변경하기

SkyFloatingLabelTextField에서 에러 메시지를 변경하려면 `errorMessageLabel` 속성을 사용하면 됩니다. 이 레이블에 대한 스타일을 변경하면 원하는 디자인에 맞게 에러 메시지를 표시할 수 있습니다. 

아래의 예시 코드를 참고해주세요:

```swift
let textField = SkyFloatingLabelTextField()
textField.errorMessageLabel.textColor = .red
textField.errorMessageLabel.font = UIFont.systemFont(ofSize: 12)
textField.errorMessageLabel.numberOfLines = 0
textField.errorMessageLabel.textAlignment = .right
textField.errorMessageLabelInsets = UIEdgeInsets(top: 2, left: 0, bottom: 0, right: 0)
```

위의 예시 코드에서는 에러 메시지 레이블의 텍스트 색상을 빨간색으로, 폰트를 시스템 기본 폰트 크기 12로 설정하였습니다. 또한 에러 메시지 레이블의 여러 줄 표시를 가능하게 하고, 정렬을 우측으로 설정하였습니다. 마지막으로 에러 메시지 레이블의 여백을 지정하여 더 좋은 레이아웃을 만들 수 있습니다.

### 요약

SkyFloatingLabelTextField 에러 메시지를 변경하려면 `errorMessageLabel` 속성을 사용하여 스타일을 변경하면 됩니다. 이렇게 하면 사용자의 입력이 유효하지 않을 때 원하는 스타일로 에러 메시지를 표시할 수 있게 됩니다.