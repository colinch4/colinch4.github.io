---
layout: post
title: "[swift] SkyFloatingLabelTextField 텍스트 정렬 방식 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift로 작성된 사용자 정의 텍스트 필드 라이브러리입니다. 이 라이브러리는 라벨을 텍스트 필드 위로 애니메이션 효과와 함께 띄워주는 기능을 제공합니다.

기본적으로 SkyFloatingLabelTextField의 텍스트는 왼쪽 정렬로 표시됩니다. 하지만 때로는 텍스트를 가운데나 오른쪽에 정렬하고 싶을 수도 있습니다. 이 경우, 파이프라인(|) 문자를 사용하여 텍스트 정렬 방식을 변경할 수 있습니다.

다음은 SkyFloatingLabelTextField에서 텍스트 정렬 방식을 변경하는 예제입니다.

```swift
textField.textAlignment = .center
```

위의 코드는 `textField`라는 인스턴스의 `textAlignment` 속성을 `.center`로 설정하여 텍스트를 가운데 정렬합니다.

```swift
textField.textAlignment = .right
```

위의 코드는 `textField` 인스턴스의 `textAlignment` 속성을 `.right`로 설정하여 텍스트를 오른쪽 정렬합니다.

이렇게 하면 SkyFloatingLabelTextField에서 텍스트의 정렬 방식을 변경할 수 있습니다. 더 자세한 내용은 SkyFloatingLabelTextField의 공식 문서를 참조하시기 바랍니다.

### 참고 자료
1. [SkyFloatingLabelTextField - GitHub](https://github.com/Skyscanner/SkyFloatingLabelTextField)
2. [UIView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview)
3. [Swift - The Swift Programming Language](https://docs.swift.org/swift-book/)