---
layout: post
title: "[android] 안드로이드 Continuous Integration의 테스트 전략"
description: " "
date: 2023-12-20
tags: [android]
comments: true
share: true
---

안드로이드 앱을 개발하는 경우, **Continuous Integration (CI)**는 품질을 유지하고 소스코드를 안정적으로 유지하는 데 중요한 요소입니다. 안드로이드 앱의 CI 플로우를 설계할 때 **테스트 전략**을 고려해야 합니다. 이 블로그에서는 안드로이드 CI에서의 테스트 전략에 대해 살펴보겠습니다.

## 테스트 유형

안드로이드 앱의 CI에서 사용되는 주요 테스트 유형은 다음과 같습니다.

1. **Unit Test**: 단일 모듈이나 함수를 테스트하는데 사용됩니다.
2. **Instrumented Test**: 앱의 동작을 시뮬레이션하여 런타임 환경에서 테스트합니다.
3. **UI Test**: 사용자 인터페이스를 테스트하여 앱의 사용자 경험을 확인합니다.

## 테스트 전략 구성

안드로이드 CI에서 테스트 전략을 구성할 때 다음을 고려해야 합니다.

### 속도와 격리

**Unit Test**를 CI에 통합하여 빠르게 실행되도록 해야 합니다. **Instrumented Test**와 **UI Test**는 시간이 더 소요되므로 별도로 분리하여 실행해야 합니다.

### 테스트 커버리지

모든 테스트 유형을 포함하여 가능한 한 많은 부분을 테스트해야 합니다. 테스트 커버리지를 높이는 것이 중요합니다.

### 모의 데이터와 의존성

테스트 중에 외부 의존성을 최소화하고, 모의 데이터를 사용하여 안정적인 테스트를 보장해야 합니다.

## 테스트 도구

### **JUnit** 및 **Mockito**

**Unit Test**를 위한 표준 도구이며 구성이 간단하고 탄력적입니다. **Mockito**를 사용하여 외부 의존성을 가로막고 테스트를 수행합니다.

### **Espresso**

안드로이드 기반의 **UI Test**를 수행하는데 사용되며, 사용자 인터페이스와 상호작용하는 테스트를 작성할 수 있습니다.

### **Firebase Test Lab**

구글 클라우드 기반의 **Instrumented Test**를 실행하는 데 사용됩니다. 다양한 디바이스 및 버전에서 앱을 테스트할 수 있습니다.

## 결론

안드로이드 앱의 CI 플로우를 구성할 때 효과적인 테스트 전략이 중요합니다. **Unit Test**, **Instrumented Test**, **UI Test**를 적절히 조합하여 안정적이고 효율적인 테스트 환경을 유지할 필요가 있습니다.

---

이 블로그는 안드로이드 CI에서의 테스트 전략에 대해 살펴보았습니다. 테스트 전략을 구성함으로써 안드로이드 앱의 CI의 품질과 안정성을 향상시킬 수 있습니다.

참고문헌:
- https://developer.android.com/training/testing/unit-testing/local-unit-tests
- https://developer.android.com/training/testing/ui-testing/espresso-testing
- https://firebase.google.com/docs/test-lab