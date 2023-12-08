---
layout: post
title: "[flutter] CircularProgressIndicator를 사용하여 원형 프로그레스 배경과 함께 진행 상태를 표시하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

## 개요
`CircularProgressIndicator`는 flutter에서 쉽게 사용할 수 있는 프로그레스 바 위젯 중 하나입니다. 이 위젯을 사용하여 원형 프로그레스 바와 함께 진행 상태를 보여줄 수 있습니다.

## 단계
1. **`CircularProgressIndicator` 위젯을 추가합니다.**
   
   ```dart
   CircularProgressIndicator()
   ```

2. **`value` 속성을 사용하여 진행 상태를 표시합니다.**

   ```dart
   CircularProgressIndicator(
     value: 0.5, // 0.0에서 1.0 사이의 값으로 진행 상태를 나타냅니다.
   )
   ```

3. **원형 프로그레스 바에 배경을 추가합니다. `CircularProgressIndicator`를 `Container`로 감싸고, `backgroundColor` 속성을 사용합니다.**

   ```dart
   Container(
     height: 50,
     width: 50,
     child: CircularProgressIndicator(
       value: 0.7,
       backgroundColor: Colors.grey, // 배경색을 지정합니다.
     ),
   )
   ```

위의 단계를 따라하면, 몇 가지 옵션을 사용하여 원형 프로그레스 바와 함께 진행 상태를 표시할 수 있습니다.

더 자세한 내용은 [flutter 공식 문서](https://api.flutter.dev/flutter/material/CircularProgressIndicator-class.html)를 확인해주세요.