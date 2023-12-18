---
layout: post
title: "[flutter] LinearProgressIndicator와 함께 사용할 수 있는 이미지 효과"
description: " "
date: 2023-12-18
tags: [flutter]
comments: true
share: true
---

Flutter 프레임워크에서 `LinearProgressIndicator`는 진행률을 시각적으로 나타내기 위해 유용하게 활용됩니다. 진행률을 보여주는 동안 사용자 경험을 향상시키기 위해 이미지 효과를 추가하는 방법에 대해 알아보겠습니다.

## 이미지 효과 추가 

`LinearProgressIndicator` 옆에 이미지를 추가하여 진행률을 더 재미있게 표현할 수 있습니다. 이를 위해 Flutter 앱의 UI를 설계할 때 `Row` 위젯을 사용하여 `LinearProgressIndicator`와 이미지를 가로로 나란히 배치하고, 이때 이미지는 `FadeInImage`나 `Image.asset` 위젯을 통해 쉽게 표시할 수 있습니다.

```dart
Row(
  children: <Widget>[
    LinearProgressIndicator(value: _progressValue),
    Image.asset('assets/your_image.png'),
  ],
)
```

프로세스의 완료 유무에 따라 이미지를 보여주거나 숨기기 위해서는 조건문과 함께 `Opacity` 위젯을 사용할 수 있습니다. 이를 통해 프로세스가 완료될 때 이미지를 서서히 사라지게 하는 효과를 줄 수 있습니다.

```dart
Opacity(
  opacity: _progressValue == 1.0 ? 0.0 : 1.0,
  child: Image.asset('assets/your_image.png'),
)
```

## 결론

`LinearProgressIndicator`는 진행률을 시각적으로 나타내는 데에 효과적이지만, 이미지를 추가함으로써 화면에 동적인 효과를 주어 사용자 경험을 개선할 수 있습니다. 위에서 설명한 방법들을 활용하여 앱의 UI를 더 흥미롭게 만들어보세요.

참고자료: [Flutter 공식 문서](https://flutter.dev/docs)