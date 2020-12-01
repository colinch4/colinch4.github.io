---
layout: post
title: "[안드로이드 기초] Activity Task & Back Stack"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---

## Task

![](https://developer.android.com/images/fundamentals/diagram_backstack.png?hl=ko)

**Task는 특정 작업을 수행할 때 사용자와 상호작용하는 Activity의 모음**이다. Activity는 **Stack안에 정렬되며 이때 순서는 각 Activity가 열린 순서이다. 해당 Stack을 Back Stack**이라고 한다.

First In Last Out 구조로 새로운 Activity를 생성하면 push되고 BackButton을 누르거나 finish()를 하여 최상단 Activity를 종료하면 pop된다.

Stack안에 있는 Acitivty들은 절대 재정렬되지 않는다.

최초 적재 Activity는 RootActivity, 마지막에 적재된 Activity는 TopActivity라고 한다.

Task는 포그라운드 백그라운드에 유지될 수 있으며 포그라운드에는 주로 한 개의 Task가 유지될 수 있고 여러 개의 Task가 백그라운드에 유지될 수 있다. 단, 백그라운드에 존재하는 Task들은 메모리 부족 시 Activity 상태가 손실될 수 있다. 이런 경우를 대비하여 onSaveInstanceState() 콜백 메서드를 이용하여 Activity의 상태를 보존해야한다.

서로 다른 앱에서 가져온 Activity도 하나의 Task에 속할 수 있다. 이렇게 함으로써 막힘 없는 UX를 제공한다. 

Activity는 Stack에 여러번 인스턴스화 될 수 있다.

## Task 관리

앱의 한 액티비티를 시작했을 때 새로운 Task를 시작하거나, 액티비티를 시작했을 때 기존 인스턴스를 가져오고 싶거나, Task를 떠날 때 RootActivity를 제외한 모든 액티비티를 지우고 싶을 때는,

**Manifest의 <activity>의 attribute**와 **startActivity()에 전달한 인텐트의** **플래그**를 사용하여 언급한 일이나 그 밖의 많은 일들을 할 수 있다.

### Launch Mode 정의

**Manifest file 사용**

Manifest file에서 액티비티를 선언하는 경우, 액티비티가 Task와 어떤 식으로 연관되어야 할지 지정하려면 <activity>의 lanuchMode 특성을 사용한다.

launchMode는 Task에 대해 액티비티가 시작되는 방식을 지정한다. 해당 방법에는 네 가지가 있다.

- standard

기본적인 동작으로, 액티비티는 여러 번 인스턴스화 될 수 있고, 각 인스턴스는 여러 Task에 속할 수 있으며, 한 Task에 여러 개의 인스턴스가 있을 수 있다.

- singleTop

액티비티의 인스턴스가 이미 현재 Task의 맨 위에 존재하는 경우, 즉 TopActivity인 경우, 시스템은 새로운 액티비티를 만드는 대신 onNewIntent() 메서드를 호출하여 인텐트를 해당 인스턴스로 보낸다. A-B-C-D에서 D가 singleTop인 경우, D 유형의 인텐트가 오면 A-B-C-D-D가 아닌 A-B-C-D가 된다. 액티비티는 여러 번 인스턴스화될 수 있고, 각 인스턴스는 서로 다른 Task에 속할 수 있으며 한 Task에 여러 개의 인스턴스가 있을 수 있다(다만 백 스택의 맨 위에 있는 액티비티가 액티비티의 기존 인스턴스가 아닌 경우에만 이것이 적용됨).

- singleTask

시스템이 새로운 Task를 만들고 루트에 액티비티를 인스턴스화 한다. 만약 다른 Task에 액티비티의 인스턴스가 이미 존재하면 시스템은 새로운 인스턴스를 만들기 보다 기존의 인스턴스로 인텐트를 보내고 onNewIntent()를 호출한다. 오직 하나의 액티비티의 인스턴스만이 존재할 수 있다.

활용방안은 여러 액티비티를 만들고 싶지 않은 브라우저 앱이나 게임 앱.

공유할 때 써먹기 - 공유하기가 암시적 인텐트로 들어왔을 때 복수의 Task를 만들지 않기 위해 만약 앱이 백그라운드에 있으면 기존의 Task에 ShareActivity 쌓이고 공유 후에 FLAG_ACTIVITY_CLEAR_TOP or FLAG_ACTIVITY_SINGLE_TOP으로 MainActivity의 기존 상태 유지하면서 보내면 된다. 만약에 인증이 필요한 경우, 인증이 되면 기존과 같게하면 되고 인증이 안되면 LoginActivity로 같은 방식으로 보내면 된다. 만약 앱이 백그라운드에 없는 경우(꺼져 있는 경우)에는 어차피 새로운 Task로 가서 ShareActivity부터 켜지고 위와 같은 프로세스 반복이니 깔끔하게 구현될 것이라고 생각한다. 토이 프로젝트에서 해당 기능에 대해 더욱 심오한 이해를 할 수 있을 것이라 생각한다.

- singleInstance

1개의 Task에 1개의 인스턴스만 존재한다. 다른 액티비티의 인스턴스를 Task에 포함하지 않는다. 이미 같은 액티비티가 실행 중이면 액티비티를 생성하지 않는다.

아래 그림은 singleTask로 실행된 경우 백그라운드에 있던 Task가 스택 맨위에 위치하게 된다.

![](https://developer.android.com/images/fundamentals/diagram_backstack_singletask_multiactivity.png?hl=ko)

**Intent Flag 사용**

intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_SINGLE_TOP | Intent.FLAG_ACTIVITY_CLEAR_TOP)

startActivity()에 전달한 인텐트에 들어있는 플래그를 포함시키면 액티비티 Task의 기본 동작을 수정할 수 있다.

- FLAG_ACTIVITY_NEW_TASK

새로운 Task를 생성하여 그 Task 안에 액티비티를 추가할 때 사용한다. 단, 기존에 존재하는 Task들 중에 생성하려는 액티비티와 동일한 affinity를 가지고 있는 Task가 있다면 그곳으로 액티비티가 들어가게 된다.

- FLAG_ACTIVITY_SINGLE_TOP

시작되고 있는 액티비티가 백 스택 맨 위에 있는 액티비티인 경우, 해당 액티비티의 새 인스턴스를 생성하는 대신 기존 인스턴스가 onNewIntent()에 대한 호출을 받는다.

singleTop과 동일 동작

- FLAG_ACTIVITY_CLEAR_TOP

시작되고 있는 액티비티가 이미 현재 Task에서 실행 중인 경우, 해당 액티비티의 새 인스턴스를 시작하는 대신 그 위에 있는 모든 액티비티가 소멸되고 이 인텐트는 해당 액티비티의 재개된 인스턴스로, onNewIntent()를 통해 전달된다.

아래와 같이 활용했을 때 위에 있는 모든 액티비티 인스턴스를 없애고 기존의 액티비티의 상태를 보존할 수 있었다. 예를 들면 A-B-B-B-B-B-B가 있었는데 A를 보존하면서 B를 전부 없애고 싶을 때 아래의 코드를 이용하면 A를 보존하면서 B를 모두 없앨 수 있었다. singleTop이 있어서 가능했다.

```kotlin
    intent.addFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP or Intent.FLAG_ACTIVITY_CLEAR_TOP)
```
아래와 같이 사용하면 다른 작업에 있는 기존 액티비티를 찾은 후, 인텐트에 응답할 수 있는 위치에 이 액티비티를 넣을 수 있다. 기존에 남아있던 액티비티를 전부 스택에서 삭제한 후 새로운 Task에 액티비티를 추가하고 싶을 때사용했었다.
```kotlin
    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
```
기타 플래그들은 아래 링크에서

[https://developer.android.com/reference/android/content/Intent.html](https://developer.android.com/reference/android/content/Intent.html)

## taskAffinity

- 액티비티가 어느 Task에 속하길 선호하는지 나타내는 것이다.
- 모든 액티비티에 대해서 <activity> 요소의 taskAffinity 특성을 사용하여 유사성을 수정할 수 있다.
- <manifest> 요소에서 선언한 기본 패키지 이름과 달리 고유해야 한다.
- 기본 값은 앱의 패키지 이름이다.
- taskAffinity 값은 allowTaskReparenting 속성이나 FLAG_ACTIVITY_NEW_TASK 와 상호작용하여 액티비티의 Task를 결정한다.
- 액티비티를 시작한 인텐트에 FLAG_ACTIVITY_NEW_TASK 플래그가 들어 있는 경우에 새 액티비티와 같은 유사성을 가진 기존 작업이 이미 존재하면 해당 액티비티는 그 Task 안으로 들어가며 시작되고 그렇지 않으면 새 Task를 시작한다.
- 액티비티의 allowTaskReparenting 특성이 "true"로 설정된 경우에 액티비티는 자신이 시작한 Task에서 벗어나 affinity을 가진 다른 Task가 포그라운드로 나오면 그 Task로 이동할 수 있다.
- 예를 들어, 이메일 메시지가 웹페이지에 대한 링크를 포함하는 경우 해당 링크를 클릭하면 페이지를 표시할 수 있는 액티비티를 표시한다. 해당 액티비티는 브라우저 애플리케이션이 정의하지만 이메일 Task의 일부로 시작된다. 액티비티 부모를 브라우저 Task으로 재지정할 경우 액티비티는 브라우저가 다음에 포그라운드로 올 때 표시되며 이메일 작업이 다시 포그라운드로 올 때 표시되지 않는다. 덧붙이자면 카카오톡으로 공유같은 것을 했을 때 처음에는 카카오톡의 공유 액티비티가 기존앱의 Task에 속하지만 액티비티를 reparent하면 나중에 카카오톡이 포그라운드로 올 때 카카오톡의 Task가 공유 액티비티를 가져오게 된다는 의미인 듯 하다.
- taskAffinity에 의해 Task가 이동된 후 Back Button으로 반환시 원래 해당하던 태스크로 돌아간다.

[https://aroundck.tistory.com/76](https://aroundck.tistory.com/76)

## Clearing the back stack

- Task를 오랫동안 사용하지 않고 방치해 두면 시스템은 Root Activity를 제외한 모든 액티비티를 Clear 시킨다. 이러한 동작은 Activity의 속성을 수정하여 제어할 수 있다
- alwaysRetainTaskState

Task의 Root Activity에 true로 설정되어 있다면 상단에 언급되었던 동작은 발생하지 않으며 Task는오랜 시간 이후에도 Stack에 있는 모든 Activity를 유지한다.

- clearTaskOnLaunch

이 속성이 true로 설정되어 있으면 alwaysRetainTaskState 와 정반대로 사용자가 Task를 떠났다가다시 돌아올 때마다 항상 Stack은 Root Activity로 정리된다.

- finishOnTaskLaunch

이 속성은 clearTaskOnLaunch와 유사하지만 전체 Task가 아닌 단일 Activity에서 동작한다. 그리고 그것은 Root Activity를 포함한 어떤 Activity가 사라지는 원인이 될 수도 있다. true로 설정되어 있을 때, Activity는 현재 Session 동안 Task의 일부만 유지한다. 만일 사용자가 해당 Task를 벗어났다가 다시 돌아오면 더 이상 존재하지 않는다.

## Starting a task

액티비티를 작업의 진입 지점으로 설정하려면
```XML
    <activity ... >
        <intent-filter ... >
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
        </intent-filter>
        ...
    </activity>
```
사용자는 Task를 떠났다가 이 액티비티 launcher를 사용하여 나중에 작업에 돌아올 수 있어야 한다. 이러한 이유로, 액티비티가 항상 Task를 시작하는 것으로 표시하는 두 가지 launch mode, 즉 "singleTask" 및 "singleInstance"는 액티비티에 ACTION_MAIN 및 CATEGORY_LAUNCHER 필터가 있을 때에만 사용되어야 한다.
