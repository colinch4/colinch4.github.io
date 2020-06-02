---
layout: post
title: "[Kotlin] Transformations와 MediatorLiveData를 이용한 Reactive 패턴"
date: 2020-04-07 15:13
category: 
author: kskim2
tags: [kotlin, livedata]
description: "Reactive 아키텍처는 수년 동안 Android에서 인기있는 주제였습니다. Android 컨퍼런스에서 꾸준히 언급 된 주제이며,보통 RxJava를 사용한 예제와 함께 언급되었었습니다.(아래의 Rx 섹션을 참조 해 주세요). Reactive 프로그래밍은 데이터 흐름 및 변경 사항 전파와 관련된 패러다임으로, 앱 구축을 단순화하고 비동기 동작의 결과값을 표시 할 수 있습니다."
summary: 
---

Reactive 아키텍처는 수년 동안 Android에서 인기있는 주제였습니다. Android 컨퍼런스에서 꾸준히 언급 된 주제이며,보통 RxJava를 사용한 예제와 함께 언급되었었습니다.(아래의 Rx 섹션을 참조 해 주세요). Reactive 프로그래밍은 데이터 흐름 및 변경 사항 전파와 관련된 패러다임으로, 앱 구축을 단순화하고 비동기 동작의 결과값을 표시 할 수 있습니다.

  
Reactive 개념 중 일부를 구현할 때 사용되는 것 중 하나로  [LiveData](https://developer.android.com/topic/libraries/architecture/livedata)가 있습니다. 관찰자의 생명주기에 따라서 간편하게 관찰될 수 있습니다. 당신이 구현한 데이터 소스 혹은 리포지토리에서 LiveData에 데이터를 연동하는 것은 아키텍처를보다 Reactive하게 만들 수 있는 간단한 방법이지만 잠재적인 위험이 있습니다.

  
이 블로그 게시물을 통해서 LiveData를 사용하여 위험을 줄이면서 좀 더 Reactive한 아키텍처를 구축하는 데 도움을 주려고 합니다.

## LiveData의 목적

Android에서, activity, fragment 그리고 view는 거의 언제든지 소멸될 수 있기 때문에, 이러한 컴포넌트 들을 참조하게 되면 누수 또는  NullPointerException을 유발할 수 있습니다.

  
LiveData는 관찰자 패턴을 구현하도록 설계되어 View 컨트롤러 (activity, fragment 등)와 UI 데이터(보통 ViewModel) 간에 데이터를 주고받도록 도와줍니다. LiveData를 사용하면이 더 안전하게 데이터를 주고받을 수 있습니다. lifecycle을 인식해서 View가 활성화 된 경우에만 데이터가 수신됩니다.  
요악하자면, View와 ViewModel간의 구독 행위를 일일이 취소 할 필요가 없다는 장점이 있습니다.

![](https://k.kakaocdn.net/dn/cAmgpt/btqyPuaMA95/hfuwDxUpKvcoIWBpQBR661/img.png)

View와 ViewModel간 상호작용

##   
  
ViewModel 밖에서의 LiveData

관찰자 패러다임은 View 컨트롤러와 ViewModel간에 잘 작동하므로, LiveData를 활용하여 앱의 다른 구성 요소들끼리도 관찰하게 함으로써 lifecycle에 맞춰서 동작하는 장점을 활용할 수 있습니다. 예를 들면 다음과 같습니다.

-   [SharedPreferences](https://developer.android.com/reference/android/content/SharedPreferences.OnSharedPreferenceChangeListener)의 변경 사항 관찰
-   [Firestore](https://firebase.google.com/docs/firestore/)의 document 혹은 collection 관찰
-   [FirebaseAuth](https://firebase.google.com/docs/auth/)와 같은 인증 SDK을 이용한 사용자 관찰
-   [Room](https://developer.android.com/topic/libraries/architecture/room)에서 쿼리를 관찰 (LiveData를 지원함)

이 패러다임의 장점은 모든 것이 연결되어 있으므로 데이터가 변경 될 때 UI가 자동으로 업데이트된다는 것입니다.

  
단점은 LiveData에는 Rx처럼 데이터 스트림을 결합하거나 스레드를 관리하기위한 툴킷이 제공되지 않는다는 것입니다.  
일반적인 앱의 모든 레이어에서 LiveData를 사용하면 다음과 같습니다.

![](https://k.kakaocdn.net/dn/bwV3is/btqyRMARlZI/2NRgjLBo06w5aR9ZFYaRBk/img.png)

LiveData를 사용하는 일반적인 앱 아키텍처

  
컴포넌트간에 데이터를 전달하려면 맵핑 및 결합 방법이 필요합니다. 이를 위해 Transformations 클래스의 몇몇 기능과 함께 MediatorLiveData가 사용됩니다.

-   [Transformations.map](https://developer.android.com/reference/android/arch/lifecycle/Transformations.html#map(android.arch.lifecycle.LiveData%3CX%3E,%20android.arch.core.util.Function%3CX,%20Y%3E))
-   [Transformations.switchMap](https://developer.android.com/reference/android/arch/lifecycle/Transformations.html#switchMap(android.arch.lifecycle.LiveData%3CX%3E,%20android.arch.core.util.Function%3CX,%20android.arch.lifecycle.LiveData%3CY%3E%3E))

> _View가 소멸되면 View의 수명주기가 그 다음 구독자로 다운 스트림으로 전달되므로 구독을 해제 할 필요가 없습니다._

##   
패턴

### 일대일 정적 변환 — map

![](https://k.kakaocdn.net/dn/ceEJBm/btqyPWLIc0i/8suoo9KCiz3s0dHqx96gnK/img.png)

ViewModel은 다른 데이터를 관찰하고, 다른것을 드러냅니다.

위의 예에서 ViewModel은 리포지토리에서 뷰로 데이터를 받아서 UI 모델로 변환합니다. 리포지토리에 새로운 데이터가있을 때마다 ViewModel은 이를  map하기만 하면됩니다.

```kotlin
class MainViewModel {
  val viewModelResult = Transformations.map(repository.getDataForUser()) { data ->
     convertDataToMainUIModel(data)
  }
}
```

  
이 변환은 매우 간단합니다. 하지만, 위 예제에서 사용자가 변경 될 수있는 경우에는 switchMap이 필요합니다.

#### 일대일 동적 변환 switchMap

사용자를 갖고 있는 UserManager를 구독하고 있고, 리포티저리를 사용하기 위해서는 사용자 ID를 얻기 위해 기다려야 하는 예제를 생각 해 보세요.

![](https://k.kakaocdn.net/dn/XOiGI/btqyQyKEly2/F54uK4sPTEOzW09xN0rmx1/img.png)

리포지터리에서 결과값을 받기 위해서는 user manager에서 제공하는 사용자 id를 알아야 됨

  
ViewModel을 초기화 할 때 사용자 id를 사용할 수 없습니다.

switchMap을 이용해서 이렇게 구현 해 보세요.

```kotlin
class MainViewModel {
  val repositoryResult = Transformations.switchMap(userManager.user) { user ->
     repository.getDataForUser(user)
  }
}
```

  
switchMap은 내부적으로 MediatorLiveData를 사용합니다. 여러 LiveData들을 결합하려는 경우 MediatorLiveData를 사용해야 하기 때문에, 이를 알아두는 것이 중요합니다.  
  

#### 일대 다 종속성 — MediatorLiveData

MediatorLiveData를 사용하면 하나의 LiveData가 하나 이상을 관찰하게 할 수 있습니다.

```kotlin
val liveData1: LiveData<Int> = ...
val liveData2: LiveData<Int> = ...

val result = MediatorLiveData<Int>()

result.addSource(liveData1) { value ->
    result.setValue(value)
}
result.addSource(liveData2) { value ->
    result.setValue(value)
}
```

  
이 [문서](https://developer.android.com/reference/android/arch/lifecycle/MediatorLiveData)에서 가져온 이 예제는 Observe 중인 것 중 어느 하나라도 업데이트 되면 값이 변경되는 예제입니다.  **데이터가 결합되지 않습니다.**  MediatorLiveData는 단순히 notification을 처리합니다.

우리의 샘플 앱에서 transformation을 구현하기 위해, 서로 다른 두 개의 LiveData를 하나로 결합해야 했습니다.

![](https://k.kakaocdn.net/dn/bsmvfe/btqyQM2UHVG/9Agi4AeYsEtezk4ansrMh0/img.png)

MediatorLiveData는 두 데이터 소스를 하나로 결합하기 위해 사용됩니다.

  
소스를 추가하고 다른 메소드에서으로 값을 설정 함으로써 MediatorLiveData를 사용할 수 있습니다.

```kotlin
fun blogpostBoilerplateExample(newUser: String): LiveData<UserDataResult> {

    val liveData1 = userOnlineDataSource.getOnlineTime(newUser)
    val liveData2 = userCheckinsDataSource.getCheckins(newUser)

    val result = MediatorLiveData<UserDataResult>()

    result.addSource(liveData1) { value ->
        result.value = combineLatestData(liveData1, liveData2)
    }
    result.addSource(liveData2) { value ->
        result.value = combineLatestData(liveData1, liveData2)
    }
    return result
}
```

  
실제 데이터 조합은 combineLatestData 메소드에서 수행됩니다.

```kotlin
private fun combineLatestData(
        onlineTimeResult: LiveData<Long>,
        checkinsResult: LiveData<CheckinsResult>
): UserDataResult {

    val onlineTime = onlineTimeResult.value
    val checkins = checkinsResult.value

    // 두 값이 모두 들어올 때 까지 success를 보내지 않음
    if (onlineTime == null || checkins == null) {
        return UserDataLoading()
    }

    // TODO: 오류 확인 및 오류 있으면 UserDataError를 반환 함.

    return UserDataSuccess(timeOnline = onlineTime, checkins = checkins)
}
```

  
이 메소드에서는 값이 준비되었는지 또는 올바른지 확인하고 결과 (loading, error 또는 success)를 내보냅니다.

  
Kotlin의 확장 기능으로 이를 깔끔하게 구현하는 법을 알아 보려면  아래에 있는 보너스 섹션을 참조하십시오.

  
**LiveData를 사용하지 않아야 하는 경우**

“Reactive”하게 하고 싶더라도, LiveData를 사용하기 전에 LiveData의 장점을 이해해야 합니다. 앱의 구성 요소가 UI에 연결되어 있지 않다면, LiveData가 사용할 필요가 없을 수도 있습니다.

예를 들어 당신의 앱 내의 user manager가 당신의 인증 제공자(Firebase Auth와 같은)의 변경 사항을 알게 되면 서버에 고유 한 토큰을 업로드한다고 해 봅시다.

![](https://k.kakaocdn.net/dn/AGICg/btqyQMV9M4f/EDQHlwEnRq8h8hI433IDZ1/img.png)

token uploader와 user manager간의 데이터 교환은 reactive해야 할까요?

토큰 업 로더는 사용자 관리자를 관찰 할 수 있지만 수명주기는요? 이 모듈은 View와 전혀 관련이 없습니다. 게다가 View가 소멸되면, 토큰은 업로드 되지 않을수도 있습니다.

또 다른 방법으로는 토큰 업 로더에서  [observeForever()](https://developer.android.com/reference/android/arch/lifecycle/LiveData#observeforever)를 사용하고 사용이 끝나면 구독을 제거할 수도 있습니다.

그러나 모든 것을 observable하게 만들 필요는 없습니다. User manager가 토큰 업 로더를 직접 호출하도록 하는게 낫습니다. (또는 당신의 어플리케이션 아키텍쳐에서 어울리는 어떤것을 써도 좋습니다).

![](https://k.kakaocdn.net/dn/bQCaN3/btqyQ6NnYy8/ag06kqQjZlwRuejl1wZzmk/img.png)

UI와 관련이 없는 동작은 LiveData를 사용할 필요가 없습니다.

> _UI에 영향을 미치지 않는 곳을 구현할 때에는, LiveData가 필요하지 않을 수 있습니다._

#### 지양해야 될 패턴: LiveData 인스턴스 공유

클래스가 LiveData를 다른 클래스에 노출시킬 때, 동일한 LiveData 인스턴스 또는 다른 인스턴스를 노출하려는 경우 신중하게 생각하십시오.

```kotlin
class SharedLiveDataSource(val dataSource: MyDataSource) {

    // 주의: 이 LiveData는 여러곳에서 사용 됨
    private val result = MutableLiveData<Long>()

    fun loadDataForUser(userId: String): LiveData<Long> {
        result.value = dataSource.getOnlineTime(userId)
        return result
    }
}
```

  
이 클래스가 앱의 싱글톤 인 경우(인스턴스가 하나 뿐인 경우), 항상 동일한 LiveData를 반환 합니다.  반드시 그럴 필요는 없습니다. 이 클래스를 사용하는 곳이 여러곳이 있을 수도 있습니다.

  
다음 예제를 고려 해 보세요:

```kotlin
sharedLiveDataSource.loadDataForUser("1").observe(this, Observer {
   // 화면에 결과를 보여줌
}) 
```

  
그리고 또 다른 곳에서 이를 사용한다고 생각 해 보세요.

```kotlin
sharedLiveDataSource.loadDataForUser("2").observe(this, Observer {
   // 화면에 결과를 보여줌
}) 
```

  
첫 번째로 사용된 곳도 사용자“2”에 대한 데이터로 업데이트 됩니다.

한 곳에서만 사용하기 위해서 만들었다고 하더라도, 이런 패턴을 이용하면 결국 버그가 생성될 확률이 높습니다.  예를 들어, 한 액티비티에서 다른 액티비티로 이동할 때,  **새로운 액티비티에서 그전으로부터 데이터를 받게 될 것입니다.**  LiveData는 새로운 관찰자에게 가장 최신의 값을 전달한다는 것을 명심하세요.  또한 Lollipop에서 액티비티 전환이 도입되었으며 이로 인해서  **두 엑티비티가 모두 active 상태**인 예상치 못한 엣지케이스(edge case)가 발생될 수 있습니다.  이는 LiveData가 사용되는 곳이 두 군데일 수 있으며, 그 중 하나는 잘못된 데이터를 표시 할 것입니다.

  
이 문제에 대한 해결책은 아래와 같이 LiveData가 사용되는 곳마다 새로운 LiveData 객체를 생성해서 주는 것입니다.

```kotlin
class SharedLiveDataSource(val dataSource: MyDataSource) {
    fun loadDataForUser(userId: String): LiveData<Long> {
        val result = MutableLiveData<Long>()
        result.value = dataSource.getOnlineTime(userId)
        return result
    }
}
```

> 소비자간에 LiveData 인스턴스를 여러군데서 공유하기 전에 신중하게 생각하십시오.

#### MediatorLiveData 가 잘못 쓰이는 예: 초기화 외부에 소스 추가  

관찰자 패턴을 사용하는 것이 뷰의 참조를 사용하는 것(MVP 아키텍처에서 일반적으로 하는 방식)보다 안전합니다.  그러나, 메모리 누수를 신경쓰지 않아도 된다는 말은 아니에요!  

아래 코드를 고려 해보세요.

```kotlin
class SlowRandomNumberGenerator {
    private val rnd = Random()

    fun getNumber(): LiveData<Int> {
        val result = MutableLiveData<Int>()

        // 잠시 후 랜덤 숫자를 전달 함
        Executors.newSingleThreadExecutor().execute {
            Thread.sleep(500)
            result.postValue(rnd.nextInt(1000))
        }

        return result
    }
}
```

  
500ms 후에 임의의 값을 갖는 새로운 LiveData 객체를 반환합니다.  여기는 아무 문제가 없습니다.

  
ViewModel에서는 위 generator에서 숫자를 가져 와서  randomNumber  속성으로 전달해야 합니다.  이런 상황에서는 MediatorLiveData를 사용하는 것은 새로운 번호가 필요할 때마다 소스를 추가해야하기 때문에 이상적이지 않습니다.

```kotlin
val randomNumber = MediatorLiveData<Int>()

/**
* 이렇게 하지 마세요
*
* 사용자가 버튼을 클릭하면 호출이 됨
*
* 이 함수는 결과에 새로운 소스를 추가함. 하지만 기존의 것은 제거하지는 않음.
*/
fun onGetNumber() {
   randomNumber.addSource(numberGenerator.getNumber()) {
       randomNumber.value = it
   }
}
```

  
사용자가 버튼을 클릭 할 때마다 MediatorLiveData를 생성해서 추가하면 앱이 의도 한대로 작동합니다.  그러나 우리는 더 이상 새로운 값을 보내지 않을 이전의 모든 LiveData가 유출되어 있으므로, 낭비입니다.

  
소스에 대한 참조를 어딘가에 저장해 둔 뒤에, 새 소스를 추가하기 전에 제거 할 수도 있습니다.  (스포일러 :  Transformations.switchMap이 이렇게 동작되고 있어요.  아래 솔루션을 참조하십시오.)

  
MediatorLiveData를 사용하는 대신  Transformation.map으로이 문제를 해결하려고합니다 (실패).

#### Transformation이 잘못 쓰이는 예 : Transformation를 외부에서 초기화 시킴

이전 예제를 사용하면 아래 코드는 작동하지 않습니다.

```kotlin
var lateinit randomNumber: LiveData<Int>

/**
 * 버튼을 클릭하면 호출 됨
 */
fun onGetNumber() {
   randomNumber = Transformations.map(numberGenerator.getNumber()) {
       it
   }
}
```

  
여기서 이해해야 할 중요한 문제가 있습니다. Transformations는 호출 될 때 (map  과  switchMap  둘 다) 새 LiveData를 만듭니다.  이 예제에서  randomNumber는 View에 전달 되지만, 사용자가 버튼을 클릭 할 때마다 다시 할당됩니다.  **옵저버가 구독 받는 순간에만 LiveData에 대한 업데이트를 받게만 받는**  실수는 하기 쉬운 흔한 실수입니다.

```kotlin
viewmodel.randomNumber.observe(this, Observer { number ->
    numberTv.text = resources.getString(R.string.random_text, number)
})
```

  
이 구독은  onCreate()에서 발생하므로 나중에  viewmodel.randomNumber  LiveData 인스턴스가 변경되더라도 옵저버는 다시 호출되지 않습니다.  
  
다시 말해:

> LiveData를 변수로 사용하지 마세요.  초기화 할 때 Transformations를 연결 시키세요.

####   
솔루션 : 초기화 할 때 Transformations 연결

노출 시킬 LiveData는 Transformation으로 초기화 시키세요.

```kotlin
private val newNumberEvent = MutableLiveData<Event<Any>>()

val randomNumber: LiveData<Int> = Transformations.switchMap(newNumberEvent) {
   numberGenerator.getNumber()
}
```

  
LiveData에  [Event](https://medium.com/google-developers/livedata-with-snackbar-navigation-and-other-events-the-singleliveevent-case-ac2622673150)를 사용하여 새 번호를 요청할시기를 나타내세요.  
  

```kotlin
/**
* 새로운 숫자를 요청하기 위해서 Event를 보냄
*/
fun onGetNumber() {
   newNumberEvent.value = Event(Unit)
}
```

  

이 패턴에 익숙하지 않은 경우  [이 블로그 글](https://medium.com/google-developers/livedata-with-snackbar-navigation-and-other-events-the-singleliveevent-case-ac2622673150)을 참조하세요.  
  

### 보너스 섹션

#### 코틀린을 사용해서 정리하기

위의 MediatorLiveData 예제는 같은 코드를 계속 사용하므로, Kotlin의 확장 기능을 활용하여 개선할 수 있습니다.  
  
  

```kotlin
/**
* Sets the value to the result of a function that is called when both `LiveData`s have data
* or when they receive updates after that.
*/
fun <T, A, B> LiveData<A>.combineAndCompute(other: LiveData<B>, onChange: (A, B) -> T): MediatorLiveData<T> {

   var source1emitted = false
   var source2emitted = false

   val result = MediatorLiveData<T>()

   val mergeF = {
       val source1Value = this.value
       val source2Value = other.value

       if (source1emitted && source2emitted) {
           result.value = onChange.invoke(source1Value!!, source2Value!! )
       }
   }

   result.addSource(this) { source1emitted = true; mergeF.invoke() }
   result.addSource(other) { source2emitted = true; mergeF.invoke() }

   return result
}
```

이제 저장소가 훨씬 깨끗해졌습니다.

```kotlin
fun getDataForUser(newUser: String?): LiveData<UserDataResult> {
   if (newUser == null) {
       return MutableLiveData<UserDataResult>().apply { value = null }
   }

   return userOnlineDataSource.getOnlineTime(newUser)
           .combineAndCompute(userCheckinsDataSource.getCheckins(newUser)) { a, b ->
       UserDataSuccess(a, b)
   }
}
```

#### LiveData와 RxJava

마지막으로, 방 안에 있는 코끼리를 다루어 봅시다.  LiveData는 View가 ViewModel을 관찰 할 수 있도록 설계되었습니다.  이것을 위해 사용하십시오!  이미 Rx를 사용하고 있더라도,  [LiveDataReactiveStreams](https://developer.android.com/reference/android/arch/lifecycle/LiveDataReactiveStreams)*와도 통신 할 수 있습니다.

  
Presentation 레이어를 넘어서 LiveData를 사용하고 싶다면, RxJava 오퍼링과 같은 데이터 스트림을 결합하고 다루기위한 툴킷을 MediatorLiveData에서 찾을 수도 있습니다. MediatorLiveData에서는 이런것을 제공하지 않습니다.  그러나 Rx는 러닝커브가 높습니다.  LiveData 변환과 Kotlin의 뛰어난 기능의 조합으로 충분할 수 있지만, 이미 RxJava를 배운 경우라면, LiveData가 필요하지 않을 수 있습니다.

*[auto-dispose](https://github.com/uber/AutoDispose)를 사용하는 경우 LiveData를 사용하면 중복됩니다.

