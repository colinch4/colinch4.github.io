---
layout: post
title: "[flutter] 플러터에서 Injectable을 사용한 테스트 주도 개발(Test-Driven Development)의 예시"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 디자인과 개발을 함께 진행할 수 있는 크로스 플랫폼 프레임워크입니다. 이번 글에서는 플러터에서 Injectable을 사용하여 테스트 주도 개발(Test-Driven Development, TDD)을 어떻게 진행할 수 있는지 예시를 들어 알아보겠습니다.

## 1. Injectable 라이브러리 설치

먼저, 테스트 주도 개발(TDD)을 위해서 ```injectable``` 라이브러리를 프로젝트에 추가해야 합니다. 이 라이브러리는 의존성 주입(Dependency Injection)을 쉽게 구현할 수 있도록 도와줍니다. ```pubspec.yaml``` 파일의 ```dependencies``` 섹션에 다음 코드를 추가합니다:

```yaml
dependencies:
  injectable: ^1.2.0
  # 다른 종속성들
```

그리고 터미널에서 다음 커맨드를 실행하여 의존성을 가져옵니다:

```bash
flutter pub get
```

## 2. Injectable 설정

다음으로, 테스트할 대상 클래스에 Injectable 어노테이션을 추가해야 합니다. 예를 들어, 간단한 계산기를 만들어보겠습니다. 

```dart
import 'package:injectable/injectable.dart';

@injectable
class Calculator {
  int add(int a, int b) {
    return a + b;
  }
}
```

위의 코드에서 ```@injectable```어노테이션은 Calculator 클래스에서 의존성 주입을 사용한다는 것을 나타냅니다.

## 3. Test 처리

이제 Calculator 클래스의 테스트를 작성해보겠습니다. ```calculator_test.dart``` 파일을 생성하고 다음과 같이 작성합니다:

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:injectable/injectable.dart';

import 'package:your_project/calculator.dart';

@injectable
void main() {
  group('Calculator', () {
    Calculator calculator;

    setUp(() {
      configureInjection(InjectableEnvironment.test);
      calculator = getIt<Calculator>();
    });

    test('1 + 1 = 2', () {
      expect(calculator.add(1, 1), 2);
    });

    test('3 + 5 = 8', () {
      expect(calculator.add(3, 5), 8);
    });
  });
}
```

위의 코드는 Calculator 클래스의 테스트를 작성하는 과정을 보여줍니다. ```setUp``` 메소드에서 ```configureInjection``` 함수를 호출하여 의존성 주입을 설정하고, ```getIt``` 함수를 사용하여 Calculator 클래스의 인스턴스를 가져옵니다. 그리고 ```test``` 메소드를 사용하여 테스트 케이스를 작성합니다.

## 4. 테스트 실행

이제 테스트를 실행해보겠습니다. 터미널에서 다음 커맨드를 실행합니다:

```bash
flutter test
```

위 커맨드는 테스트를 실행하고 결과를 출력합니다. 테스트가 실패할 경우 오류 메시지와 함께 원인을 파악할 수 있습니다.

## 결론

이번 글에서는 플러터(Flutter)에서 Injectable을 사용하여 테스트 주도 개발(Test-Driven Development, TDD)을 어떻게 진행할 수 있는지 예시를 알아보았습니다. Injectable 라이브러리를 사용하면 의존성 주입을 간편하게 구현할 수 있으며, 테스트를 작성하고 실행하는 과정을 통해 안정적인 앱을 개발할 수 있습니다.

**참고 자료:**
- [Injectable 문서](https://pub.dev/packages/injectable)
- [의존성 주입(Dependency Injection)이란?](https://ko.wikipedia.org/wiki/의존성_주입)