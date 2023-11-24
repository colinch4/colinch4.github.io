---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력 항목 간 수직 정렬 방식 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자의 입력을 받을 때 입력 항목과 해당 항목의 라벨을 함께 표시하는 기능을 제공하는 텍스트 필드입니다. 이번에는 SkyFloatingLabelTextField를 사용하여 입력 항목과 라벨의 수직 정렬 방식을 설정하는 방법에 대해 알아보겠습니다.

## 1. 기본 설정

SkyFloatingLabelTextField를 사용하기 위해 먼저 프로젝트에 SkyFloatingLabelTextField 패키지를 추가해야 합니다. 패키지 관리자(Swift Package Manager 또는 CocoaPods)를 사용하여 SkyFloatingLabelTextField를 프로젝트에 추가할 수 있습니다.

```swift
import SkyFloatingLabelTextField
```
먼저 SkyFloatingLabelTextField를 import해야 합니다.

TextField와 Label의 수직 정렬 방식을 설정하는 방법은 다음과 같습니다.

## 2. 수직 내려쓰기

TextField와 Label을 수직으로 정렬하기 위해 `verticalAlignment` 속성을 사용합니다. `verticalAlignment` 속성은 `.center`, `.top`, `.bottom` 중 하나로 설정할 수 있습니다.

```swift
let textField = SkyFloatingLabelTextField()
textField.verticalAlignment = .center
```
TextField와 Label이 수직으로 중앙 정렬됩니다.

## 3. 수직 위쪽 정렬

TextField와 Label을 수직으로 위쪽으로 정렬하기 위해서는 `verticalAlignment` 속성을 `.top`으로 설정합니다.

```swift
let textField = SkyFloatingLabelTextField()
textField.verticalAlignment = .top
```
TextField와 Label이 수직으로 위쪽에 정렬됩니다.

## 4. 수직 아래쪽 정렬

TextField와 Label을 수직으로 아래쪽으로 정렬하기 위해서는 `verticalAlignment` 속성을 `.bottom`으로 설정합니다.

```swift
let textField = SkyFloatingLabelTextField()
textField.verticalAlignment = .bottom
```
TextField와 Label이 수직으로 아래쪽에 정렬됩니다.

## 5. 결론

SkyFloatingLabelTextField를 사용하여 입력 항목과 해당 항목의 라벨의 수직 정렬 방식을 설정하는 방법을 알아보았습니다. `verticalAlignment` 속성을 사용하여 원하는 수직 정렬 방식에 따라 TextField와 Label을 조정할 수 있습니다. 자신의 프로젝트에 맞게 적절한 방식을 선택하여 사용해보세요.

> 참고: [SkyFloatingLabelTextField 깃허브 저장소](https://github.com/misto/SkyFloatingLabelTextField)