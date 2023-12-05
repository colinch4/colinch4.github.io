---
layout: post
title: "[flutter] 플러터에서 Dependency Injection을 위한 Injectable의 활용"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

## 소개
의존성 주입(Dependency Injection)은 애플리케이션의 구성 요소 간의 의존 관계를 인스턴스화하는 과정을 대신해줌으로써 코드의 유연성과 재사용성을 향상시키는 패턴입니다. 이러한 패턴을 효과적으로 구현하기 위해 "Injectable"이라는 이름의 플러터 패키지를 사용할 수 있습니다.

## Injectable 패키지 소개
Injectable 패키지는 플러터 어플리케이션에서 의존성 주입을 구현하기 위한 패키지입니다. 여러 가지 기능을 제공하여 의존성 주입을 쉽고 효율적으로 할 수 있도록 도와줍니다.

### 주요 기능
Injectable 패키지의 주요 기능은 다음과 같습니다:
- 의존성 주입을 위한 주석 기반 설정
- 자동으로 코드 생성하여 의존성 주입 클래스를 생성
- Singleton, LazySingleton, Factory 등 다양한 의존성 주입 방식 지원

## 사용 방법
아래 예제에서는 Injectable 패키지를 사용하여 플러터 애플리케이션에서 의존성 주입을 구현하는 방법을 설명합니다.

### 1. Injectable 패키지 및 어노테이션 추가
먼저, 프로젝트의 `pubspec.yaml` 파일에 Injectable 패키지 의존성을 추가해야 합니다:

```
dependencies:
  injectable: ^1.0.0
```

그리고 main.dart 파일에서 Injectable 패키지를 import 합니다:

```dart
import 'package:injectable/injectable.dart';
```

### 2. 의존성 주입 클래스 생성
다음으로, 의존성 주입이 필요한 클래스를 생성합니다. 예를 들어, `DatabaseManager` 클래스를 생성해보겠습니다:

```dart
@LazySingleton(as: DatabaseManager)
class DatabaseManagerImpl implements DatabaseManager {
  // DatabaseManager 인터페이스 구현
}
```

위의 코드에서 `@LazySingleton(as: DatabaseManager)` 어노테이션은 `DatabaseManagerImpl` 클래스가 `DatabaseManager` 인터페이스의 구현체임을 나타냅니다. `@LazySingleton`은 첫 번째 인스턴스 요청시에만 인스턴스를 생성하는 싱글톤 방식으로 의존성을 주입합니다.

### 3. 의존성 주입 설정
의존성 주입 설정을 위해 `injectable` 어노테이션을 사용하여 설정 파일을 생성해야 합니다. 프로젝트 루트 경로에 `injection.iconfig.dart` 파일을 생성하고, 다음과 같이 내용을 작성합니다:

```dart
import 'package:injectable/injectable.dart';
import 'package:your_app_name/main.dart';

@InjectableInit()
void configureDependencies() => $initGetIt(getIt);
```

위의 코드에서 `main.dart` 파일에서 import한 `injectable.dart`를 이용하여 의존성 주입 설정을 초기화합니다.

### 4. 사용하기
이제 의존성 주입이 필요한 클래스 내에서 `GetIt` 인스턴스를 이용하여 의존성을 주입할 수 있습니다:

```dart
final databaseManager = GetIt.instance.get<DatabaseManager>();
```

위의 코드에서 `GetIt.instance.get<DatabaseManager>()`는 `DatabaseManager` 의존성 주입을 요청하는 방법입니다.

## 마무리
이와 같이 Injectable 패키지를 사용하면 플러터에서 쉽게 의존성 주입을 구현할 수 있습니다. 의존성 주입을 통해 코드의 유지 보수성과 재사용성을 향상시키며, 애플리케이션 개발을 더욱 효율적으로 할 수 있습니다.

## 참고 자료
- [Injectable GitHub Repository](https://github.com/google/inject.dart)