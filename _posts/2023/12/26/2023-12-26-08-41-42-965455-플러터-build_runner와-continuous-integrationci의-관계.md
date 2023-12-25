---
layout: post
title: "[flutter] 플러터 build_runner와 Continuous Integration(CI)의 관계"
description: " "
date: 2023-12-26
tags: [flutter]
comments: true
share: true
---
- [플러터 build_runner란 무엇인가요?](#플러터-build_runner란-무엇인가요)
- [Continuous Integration(CI)이란 무엇인가요?](#continuous-integrationci이란-무엇인가요)
- [플러터 build_runner와 CI의 관계는 무엇인가요?](#플러터-build_runner와-ci의-관계는-무엇인가요)
- [CI에서 플러터 build_runner를 어떻게 사용할 수 있을까요?](#ci에서-플러터-build_runner를-어떻게-사용할-수-있을까요)
- [결론](#결론)

---

## 플러터 build_runner란 무엇인가요?
플러터 프레임워크는 `build_runner` 도구를 사용하여 반복적이고 번거로운 작업들을 자동화하는 데 사용됩니다. 이 도구를 사용하면 애너테이션 처리, 코드 생성, 파일/폴더 생성 등을 자동화할 수 있습니다.

## Continuous Integration(CI)이란 무엇인가요?
Continuous Integration(CI)은 소프트웨어 개발 과정의 일환으로, 자동화된 빌드 및 테스트 프로세스를 통해 팀 내 여러 명의 개발자가 작업한 코드를 통합하는 것을 의미합니다. CI를 통해 코드 변경사항을 신속하게 통합하고 품질을 유지할 수 있습니다.

## 플러터 build_runner와 CI의 관계는 무엇인가요?
플러터 애플리케이션에서 `build_runner`를 이용하여 코드 생성 및 자동화된 작업을 처리하면 CI 시스템을 사용하여 이러한 작업을 최적화할 수 있습니다. CI는 빌드 및 테스트를 자동화하는 것이 목적이므로, `build_runner`와 함께 사용하면 애플리케이션 빌드 프로세스를 효율적으로 관리할 수 있습니다.

## CI에서 플러터 build_runner를 어떻게 사용할 수 있을까요?
CI 시스템에서 플러터 `build_runner`를 사용하려면 해당 시스템의 설정 파일에 `build_runner` 명령을 추가하여 실행해야 합니다. 예를 들어, Jenkins나 Travis CI와 같은 CI 도구를 사용한다면 해당 도구의 설정 파일에 `build_runner` 명령을 추가하여 플러터 애플리케이션의 빌드 프로세스를 자동화할 수 있습니다.

아래는 `build_runner` 명령을 사용하여 플러터 프로젝트를 빌드하는 예시입니다.

```yaml
# pubspec.yaml
dev_dependencies:
  build_runner: ^1.12.2
  flutter_test:
    sdk: flutter

# 터미널에서 실행
flutter pub get
flutter pub run build_runner build
```

## 결론
플러터 애플리케이션의 빌드 및 자동화 작업을 처리하기 위해 `build_runner`를 사용하고, CI 시스템을 통해 코드 변경사항을 신속하게 통합하고 개발 및 빌드 프로세스를 최적화할 수 있습니다.