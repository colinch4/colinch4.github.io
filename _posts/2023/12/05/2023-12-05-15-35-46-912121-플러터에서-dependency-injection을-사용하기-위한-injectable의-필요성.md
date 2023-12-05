---
layout: post
title: "[flutter] 플러터에서 Dependency Injection을 사용하기 위한 Injectable의 필요성"
description: " "
date: 2023-12-05
tags: [flutter]
comments: true
share: true
---

## 소개
플러터(Flutter)는 크로스 플랫폼 모바일 애플리케이션 개발을 위한 작고 빠른 UI 프레임워크입니다. 대부분의 플러터 앱은 의존성 주입(Dependency Injection, DI) 패턴을 사용하여 앱의 모듈화, 테스트 용이성 및 유연성을 향상시킵니다. 이를 위해 `injectable` 패키지는 매우 유용한 도구입니다.

## Dependency Injection이란?
의존성 주입은 앱 내에서 객체 간의 의존성을 외부에서 결정하고 제공하는 디자인 패턴입니다. 이를 통해 코드의 재사용성, 유지 보수성 및 테스트 용이성이 증가하며, 객체 간 결합도를 낮출 수 있습니다. 

## Injectable 패키지
`injectable`은 플러터 애플리케이션에서 DI를 구현하기 위한 패키지입니다. 이 패키지는 `get_it`이라는 서비스 로케이터 패턴과 함께 사용됩니다. `get_it`은 DI 컨테이너로서 객체의 인스턴스를 제공하는 역할을 합니다.

## 사용법
1. `pubspec.yaml` 파일에 `injectable` 및 `get_it` 패키지를 추가합니다.
   ```yaml
   dependencies:
     injectable: ^1.0.0
     get_it: ^3.0.3
   ```

2. 프로젝트 디렉토리에 `injectable`을 적용할 파일을 만듭니다. (`app_module.dart` 등)
   ```dart
   import 'package:injectable/injectable.dart';
   import 'package:get_it/get_it.dart';

   @module
   abstract class AppModule {
     @lazySingleton
     MyService get myService => MyService();
   }

   final GetIt getIt = GetIt.instance;

   @injectableInit
   void configureInjection() => $initGetIt(getIt);
   ```

3. DI를 사용할 클래스에서 `@injectable` 어노테이션을 추가합니다.
   ```dart
   import 'package:injectable/injectable.dart';

   @injectable
   class MyService {
     // ...
   }
   ```

4. `main.dart` 파일에서 DI 설정을 초기화합니다.
   ```dart
   void main() {
     configureInjection();
     runApp(MyApp());
   }
   ```

5. DI를 사용할 클래스를 필요로 하는 곳에서 `getIt`을 통해 인스턴스를 얻어옵니다.
   ```dart
   final myService = getIt<MyService>();
   ```

## 결론
플러터 애플리케이션에서 Dependency Injection을 사용하면 코드의 유연성과 재사용성을 크게 향상시킬 수 있습니다. `injectable` 패키지를 사용하면 DI 패턴을 쉽게 구현할 수 있으며, `get_it`을 통해 객체의 인스턴스를 쉽게 제공할 수 있습니다. 따라서, 앱의 모듈화와 테스트 용이성에 중점을 두는 개발자들은 `injectable` 패키지를 적극 활용할 것을 권장합니다.

## 참고 자료
- [injectable 패키지 문서](https://pub.dev/packages/injectable)
- [get_it 패키지 문서](https://pub.dev/packages/get_it)