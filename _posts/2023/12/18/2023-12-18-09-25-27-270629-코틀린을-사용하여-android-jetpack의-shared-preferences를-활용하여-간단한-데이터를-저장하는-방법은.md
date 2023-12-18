---
layout: post
title: "[kotlin] 코틀린을 사용하여 Android Jetpack의 Shared Preferences를 활용하여 간단한 데이터를 저장하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

안드로이드 앱에서 간단한 데이터를 저장하기 위해 Shared Preferences를 활용할 수 있습니다. Shared Preferences는 쉽게 접근할 수 있는 키-값 쌍으로 데이터를 저장하는데 사용됩니다. 이 기능은 안드로이드 Jetpack 라이브러리에서 제공되며, 코틀린으로 쉽게 활용할 수 있습니다.

## 1. 의존성 추가

먼저, build.gradle 파일에 다음 의존성을 추가합니다.

```kotlin
implementation 'androidx.preference:preference-ktx:1.1.1'
```

## 2. Shared Preferences 초기화

앱의 액티비티나 프래그먼트에서 Shared Preferences를 초기화하고저, 다음 코드를 사용합니다.

```kotlin
val sharedPref = requireActivity().getPreferences(Context.MODE_PRIVATE)
```

## 3. 데이터 저장

간단한 데이터 (예: 사용자 설정)를 저장하기 위해 다음과 같이 코드를 작성할 수 있습니다.

```kotlin
with (sharedPref.edit()) {
    putString("key", "value")
    apply()
}
```

## 4. 데이터 불러오기

저장된 데이터를 불러오려면 다음과 같이 코드를 작성합니다.

```kotlin
val value = sharedPref.getString("key", "default value")
```

위의 코드에서 "key"는 저장할 데이터의 식별자이고, "default value"는 "key"에 해당하는 값이 없을 때 반환할 기본 값입니다.

## 마무리

간단한 데이터를 저장하고 불러오는 것은 안드로이드 앱 개발에서 빈번하게 사용되며, Shared Preferences는 이를 쉽게 처리할 수 있는 방법을 제공합니다. 안드로이드 Jetpack의 Shared Preferences를 활용하면 코드를 간결하게 유지하면서 안정적으로 데이터를 저장하고 사용할 수 있습니다.

더 자세한 내용은 [Shared Preferences 공식 문서](https://developer.android.com/reference/androidx/preference/package-summary)를 참고하세요.