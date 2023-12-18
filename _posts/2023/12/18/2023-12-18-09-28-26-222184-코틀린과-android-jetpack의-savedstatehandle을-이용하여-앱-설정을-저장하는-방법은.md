---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 SavedStateHandle을 이용하여 앱 설정을 저장하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

안드로이드 앱에서 사용자 설정을 저장하고 관리하는 것은 중요한 부분입니다. 안정적으로 설정 정보를 유지하고 복원하기 위해 Android Jetpack의 SavedStateHandle을 사용할 수 있습니다. 이 토픽에서는 코틀린과 Android Jetpack의 SavedStateHandle을 활용하여 앱 설정을 저장하는 방법에 대해 알아보겠습니다.

## SavedStateHandle 이란?

`SavedStateHandle`은 Android Jetpack의 ViewModel을 지원하는 구성요소 중 하나입니다. 이를 사용하면 ViewModel이 구성 변경(예: 회전)으로 인해 파괴되었을 때 상태를 안전하게 보존할 수 있습니다. `SavedStateHandle`은 키-값 쌍으로 데이터를 관리하고, 이를 통해 ViewModel의 상태를 저장하고 복원할 수 있습니다.

## 사용 방법

먼저, `ViewModel` 클래스를 만들고 `SavedStateHandle`을 생성자 매개변수로 전달합니다.

```kotlin
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel

class MyViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {
    // ViewModel 내부에서 SavedStateHandle을 사용하여 데이터 관리
}
```

위와 같이 `ViewModel` 내에서 `SavedStateHandle`을 사용하여 데이터를 관리할 수 있습니다. 예를 들어, 사용자의 설정 값을 저장하고 복원하는 코드는 다음과 같을 수 있습니다.

```kotlin
fun saveSettings(settingKey: String, settingValue: String) {
    savedStateHandle.set(settingKey, settingValue)
}

fun getSettings(settingKey: String): String? {
    return savedStateHandle.get(settingKey)
}
```

위의 코드에서 `saveSettings` 함수는 지정된 키와 값으로 설정을 저장하고, `getSettings` 함수는 지정된 키에 해당하는 설정 값을 반환합니다.

## 예제

다음은 ViewModel 클래스에서 `SavedStateHandle`을 사용하여 사용자 설정을 저장하고 복원하는 간단한 예제입니다.

```kotlin
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel

class SettingsViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {
    
    fun saveSetting(key: String, value: String) {
        savedStateHandle.set(key, value)
    }

    fun getSetting(key: String): String? {
        return savedStateHandle.get(key)
    }
}
```

이제 앱의 사용자 설정을 안전하게 저장하고 관리할 수 있게 되었습니다. 안드로이드 개발에서 사용자 설정을 저장하고 복원하는 데 있어 `SavedStateHandle`은 매우 유용한 도구입니다.

이 상태 관리 기술을 통해 앱의 사용자 경험을 개선하고 사용자가 최근의 설정을 기억할 수 있도록 도울 수 있습니다. 안드로이드 개발에 있어서, 사용자가 앱의 현재 상태와 설정을 보존하고 관리하는 것은 항상 중요한 과제입니다.

## 참고 자료

- [Android Developers - ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel)
- [Android Developers - SavedStateHandle](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle)

위에서 안내드린 자료를 참고하시면 더 많은 정보를 얻을 수 있습니다.