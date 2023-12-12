---
layout: post
title: "[flutter] 플러터에서 Equatable과 Custom Equality의 장단점 비교"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 앱을 개발할 때 객체의 동등성(equality)을 비교해야 하는 경우가 많이 있습니다. Equatable과 Custom Equality는 두 가지 주요 방법으로, 어떤 상황에서 어떤 것을 선택해야 하는지 비교해 보겠습니다.

## Equatable

`Equatable` 패키지는 객체의 동등성 비교를 처리하기 위한 강력한 도구입니다. 객체를 생성할 때 `Equatable` 클래스를 상속받아 `equals`와 `hashCode` 메서드를 구현하는 것으로 간단히 동등성 비교를 할 수 있습니다.

장점:
- 불필요한 코드를 줄일 수 있습니다.
- `Equatable`을 사용하면 `==` 연산자와 `hashCode` 메서드를 자동으로 생성할 수 있습니다.

단점:
- `Equatable` 클래스를 상속해야 하므로 다른 클래스를 상속할 수 없습니다. 이는 단일 상속(singleton)의 제약으로 이어질 수 있습니다.

## Custom Equality

일반적으로 `==` 연산자를 오버라이드하여 개별 클래스에서 동등성 비교를 구현할 수도 있습니다. 여기에는 직접 `equals` 메서드와 `hashCode` 메서드를 구현하는 작업이 포함됩니다.

장점:
- 동등성 비교 로직을 완전히 제어할 수 있습니다.
- 다중 상속을 통해 `Custom Equality`을 다른 클래스와 조합할 수 있습니다.

단점:
- 더 많은 코드를 직접 작성해야 합니다.
- `equals` 및 `hashCode` 메서드를 수동으로 관리해야 합니다.

이러한 장단점을 고려하고 특정 상황에 맞게 Equatable과 Custom Equality 중에서 선택하면 됩니다. 어떤 상황에 어떤 것을 선택할지에 대한 구체적인 예제 코드는 다음과 같습니다.

```dart
// Equatable 사용 예제
import 'package:equatable/equatable.dart';

class User extends Equatable {
  final String id;
  final String name;

  User(this.id, this.name);

  @override
  List<Object> get props => [id, name];
}

// Custom Equality 사용 예제
class CustomUser {
  final String id;
  final String name;

  CustomUser(this.id, this.name);

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is CustomUser &&
          runtimeType == other.runtimeType &&
          id == other.id &&
          name == other.name;

  @override
  int get hashCode => id.hashCode ^ name.hashCode;
}
```

## 마무리

각각의 방법은 특정한 상황에 적합합니다. `Equatable`은 간단하게 사용할 수 있으며 `Custom Equality`는 보다 다양한 상황에서 유연하게 사용할 수 있습니다. 그러므로 상황에 맞게 적절한 동등성 비교 방법을 선택하여 개발을 진행하는 것이 중요합니다.

이상으로 Equatable과 Custom Equality의 장단점 비교에 대한 내용을 마치도록 하겠습니다.

[Equatable 패키지 공식 문서](https://pub.dev/packages/equatable)

[플러터(Flutter) 공식 문서](https://flutter.dev)