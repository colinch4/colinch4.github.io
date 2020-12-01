---
layout: post
title: "[안드로이드 기초] Android Lifecycle & State"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---


![](https://developer.android.com/guide/components/images/activity_lifecycle.png?hl=ko)

Activity에는 세 가지 상태가 있고, 상태를 변경할 때마다 콜백이 안드로이드 프레임워크에서 호출된다.

**Resumed**

Activity가 포그라운드에 있고 사용자 포커스를 갖고 있다. ("실행 중"이라고도 한다)

**Paused**

다른 Acitivity가 포그라운드에 나와 있지만 여전히 해당 Activity도 표시되어 있다. 즉, 다른 Activity가 해당 Activity 위에 표시되어 있으며 해당 Activity는 부분적으로 투명하거나 전체 화면을 덮지 않는 상태라는 뜻이다. 일시정지된 Activity는 완전히 살아있지만(Activity 객체가 메모리에 보관되어 있고, 모든 상태 및 멤버 정보를 유지하며, 창 관리자에 붙어 있는 상태로 유지됨), 메모리가 극히 부족한 경우 시스템이 중단시킬 수 있습니다.

**Stopped**

해당 Activity가 다른 Activity에 완전히 가려진 상태이다(Activity가 이제 "백그라운드"에 위치함). 중단된 Activity도 여전히 살아 있기는 마찬가지이다(Activity 객체가 메모리에 보관되어 있고, 모든 상태와 멤버 정보를 유지하시만 창 관리자에 붙어 있지 않음 ). 그러나, 이는 더 이상 사용자에게 표시되지 않으며 다른 곳에 메모리가 필요하면 시스템이 종료시킬 수 있다.

Metohd | 시점 | 처리 예 | 설명
---- | ---- | ---- | ----
onCreate | 생성 시 | 초기화 처리와 뷰 생성(setContentView 호출) 등 | Activity가 처음 만들어질 때 호출되는 함수이면서, 어플리케이션이 처음 시작할 때 최초로 한번 실행되는 함수이다. 주로 View를 만들거나 view resource bind , data to list 등을 onCreate()에서 담당하며, 이전 상태의 정보를 담고있는 Bundle을 제공한다.
onStart | 비표시 시 | 통신이나 센서 처리를 시작 | Activity가 사용자에게 보여지기 직전에 호출되는 함수
onRestart | 표시 시(재시작만) | 보통은 아무것도 하지 않아도 된다. | Activity가 멈춰있다가 다시 호출될 때 불리는 함수, 즉 Stopped 상태였을 때 다시 호출되어 시작될 때 불린다.
onResume | 최전면 표시 | 필요한 애니메이션 실행 등의 화면 갱신 처리 | Activity가 비로소 화면에 보여지는 단계, 사용자에게 Focus를 잡은 상태
onPause | 일부 표시(일시정지) 상태 | 애니메이션 등 화면 갱신 처리를 정지 또는 일시정지할 때 필요 없는 리소스를 해제하거나 필요한 데이터를 영속화 | **Activity위에 다른 Activity가 올라와서 focus를 잃었을 때 호출되는 함수이다.** 완전 Activity가 가려지지 않은 상태에서 호출되는 함수이다. 즉, 일부분이 보이거나 투명상태일 경우 호출된다. 다른 Activity가 호출되기 전에 실행되기 때문에 onPause()함수에서 시간이 많이 소요되는 작업이나, 많은 일을 처리하면, 다른 Activity가 호출되는 시간이 지연되기 때문에 많은 일을 처리하지 않도록 주의하자. 영구적인 Data는 여기서 저장한다. Dialog 등에 의해 Focus를 잃은 경우는 onPause()상태가 되지 않는다. Dialog 스타일의 Activity를 띄웠을 경우에는 onPause()상태가 된다.
onStop | 비표시(정지) 상태 | 통신이나 센서 처리를 정리 | Activity위에 다른 Activity가 완전히 올라와 화면에서 100% 가려질 때 호출되는 함수이다. 홈키를 누르는 경우 또는 다른 Activity 페이지 이동이 있는 경우. 만약 이상태에서 Activity가 다시 불려지면, onRestart()함수가 호출된다.
onDestroy | 폐기 시 | 필요 없는 리소스를 해제. 액티비티 참조는 모두 정리 | Activity가 완전히 스택에서 없어질 때 호출되는 함수, 즉 제거되는 경우. finish() 메소드가 호출되거나, 시스템 메모리 확보를 위해 호출된다.

***onStop(), onDestroy() 함수는 호출되지 않을 수 있다.**

ex) 메모리 부족으로 인해 onStop()을 안 탈 수 있다.
```Java
public class ExampleActivity extends Activity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // The activity is being created.
    }
    @Override
    protected void onStart() {
        super.onStart();
        // The activity is about to become visible.
    }
    @Override
    protected void onResume() {
        super.onResume();
        // The activity has become visible (it is now "resumed").
    }
    @Override
    protected void onPause() {
        super.onPause();
        // Another activity is taking focus (this activity is about to be "paused").
    }
    @Override
    protected void onStop() {
        super.onStop();
        // The activity is no longer visible (it is now "stopped")
    }
    @Override
    protected void onDestroy() {
        super.onDestroy();
        // The activity is about to be destroyed.
    }
}
```
    
## Activity 상태 저장

![](https://developer.android.com/images/fundamentals/restore_instance.png?hl=ko)

시스템이 메모리를 복구하기 위해 액티비티를 소멸시키는 경우에는 Activity 객체가 소멸되므로 시스템이 액티비티의 상태를 온전히 유지한 채로 간단하게 재개할 수 없게 된다. 대신, 사용자가 다시 이 Activity로 이동해 오면 시스템이 Activity 객체를 다시 생성해야 한다. 이런 경우는 **사용자가 앱을 백그라운드에 두고 장시간 다른 일을 하다 다시 앱을 사용하기 시작했을 때나 화면 회전을 했을 때, 키보드 가용성 및 언어를 변경했을 때** 발생한다. 이런 상황에서는 Activity 상태에 관한 정보를 저장할 수 있는 추가 콜백 메서드 **onSaveInstanceState()를 구현하여 Activity 상태에 관한 중요한 정보를 보존**해야 한다. 시스템이 애플리케이션 프로세스를 종료하고 사용자가 Activity로 다시 돌아오면, 시스템이 Activity를 다시 생성하고 **Bundle을 onCreate()와 onRestoreInstanceState()에게 전달**한다. 이들 메서드 중 하나를 사용하여 **Bundle에서 저장된 상태를 추출하고 Activity 상태 를 복원**할 수 있다. 복구할 상태 정보가 없는 경우, 전달되는 Bundle은 null이다. onSaveInstanceState()의 기본 구현이 UI 상태를 저장하는 데 도움이 되기 때문에, 추가 상태 정보를 저장하기 위해 이 메서드를 재정의하려면 작업을 하기 전에 항상 onSaveInstanceState()의 슈퍼클래스 구현을 호출해야 한다. 이와 마찬가지로 onRestoreInstanceState()를 재정의하는 경우, 이것의 슈퍼클래스 구현도 호출해야 한다. 이렇게 해야 기본 구현이 뷰 상태를 복구할 수 있다.

설정할 수 있는 자료형은 int, float 등의 자바 기본형과 문자열 또는 리스트와 Parcelable 형을 구현한 인스턴스이다. Pacelable은 '작은 화물'이라는 의미에 '가능하다' 라는 접미사를 붙여 '짐으로서 운반할 수 있는 것'이 된다.  onSaveInstanceState() / onRestoreInstanceState()에서는 시스템의 임시 영역을 활용하고, 프로세스 간 통신으로 데이터를 주고 받는다. 프로세스 간 통신에서는 서로의 자료형을 어떻게 주고받을지 정해 둘 필요가 있는데, 그 전달 방법이 Pacelable 인터페이스로 정의돼 있다고 이해하면 된다.

onSaveInstanceState()의 호출이 보장되지 않으므로 이것은 Activity의 일시적 상태(UI의 상태 )를 기록하는 데에만 사용하고, 영구 데이터를 보관하는 데 사용해서는 안 된다.

애플리케이션의 상태 저장 기능을 시험하는 좋은 방법은 기기를 회전해보고 화면 방향이 바뀌는지 확인하는 것이다.

```kotlin
override fun onSaveInstanceState(outState: Bundle?) {
    // Save the user's current game state
    outState?.run {
        putInt(STATE_SCORE, currentScore)
        putInt(STATE_LEVEL, currentLevel)
    }

    // Always call the superclass so it can save the view hierarchy state
    super.onSaveInstanceState(outState)
}

companion object {
    val STATE_SCORE = "playerScore"
    val STATE_LEVEL = "playerLevel"
}
```

onCreate()에서 복원하는 경우
```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState) // Always call the superclass first

    // Check whether we're recreating a previously destroyed instance
    if (savedInstanceState != null) {
        with(savedInstanceState) {
            // Restore value of members from saved state
            currentScore = getInt(STATE_SCORE)
            currentLevel = getInt(STATE_LEVEL)
        }
    } else {
        // Probably initialize members with default values for a new instance
    }
    // ...
}
```

onStart() 메서드 호출 후 onRestoreInstanceState()에서 복원하는 경우
```kotlin
override fun onRestoreInstanceState(savedInstanceState: Bundle?) {
    // Always call the superclass so it can restore the view hierarchy
    super.onRestoreInstanceState(savedInstanceState)

    // Restore state members from saved instance
    savedInstanceState?.run {
        currentScore = getInt(STATE_SCORE)
        currentLevel = getInt(STATE_LEVEL)
    }
}
```

## Activity 조정

수명 주기 콜백은 분명히 정의된 순서가 있으며 특히 두 개의 Activity가 같은 프로세스 안에 있으면서 하나가 다른 하나를 시작하는 경우 순서가 더욱 확실하다. 다음은 Activity A가 Activity B를 시작할 때 발생하는 작업 순서이다.

1. Activity A의 onPause() 메서드가 실행된다.
2. Activity B의 onCreate(), onStart() 및 onResume() 메서드가 순차적으로 실행된다. (이제 사용자는 Activity B에 시선을 집중한다).
3. 그런 다음, Activity A가 더 이상 화면에 표시되지 않는 경우 이 Activity의 onStop() 메서드가 실행된다.
4. 이후 Activity A에서 onSaveInstanceState()가 호출되어 상태를 저장한다.

이처럼 수명 주기 콜백의 순서를 예측할 수 있기 때문에 한 Activity에서 다른 Activity로 전환되는 정보를 관리할 수 있다. 예를 들어 첫 번째 Activity가 중단될 때 데이터베이스에 내용을 작성해서 다음 Activity가 그 내용을 읽을 수 있도록 하려면, 데이터베이스에는 onPause() 중에(onStop() 중이 아니라) 쓰기 작업을 해야 한다.

반대로 Activity B에서 Back Button을 눌렀을 때 발생하는 작업 순서이다.

1. Activity B의 onPause() 메서드가 실행된다.
2. Activity B의 onRestart(), onStart() 및 onResume() 메서드가 순차적으로 실행된다. (이제 사용자는 Activity B에 시선을 집중한다).
3. 그런 다음, Activity A가 더 이상 화면에 표시되지 않는 경우 이 Activity의 onStop() 메서드가 실행된다.
4. 이후 onDestroy()가 호출되어 Activity B를 폐기한다.
