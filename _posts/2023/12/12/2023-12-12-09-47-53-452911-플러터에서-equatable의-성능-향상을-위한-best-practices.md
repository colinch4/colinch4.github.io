---
layout: post
title: "[flutter] 플러터에서 Equatable의 성능 향상을 위한 Best Practices"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

Equatable은 객체의 동등성 비교를 편리하게 해주는 플러터 라이브러리 중 하나입니다. Equatable을 사용하면 객체의 동등성을 간단히 비교할 수 있어 개발 생산성을 높일 수 있지만, 가끔 성능 문제가 발생할 수 있습니다. 이를 최적화하는 방법에 대해 알아봅시다.

## Equatable이란?

Equatable은 플러터에서 객체의 동등성을 비교할 때 사용하는 패키지입니다. 클래스에서 Equatable을 구현하면 `==` 연산자와 `hashCode`를 자동으로 생성해주어 객체들 간의 비교를 간편하게 할 수 있습니다.

```dart
import 'package:equatable/equatable.dart';

class User extends Equatable {
  final String name;
  final int age;

  const User(this.name, this.age);

  @override
  List<Object> get props => [name, age];
}
```

위의 예시에서 `props` 메서드는 동등성 비교에 사용될 필드들을 정의하고 있습니다.

## Best Practices를 적용해 성능 향상

Equatable을 사용할 때 성능을 향상시키기 위해 몇 가지 Best Practices를 준수할 수 있습니다.

### 1. `props` 메서드 최적화

`props` 메서드에 속성이 많은 경우, 비교에 필요한 최소한의 필드만을 반환하도록 최적화할 필요가 있습니다. 많은 필드를 가진 경우 필요한 속성만을 반환함으로써 비교하는 속도를 향상시킬 수 있습니다.

```dart
@override
List<Object> get props => [name, age];
```

### 2. Immutable 속성 사용

Equatable을 사용할 때 불변(Immutable) 속성을 사용하는 것이 중요합니다. 객체가 변경되지 않으면 Equatable의 내부 최적화 기능을 활용하여 성능을 향상시킬 수 있습니다.

```dart
class User extends Equatable {
  final String name;
  final int age;

  const User(this.name, this.age);
  //...
}
```

### 3. 커스텀 `==` 연산자 사용

필요에 따라 커스텀 `==` 연산자를 정의하여 Equatable의 기본 동등성 비교 동작을 변경할 수 있습니다. 이를 통해 성능과 유연성을 극대화할 수 있습니다.

```dart
@override
bool operator ==(Object other) =>
      identical(this, other) ||
      other is User &&
        runtimeType == other.runtimeType &&
        name == other.name &&
        age == other.age;

@override
int get hashCode => name.hashCode ^ age.hashCode;
```

## 결론

Equatable을 사용하여 객체의 동등성을 쉽게 비교할 수 있지만, 성능 문제가 발생할 수 있습니다. 따라서 `props` 메서드의 최적화, Immutable 속성 사용, 커스텀 `==` 연산자 등의 Best Practices를 적용하여 성능을 최대화하는 것이 중요합니다.

위의 Best Practices를 준수하면서 Equatable의 사용을 최적화하여 **플러터 애플리케이션의 성능을 향상**시킬 수 있습니다.

[Equatable 패키지 문서](https://pub.dev/packages/equatable)

[플러터 - 공식 홈페이지](https://flutter.dev/)