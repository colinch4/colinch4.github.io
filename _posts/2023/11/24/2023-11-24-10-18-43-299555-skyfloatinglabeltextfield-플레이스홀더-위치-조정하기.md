---
layout: post
title: "[swift] SkyFloatingLabelTextField 플레이스홀더 위치 조정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자에게 텍스트 입력을 도와주는 기능을 제공하는 UITextField의 서브클래스입니다. 이 UITextField의 placeholder를 담당하는 텍스트를 플레이스홀더라고 하는데, 기본적으로 플레이스홀더는 UITextField의 상단에 위치합니다.

하지만 때로는 플레이스홀더를 다른 위치에 표시하고 싶을 수도 있습니다. 이번 글에서는 SkyFloatingLabelTextField의 플레이스홀더 위치를 조정하는 방법에 대해 알아보겠습니다.

## SkyFloatingLabelTextField 플레이스홀더 위치 조정

SkyFloatingLabelTextField의 플레이스홀더 위치를 조정하기 위해서는 아래의 단계들을 따르면 됩니다.

1. SkyFloatingLabelTextField 인스턴스를 생성합니다.
2. 플레이스홀더를 원하는 위치로 조정합니다.
3. SkyFloatingLabelTextField를 뷰에 추가합니다.

아래는 코드로 나타낸 예시입니다.

```swift
import SkyFloatingLabelTextField

// SkyFloatingLabelTextField 인스턴스 생성
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))

// 플레이스홀더 위치 조정
textField.titleLabel.font = UIFont.systemFont(ofSize: 10) // 플레이스홀더 폰트 크기 조정
textField.titleLabel.textColor = .gray // 플레이스홀더 텍스트 색상 조정
textField.placeholderFont = UIFont.systemFont(ofSize: 15) // 플레이스홀더 폰트 크기 조정

// SkyFloatingLabelTextField 뷰에 추가
self.view.addSubview(textField)
```

이렇게하면 플레이스홀더가 원하는 위치로 조정되어 사용자에게 보다 직관적인 입력 도움을 제공할 수 있습니다.

더 자세한 설정 사항에 대해서는 [SkyFloatingLabelTextField](https://github.com/Skyscanner/SkyFloatingLabelTextField)의 공식 GitHub 페이지를 참고하시기 바랍니다.