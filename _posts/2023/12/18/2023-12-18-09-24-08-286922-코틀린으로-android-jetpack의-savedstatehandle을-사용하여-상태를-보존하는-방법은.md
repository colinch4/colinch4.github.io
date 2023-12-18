---
layout: post
title: "[kotlin] 코틀린으로 Android Jetpack의 SavedStateHandle을 사용하여 상태를 보존하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

Android Jetpack의 SavedStateHandle을 사용하여 상태를 보존하는 기본적인 방법에 대해 알아보겠습니다.

1. **의존성 추가**: 먼저 `build.gradle` 파일에 아래의 의존성을 추가합니다.

```gradle
implementation "androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0"
```

2. **ViewModel에 SavedStateHandle 주입**: ViewModel 클래스의 생성자에서 SavedStateHandle을 주입받도록 설정합니다.

```kotlin
class YourViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {
    // ViewModel 내에서 SavedStateHandle을 사용하여 상태를 저장하거나 로드할 수 있습니다.
}
```

3. **상태 저장 및 로드**: ViewModel 내에서 SavedStateHandle을 사용하여 상태를 저장하고 로드할 수 있습니다. 

```kotlin
// 상태 저장
savedStateHandle.set("your_key", yourState)

// 상태 로드
val yourState = savedStateHandle.get<YourType>("your_key") ?: defaultValue
```

이러한 방식으로, SavedStateHandle을 사용하여 Android Jetpack에서 상태를 보존할 수 있습니다. 또한, 앱의 수명 주기에 대한 처리를 ViewModel에 위임하여, 상태를 안전하게 보존할 수 있습니다.

더 자세한 정보는 [Android 개발자 사이트](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle)를 참고하세요.