---
layout: post
title: "[swift] SkyFloatingLabelTextField의 텍스트 및 플레이스홀더 색상 변경하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 iOS 앱에서 사용하기 쉽고 현대적인 텍스트 입력 필드를 제공하는 오픈 소스 라이브러리입니다. 이 라이브러리를 사용하여 텍스트 필드의 텍스트 및 플레이스홀더의 색상을 변경하는 방법을 소개하겠습니다.

### 작업 절차

1. SkyFloatingLabelTextField 라이브러리를 프로젝트에 추가합니다. Pod을 사용하는 경우 `Podfile`에 다음을 추가하고 `pod install`을 실행합니다.

```ruby
pod 'SkyFloatingLabelTextField'
```

2. 소스 코드에서 `import SkyFloatingLabelTextField`를 추가하여 라이브러리를 임포트합니다.

3. 텍스트 필드를 초기화하고 설정합니다.

```swift
let textField = SkyFloatingLabelTextField(frame: CGRect(x: 0, y: 0, width: 200, height: 40))
textField.placeholder = "이름"
textField.title = "이름"
textField.selectedTitleColor = UIColor.blue // 선택된 상태의 플레이스홀더 색상
textField.selectedLineColor = UIColor.blue // 선택된 상태의 밑줄 색상
textField.lineColor = UIColor.lightGray // 비선택 상태의 밑줄 색상
textField.textColor = UIColor.black // 텍스트 색상
textField.placeholderColor = UIColor.lightGray // 플레이스홀더 색상
```

### 주의사항

- 색상을 설정할 때, UIColor 객체를 사용하여 적절한 색상을 지정해야 합니다.
- `selectedTitleColor` 및 `selectedLineColor`은 텍스트 필드가 선택된 상태일 때의 색상을 지정하는 속성입니다.
- `lineColor`은 비선택 상태의 밑줄 색상을 지정하는 속성입니다.
- `textColor`은 텍스트의 색상을 지정하는 속성입니다.
- `placeholderColor`는 플레이스홀더의 색상을 지정하는 속성입니다.

### 참고 자료

- [SkyFloatingLabelTextField 라이브러리 문서](https://github.com/Skyscanner/SkyFloatingLabelTextField)