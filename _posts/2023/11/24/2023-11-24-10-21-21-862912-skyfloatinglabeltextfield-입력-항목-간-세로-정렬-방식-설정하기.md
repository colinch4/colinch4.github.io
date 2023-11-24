---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 항목 간 세로 정렬 방식 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 유용한 Swift 라이브러리로, 텍스트 필드에 부가적인 기능을 추가할 수 있습니다. 그 중 하나는 입력 항목 간의 세로 정렬 방식을 설정하는 것입니다. 이 기능을 사용하면 입력 항목을 간편하게 정렬할 수 있습니다.

## SkyFloatingLabelTextField 세로 정렬 방식 설정하기

SkyFloatingLabelTextField의 기본 세로 정렬 방식은 .center입니다. 하지만 이 방식을 다른 값으로 변경하여 입력 항목을 원하는대로 정렬할 수 있습니다. 

```swift
textField.verticalAlignment = .top // 입력 항목을 위로 정렬
textField.verticalAlignment = .center // 입력 항목을 중앙에 정렬
textField.verticalAlignment = .bottom // 입력 항목을 아래로 정렬
```

입력 항목을 위, 아래 또는 중앙으로 정렬할 수 있습니다.

## 예시

```swift
let textField = SkyFloatingLabelTextField()
textField.placeholder = "이름"
textField.verticalAlignment = .top

let emailField = SkyFloatingLabelTextField()
emailField.placeholder = "이메일 주소"
emailField.verticalAlignment = .center

let passwordField = SkyFloatingLabelTextField()
passwordField.placeholder = "비밀번호"
passwordField.verticalAlignment = .bottom
```

위의 코드 예제에서는 각각의 입력 항목을 다른 세로 정렬 방식으로 설정하였습니다.

## 결론

SkyFloatingLabelTextField를 사용하여 입력 항목 간의 세로 정렬 방식을 설정하는 방법에 대해 알아보았습니다. 이를 통해 원하는대로 입력 항목을 스타일링할 수 있습니다. 추가적으로 SkyFloatingLabelTextField에 대한 더 자세한 정보는 [공식 문서](https://github.com/Skyscanner/SkyFloatingLabelTextField)를 참고하시기 바랍니다.