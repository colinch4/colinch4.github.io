---
layout: post
title: "[kotlin] 코틀린을 사용하여 Android Jetpack의 Navigation 구성 요소를 적용하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

Android 앱에서 화면 간 전환 및 탐색을 관리하는 것은 매우 중요합니다. Android Jetpack의 Navigation 구성 요소는 이러한 작업을 더 쉽게 만들어주는 라이브러리입니다. 이 라이브러리를 사용하면 화면 간 전환, 깊은 링크, 백 스택 관리 및 **애니메이션 효과** 등을 쉽게 구현할 수 있습니다.

## Navigation 구성 요소 추가

먼저, `build.gradle` 파일에 다음 코드를 추가하여 Navigation 구성 요소를 프로젝트에 추가합니다.

```kotlin
implementation "androidx.navigation:navigation-fragment-ktx:$nav_version"
implementation "androidx.navigation:navigation-ui-ktx:$nav_version"
```

여기서 `$nav_version`은 사용하려는 Navigation 구성 요소 라이브러리의 버전을 나타냅니다.

## NavGraph 생성

NavGraph는 앱의 탐색 구조를 정의하는 데 사용됩니다. `res/navigation` 디렉토리에 새로운 XML 파일을 생성하여 NavGraph를 정의합니다.

```xml
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/nav_graph"
    app:startDestination="@id/firstFragment">

    <fragment
        android:id="@+id/firstFragment"
        android:name="com.example.myapp.FirstFragment"
        android:label="fragment_first"
        tools:layout="@layout/fragment_first">

        <action
            android:id="@+id/action_firstFragment_to_secondFragment"
            app:destination="@id/secondFragment" />

    </fragment>

    <fragment
        android:id="@+id/secondFragment"
        android:name="com.example.myapp.SecondFragment"
        android:label="fragment_second"
        tools:layout="@layout/fragment_second" />

</navigation>
```

## Navigation 호스트 추가

NavHostFragment를 추가하여 NavGraph와 연결하고 화면에 표시합니다.

```xml
<fragment
    android:id="@+id/nav_host_fragment"
    android:name="androidx.navigation.fragment.NavHostFragment"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:defaultNavHost="true"
    app:navGraph="@navigation/nav_graph" />
```

여기서 `nav_graph`는 이전에 정의한 NavGraph 파일의 이름을 나타냅니다.

## ViewModel 생성

다음으로, 화면 간 데이터 교환 및 상태 관리를 위해 ViewModel을 생성합니다.

```kotlin
class MyViewModel : ViewModel() {
    // ViewModel 코드 작성
}
```

## 코틀린 코드에서 Navigation 사용

마지막으로, Kotlin 코드에서 Navigation 구성 요소를 사용하여 화면 간 전환을 처리할 수 있습니다.

```kotlin
val navController = findNavController(R.id.nav_host_fragment)
navController.navigate(R.id.action_firstFragment_to_secondFragment)
```

Navigation 구성 요소를 사용하여 쉽게 Android 앱의 탐색을 관리할 수 있습니다. 이를 통해 화면 간 전환 로직을 보다 간단하게 작성할 수 있으며, 엄격한 백 스택 및 **깊은 링크** 관리 등의 고급 기능을 더 쉽게 구현할 수 있습니다. Kotlin을 사용하여 Android 앱을 개발할 때는 Navigation 구성 요소를 적극적으로 활용하여 보다 효율적인 앱을 구축할 수 있습니다.

더 자세한 내용은 [공식 Android 개발자 사이트](https://developer.android.com/guide/navigation)를 참고하세요.