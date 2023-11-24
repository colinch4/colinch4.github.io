---
layout: post
title: "[swift] SkyFloatingLabelTextField 텍스트 커서 색상 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서 SkyFloatingLabelTextField는 텍스트 입력 필드를 가지고 있는 자주 사용되는 라이브러리입니다. 이 라이브러리를 사용하면 텍스트 입력 필드에 부가적인 기능을 추가할 수 있습니다. 이 중 하나는 텍스트 커서의 색상을 변경하는 것입니다.

다음은 SkyFloatingLabelTextField에서 텍스트 커서 색상을 변경하는 방법에 대한 예시 코드입니다.

```swift
extension SkyFloatingLabelTextField {
    open override func caretRect(for position: UITextPosition) -> CGRect {
        var rect = super.caretRect(for: position)
        let width: CGFloat = 1.5
        rect.size.width = width
        return rect
    }
    
    open override func selectionRects(for range: UITextRange) -> [UITextSelectionRect] {
        var rects = super.selectionRects(for: range)
        rects.forEach {
            $0.rect.size.width = 1.5
        }
        return rects
    }
}
```

위의 예시 코드에서는 SkyFloatingLabelTextField의 extension을 생성하여 `caretRect(for position: UITextPosition)`과 `selectionRects(for range: UITextRange)` 메서드를 오버라이드하고 있습니다.

`caretRect(for position: UITextPosition)` 메서드는 텍스트 커서의 사각형 프레임을 변경합니다. 여기서 `rect.size.width`를 원하는 값으로 설정하여 텍스트 커서의 너비를 변경할 수 있습니다.

`selectionRects(for range: UITextRange)` 메서드는 텍스트 선택영역의 사각형 프레임을 변경합니다. 위의 예시 코드에서는 `rect.size.width`를 원하는 값으로 설정하여 선택영역의 너비를 변경하고 있습니다.

이렇게 변경한 후에는 SkyFloatingLabelTextField의 텍스트 커서와 선택영역의 너비가 설정한 값으로 변경됩니다.

## 참고 자료
- [SkyFloatingLabelTextField GitHub 저장소](https://github.com/Skyscanner/SkyFloatingLabelTextField)