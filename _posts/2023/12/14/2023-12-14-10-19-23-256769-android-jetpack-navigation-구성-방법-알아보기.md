---
layout: post
title: "[kotlin] Android Jetpack Navigation 구성 방법 알아보기"
description: " "
date: 2023-12-14
tags: [kotlin]
comments: true
share: true
---

Android 앱을 개발할 때 화면 간 이동을 간편하게 처리하기 위해 Jetpack Navigation 구성을 사용할 수 있습니다. 이를 통해 Android Jetpack Navigation을 어떻게 구성하는지 알아보도록 하겠습니다.

## Jetpack Navigation이란?

**Jetpack Navigation**은 Android Jetpack 라이브러리에 포함된 일부 기능으로, 화면 간 이동 및 깊은 링크(deep linking) 처리를 쉽게 구성할 수 있도록 도와주는 라이브러리입니다. 이를 통해 개발자는 보다 직관적이고 유지보수가 용이한 앱 내에서의 화면 전환을 구현할 수 있습니다.

## Jetpack Navigation 구성 방법

Jetpack Navigation을 구성하는 방법은 다음과 같습니다.

1. **Navigation Graph 생성**: 네비게이션 그래프 파일을 생성하여 앱 내에서의 이동 경로를 정의합니다.
2. **NavHost 설정**: 앱의 메인 액티비티나 프래그먼트에 NavHost를 설정하여 네비게이션 그래프와의 연결을 구축합니다.
3. **액션 및 대상 설정**: 네비게이션 그래프에서 각 화면 간의 이동을 나타내는 액션 및 대상을 설정합니다.
4. **레이아웃 파일에 연결**: 각각의 레이아웃 파일에서 해당하는 NavHost와 네비게이션 그래프를 연결합니다.

간단한 Jetpack Navigation 구성 예시를 살펴보겠습니다.

```kotlin
// navigation_graph.xml
<navigation>
    <fragment
        android:id="@+id/homeFragment"
        android:name="com.example.HomeFragment"
        android:label="fragment_home"
        tools:layout="@layout/fragment_home" >
        <action
            android:id="@+id/action_homeFragment_to_detailFragment"
            app:destination="@id/detailFragment" />
    </fragment>
    <fragment
        android:id="@+id/detailFragment"
        android:name="com.example.DetailFragment"
        android:label="fragment_detail"
        tools:layout="@layout/fragment_detail" />
</navigation>

// activity_main.xml
<androidx.fragment.app.FragmentContainerView
    android:id="@+id/nav_host_fragment"
    android:name="androidx.navigation.fragment.NavHostFragment"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    app:defaultNavHost="true"
    app:navGraph="@navigation/navigation_graph" />
```

## 마무리

이제 Android Jetpack Navigation을 사용하여 간편하고 구조화된 화면 이동 구성을 구현할 수 있게 되었습니다. Jetpack Navigation은 Android 앱의 네비게이션을 보다 효율적으로 관리하고 구성하는 데 도움을 줄 수 있습니다.

더 자세한 정보는 [Android Developers 공식 문서](https://developer.android.com/guide/navigation)를 참고하시기 바랍니다.