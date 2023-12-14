---
layout: post
title: "[kotlin] MVVM 아키텍처에서의 의존성 주입(Dependency Injection) 패턴"
description: " "
date: 2023-12-15
tags: [kotlin]
comments: true
share: true
---

의존성 주입은 객체 간 의존 관계를 만들어 주입하는 방식으로 이루어집니다. MVVM 아키텍처에서의 의존성 주입은 ViewModel이 Repository나 UseCase와 같은 외부 의존성을 직접 생성하는 것이 아니라, 외부에서 이러한 의존성을 제공받도록 설계되어야 합니다.

의존성 주입을 위해 Dagger, Koin, Hilt와 같은 라이브러리를 사용할 수 있습니다. Kotlin에서는 Koin이나 Dagger와 같은 의존성 주입 라이브러리를 사용하여 ViewModel이나 Repository 등을 주입할 수 있습니다. 이를 통해 코드의 유연성을 높일 수 있고, 테스트 용이성을 개선할 수 있으며, 결합도를 줄일 수 있습니다.

의존성 주입 패턴을 통해 MVVM 아키텍처를 더 효율적으로 구현할 수 있으며, 앱의 유지보수성과 확장성을 향상시킬 수 있습니다.

의존성 주입 패턴을 적용하여 MVVM 아키텍처를 보다 견고하고 유연하게 구현하는 것은 안드로이드 앱의 품질을 향상시키는 데 중요한 일입니다.

### 참고 자료
- Dagger: [https://dagger.dev/](https://dagger.dev/)
- Koin: [https://insert-koin.io/](https://insert-koin.io/)
- Hilt: [https://developer.android.com/training/dependency-injection/hilt-android](https://developer.android.com/training/dependency-injection/hilt-android)