---
layout: post
title: "[kotlin] 코틀린으로 Android Jetpack의 Navigation 구성 요소를 이용하여 깊은 링크 기능을 구현하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

## Navigation 그래프 설정
먼저, Navigation 그래프에 목적지(destination) 및 깊은 링크를 추가해야 합니다. 예를 들어, `nav_graph.xml` 파일을 열고 아래와 같이 목적지 및 깊은 링크를 추가합니다.

```xml
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/nav_graph"
    app:startDestination="@id/mainFragment">

    <fragment
        android:id="@+id/mainFragment"
        android:name="com.example.MainFragment"
        android:label="fragment_main"
        tools:layout="@layout/fragment_main" >
        <deepLink
            android:id="@+id/deepLinkMain"
            app:uri="https://www.example.com/main" />
    </fragment>

    <!-- 다른 목적지들과 깊은 링크 추가 -->
  
</navigation>
```

위의 예제에서는 `mainFragment` 목적지에 `https://www.example.com/main` 깊은 링크를 추가하였습니다.

## Manifest 설정
다음으로, 매니페스트 파일에 앱의 깊은 링크를 설정해야 합니다.

```xml
<activity ...>
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="https" android:host="www.example.com" />
    </intent-filter>
</activity>
```

## DeepLinkListener 구현
마지막으로, 앱 내에서 `DeepLinkListener`를 구현하여 깊은 링크를 처리합니다.

```kotlin
class DeepLinkHandler(private val navController: NavController) {

    fun handleDeepLink(intent: Intent) {
        if (intent.action == Intent.ACTION_VIEW) {
            val deepLink = intent.data
            deepLink?.let {
                navController.handleDeepLink(it)
            }
        }
    }
}
```

위의 예제에서는 `DeepLinkHandler` 클래스를 사용하여 깊은 링크를 처리하고, 해당 링크를 `NavController`에 전달하여 목적지로 이동합니다.

이제 코틀린을 사용하여 Android Jetpack의 Navigation 구성 요소를 활용하여 깊은 링크 기능을 구현하는 방법에 대해 알아보았습니다.