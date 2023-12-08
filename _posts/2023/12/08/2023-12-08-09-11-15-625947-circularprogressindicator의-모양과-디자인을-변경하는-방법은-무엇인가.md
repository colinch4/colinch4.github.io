---
layout: post
title: "[flutter] CircularProgressIndicator의 모양과 디자인을 변경하는 방법은 무엇인가?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

`CircularProgressIndicator`는 기본적으로 Material 디자인을 따르며, 다양한 속성과 맞춤 설정을 통해 모양을 변경할 수 있습니다. 

이를 위해 `CircularProgressIndicator`의 속성 중 하나인 `valueColor`를 활용하여 색상을 조정할 수 있습니다. 예를 들어, `valueColor: AlwaysStoppedAnimation(Colors.red)`과 같이 사용하여 색상을 변경할 수 있습니다. 

또한, `CircularProgressIndicator`의 모양을 더욱 세부적으로 조절하려면 `LinearProgressIndicator`의 경우와 같이 `StrokeCap` 및 `strokeWidth`와 같은 다양한 속성을 사용하여 직접 모양을 조정할 수 있습니다.

```dart
CircularProgressIndicator(
  valueColor: AlwaysStoppedAnimation(Colors.red), // 색상 변경
  strokeWidth: 5, // 선 두께 변경
  backgroundColor: Colors.yellow, // 배경색 변경
)
```

또한, 별도의 라이브러리나 패키지를 사용하여 `CircularProgressIndicator`의 디자인을 더욱 다채롭게 커스터마이징할 수도 있습니다.

참고로, 관련 문서나 자료를 참고하시면 더 자세한 정보를 얻을 수 있습니다.

이렇게 해서 `CircularProgressIndicator`의 모양과 디자인을 변경할 수 있습니다.