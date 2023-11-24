---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 항목 위치 조정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 Swift로 개발된 매우 강력한 입력 필드 라이브러리입니다. 이 라이브러리는 입력 필드에 플로팅 라벨을 추가하여 더 편리한 사용자 인터페이스를 제공합니다. 하지만 때로는 기본 설정된 입력 항목 위치가 우리가 원하는 대로 레이아웃되지 않을 수 있습니다.

이번 포스트에서는 SkyFloatingLabelTextField의 입력 항목 위치를 조정하는 방법에 대해 알아보겠습니다. 

## 1. 입력 텍스트 위치 조정하기

입력 텍스트를 위로 또는 아래로 이동시키기 위해서는 `contentVerticalPadding` 속성을 사용할 수 있습니다. 이 속성은 입력 필드의 상단과 하단 사이의 여백을 조정하는 데 사용됩니다. 기본적으로 `8.0`으로 설정되어 있으며, 필요에 따라 이 값을 조정할 수 있습니다.

```swift
textField.contentVerticalPadding = 10.0
```

위의 코드는 입력 필드의 상단과 하단의 여백을 `10.0`으로 조정합니다. 이 값을 적절하게 조정하여 원하는 위치로 입력 필드를 이동시킬 수 있습니다.

## 2. 플로팅 라벨 위치 조정하기

기본적으로 SkyFloatingLabelTextField의 플로팅 라벨은 입력 필드에 입력이 있는 경우 위로 이동하여 라벨로 표시됩니다. 하지만 때로는 라벨을 원하는 위치로 이동시키고 싶을 수도 있습니다.

`floatingLabelYPadding` 속성을 사용하여 플로팅 라벨의 위치를 조정할 수 있습니다. 이 속성은 입력 필드의 상단부터 플로팅 라벨까지의 여백을 조정하는 데 사용됩니다. 기본적으로 `0.0`으로 설정되어 있으며, 필요에 따라 이 값을 조정할 수 있습니다.

```swift
textField.floatingLabelYPadding = 5.0
```

위의 코드는 플로팅 라벨과 입력 필드 사이의 여백을 `5.0`으로 조정합니다. 이 값을 적절하게 조정하여 원하는 위치로 플로팅 라벨을 이동시킬 수 있습니다.

## 3. 결과 확인하기

위의 코드를 적용하고 실행하면 입력 항목의 위치가 조정되어 플로팅 라벨과 입력 텍스트가 원하는 위치에 레이아웃될 것입니다. 필요에 따라 여러 가지 값을 실험해보고 적절한 위치를 찾아보세요.

## 참고 자료

- [SkyFloatingLabelTextField on GitHub](https://github.com/Skyscanner/SkyFloatingLabelTextField)