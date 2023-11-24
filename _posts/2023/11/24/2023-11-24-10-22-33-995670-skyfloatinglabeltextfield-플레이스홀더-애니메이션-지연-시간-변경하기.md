---
layout: post
title: "[swift] SkyFloatingLabelTextField 플레이스홀더 애니메이션 지연 시간 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift에서 사용할 수 있는 플레이스홀더 애니메이션을 지원하는 텍스트 필드 라이브러리입니다. 기본적으로 플레이스홀더가 텍스트 필드 위로 올라올 때 애니메이션 효과가 적용되는데, 이 애니메이션의 지연 시간을 변경하는 방법을 알아보겠습니다.

## 지연 시간 변경하기

SkyFloatingLabelTextField는 animationDuration 속성을 통해 플레이스홀더 애니메이션의 지속 시간을 설정할 수 있습니다. 기본적으로는 0.3초가 설정되어 있지만, 이 값을 변경하여 원하는 지연 시간을 설정할 수 있습니다.

```swift
import SkyFloatingLabelTextField

let textField = SkyFloatingLabelTextField()
textField.animationDuration = 0.5 // 애니메이션 지연 시간을 0.5초로 설정
```

위의 예시 코드에서는 animationDuration 속성을 0.5로 설정하여 애니메이션 지연 시간을 0.5초로 변경하였습니다.

## 결론

SkyFloatingLabelTextField의 플레이스홀더 애니메이션 지연 시간을 변경하는 방법에 대해 알아보았습니다. animationDuration 속성을 조정하여 원하는 지연 시간을 설정할 수 있습니다. 이를 통해 앱의 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료

- [SkyFloatingLabelTextField GitHub 리포지토리](https://github.com/Skyscanner/SkyFloatingLabelTextField)