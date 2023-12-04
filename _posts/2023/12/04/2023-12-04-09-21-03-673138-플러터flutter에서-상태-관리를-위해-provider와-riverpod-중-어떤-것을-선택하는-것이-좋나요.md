---
layout: post
title: "[flutter] 플러터(Flutter)에서 상태 관리를 위해 Provider와 Riverpod 중 어떤 것을 선택하는 것이 좋나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

상태 관리는 플러터(Flutter) 앱 개발에서 매우 중요한 부분입니다. 상태 관리를 효과적으로 수행하기 위해 Provider와 Riverpod는 두 가지 인기있는 선택지입니다.

Provider는 플러터(Flutter) 팀에서 공식적으로 지원하는 상태 관리 패키지입니다. Provider는 단순하고 직관적인 API를 제공하여 상태 관리를 간편하게 할 수 있도록 도와줍니다. Provider는 InheritedWidget을 사용하여 모든 자식 위젯에 상태를 전달하며, 위젯 트리를 효율적으로 업데이트하여 퍼포먼스를 최적화합니다. Provider는 확장성이 뛰어나며, 다양한 상태 관리 패턴 (예: Provider, ChangeNotifier, StreamBuilder)을 지원합니다.

Riverpod는 Provider의 새로운 버전으로, 개발자인 Remi Rousselet이 만든 패키지입니다. Riverpod는 Provider의 개선된 버전이며, 다양한 새로운 기능과 향상된 성능을 제공합니다. Riverpod는 상태 관리를 위해 Provider를 사용하지만, Provider보다 더욱 간결한 문법과 직관적인 API를 제공합니다. Riverpod는 Provider의 문제점인 "BuildContext" 의존성을 해결하고, 명시적인 상태 종속성 관리를 가능하게 합니다. Riverpod는 또한 Flutter DevTools와의 통합을 지원하여 디버깅과 프로파일링을 보다 쉽게 할 수 있도록 도와줍니다.

어떤 것을 선택하는 것이 좋을까요? Provider는 플러터(Flutter)팀의 공식 지원을 받으므로 안정적이고 성숙한 패키지입니다. Provider를 이미 사용해 보았거나 Provider에서 제공하는 기능으로 충분하다고 판단된다면, 계속해서 Provider를 사용하는 것이 좋습니다. 그러나 새로운 프로젝트를 시작하거나 향상된 기능과 성능을 원한다면 Riverpod를 고려해 볼 수 있습니다.

두 패키지는 모두 좋은 상태 관리 도구로 선택할 수 있지만, 프로젝트의 요구 사항, 개발 팀의 선호도, 그리고 개인적인 취향에 따라 선택할 수 있습니다. 어느 것을 선택하든, 잘 동작하는 상태 관리 시스템을 구축하기 위해 문서를 참조하고 예제 코드를 살펴보는 것이 좋습니다.