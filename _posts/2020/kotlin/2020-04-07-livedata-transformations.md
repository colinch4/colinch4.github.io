---
layout: post
title: "[Kotlin] Transformations로 LiveData 변형하기"
date: 2020-04-07 15:07
category: 
author: kskim2
tags: [kotlin, livedata]
description: "프로젝트 개발시 ViewModel을 사용함과 동시에 궁합이 잘 맞는 LiveData를 많이 사용한다. 그러나 Observavle을 위해  LiveData를 그 자체로만 사용한다면 LiveData의 편리함을 모두 누릴 수 없다. Transformations 클래스를 알아보면서 평소 생각없이 사용했던 LiveData를 더 가치있게 만들어보자."
summary: 
---


프로젝트 개발시 ViewModel을 사용함과 동시에 궁합이 잘 맞는 LiveData를 많이 사용한다. 그러나 Observavle을 위해  `LiveData`를 그 자체로만 사용한다면 LiveData의 편리함을 모두 누릴 수 없다. Transformations 클래스를 알아보면서 평소 생각없이 사용했던 LiveData를 더 가치있게 만들어보자.

## Transformations

Transformations는 LiveData를 위한 클래스이기 때문에 당연히 AAC로 제공된다. 실제 패키지는 아래와 같다.

```kotlin
android.arch.lifecycle.Transformations

```

Transformations 클래스의 도움을 받으면 기본에 선언해 놓았던 LiveData를 변형시켜 개발자 입맛에 맞춰 사용할 수 있다. 공식문서에 소개되어있는 기능으로는 map과 switchMap이 있는데, 함수형을 알고있는 개발자라면 컬렉션에서 제공하는 map과 switchMap과 거의 동일하다고 보면 될것같다.

### Transformations.map

Transformations.map을 알아보기에 앞서 일반 배열의 map을 보자.

```kotlin
val list1 = listOf(1,2,3)
val list2 = list1.map { it.times(2) }
println(list2) // [ 2, 4, 6 ]

```

코틀린 컬렉션에서 제공하는 map은 위에서 보듯이 요소 각각에 2를 곱해 새로운 List를 반환한다.  **포인트는 새로운 List를 반환한다는 것이다.**

`Transformations.map`역시 마찬가지다.

```kotlin
val userLiveData: MutableLiveData<User> = repository.getUser(id)
val userNameLiveData: LiveData<String> = Transformations.map(userLiveData) { user ->
    user.firstName + " " + user.lastName
}

```

공식문서의 코드 샘플을 약간 수정했다.

-   **map의 첫 번째 인자로 LiveData source를 넘겨준다.**  넘겨준 LiveData source 가 변경될 때마다 map이 반환하는 새로운 LiveData의 value역시 새롭게 갱신된다.
    
-   **두 번째 인자로는 함수를 넘겨준다.**  함수의 파라미터 타입은 source로 넘겨준 LiveData의 value Type(`<User>`)이며 함수의 return값은 무엇이든 상관없다.
    
-   **Transformations.map의 return 값(람다의 결과물 말고)은 LiveData**이다. 기존 컬렉션의 map이 그러하듯 Transformations.map 역시 내용물 요소의 값만 변환 시킬 뿐 LiveData를 리턴한다.
    

직관적으로 보면  `userNameLiveData`는 그저  `userLiveData`의 User 이름만 추출하여 새롭게 만든 LiveData이다. 따라서  `userLiveData`와  `userNameLiveData`는 서로 독립적인 객체인 것처럼 느껴진다. 그러나  `userNameLiveData`의 value는  `userLiveData`의 value가 바뀔 때 마다 함께 갱신된다.

어떻게 그렇게 될까?  `Transformations.map`의 내부적으로  `MediatorLiveData`를 사용하고 있기 때문이다.

[MediatorLiveData](https://developer.android.com/reference/android/arch/lifecycle/MediatorLiveData)를 간단히 설명하자면 Rx의 merge 함수와 비슷하다. 서로다른  `data source`(여기서는 LiveData)가 독립적으로 존재하는 상황에서, 각각의 데이터 소스들이 변경되는 것을 따로 따로 관찰하는 것이 아니라 어떤 소스에서 변경이 일어나든 한번에 관찰하려고 하는 것이다. 사실 다 필요 없고 공식문서 한 번 보면 다 이해된다.  [공식문서](https://developer.android.com/reference/android/arch/lifecycle/MediatorLiveData)를 보자ㅠㅠ.

참고로  `Transformations.map`의 내부 구현은 아래와 같다.

```java
@MainThread
@NonNull
public static <X, Y> LiveData<Y> map(
        @NonNull LiveData<X> source,
        @NonNull final Function<X, Y> mapFunction) {
    final MediatorLiveData<Y> result = new MediatorLiveData<>();
    result.addSource(source, new Observer<X>() {
        @Override
        public void onChanged(@Nullable X x) {
            result.setValue(mapFunction.apply(x));
        }
    });
    return result;
}

```

### Transformations.switchMap

`Transformations.map`을 이해했다면  `switchMap`는 90% 먹고들어간 셈이다.

```kotlin
 val userIdLiveData: MutableLiveData<Int> = MutableLiveData<Int>().apply { value = 1 };
 val userLiveData: LiveData<User> = Transformations.switchMap(userIdLiveData) { id ->
     repository.getUserById(id)
 }

 fun setUserId(userId: Int) {
      userIdLiveData.setValue(userId);
 }

```

![image](https://user-images.githubusercontent.com/18481078/61167008-efd3ca00-a572-11e9-9717-1670623c1e6b.png)

-   **switchMap의 첫 번째 인자로 LiveData source를 넘겨준다.**  넘겨준 LiveData source 가 변경될 때마다  `switchMap`이 반환하는 새로운 LiveData의 value역시 새롭게 갱신된다.
    
-   **두 번째 인자로는 함수를 넘겨준다.**  함수의 파라미터 타입은 source로 넘겨준 LiveData의 value Type(`<Int>`)이며 함수의 return값은  `LiveData`이어야만 한다.
    

`map`과 다른점은 람다 함수의 return값이 LiveData여야 한다는 것이다.  `map`의 경우 람다함수의 return값이 각 요소의 값들을 변경시키는 것에 불과하며 자동으로 LiveData가 되어서 결과물이 반환되었지만,  `switchMap`의 경우 실제로 LiveData 하나를 반환해야 한다. 그래서  `switchMap`은 Model단이나 Room데이터베이스와 같이 애초에 LiveData를 반환하는 기능들과 자주 함께 쓰인다.

`userLiveData`의 value역시  `userIdLiveData`의 value가 바뀌면 자동으로 갱신되는데 map과 마찬가지로 내부적으로  `MediatorLiveData`가 사용되기 때문이다.

내부 구현은 아래와 같다.

```java
@MainThread
@NonNull
public static <X, Y> LiveData<Y> switchMap(
        @NonNull LiveData<X> source,
        @NonNull final Function<X, LiveData<Y>> switchMapFunction) {
    final MediatorLiveData<Y> result = new MediatorLiveData<>();
    result.addSource(source, new Observer<X>() {
        LiveData<Y> mSource;

        @Override
        public void onChanged(@Nullable X x) {
            LiveData<Y> newLiveData = switchMapFunction.apply(x);
            if (mSource == newLiveData) {
                return;
            }
            if (mSource != null) {
                result.removeSource(mSource);
            }
            mSource = newLiveData;
            if (mSource != null) {
                result.addSource(mSource, new Observer<Y>() {
                    @Override
                    public void onChanged(@Nullable Y y) {
                        result.setValue(y);
                    }
                });
            }
        }
    });
    return result;
}
```