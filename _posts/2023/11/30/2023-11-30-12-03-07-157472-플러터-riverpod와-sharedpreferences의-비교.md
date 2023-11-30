---
layout: post
title: "[flutter] 플러터 Riverpod와 SharedPreferences의 비교"
description: " "
date: 2023-11-30
tags: [flutter]
comments: true
share: true
---

플러터(Flutter)는 사용자 인터페이스를 개발하기 위한 훌륭한 프레임워크입니다. 그러나 앱에서 상태 관리나 데이터 저장이 필요할 때에는 추가적인 도구나 패키지를 사용해야 합니다. 이번 포스트에서는 Riverpod와 SharedPreferences라는 두 가지 접근 방식을 비교해보고, 각각의 특징과 장단점을 알아보겠습니다.

## Riverpod

Riverpod는 플러터 프레임워크의 상태 관리 솔루션 중 하나로, Provider 패턴에 기반을 둔 패키지입니다. Riverpod를 사용하면 앱 전역에서 상태를 쉽게 공유하고 업데이트할 수 있습니다. Riverpod는 변경 가능한 상태를 제공하는 Provider를 통해 상태를 관리하며, ChangeNotifier나 Stream 등과 함께 사용할 수 있습니다.

Riverpod의 장점은 다음과 같습니다:
- Provider 패턴을 사용하여 상태를 관리하기 때문에 코드가 간결하고 읽기 쉽습니다.
- 앱 전역에서 상태를 공유하고 업데이트할 수 있으므로, 다른 위젯들 간에 손쉽게 데이터를 전달할 수 있습니다.
- Provider 패턴의 장점인 의존성 주입(Dependency Injection)을 활용하여 유연하게 상태를 관리할 수 있습니다.

Riverpod의 단점은 다음과 같습니다:
- 러닝 커브가 있는 것이 일부 사용자들에게는 어려울 수 있습니다.
- 상태의 업데이트에 따른 콜백 함수를 작성해야 하는 경우, 이를 관리하는 것이 조금 복잡해질 수 있습니다.

## SharedPreferences

SharedPreferences는 안드로이드 플랫폼에서 데이터를 지속적으로 저장하기 위한 기능입니다. Flutter 앱에서도 SharedPreferences 패키지를 사용하여 앱의 설정이나 사용자 데이터를 저장할 수 있습니다. SharedPreferences는 사용자의 기기에 키-값 형식으로 데이터를 저장하는 기능을 제공합니다.

SharedPreferences의 장점은 다음과 같습니다:
- 간단하고 간편한 사용법으로, 개발자가 쉽게 데이터를 저장하고 가져올 수 있습니다.
- 기기에 데이터를 저장하기 때문에 앱을 종료하고 재실행해도 데이터가 유지됩니다.

SharedPreferences의 단점은 다음과 같습니다:
- 앱의 전역 상태 관리에는 적합하지 않습니다. SharedPreferences는 단순한 키-값 저장소로, 상태 관리를 위한 고급 기능을 제공하지 않습니다.
- 데이터를 읽고 쓰는 과정이 비동기적으로 처리되기 때문에 앱의 성능에 영향을 줄 수 있습니다.

## 비교 결과

Riverpod와 SharedPreferences는 각각 데이터의 관점에서 다른 방식으로 접근합니다. Riverpod는 플러터 앱 전역에서 상태 관리를 위한 솔루션으로 사용할 수 있지만, SharedPreferences는 단순한 키-값 저장소로 사용됩니다. 따라서, 앱의 상태 관리나 복잡한 데이터 처리가 필요한 경우에는 Riverpod를 사용하는 것이 좋습니다. 반면에, 단순한 설정값이나 사용자 기본 설정을 저장하는 등의 간단한 데이터 저장에는 SharedPreferences를 사용하는 것이 편리할 수 있습니다.

물론, 상황에 따라 Riverpod와 SharedPreferences를 함께 사용할 수도 있습니다. 앱의 필요에 따라 적절한 도구를 선택하여 사용하면 됩니다.

## 결론

Riverpod와 SharedPreferences는 플러터 앱 개발에서 상태 관리와 데이터 저장에 유용한 도구입니다. Riverpod는 상태 관리에 더 특화되어 있으며, SharedPreferences는 단순한 데이터 저장에 적합합니다. 앱의 요구사항에 맞게 적절한 도구를 선택하여 프로젝트를 진행하면 됩니다.