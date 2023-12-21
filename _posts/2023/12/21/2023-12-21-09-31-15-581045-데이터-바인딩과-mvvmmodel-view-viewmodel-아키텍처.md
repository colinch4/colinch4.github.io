---
layout: post
title: "[android] 데이터 바인딩과 MVVM(Model-View-ViewModel) 아키텍처"
description: " "
date: 2023-12-21
tags: [android]
comments: true
share: true
---

안드로이드 앱을 개발할 때 데이터 관리와 UI 업데이트를 효율적으로 처리하기 위해 데이터 바인딩과 MVVM(Model-View-ViewModel) 아키텍처를 사용하는 것이 유용합니다. 

본 포스트에서는 안드로이드 앱에서 데이터 바인딩과 MVVM 아키텍처를 어떻게 사용하는지 알아보겠습니다.

## 1. 데이터 바인딩(Data Binding)이란?

데이터 바인딩은 레이아웃과 데이터를 손쉽게 바인딩할 수 있도록 하는 안드로이드 라이브러리입니다. XML 레이아웃 파일에서 표현된 UI 요소들과 그에 해당하는 데이터를 쉽게 연결할 수 있게 도와줍니다. 

다음은 데이터 바인딩을 사용한 XML 레이아웃 파일의 예제 코드입니다.

```xml
<layout xmlns:android="http://schemas.android.com/apk/res/android">
    <data>
        <variable
            name="user"
            type="com.example.mvvm.User" />
    </data>
    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{user.name}" />

        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Update Name"
            android:onClick="@{() -> viewModel.updateName()}" />
    </LinearLayout>
</layout>
```

위 코드에서 `@{user.name}`은 User 객체의 name 속성과 연결되어 텍스트 뷰에 표시됩니다.

## 2. MVVM(Model-View-ViewModel) 아키텍처란?

MVVM 아키텍처는 Model, View, ViewModel 3가지 요소로 구성됩니다. 

- **Model**: 데이터와 비즈니스 로직을 다루는 부분
- **View**: 사용자에게 보여지는 UI를 담당하는 부분
- **ViewModel**: View와 Model 사이에서 상호작용을 중개하고 View가 표시해야 할 데이터를 가공하는 부분

다음은 간단한 MVVM 아키텍처의 예제 코드입니다.

```kotlin
class UserViewModel : ViewModel() {
    private val _username = MutableLiveData<String>()
    val username: LiveData<String> get() = _username

    fun updateName(newName: String) {
        _username.value = newName
    }
}
```
```kotlin
class UserActivity : AppCompatActivity() {

    private lateinit var userViewModel: UserViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val binding: ActivityUserBinding = DataBindingUtil.setContentView(this, R.layout.activity_user)
        binding.lifecycleOwner = this

        userViewModel = ViewModelProvider(this).get(UserViewModel::class.java)
        binding.user = userViewModel

        binding.updateButton.setOnClickListener {
            userViewModel.updateName("New Name")
        }
    }
}
```

위 코드는 UserActivity에서 UserViewModel을 생성하고 데이터 바인딩을 통해 View와 ViewModel을 연결하는 예제입니다.

## 3. 데이터 바인딩과 MVVM 아키텍처의 혜택

- **UI 업데이트의 단순화**: 데이터 바인딩을 통해 UI 요소를 쉽게 갱신할 수 있으며, MVVM 아키텍처를 사용하면 비즈니스 로직과 UI 업데이트를 분리하여 구현할 수 있습니다.
- **코드 재사용성**: MVVM 아키텍처를 통해 ViewModel을 개발하면 View와 분리되므로 재사용성이 높아집니다.
- **테스트 용이성**: MVVM 아키텍처를 사용하면 ViewModel의 단위 테스트를 쉽게 구현할 수 있습니다.

데이터 바인딩과 MVVM 아키텍처는 안드로이드 앱의 개발 생산성을 향상시키고 유지보수를 용이하게 만들어줍니다. 이러한 이점을 고려하여 안드로이드 앱을 개발할 때 데이터 바인딩과 MVVM 아키텍처를 적극적으로 활용해보시기 바랍니다.

## 참고 자료
- [Android Developers - Data Binding Library](https://developer.android.com/topic/libraries/data-binding)
- [Android Developers - Guide to App Architecture](https://developer.android.com/jetpack/guide)