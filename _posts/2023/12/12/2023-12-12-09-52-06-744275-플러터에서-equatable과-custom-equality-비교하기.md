---
layout: post
title: "[flutter] 플러터에서 Equatable과 Custom Equality 비교하기"
description: " "
date: 2023-12-12
tags: [flutter]
comments: true
share: true
---

플러터(Flutter) 앱을 개발하다보면 객체 간의 동등성(equality)을 비교해야 하는 경우가 있습니다. **Equatable**와 **Custom Equality**를 사용하여 객체의 동등성을 비교하는 방법을 알아보겠습니다.

## Equatable

**Equatable**는 플러터 프레임워크에서 제공하는 라이브러리로, 객체의 동등성을 간편하게 비교할 수 있도록 도와줍니다. 예를 들어, 다음과 같이 Equatable을 사용하여 객체를 생성하고 동등성을 비교할 수 있습니다.

```dart
import 'package:equatable/equatable.dart';

class User extends Equatable {
  final String name;
  final int age;

  User(this.name, this.age);

  @override
  List<Object> get props => [name, age];
}
```

위 코드에서 Equatable 클래스를 상속하고, `props` 메서드를 오버라이딩하여 동등성을 비교할 속성을 정의합니다. 이후 Equatable를 통해 `==` 연산자를 오버라이딩하지 않아도 `==` 연산자를 사용하여 객체를 비교할 수 있습니다.

## Custom Equality

때로는 Equatable로는 충분하지 않을 수 있습니다. 사용자 정의 동등성을 위해 Custom Equality를 구현해야할 때가 있습니다. 예를 들어, 다음과 같이 `==` 연산자를 오버라이딩하여 객체의 동등성을 비교할 수 있습니다.

```dart
class CustomUser {
  final String name;
  final int age;

  CustomUser(this.name, this.age);

  @override
  bool operator ==(Object other) =>
    identical(this, other) || 
    other is CustomUser &&
    other.name == name &&
    other.age == age;

  @override
  int get hashCode => name.hashCode ^ age.hashCode;
}
```

위 코드에서 `==` 연산자를 오버라이딩하여 사용자 정의로 동등성을 비교하고, `hashCode` 메서드를 오버라이딩하여 해시 코드를 반환합니다.

## 결론

**Equatable**는 간편하고 빠르게 객체의 동등성을 비교할 수 있는 방법을 제공합니다. 그러나 경우에 따라 **Custom Equality**를 구현해야할 때도 있습니다. 적절한 상황에 맞게 Equatable와 Custom Equality를 활용하여 객체의 동등성을 비교하는 것이 중요합니다.

이러한 방법을 사용하여 플러터 앱을 개발하면 코드를 보다 간결하게 유지할 수 있고, 객체의 동등성을 올바르게 비교할 수 있습니다.

참고 자료:
- [Equatable 라이브러리 공식 문서](https://pub.dev/packages/equatable)
- [Effective Dart: Equality](https://dart.dev/guides/language/effective-dart/design#avoid-implementing-equality-for-different-logical-instances)