---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 DataStore를 사용하여 사용자 데이터를 저장하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

안녕하세요! 이번 포스트에서는 코틀린과 Android Jetpack의 DataStore를 사용하여 사용자 데이터를 저장하는 방법에 대해 알아보겠습니다.

## DataStore란 무엇인가요?

DataStore는 안드로이드 앱에서 간단한 키-값 쌍 형태의 데이터를 안전하게 저장하고 관리할 수 있는 라이브러리입니다. DataStore는 SharedPreferences와는 달리 비동기적으로 데이터를 저장하고 읽어오며, 안전하게 데이터를 암호화할 수 있습니다.

## DataStore 설정

먼저, `build.gradle` 파일에 DataStore를 추가합니다.

```kotlin
dependencies {
    implementation "androidx.datastore:datastore-preferences:1.0.0"
}
```

DataStore의 사용을 시작하기 위해 앱의 `Application` 클래스에서 초기화합니다.

```kotlin
class MyApplication : Application() {
    val dataStore: DataStore<Preferences> by lazy {
        applicationContext.createDataStore(name = "settings")
    }
    // ...
}
```

## 데이터 저장하기

사용자 데이터를 저장하기 위해 `Preferences` 클래스를 사용합니다.

```kotlin
data class UserSettings(val username: String, val age: Int)

suspend fun saveUserSettings(username: String, age: Int, dataStore: DataStore<Preferences>) {
    dataStore.edit { preferences ->
        preferences[KEY_USERNAME] = username
        preferences[KEY_AGE] = age
    }
}

private object PreferencesKeys {
    val KEY_USERNAME = preferencesKey<String>("key_username")
    val KEY_AGE = preferencesKey<Int>("key_age")
}
```

위 코드에서 `saveUserSettings` 함수를 호출하여 사용자 설정을 저장할 수 있습니다.

## 데이터 불러오기

저장된 사용자 데이터를 불러오기 위해서는 다음과 같이 코드를 작성할 수 있습니다.

```kotlin
suspend fun getUserSettings(dataStore: DataStore<Preferences>): UserSettings {
    val preferences = dataStore.data.first()
    val username = preferences[PreferencesKeys.KEY_USERNAME] ?: "default_username"
    val age = preferences[PreferencesKeys.KEY_AGE] ?: 0
    return UserSettings(username, age)
}
```

## 요약

이렇게 DataStore를 사용하여 안드로이드 앱에서 사용자 데이터를 저장하고 관리하는 방법에 대해 알아보았습니다. DataStore는 SharedPreferences보다 더 안전하고 효율적으로 데이터를 다룰 수 있습니다. 안드로이드 앱에서 데이터를 다룰 때는 DataStore를 고려해보시기 바랍니다.

더 많은 정보를 원하시면 [Android Developers 공식 문서](https://developer.android.com/topic/libraries/architecture/datastore)를 참고하시기 바랍니다.