---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 항목 간 가로 위치 조정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 SkyFloatingLabelTextField 라이브러리를 사용하여 입력 항목 간 가로 위치를 조정하는 방법을 알아보겠습니다.

SkyFloatingLabelTextField는 사용자에게 입력란을 표시하고, 라벨을 위에 떠오르게 하는 효과를 제공하는 라이브러리입니다. 기본적으로 제공되는 라이브러리에서는 입력 항목들이 자동으로 나란히 정렬되게 됩니다. 하지만 때에 따라서는 입력 항목간의 가로 위치를 조정해야 할 필요가 있을 수 있습니다.

## 1. 입력 항목 정렬하기

SkyFloatingLabelTextField에서 입력 항목을 정렬하는 방법은 `contentHorizontalAlignment` 속성을 이용하는 것입니다. 이 속성을 이용하여 입력 항목을 왼쪽, 가운데, 오른쪽으로 정렬할 수 있습니다.

```swift
// 왼쪽 정렬
textField.contentHorizontalAlignment = .left

// 가운데 정렬
textField.contentHorizontalAlignment = .center

// 오른쪽 정렬
textField.contentHorizontalAlignment = .right
```

## 2. 입력 항목 간 가로 위치 조정하기

입력 항목 간의 가로 위치를 조정하는 방법은 약간의 트릭을 사용하는 것입니다. 해당 기능을 구현하기 위해서는 입력 항목을 감싸는 StackView를 사용해야 합니다. StackView를 사용하면 입력 항목들을 유연하게 배치할 수 있습니다.

아래는 입력 항목 간의 가로 위치를 조정하는 예제 코드입니다.

```swift
// StackView 생성
let stackView = UIStackView()
stackView.axis = .horizontal
stackView.distribution = .fillEqually

// 입력 항목 생성
let textField1 = SkyFloatingLabelTextField()
textField1.placeholder = "항목 1"
let textField2 = SkyFloatingLabelTextField()
textField2.placeholder = "항목 2"
let textField3 = SkyFloatingLabelTextField()
textField3.placeholder = "항목 3"

// StackView에 입력 항목 추가
stackView.addArrangedSubview(textField1)
stackView.addArrangedSubview(textField2)
stackView.addArrangedSubview(textField3)

// 입력 항목 간 가로 간격 설정
stackView.spacing = 10

// StackView를 뷰에 추가
view.addSubview(stackView)

// StackView의 Auto Layout 설정
stackView.translatesAutoresizingMaskIntoConstraints = false
stackView.topAnchor.constraint(equalTo: view.topAnchor, constant: 20).isActive = true
stackView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20).isActive = true
stackView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20).isActive = true
```

위의 코드에서는 `UIStackView`를 사용하여 입력 항목들을 가로로 정렬합니다. `addArrangedSubview` 메소드를 이용하여 입력 항목을 StackView에 추가하고, `spacing` 속성을 이용하여 입력 항목들 간의 가로 간격을 설정합니다. 마지막으로 StackView를 화면에 추가하고 Auto Layout을 설정합니다.

이제 입력 항목 간의 가로 위치를 조정할 수 있게 되었습니다.

## 3. 마무리

위에서는 SkyFloatingLabelTextField를 사용하여 입력 항목 간의 가로 위치를 조정하는 방법을 알아보았습니다. 코드를 참고하여 원하는 방식으로 입력 항목을 배치하고 가로 위치를 조정할 수 있습니다.

참고 자료:
- [SkyFloatingLabelTextField 라이브러리](https://github.com/Skyscanner/SkyFloatingLabelTextField)