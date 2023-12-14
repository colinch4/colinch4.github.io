---
layout: post
title: "[kotlin] LiveData와 Observable 등 MVVM 아키텍처에서 사용되는 데이터 관찰 방식"
description: " "
date: 2023-12-15
tags: [kotlin]
comments: true
share: true
---

안녕하세요! 이번에는 안드로이드 앱에서 MVVM(MVVM - Model-View-ViewModel) 아키텍처를 사용할 때 데이터를 관찰하고 업데이트하는 방법에 대해 알아보겠습니다. MVVM 아키텍처에서는 데이터 바인딩과 함께 데이터 관찰을 통해 UI 업데이트를 처리하는데, 여기서는 주로 `LiveData`와 `Observable`이 사용됩니다.

## 1. LiveData

`LiveData`는 안드로이드 아키텍처 컴포넌트 라이브러리에서 제공하는 클래스로, 생명주기를 인식하여 관찰 가능한 데이터 홀더입니다. 이를 통해 데이터가 변경될 때마다 관련된 UI를 자동으로 업데이트할 수 있습니다. 

```kotlin
val liveData: LiveData<String> = MutableLiveData()
```

위의 코드에서 `liveData`는 `String` 타입의 데이터를 보유하는 `LiveData` 객체를 선언합니다. 데이터가 변경될 때마다 UI 업데이트가 자동으로 처리됩니다.

## 2. Observable

`Observable`은 안드로이드에서는 주로 RxJava나 Kotlin의 `Observable` 등이 사용됩니다. MVVM 아키텍처에서는 `Observable`을 통해 데이터 변경을 감지하고 UI를 업데이트합니다.

```kotlin
val data: Observable<String> = Observable.create {
    // 데이터 변경 로직
}
```

`Observable`을 사용하여 데이터 변경을 감지하고, 해당 데이터로 UI를 업데이트할 수 있습니다.

## 결론

MVVM 아키텍처에서는 `LiveData`와 `Observable`을 통해 데이터 관찰과 UI 업데이트를 효과적으로 처리할 수 있습니다. 두 방식 모두 데이터 변화를 관찰하고, 이에 따라 UI를 업데이트하는데 사용됩니다.

이상으로 MVVM 아키텍처에서 사용되는 데이터 관찰 방식에 대해 알아보았습니다. 감사합니다!

자료 참고: 
- [Android Developers - LiveData](https://developer.android.com/topic/libraries/architecture/livedata)
- [ReactiveX - RxJava](http://reactivex.io/)