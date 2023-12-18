---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 Navigation 구성 요소를 이용하여 화면 간 전환하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

안녕하세요! 이번에는 코틀린과 Android Jetpack Navigation 구성 요소를 사용하여 화면 간 전환하는 방법에 대해 알아보겠습니다.

## 1. Navigation 구성 요소 추가

먼저, 프로젝트의 `build.gradle` 파일에 아래의 의존성을 추가하여 Navigation 구성 요소를 프로젝트에 포함시킵니다.

```gradle
dependencies {
    def nav_version = "2.3.5"
    implementation "androidx.navigation:navigation-fragment-ktx:$nav_version"
    implementation "androidx.navigation:navigation-ui-ktx:$nav_version"
}
```

## 2. Navigation 그래프 생성

다음으로, `res` 디렉토리 내에 `navigation` 디렉토리를 생성하고, `nav_graph.xml` 파일을 만들어 Navigation 그래프를 정의합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/nav_graph"
    app:startDestination="@id/startingFragment">

    <fragment
        android:id="@+id/startingFragment"
        android:name="com.example.StartingFragment"
        tools:layout="@layout/fragment_starting">
        <action
            android:id="@+id/action_startingFragment_to_destinationFragment"
            app:destination="@id/destinationFragment" />
    </fragment>

    <fragment
        android:id="@+id/destinationFragment"
        android:name="com.example.DestinationFragment"
        android:label="Destination"
        tools:layout="@layout/fragment_destination" />

</navigation>
```

위의 예제에서는 `startingFragment`에서 `destinationFragment`로 전환하는 액션을 정의했습니다.

## 3. Navigation 호스트 추가

이제 Activity 레이아웃 파일에 `<fragment>`를 추가하여 Navigation 호스트를 정의합니다.

```xml
<fragment
    android:id="@+id/nav_host_fragment"
    android:name="androidx.navigation.fragment.NavHostFragment"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:defaultNavHost="true"
    app:navGraph="@navigation/nav_graph" />
```

## 4. 화면 간 전환 실행

화면 간 전환은 Fragment에서 `findNavController().navigate()` 메서드를 사용하여 실행할 수 있습니다.

```kotlin
// Fragment 내에서 화면 전환 실행
button.setOnClickListener {
    findNavController().navigate(R.id.action_startingFragment_to_destinationFragment)
}
```

이렇게하면 코틀린 및 Android Jetpack Navigation 구성 요소를 사용하여 화면 간 전환을 쉽게 구현할 수 있습니다.

더 많은 자세한 내용은 [Android Developers 공식 문서](https://developer.android.com/guide/navigation)를 참고하시기 바랍니다.