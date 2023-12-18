---
layout: post
title: "[kotlin] 코틀린을 사용하여 Android Jetpack의 ViewModel 기능을 사용하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

Android Jetpack은 안드로이드 앱 개발을 위한 기능들을 모은 라이브러리이다. 그 중에서도 ViewModel은 화면 회전과 같은 구성 변경 시에도 데이터를 유지하고 관리하는 데 도움을 주는 기능이다. 코틀린을 사용하여 Android Jetpack의 ViewModel을 어떻게 활용하는지 알아보자.

## 1. ViewModel 라이브러리 추가

먼저 `build.gradle` 파일에 다음과 같이 ViewModel 라이브러리를 추가한다.

```gradle
implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:2.3.1"
```

## 2. ViewModel 생성

ViewModel을 생성하기 위해서는 `ViewModel` 클래스를 상속받아 해당 액티비티 또는 프래그먼트에 대한 데이터를 관리하는 로직을 구현한다. 

```kotlin
import androidx.lifecycle.ViewModel

class MyViewModel : ViewModel() {
    // 데이터 및 비즈니스 로직 관리
}
```

## 3. ViewModel과 View 바인딩

액티비티 또는 프래그먼트에서 ViewModel을 생성하고 사용하는 방법은 다음과 같다.

```kotlin
class MyActivity : AppCompatActivity() {
    private val viewModel by viewModels<MyViewModel>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_my)

        // ViewModel 사용 예시
        viewModel.someData.observe(this, Observer {
            // 데이터 업데이트 시 처리
        })
    }
}
```

## 요약

코틀린을 사용하여 Android Jetpack의 ViewModel을 활용하는 방법은 간단하다. ViewModel을 생성하고 액티비티 또는 프래그먼트에서 그것을 사용하여 데이터를 관리하고 화면에 반영하는 것이 주요한 포인트이다.

더 자세한 정보는 [Android 공식 문서](https://developer.android.com/topic/libraries/architecture/viewmodel)에서 확인할 수 있다.