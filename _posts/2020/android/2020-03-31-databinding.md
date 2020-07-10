---
layout: post
title: "[Kotlin] android DataBinding Library for kotlin"
date: 2020-03-31 10:14
category: 
author: colinch4
tags: [kotlin]
description: "DataBinding Library 는 유연성과 폭넓은 호환성을 제공하여 선언적 레이아웃을 작성 가능하게끔 지원해줌으로써, 어플리케이션 로직과 레이아웃을 바인딩 하는데 유용하게 사용 할 수 있습니다."
comments: true
share: true
---


DataBinding Library 는 유연성과 폭넓은 호환성을 제공하여 선언적 레이아웃을 작성 가능하게끔 지원해줌으로써, 어플리케이션 로직과 레이아웃을 바인딩 하는데 유용하게 사용 할 수 있습니다.

# 프로젝트 설정 

먼저 DataBinding 사용을 위한 프로젝트 설정법을 살펴봅시다.
모듈 수준의 build.gradle 에서 다음과 같이 설정 합니다.

```java
android {
    ....
    dataBinding {
        enabled = true
    }
}
```

java 언어로 사용 할 경우 위 설정 하나로 바로 사용이 가능합니다만, kotlin 의 경우 추가 설정이 필요 합니다.
모듈 수준의 build.gradle 에서 다음과 같은 속성을 추가로 설정 합니다.

com.android.databinding:compiler 버전을 3.1.2 로 설정 하였는데, 이는 사용중인 gradle 버전을 설정해주시면 됩니다.
(gradle 버전은 프로젝트 수준의 build.gradle 에서 com.android.tools.build:gradle 버전을 참고 하시면 됩니다)

# 기본 사용법 

이제 DataBinding 사용을 위한 설정이 끝났습니다.
그러면 기본적인 사용법을 알아보도록 하겠습니다.


```xml
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android">

    <data>

        <variable
            name="user"
            type="pistolcaffe.databindingexample.model.User" />
    </data>

    <LinearLayout
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="vertical">

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{user.firstName}" />

        <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@{user.lastName}" />

    </LinearLayout>
</layout>
```

Activity 를 하나 생성 하였고, content view 로 설정할 레이아웃을 위와같이 작성 하였습니다.
DataBinding 상에서는 레이아웃 파일 작성에 있어서 차이점이 있는데, 루트 태그는 layout 로 시작하고, data 요소와 view 루트 요소로 작성 되어 집니다.
data 태그 내에 작성 하는 내용은 이 레이아웃에서 사용할수 있는 변수들에 대한 내용 입니다.



```xml
<variable name="user" type="pistolcaffe.databindingexample.model.User" />

```

pistolcaffe.databindingexample.model package 에 있는 User class 를 user 라는 이름으로 이 레이아웃에서 사용한다는 내용 입니다.
레이아웃 binding 을 위해서는 "@{}" 구문이 사용 되어 집니다. 위 예제 코드에서 첫번째 TextView 의 코드를 다시 보겠습니다.


```xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@{user.firstName}" />

```

android:text 속성을 "@{}" 구문내에 user.firstName 으로 설정 하였습니다. 이는 앱이 실행 되고 binding 이 이뤄질때 text 를 user 객체의 firstName 변수에 있는 값으로 설정 한다는 뜻인데요. 기초적인 레이아웃 binding 방법을 살펴보았고 이제 binding 하려는 data 클래스에 대해 살펴보겠습니다. 여기서는 User 클래스를 작성하였으므로 User 클래스를 보겠습니다.


```kotlin
data class User(val firstName: String, val lastName: String)

```

kotlin 에서 데이터 저장을 위해 유용하게 사용 할수 있는 data class 로 설정한 User 클래스 입니다.
firstName 는 public 이며 final 로 선언 하였습니다. 따라서 위의 TextView 에서 @{user.firstName} 으로 설정 하였으므로 firstName 에 들어간 값이 binding 될 것 입니다. 이 경우에 만약 firstName 이 private 으로 되어있다면 컴파일이 에러가 발생 합니다.
그렇다면 private 변수에 대한 처리를 알아봅시다.


```kotlin
data class User(private val firstName: String, val lastName: String){
   fun getFirstName() = firstName
}

```

firstName 에 대한 접근자 메소드를 추가 하였습니다.
이렇게 별도의 접근자 메소드를 작성 한 경우 @{user.firstName} 에 대해서 접근자 메소드를 통해 firstName 값을 binding 하게 됩니다.
이때 접근자 메소드 이름이 일반적인 접근자 메소드 이름 형태가 아닐 경우 바인딩이 되지 않고 컴파일 에러가 발생 합니다.
테스트를 해보니 별도의 메소드 이름으로 지정하거나 getfirstname 등 카멜표기법으로 되어 있지 않거나 하는 경우 바인딩이 되지 않았습니다.

대신 @{user.firstName} 으로 작성 하였으므로 해당 binding 객체에 firstName() 이라는 메소드가 있을 경우 해당 메소드가 binding 되어 사용 되어 집니다.
또한, 이렇게 별도의 접근자 메소드를 작성 하였을 경우 @{user.firstName} 혹은 @{user.getFirstName} 으로도 사용 가능 합니다.

databinding 을 위한 기초적인 레이아웃 파일 작성법과 레이아웃과 binding 될 데이터 객체를 살펴 보았습니다.
그러면 이제 본격적으로 Databinding 을 시켜 보도록 하겠습니다


```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    val binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout.activity_main)
    binding.user = User("sumin", "jin")
}

```

Activity 의 onCreate() 에서 다음과 같이 작성 하였습니다.
Databinding 을 위해서는 DataBindingUtil 의 setContentView 를 사용해야 합니다.
여기서 binding 변수의 타입이 ActivityMainBinding 임을 볼수 있는데, 이 binding 클래스는 빌드시 자동으로 생성 되는 클래스로써, 해당 레이아웃 파일의 이름을 참고하여 클래스가 생성 됩니다.
예를들어, 위 코드에서 databinding 하려는 레이아웃 파일 이름이 activity_main.xml 이므로 ActivityMainBinding 이라는 이름으로 binding 클래스가 자동 생성 됩니다. 만약 레이아웃 파일이름이 test.xml 라면 TestBinding 이라는 이름으로 binding 클래스가 생성 될 것 입니다.
임의로 binding 클래스를 지정 할 수도 있는데 이부분은 밑에서 언급 하도록 하겠습니다.

binding 하고자 하는 레이아웃 파일을 DataBindingUtil.setContentView() 를 통해 설정 하였고 이제 레이아웃 파일에서 사용하려는 binding 객체를 설정할 차례 입니다. 레이아웃 파일 작성 예제에서, data 태그내에 다음과 같이 작성 하였는데요.


```xml
<variable name="user" type="pistolcaffe.databindingexample.model.User" />

```

이때 variable name 을 user 로 설정 하였습니다. 그러면 위에서 ActivityMainBinding 클래스가 작성 될 때 user 에 대한 접근자/설정자 메소드가 자동으로 추가되며, binding 하려는 데이터 객체를 다음과 같이 설정 할 수 있습니다.


```kotlin
binding.user = User("gil-dong", "Hong")
```
이제 DataBinding 을 위한 모든 단계가 끝났습니다. 앱을 실행하면 다음과 같이 결과가 나타날 것입니다.

# 이벤트 처리

```java
android:onClick
android:onCheckChanged
```

위와 같은 속성을 사용해본적이 있으실 겁니다.
DataBinding 을 사용하면 위와같은 속성에 이벤트 핸들러 메소드를 바인딩 하거나 리스너를 바인딩 하여 원하는 작업을 수행 할 수 있습니다.
장점은 컴파일 시 처리가 되므로, 바인딩 하려는 메소드가 존재하지 않거나 잘못 되었을 경우 런타임 에러가 발생하는 것이 아니라 컴파일 에러가 발생 한다는 점입니다. 이벤트 핸들러 바인딩은 두가지 방식이 있는데요.

● 핸들러 메소드를 직접 바인딩 하는 방식

● 리스너를 바인딩 하는 방식

먼저 핸들러 메소드를 직접 바인딩 하는 방식을 보겠습니다.
친구추가 버튼을 추가하여 클릭 시 이벤트 처리를 위한 핸들러 메소드를 직접 바인딩 시켜 보겠습니다.


```kotlin
//이벤트 처리를 위한 클래스 작성
class MyHandlers {
    fun onClickAddFriend(v: View) {
        ...
        Toast.makeText(v.context, "친구로 등록 되었습니다", Toast.LENGTH_SHORT).show()
    }
}
```

레이아웃 파일에 handler 등록을 위해 data 태그 안에 클래스 정보를 추가하고 버튼을 배치합니다


```xml
<data
    ...
    <variable name="handler" type="pistolcaffe.databindingexample.MyHandlers"/>
/data>
....
<Button
    android:layout_width="wrap_content"
    android:layout_height="wrap_content
    android:onClick="@{handler::onClickAddFriend}"
    android:text="친구추가" />
```

친구추가 버튼에 android:onClick="@{handler::onClickAddFriend}" 로 정의 함으로써, 클릭 이벤트 핸들러 메소드를 직접 바인딩 하였습니다.
유의할부분은 "variable::메소드명" 이 아닌 "variable.메소드명" 으로 작성 하여도 동작은 하지만 deprecated 되어 "::" 사용을 권고 하고 있습니다.
또한, 바인딩 하려는 핸들러 메소드는 해당 이벤트 클릭 리스너의 메소드 형태와 동일 해야 합니다.

예를들어 클릭 이벤트의 경우, 아래와 같은 형태이므로 return type 이 void 이고 매개변수로 View 가 있으므로 이 형태로 바인딩 메소드를 작성 해야 합니다.
```java
//click listener
public interface OnClickListener {
    void onClick(View v);
}
```
```kotlin
//binding method
fun 메소드명 (v: View) // ok
fun 메소드명 () // 매개변수가 없으므로 바인딩 실패
fun 메소드명 (idx: Int) // 매개변수가 잘못 되었으므로 바인딩 실패
fun 메소드명 () : Boolean // return type 이 boolean 이므로 바인딩 실패
```
마지막으로 레이아웃 파일에 추가한 MyHandler data 객체를 설정 합니다.
```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    val binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout.activity_main)
    binding.user = User("sumin", "jin")

    //handler variable 에 MyHandler 객체 설정
    binding.handler = MyHandlers()
}
```
다음은 리스너를 바인딩 하는 방식 입니다.
// 친구관리를 하는 Manager 클래스 작성
```java
class FriendManager {
    fun addFriend(friend: User) {
        ....
    }
}
```
// 레이아웃에 variable 추가
```xml
<variable name="manager" type="pistolcaffe.databindingexample.FriendManager" />

// onClick 정의
<Button
    android:layout_width="wrap_content"
    android:layout_height="wrap_content
    android:onClick="@{() -> manager.addFriend(user)}"
    android:text="친구추가" />
```
리스너는 람다 형태로 표현 합니다. 바인딩이 필요한 이벤트 리스너를 자동으로 생성하고, 이벤트가 발생하면 바인딩 된 식을 실행하는 형태 입니다
위의 예시에서는 onClick(view : View) 로 전달 되는 view 매개변수를 지정하지 않았는데요. 리스너를 바인딩 할때는 모든 매개변수를 지정하거나, 지정하지 않고 사용 할 수 있습니다. 매개변수를 지정하면 메소드에 해당 변수를 그대로 사용 할 수 있습니다. 예시는 아래와 같습니다.

```kotlin
class FriendManager {
    //메소드에 view 매개변수 추가
    fun addFriend(v: View, friend: User) {
        ....
    }
}
```

```xml
//리스너에 매개변수 추가
<Button
    android:layout_width="wrap_content"
    android:layout_height="wrap_content
    android:onClick="@{(view) -> manager.addFriend(view, user)}"
    android:text="친구추가" />
```
이때 리스너 안에 바인딩 된 식은 발생한 이벤트리스너의 return type 과 동일한 type 을 return 해야 합니다.
```java
public interface OnLongClickListener {
    boolean onLongClick(View v);
}

class FriendManager {
    fun onUserLongClick() : Boolean {
        ....
    }
}
```
예를들어 longclick 이벤트 리스너의 경우 onLongClick 메소드가 boolean 형태의 return type 으로 선언 되어있기 때문에 바인딩 할 메소드에서도 boolean 을 return 해야 합니다.


# 레이아웃 세부 정보

## Import

레이아웃에서 import 를 통해 해당 클래스를 참조 할 수 있습니다. 예를들어 View 클래스를 참조하려면 아래와 같이 추가 하여 사용 합니다.
```xml
<data>
    <import type="android.view.View"/>
    ....
</data>
```
그러면 View 클래스를 import 하고 있으므로 View.VISIBLE , View.GONE 을 사용하여 아래와 같은 바인딩 코드를 작성 할 수 있습니다
```xml
<ImageView
    android:id="@+id/bookMarkImg"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:visibility="@{item.isBookMark ? View.VISIBLE : View.GONE}" />
```
정적 필드와 정적 메소드 또한 import 후 사용 할 수 있습니다.
다만 kotlin 에서 사용하기 위해서 companion object 에 선언한 필드 혹은 메소드에 @JvmField 혹은 @JvmStatic Annotation 을 추가 한 후 사용 할 수 있습니다. (정적필드가 primitive type 혹은 string 이면 별도의 annotation 을 추가하지 않고 사용 가능합니다)
```kotlin
//Utils.kt
class Utils {
    companion object {
        @JvmStatic
        fun capitalize(name: String): String {
            return name.toUpperCase()
        }
    }
}
```
```xml
//layout
<data>
    <import type="pistolcaffe.databindingexample.Utils"/>
    ....
</data>

<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@{Utils.capitalize(user.firstName)}" />
```
만약 import 하려는 class 명이 같다면, 아래와 같이 별도의 alias 를 지정하여 사용 할 수 있습니다.
```xml
<data>
    <import type="pistolcaffe.databindingexample.View"
           alias="AppView" />
    <import type="android.view.View" />
    ....
</data>
```

## Variables
```xml
<data>
    <import type="android.graphics.drawable.Drawable"/>
    <variable name="user"  type="com.example.User"/>
    <variable name="image" type="Drawable"/>
    <variable name="note"  type="String"/>
</data>
```

data 안에 선언되는 variable 은 빌드 시 binding 클래스가 생성 되면서 각각의 setter/getter 메소드를 갖게 됩니다.
이때 setter 가 호출 되기 전 기본 값은 참조 형식의 variable 은 null, int 의 경우 0, boolean 의 경우 false 를 갖습니다.

만약 참조하려는 variable 이 null일 경우 NullpointerException 을 방지 하기 위해 위와 같은 기본 값이 return 됩니다.
예를들어 "@{user.age}" 일 때 user 가 null 인 경우 age(Int) 의 기본 값인 0 이 할당되게 됩니다.

또한 기본적으로 binding 클래스가 생성 될때 root view 의 context 를 가져오게 되는데, 레이아웃 파일에서 "context" 라는 이름으로 context 를 사용 할 수도 있습니다. context 를 사용하여 color resource 를 가져온 뒤 textColor 를 설정해 보겠습니다.


```xml
<data>
    <import type="android.support.v4.content.ContextCompat"/>
</data>

<TextView
    android:id="@+id/test1"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:textColor="@{ContextCompat.getColor(context, android.R.color.holo_green_light)}" />
```

color resource 를 바로 설정해도 되지만 레이아웃 파일에서 context variable 사용 예제를 위해 작성해보았습니다.
변수선언에 있어 유의사항은 가로/세로 모드에 따른 별도의 binding 구현 시 변수이름이 충돌되지 않게 선언하여 사용해야 한다는 점입니다.

## Binding class

위에서 한번 언급하였지만 빌드 시 레이아웃 파일 이름을 기준으로 binding 클래스가 생성 됩니다.
이때 파일이름 기준으로 대문자로 시작하고  "_" 가 제거 되고 다음문자를 대문자로 바꾼다음 "Binding" 이 접미사로 붙습니다.
이 클래스는 모듈 패키지 하위에 databinding 패키지에 배치 되게 됩니다. 예를들어 모듈 패키지가 "com.example" 인 경우 "com.example.databinding" 패키지에 binding 클래스가 생성되어 배치되게 됩니다.

binding 클래스는 임의로 정의 할수도 있는데, 아래와 같이 원하는 이름을 지정합니다.

```xml
//type1 모듈패키지 하위 databinding 패키지에 생성
<data class="임의의클래스명">
...
</data>

//type2 모듈패키지에 바로 생성
<data class=".임의의클래스명">
...
</data>

//type3 특정패키지에 생성 (com.example.app)
<data class="com.example.app.임의의클래스명">
...
</data>
```

이렇게 하면 해당 레이아웃 파일에 대한 binding 클래스는 지정한 이름으로 생성 되게 됩니다.

## Include

레이아웃 파일에서 include 태그를 사용 시 include 하려는 레이아웃 파일로 변수를 전달 할 수 있습니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:bind="http://schemas.android.com/apk/res-auto">
   <data>
       <variable name="user" type="com.example.User"/>
   </data>
   <LinearLayout
       android:orientation="vertical"
       android:layout_width="match_parent"
       android:layout_height="match_parent">
       <include layout="@layout/name"
           bind:user="@{user}"/>
       <include layout="@layout/contact"
           bind:user="@{user}"/>
   </LinearLayout>
</layout>
```

include 한 name.xml 과 contact.xml 에 bind:variable 속성을 통해 user 변수를 전달 하였습니다.
이렇게 사용하기 위해서는 전달 받고자 하는 레이아웃 파일에서 같은 이름의 변수가 선언 되어있어야 합니다

그러나 merge 태그의 하위요소로서 include 를 허용하지 않습니다. 예를들어 다음과 같은 형태는 지원하지 않습니다

```xml
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:bind="http://schemas.android.com/apk/res-auto">
   <data>
       <variable name="user" type="com.example.User"/>
   </data>
   <merge>
       <include layout="@layout/name"
           bind:user="@{user}"/>
       <include layout="@layout/contact"
           bind:user="@{user}"/>
   </merge>
</layout>
```

## 공통 표현식

아래와 같은 표현은 java 와 동일하게 사용 할 수 있습니다

<pre>
수학 + - / * %
문자열 연결 +
논리 && ||
이항 & | ^
단항 + - ! ~
시프트 >> >>> <<
비교 == > < >= <=
instanceof
그룹화 ()
리터럴 - 문자, 문자열, 숫자, null
형변환
메서드 호출
필드 액세스
배열 액세스 []
삼항 연산자 ?:
</pre>

예시 

```xml
android:text="@{String.valueOf(index + 1)}"
android:visibility="@{age < 13 ? View.GONE : View.VISIBLE}"
android:transitionName='@{"image_" + id}'
```

또한 null 병합 연산자(??) 를 지원하는데 다음과 같이 사용합니다

```xml
android:text="@{user.displayName ?? user.lastName}"
//아래와 같은 표현식으로 사용 됩니다
android:text="@{user.diaplyName != null ? user.displayName : user.lastName}"
```

왼쪽 피연산자가 null 이 아니면 왼쪽 피연산자가 선택 되고 오른쪽 피연산자가 null 이 아니면 오른쪽 피연산자가 선택 됩니다.

## Collection

편의상 [] 를 통해 collection 에 접근 할 수 있습니다.

```xml
<data>
    <import type="android.util.SparseArray"/>
    <import type="java.util.Map"/>
    <import type="java.util.List"/>
    <variable name="list" type="List&lt;String&gt;"/>
    <variable name="sparse" type="SparseArray&lt;String&gt;"/>
    <variable name="map" type="Map&lt;String, String&gt;"/>
    <variable name="index" type="int"/>
    <variable name="key" type="String"/>
</data>
…
android:text="@{list[index]}"
…
android:text="@{sparse[index]}"
…
android:text="@{map[key]}"
```

## 문자 리터럴
참조 값이 아닌 문자열을 바로 사용해야 하는 경우가 있습니다.
이때는 다음과 같은 형태로 바인딩을 표현하여 사용합니다.

```xml
android:text='@{map["firstName"]}' //작은 따옴표로 묶고 특성 값을 큰 따옴표를 사용
android:text="@{map[`firstName`]}" //큰 따옴표로 묶고 역따옴표를 사용
android:text="@{map[&quot;firstName&quot;]}" //큰 따옴표로 묶고 작은 따옴표 사용 (이때 xml 상에서 인식 되기 위해 &quot; 로 표현
```

## Resource

다음과 같이 바인딩 구문에 리소스를 직접 참조 할 수 있습니다.

```xml
android:padding="@{large? @dimen/largePadding : @dimen/smallPadding}"
```

또한 특정 리소스가 매개변수를 필요로 할 경우 아래와 같이 표현하여 사용합니다

```xml
android:text="@{@string/nameFormat(firstName, lastName)}"
android:text="@{@plurals/banana(bananaCount)}"
```

그러나 일부 리소스 참조의 경우, 아래와 같은 명시적인 사용이 필요 합니다.
		
| 형식 | 일반참조 | 바인딩 표현 상에서 참조 | 
| ---------- | ---------- | ------------ |
| String[]    | @array       | @stringArray       | 
| int[]	   | @array      | @intArray       | 
| TypedArray    | @array       | @typedArray       | 
| Animator | @animator | @animator |
| StateListAnimator	| @animator	| @stateListAnimator |
| color int	| @color	| @color |
| ColorStateList	| @color	| @colorStateList |


# 데이터 객체 


기본적으로는 databinding 에서 임의의 데이터 객체를 사용하여 레이아웃과 바인딩을 구현 할 수 있지만 바인딩 하고 있는 객체의 값이 변경 되어도 UI  가 업데이트 되진 않습니다. 데이터가 변경 되었을 때 이를 알려주는 기능을 데이터 객체에 부여하면 databinding 의 장점을 극대화 시킬 수 있습니다.
databinding 은 데이터 변경에 대응하기 위한 세 가지 메커니즘을 제공 합니다. 차례대로 살펴보도록 하겠습니다.

## Observable Objects

바인딩 하려는 객체에 android.databinding.Observable 인터페이스를 구현하면 해당 객체에 단일 리스너를 연결하여 그 객체에 모든 속성의 변경사항을 수신 할 수 있게 됩니다. 편의를 위해 BaseObservable 클래스를 제공하고 있으며, 원하는 객체에 BaseObservable 클래스를 확장하여 사용 할 수 있습니다.
내부적으로 리스너를 추가/해제 하는 메커니즘을 갖고 있지만 최종적으로 데이터 변경에 대해 처리를 하기 위해서는 해당 필드의 접근자 메소드에 android.databinding.Bindable annotation 을 추가하고 설정자 메소드에서 이를 알림으로써 구현 할 수 있습니다. 예제코드를 살펴보겠습니다.

```kotlin
data class User(private var firstName: String,
                private var lastName: String) : BaseObservable() { //BaseObservable 상속

    //데이터 변경 시 알림을 수신 하고자 하는 필드에 Bindable annotation 추가
    @Bindable
    fun getFirstName() = firstName

    @Bindable
    fun getLastName() = lastName

    fun setFirstName(firstName: String) {
        this.firstName = firstName

        //데이터 변경을 알리기 위해 notifyPropertyChanged() 호출
        notifyPropertyChanged(BR.firstName)
    }

    fun setLastName(lastName: String) {
        this.lastName = lastName
        notifyPropertyChanged(BR.lastName)
    }
}
```

getFirstName() , getLastName() 에 Bindable annotation 을 설정 하였습니다. Bindable annotation 을 설정한 필드는 컴파일 시 BR 이라는 클래스에 filedId 를 자동 생성하게 되는데, 이후 데이터 변경 알림을 위해 notifyPropertyChanged(filedId : Int) 를 호출 할 때 파라미터로 사용 됩니다. (BR 클래스 파일은 모듈 패키지 내에 생성 됩니다)
그리고 setFirstName() , setLastName() 내에서 notifyPropertyChanged() 를 호출하여 값이 변경 되었음을 알리게 됩니다.

위 에제코드에서는 data class 로 작성하였는데 만약 일반 class 로 작성한다면 아래와 같은 방법으로도 사용 할 수 있겠네요. 참고하시기 바랍니다.

```kotlin
class User(firstName: String, lastName: String) : BaseObservable() {
    var firstName = firstName
        @Bindable
        get() = field
        set(value) {
            field = value
            notifyPropertyChanged(BR.firstName)
        }
    var lastName = lastName
        @Bindable
        get() = field
        set(value) {
            field = value
            notifyPropertyChanged(BR.lastName)
        }
}
```

## Observable Fields

위에서 데이터 객체에 Observable interface 를 구현하여 사용하는 방식을 알아보았습니다.
두번째로 Databinding library 에서는 각 필드단위로 Observable 를 구현 할 수 있는 Observable Fileds 를 제공 합니다.
제공하는 Observable Fileds 목록은 아래와 같습니다.

```kotlin
ObservableField<T>
ObservableBoolean
ObservableByte
ObservableChar
ObservableShort
ObservableInt
ObservableLong
ObservableFloat
ObservableDouble
ObservableParcelable
```

예제 코드를 보겠습니다.

```kotlin
class User {
    val firstName: ObservableField<String> = ObservableField()
    val lastName: ObservableField<String> = ObservableField()
    val age: ObservableInt = ObservableInt()
}
```

이렇게 Observable 을 구현하려는 필드에 위와 같이 선언 해서 사용 할 수 있습니다.  값에 엑세스 하려면 set() , get() 메소드를 사용합니다.

```kotlin
val binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout.activity_main)
binding.user?.apply{
    firstName.set("gildong")
    lastName.set("Hong")
    age.set(20)
}

val userAge = binding.user?.age?.get()
```

## Observable Collection

마지막으로 databinding librar 는 Observable Collection 을 제공 합니다. 제공하는 Collection 은 아래와 같습니다.

```kotlin
ObservableArrayList<T>
ObservableArrayMap<K,V>
ObservableMap<K,V>
```

ObservableArrayMap 을 사용해보겠습니다. 키가 String 과 같은 참조 형식 일때 사용하기 적절합니다

```kotlin
ObservableArrayMap<String, Object> user = new ObservableArrayMap<>();
user.put("firstName", "Google");
user.put("lastName", "Inc.");
user.put("age", 17);
```

이제 레이아웃을 아래와 같이 수정하여 바인딩 할 수 있습니다.

```xml
<data>
    <import type="android.databinding.ObservableMap"/>
    <variable name="user" type="ObservableMap&lt;String, Object&gt;"/>
</data>
…
<TextView
   android:text='@{user["lastName"]}'
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>
<TextView
   android:text='@{String.valueOf(1 + (Integer)user["age"])}'
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>
```

ObservableList 의 예제도 한번 살펴 보겠습니다. List 에 값을 저장하고 바인딩 식에서 index 를 통해 바인딩이 가능합니다.

```xml
<data>
    <import type="android.databinding.ObservableList"/>
    <variable name="user" type="ObservableList&lt;Object&gt;"/>
</data>
....
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@{user[0]}" />

<TextView
    android:id="@+id/test1"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@{user[1]}" />
```

```kotlin
val binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout.activity_main)
binding.user = ObservableArrayList<Any>().apply{
    add("Google")
    add("Inc.")
    add(17)
}
```

kotlin 에서는 Object 대신 Any 라는 이름을 사용하지만 레이아웃에 variable 을 생성할때는 Object 로 선언해야 하는 점을 주의 하시기 바랍니다.

# 생성되는 바인딩 클래스 

앞서 언급했듯이 컴파일 단계에서 자동으로 바인딩 클래스가 생성 됩니다. 레이아웃 파일 이름을 기준으로 생성되며, 원하는 이름으로 지정 할 수 있는 방법도 알아 보았습니다. 생성 되는 바인딩 클래스들은 모두 android.databinding.ViewDataBinding 클래스를 확장 합니다.

## binding 생성

Activity 의 contentview 로 설정함과 동시에 binding 을 하기 위해 아래의 메소드를 사용했었습니다.

```kotlin
DataBindingUtil.setContentView(this, R.layout.레이아웃이름)
```

레이아웃에 바인딩하는 추가적인 방법은 여러 방식이 있으나 가장 일반적인 방법은 binding class 의 정적 메소드를 사용하는 것입니다 inflate() 를 사용하면 View 계층을 확장함과 동시에 data binding 이 이뤄집니다

```kotlin
val binding : MyLayoutBinding = MyLayoutBinding.inflate(layoutInflater)
val binding : MyLayoutBinding = MyLayoutBinding.inflate(layoutInflater, viewGroup, false)
```

이미 다른 메커니즘으로 infalte() 된 view 에 대해서는 아래와 같이 binding 작업만 따로 수행 할 수도 있습니다

```kotlin
//여기서 viewroot 는 이미 infalte 되어있는 view 입니다
val binding : MyLayoutBinding = MyLayoutBinding.bind(viewRoot)
```

바인딩클래스를 미리 알 수 없을떄도 있습니다. 이때는 DataBindingUtil 클래스를 사용하여 바인딩을 생성 할 수 있습니다.

```kotlin
val binding : ViewDataBinding = DataBindingUtil.inflate(layoutInflater, layoutId, parent, attachToParent)
val binding : ViewDataBinding = DataBindingUtil.bindTo(viewRoot, layoutId)
```

## ID 가 있는 view 에 대한 binding
databinding 은 id 가 있는 view 에 대해서는 자동으로 해당 view 에 대한 필드를 생성하여 findViewById 를 사용하지 않아도 view 에 바로 엑세스 할 수 있습니다.(또한 이 메커니즘이 findViewById 를 사용하는것 보다 더 빠를 수 있습니다)
kotlin 의 경우 kotlin-extension 을 통해 layout id 로 생성 되어지는 view 에 바로 엑세스가 가능한 맥락과 유사한 내용입니다.
예를들어 아래와 같은 id 를 갖는 view 들에 대해서 binding 클래스는 다음과 같이 필드를 생성 합니다.

```xml
<TextView
    android:id="@+id/lastNameTextView"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@{user[0]}" />

<TextView
    android:id="@+id/firstNameTextView"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@{user[1]}" />
```

```java
@NonNull
public final android.widget.TextView firstNameTextView;
@NonNull
public final android.widget.TextView lastNameTextView;
```

## 변수
레이아웃에 binding 을 위해 선언한 변수들에 대해서 binding class 에서는 접근자/생성자 메소드를 제공 합니다.

```xml
<data>
    <import type="android.graphics.drawable.Drawable"/>
    <variable name="user"  type="com.example.User"/>
    <variable name="image" type="Drawable"/>
    <variable name="note"  type="String"/>
</data>
```

```java
public abstract com.example.User getUser();
public abstract void setUser(com.example.User user);
public abstract Drawable getImage();
public abstract void setImage(Drawable image);
public abstract String getNote();
public abstract void setNote(String note);
```

## ViewStub 과 함께 사용하기 & 고급 바인딩
이 내용은 따로 포스팅 할 예정입니다. 포스팅 후 링크를 첨부 하도록 하겠습니다.

# 속성 값 설정 

## layout 속성에 대한 자동 메소드 선택
layout 속성에는 여러 종류가 있습니다. TextView 를 예로 들면 android:textColor, android:text 등이 있죠.
데이터 바인딩을 사용하면 바인딩 식이 적용 된 xml 속성에 대해 자동으로 setter 메소드를 찾아서 선택하고, 호출 합니다. 속성의 namespace 는 중요하지 않고 속성 이름만 정확하게 사용 하면 됩니다. 만약 android:text 속성에 바인딩 식이 적용 되어있다면 TextView 의 setText() 를 찾아서 binding 되는 것이 그 예 입니다.

또한 별도의 xml 속성을 제공하지 않는 특정 setter 메소드와 바인딩 하여 사용 할 수 있습니다.
DrawerLayout 을 예로 들어 보겠습니다. DrawerLayout 의 경우에는 해당 위젯에 대한 어떠한 XML attribute 도 제공하지 않습니다.
하지만 다양한 setter 메소드를 제공 하고 있죠. 여기서 setScrimColor(int color), setDrawerListener(DrawerLayout.DrawerListener listener) 이 두개의 setter 메소드로 예제를 살펴보겠습니다.

```xml
<android.support.v4.widget.DrawerLayout
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:scrimColor="@{@color/scrim}"
    app:drawerListener="@{fragment.drawerListener}"/>
```

app:scrimColor 와 app:drawerListener는 기본으로 제공하는 XML 속성이 아니지만,  
데이터바인딩 라이브러리를 사용하면 scrimColor 와 drawerListener 에 대한 setter 메소드를 찾아서 자동으로 적용 하게 됩니다
앞서 언급한 것과 같이 namespace 는 중요하지 않으며, setter 의 이름과 매개변수 타입을 동일하게 설정해주면 됩니다.

그러나 setter 와 속성 이름이 일치하지 않는 경우가 있을 것입니다. android:tint 의 경우 매핑 되는 setter 메소드는 setTint() 가 아닌 setImageTintList() 인데요.
이런 경우에는 BindingMethod annotation 을 사용하여 속성과 setter 를 연결 할 수 있습니다.

```kotlin
@BindingMethods({
       @BindingMethod(type = "android.widget.ImageView",
                      attribute = "android:tint",
                      method = "setImageTintList"),
})
```

가이드 문서에 따르면 framework 쪽에는 이미 위와같은 처리가 되있기 때문에 개발자가 직접 위와 같은 처리를 할 일은 거의 없을 것이라고 하네요.

## 커스텀 바인딩 로직
일부 XML 속성에 대해서는 별도의 바인딩 로직이 필요 할 수 있습니다. 예를 들어 android:paddingLeft 의 경우 제공하는 특정 setter 메소드가 없습니다.
그대신 setPadding() 이라는 setter 가 있으며 이 메소드를 이용하여 커스텀 바인딩 메소드를 생성하여 XML 속성과 연결 할 수 있습니다.
framework 에는 이미 이러한 처리가 되어 있는데 예시를 보도록 하겠습니다.

```java
@BindingAdapter("android:paddingLeft")
public static void setPaddingLeft(View view, int padding) {
   view.setPadding(padding,
                   view.getPaddingTop(),
                   view.getPaddingRight(),
                   view.getPaddingBottom());
}
```

setPadding(int left, int top, int right, int bottom) 메소드를 이용해서 커스텀 바인딩 메소드가 구현 된 예시입니다.
커스텀 바인딩 로직 구현을 위해서는 BindingAdapter annotation 을 사용 합니다. 괄호안에는 연결시키고자 하는 xml 속성 이름이 들어가고, namespace 는 중요하지 않습니다. 또한 여러개의 속성과 연결 시킬 수도 있습니다. 이번에는 직접 커스텀 바인딩 메소드를 구현해보겠습니다.

```kotlin
class MyBindingAdapter {
    companion object {
        @JvmStatic
        @BindingAdapter("imageUrl", "error")
        fun loadImage(view: ImageView, url: String, errorDrawable: Drawable) {
            Picasso.with(view.getContext()).load(url).error(errorDrawable).into(view);
        }
    }
}
```

1. BindingAdapter 메소드는 접근자가 public 이고 static 메소드로 작성해야 합니다. 따라서 kotlin 에서 사용하기 위해 @JvmStatic 을 추가로 정의 하였습니다.
2. @BindingAdapter annotation 을 작성 합니다. 여기서는 "imageUrl", "error" 속성과 매핑 하였습니다. "bind:imageUrl" 과 같이 특정 namespace 로 작성       할 수 있으나 xml 에서 꼭 namespace 를 동일하게 사용할 필요는 없습니다. "android" namespace 의 경우에는 동일한 namespace 를 사용해야 합니다.
3. 여러개의 속성을 적용 할때는 XML 에서 해당 속성들을 모두 사용해야 해당 BindingAdapter를 사용 할 수 있습니다.
    위의 코드로 예를들면 xml 에서 imageUrl 속성은 사용하고 error 속성은 사용하지 않으면 해당 adapter 를 사용 할 수 없습니다
4. 메소드의 매개변수는 중요합니다. 첫번째 인자는 반드시 적용하려는 view 를 매개변수로 해야 합니다.
    나머지 인자는 BindingAdapter annotation 에 정의한 속성에 들어갈 타입에 맞춰서 순서대로 작성 되어야 합니다.
    annotation 의 속성을 imageUrl (String) error (Drawable) 순서로 작성 하였기 때문에 메소드의 두번째 , 세번째 매개변수의 타입이 각각 String 과
    Drawable 로 작성 되었습니다

XML 에서는 아래와 같이 사용하면 됩니다.

```xml
<ImageView
    ...
    app:imageUrl="@{user.profileImgUrl}"
    app:error="@{@drawable/profile_load_error}"/>
```

또한 BindingAdapter 는 선택적으로 기존 값을 취할 수도 있습니다. 기존 값과 새 값을 취하는 메서드는 속성의 모든 기존 값을 먼저 가진 후 새 값을 가져 와야 합니다.

```kotlin
companion object{
    @JvmStatic
    @BindingAdapter("android:paddingLeft")
    fun setPaddingLeft(view: View, oldPadding: Int, newPadding: Int){
        if(oldPadding != newPadding){
            view.apply{ setPadding(oldPadding, paddingTop, paddingRight, paddingBottom) }
        }
    }
}
```

이렇게 BindingAdapter 메소드를 작성하면 두번째 인자는 기존 값, 세번째 인자는 새 값을 취하게 됩니다.

이벤트 핸들러의 경우 오직 한개의 추상메서드를 가진 추상클래스 혹은 인터페이스와 사용 할 수 있습니다.
framework 에 처리 되어있는 메소드를 보겠습니다.

```java
@BindingAdapter("android:onLayoutChange")
public static void setOnLayoutChangeListener(View view, View.OnLayoutChangeListener oldValue,
       View.OnLayoutChangeListener newValue) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
        if (oldValue != null) {
            view.removeOnLayoutChangeListener(oldValue);
        }
        if (newValue != null) {
            view.addOnLayoutChangeListener(newValue);
        }
    }
}
```

```kotlin
//for kotlin
companion object{
    @JvmStatic
    @BindingAdapter("android:onLayoutChange")
    fun setOnLayoutChangeListener(view: View, oldValue: View.OnLayoutChangeListener?, newValue: View.OnLayoutChangeListener?) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB) {
            oldValue?.let { view.removeOnLayoutChangeListener(it) }
            newValue?.let { view.addOnLayoutChangeListener(it) }
        }
    }
}
```

그렇다면 두개 이상의 추상메소드를 갖는 이벤트핸들러는 어떻게 처리할 수 있을까요?
예를들어 View.OnAttachStateChangeListener 에는 onViewAttachedToWindow() 와 onViewDetachedFromWindow() 두 메소드가 있습니다.
그러면 이들 메소드의 속성과 핸들러를 구분하기 위해 두개의 인터페이스를 생성해야 합니다. 계속해서 framework 에 처리 된 것을 예시로 보겠습니다

```java
@TargetApi(VERSION_CODES.HONEYCOMB_MR1)
public interface OnViewDetachedFromWindow {
    void onViewDetachedFromWindow(View v);
}
@TargetApi(VERSION_CODES.HONEYCOMB_MR1)
public interface OnViewAttachedToWindow {
    void onViewAttachedToWindow(View v);
}

//for kotlin
@TargetApi(VERSION_CODES.HONEYCOMB_MR1)
interface OnViewDetachedFromWindow {
    fun onViewDetachedFromWindow(v: View)
}
@TargetApi(VERSION_CODES.HONEYCOMB_MR1)
interface OnViewAttachedToWindow {
    fun onViewAttachedToWindow(v: View)
}
```

한 listener 를 변경 할 경우 다른 listener 에도 영향을 미칠 것이므로 아래와 같이 세가지의 각각 다른 BindingAdapter 가 필요 합니다.
즉 각 속성을 위한 BindingAdapter 하나와 두 listener 에 대한 각각의 BindingAdapter 가 필요 합니다.

```java
@BindingAdapter("android:onViewAttachedToWindow")
public static void setListener(View view, OnViewAttachedToWindow attached) {
    setListener(view, null, attached);
}

@BindingAdapter("android:onViewDetachedFromWindow")
public static void setListener(View view, OnViewDetachedFromWindow detached) {
    setListener(view, detached, null);
}

@BindingAdapter({"android:onViewDetachedFromWindow", "android:onViewAttachedToWindow"})
public static void setListener(View view, final OnViewDetachedFromWindow detach,
        final OnViewAttachedToWindow attach) {
    if (VERSION.SDK_INT >= VERSION_CODES.HONEYCOMB_MR1) {
        final OnAttachStateChangeListener newListener;
        if (detach == null && attach == null) {
            newListener = null;
        } else {
            newListener = new OnAttachStateChangeListener() {
                @Override
                public void onViewAttachedToWindow(View v) {
                    if (attach != null) {
                        attach.onViewAttachedToWindow(v);
                    }
                }

                @Override
                public void onViewDetachedFromWindow(View v) {
                    if (detach != null) {
                        detach.onViewDetachedFromWindow(v);
                    }
                }
            };
        }
        final OnAttachStateChangeListener oldListener = ListenerUtil.trackListener(view,
                newListener, R.id.onAttachStateChangeListener);
        if (oldListener != null) {
            view.removeOnAttachStateChangeListener(oldListener);
        }
        if (newListener != null) {
            view.addOnAttachStateChangeListener(newListener);
        }
    }
}

//for kotlin
@JvmStatic
@BindingAdapter("android:onViewAttachedToWindow")
fun setListener(view: View, attached: OnViewAttachedToWindow) {
    setListener(view, null, attached)
}

@JvmStatic
@BindingAdapter("android:onViewDetachedFromWindow")
fun setListener(view: View, detached: OnViewDetachedFromWindow) {
    setListener(view, detached, null)
}

@JvmStatic
@BindingAdapter("android:onViewDetachedFromWindow", "android:onViewAttachedToWindow")
fun setListener(view: View, detach: OnViewDetachedFromWindow?, attach: OnViewAttachedToWindow?) {
    if (VERSION.SDK_INT >= VERSION_CODES.HONEYCOMB_MR1) {
        val newListener: OnAttachStateChangeListener?
        if (detach == null && attach == null) {
            newListener = null
        } else {
            newListener = object : OnAttachStateChangeListener {
                override fun onViewAttachedToWindow(v: View) {
                    attach?.let { it.onViewAttachedToWindow(v) }
                }

                override fun onViewDetachedFromWindow(v: View) {
                    detach?.let { it.onViewDetachedFromWindow(v) }
                }
            }
        }
        val oldListener = ListenerUtil.trackListener(view, newListener, R.id.onAttachStateChangeListener)
        oldListener?.let{view.removeOnAttachStateChangeListener(it)}
        newListener?.let{view.addOnAttachStateChangeListener(it)}
    }
}
```

View.OnAttachStateChangeListener 는 setter 메소드 대신에 add, remove를 사용하기 때문에 위 예시의 경우는 일반적인 경우보다 복잡합니다.
위 예제코드에서 ListenerUtil 클래스를 볼수 있는데, 이것은 BindingAdapter 에서 이전의 listener 를 제거할 수 있도록 이들을 계속 찾는데 사용 할 수 있는 클래스 입니다.

# 객체 변환


## 자동 객체 형 변환

바인딩 식에서 객체가 리턴 될때, 데이터바인딩 라이브러리 내부에서 속성에 값을 설정할 적절한 메소드를 선택하게 됩니다.
객체는 선택 된 메소드의 매개변수 타입으로 캐스팅 되는데, 이것은 ObservableMap 을 사용하여 데이터를 관리할 경우 편리합니다.
예제를 보겠습니다. 

```xml
//xml
<layout>
<data>
    <import type="android.databinding.ObservableMap" />
    <variable name="map" type="ObservableMap&lt;String, Object&gt;" />
</data>

<TextView
    ....
    android:text="@{map[`firstName`]}" />
</layout>
```

```kotlin
//MainActivity.kt
val binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout.activity_main)
binding.map = ObservableArrayMap<String, Any>().apply {
            put("firstName", "hong")
            put("age", 20)
        }
```

layout 에 TextView 가 있고 android:text 속성에 @{map['firstName']} 바인딩 식이 적용 되어 있습니다.
MainActivity.kt 에서 map 은 ObservableArrayMap 이고, firstName 에 대한 값은 hong 이며 String type 인것을 볼 수 있습니다.
xml 에서 map 변수에 대한 type 이 ObservableMap<String, Object> 로 되어있지만 라이브러리 내에서 setText(text : CharSequence) 를 선택하기 때문에 매개변수인 CharSequence 로 캐스팅 되어 적용 되는 것입니다. 그렇다면 만약 @{map[`age`]} 로 바꾸면 어떻게 될까요?
age 에 대한 값은 20 즉, Int 형이기 떄문에 java.lang.ClassCastException: java.lang.Integer cannot be cast to java.lang.CharSequence 가 발생하게 됩니다.

이렇게 객체 타입이 불확실할 경우 별도의 캐스팅 동작을 바인딩 식에 적절히 추가해줘야 합니다. 아래와 같이 바인딩 식을 바꿔볼수 있겠네요.

```xml
<TextView
    ....
    android:text="@{String.valueOf(map[`firstName`])}" />

## 커스텀 형 변환 로직

하지만 특정 형식 간에 자동으로 변환이 이루어져야 할 상황이 있을 수 있습니다. background 속성을 지정할때를 예로 들면 아래와 같습니다

```xml
<View
   android:background="@{isError ? @color/red : @color/white}"
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>
```

android:background 속성은 Drawable 을 취하지만 color 는 정수 형태 입니다.
정수가 반환 될 때 int 가 ColorDrawable 로 변환 되어야 합니다. 이 변환은 BindingConversion annotation 을 통해 적용 할 수 있습니다.
아래 예제코드는 Drawable 이 필요한 속성에 int 값이 들어올 경우 자동으로 형변환을 해주는 BindingConversion 메소드이며, Databinding library 에서 기본적으로 제공하고 있습니다.

```java
@BindingConversion
public static ColorDrawable convertColorToDrawable(int color) {
   return new ColorDrawable(color);
}

//for kotlin
companion object{
    @JvmStatic
    @BindingConversion
    fun convertColorToDrawable(color : Int) : ColorDrawable {
       return ColorDrawable(color)
    }
}
```
참고로 변환은 setter 단계에서 이뤄지기 때문에 아래와 같이 형태를 혼합하여 사용 할 수 없습니다.
```xml
<View
   android:background="@{isError ? @drawable/error : @color/white}"
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"/>
```
이렇게 해서 DataBinding 에 대한 내용을 모두 살펴보았습니다. 
DataBinding 을 잘 활용하면 XML 과 혼합하여 굉장히 유연한 프로그래밍을 할 수 있을것 같네요.


