---
layout: post
title: "[flutter] 플러터 Slider와 BottomNavigationBar 위젯의 연동 방법은?"
description: " "
date: 2023-12-08
tags: [flutter]
comments: true
share: true
---

Flutter는 풍부한 위젯 라이브러리를 제공하여 다양한 UI를 구현할 수 있습니다. Slider와 BottomNavigationBar는 많은 앱에서 자주 사용되는 UI 요소 중의 하나입니다. 이 두 위젯을 효과적으로 연동하여 사용자와의 상호작용을 높일 수 있습니다.

## Slider 위젯과 BottomNavigationBar 위젯의 기본 사용

Slider 위젯은 숫자나 값을 선택할 때 사용되며, BottomNavigationBar 위젯은 여러 항목 중 하나를 선택할 때 사용됩니다. 

Slider 위젯을 생성하는 예제:

```dart
Slider(
  value: _currentSliderValue,
  min: 0,
  max: 100,
  onChanged: (double value) {
    setState(() {
      _currentSliderValue = value;
    });
  },
),
```

BottomNavigationBar 위젯을 생성하는 예제:
```dart
BottomNavigationBar(
  items: const <BottomNavigationBarItem>[
    BottomNavigationBarItem(
      icon: Icon(Icons.home),
      label: 'Home',
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.business),
      label: 'Business',
    ),
  ],
  currentIndex: _selectedIndex,
  onTap: _onItemTapped,
),
```

## Slider와 BottomNavigationBar의 연동 방법

Slider와 BottomNavigationBar를 연동하여 사용자가 Slider 값을 조절할 때 BottomNavigationBar 항목이 변화하도록 하려면, Slider의 onChanged 콜백을 사용하여 BottomNavigationBar의 항목을 변경하면 됩니다.

```dart
onChanged: (double value) {
  setState(() {
    _currentSliderValue = value;
    _selectedIndex = calculateSelectedIndex(value);
  });
}
```

위 코드에서 `calculateSelectedIndex` 함수는 Slider의 값에 따라 선택될 BottomNavigationBar의 항목을 계산하는 함수입니다.

이제 Slider와 BottomNavigationBar 위젯을 효과적으로 연동할 수 있게 되었습니다.

## 결론

Slider와 BottomNavigationBar 위젯은 각각의 기능을 가지고 있지만, 상호작용하도록 연동하는 것은 사용자 경험을 향상시키는 데 중요합니다. Flutter를 사용하여 이러한 상호작용을 쉽게 구현할 수 있으며, 이를 통해 사용자가 앱을 즐겁게 사용할 수 있는 경험을 제공할 수 있습니다.

이와 관련한 자세한 내용은 [Flutter 공식 문서](https://flutter.dev/docs)를 참조하시기 바랍니다.