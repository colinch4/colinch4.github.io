---
layout: post
title: "[안드로이드 기초] Android는 어떻게 UI를 구성할까?(1) - Inflate"
description: " "
date: 2020-12-01
tags: [android]
comments: true
share: true
---



여태까지 안드로이드 UI를 구성하는데 크게 고민하지 않고 XML을 그리고 setContentView함수를 통해 불러오기만 했었다. 안드로이드 시스템은 어떻게 XML을 실제로 그려낼 수 있을까? 지금부터 파헤쳐본다.

## Inflate

안드로이드 프로그래밍을 하다보면 **Inflate**에 대해 많이 들어봤을 것이다.

Inflate는 사전적인 의미로 '부풀리다'라는 뜻이다. 안드로이드에서는 Inflate를 사용하면 XML에 작성된 View의 실체를 인스턴스화 하게 된다. XML에 정의된 Root Layout과 Child View들의 속성을 읽어서 실제로 View를 만들게 된다. 성능 상의 문제 때문에 XML파일은 빌드 과정에서 미리 컴파일 되어있다. 이렇게 미리 컴파일된 파일들을 R.XXX 형태의 리소스 ID를 찾아서 메모리에 로드한 후에 이용을 시작하는 것이다.

---

그렇다면 이러한 Inflate는 어떻게 실행될 수 있을까?

### setContentView()

setContentView()는 Activity 전체에 XML이나 View를 채우게 된다.

1. void setContentView(int layoutResID)
2. void setContentView(View view)
3. void setContentView(View view, ViewGroup.LayoutParams params)

위의 세 가지 메서드를 이용하면 R.layout.XXX나 View 객체를 통해 Activity를 채울 수 있게 된다.

이외에 addContentView()라는 메서드가 있는데 

```kotlin
    addContentView(linearLayout, ViewGroup.LayoutParams(MATCH_PARENT, WRAP_CONTENT))
```

이와 같이 기존에 생성된 View에 레이아웃을 겹칠 수 있는 기능을 한다.

### getSystemService(Context.LAYOUT_INFLATER_SERVICE), LayoutInflater.from

```kotlin
    val linearLayout = LinearLayout(this)
    linearLayout.orientation = LinearLayout.VERTICAL
    linearLayout.setBackgroundColor(Color.RED)
    
    val tv = TextView(this)
    tv.text = "하요"
    tv.textSize = 16.0f
    
    linearLayout.addView(tv)
    
    val view = LayoutInflater.from(this).inflate(R.layout.activity_home, linearLayout, false)
    
    val inflater : LayoutInflater = getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater
    val view2 = inflater.inflate(R.layout.activity_home, linearLayout, true)
```

위의 두 메서드는 원하는 XML 파일을 집어 넣고자 하는 Layout에 맞춰서 inflate하는 내용이다.

linearLayout은 XML 파일을 집어 넣고자 하는 Root View이며 해당 View에 맞춰서 inflate된다. 마지막 boolean 값은 attachToRoot로 true면 linearLayout에 View가 자식으로 추가되고 false면 Root View는 그저 생성될 View의 LayoutParams를 생성하는데만 쓰이게 된다.

```kotlin
    val view = LayoutInflater.from(this).inflate(R.layout.activity_home, linearLayout, false)
```

해당 코드는 특히 RecyclerView를 사용할 때 onCreateViewHolder에서 자주 볼 수 있는 형태의 패턴이다.

---

setContentView를 통해 객체가 만들어지기는 했다. 그렇다면 이 만들어진 layout이 실제로 기기의 화면에 그려지는 과정은 어떻게 될까? 이러한 layout들은 Surface와 Window에 의해 사용자의 눈에 보이게 된다.

![](https://i.stack.imgur.com/z1OpA.jpg)

## Window

View는 UI를 구성하는 최소단위이고, Window는 UI를 구성하는 최대단위이다. StatusBar, NavigationBar를 포함한 Android 전체 화면부터 Android UI를 보여줄 수 있는 대표적인 개체들인 Activity, Dialog, Toast 등은 모두 각자의 개별적인 Window를 가지고 있다. 홈 화면에서 OK캐시백 동전 UI가 보인다거나 하는 기능도 Window를 활용하여 구현할 수 있다. 자세한 Window의 종류는 해당 [링크](https://developer.android.com/reference/android/view/WindowManager.LayoutParams)에서 확인한다. 

Window는 사실 Interface이며 구현 클래스인 PhoneWindow를 활용하여 View가 Window에 배치되는 것 같다. 그리고 PhoneWindow는 Root View인 DecorView를 생성한다. 설정된 Window는 속성 값에 따라 DecorView에 기본으로 설정 될 layour resouce를 선정하고, 해당 layout 안에서 id 속성으로 android:id/content 값을 갖는 ViewGroup을 찾아서 해당 ViewGroup을 parent view로 설정한다. 그 parent view가 FrameLayout이고 이 안에 setContentView()에 설정한 XML이 배치되게 된다.

이를 깔끔하게 정리하면 이렇게 된다. 에코지오님이 정리를 잘해주셔서 인용한다.

1. ActivityManagerService는 ActivityThread를 호출하여 액티비티 런치. 

ActivityThread.performLaunchActivity()에서 Activity 인스턴스 생성하고 activity.attach() 호출

2. Activity는 attach()에서 PhoneWindow 객체 생성. 이 PhoneWindow는 액티비티내 뷰들의 root로서 DecorView 인스턴스 포함.

mWindow = PolicyManager.makeNewWindow(this);

3. ActivityManagerService는 ActivityThread를 호출하여 액티비티를 resume시킴.

WindowManager 인스턴스가 생성되고 decorView가 WindowManager에 추가됨.

ActivityThread.handleResumeActivity()

4. WindowManager의 addView(decor)에서 ViewRoot 인스턴스를 생성하고 viewRoot.setView(decor) 호출
5. viewroot.setView(decor)에서 IWindowSession을 통해 WindowManagerService에 IWindow인스턴스를 추가

IWindowSession.add(window)

출처: [https://ecogeo.tistory.com/251](https://ecogeo.tistory.com/251)

## Surface

![https://t1.daumcdn.net/cfile/tistory/232CCB4A586614EC1F](https://t1.daumcdn.net/cfile/tistory/232CCB4A586614EC1F)

각각의 Window는 고유한 Surface를 가진다. DecorView는 그릴 것이 있는 경우, 할당 받은 Surface에 그리게 된다. 여기서 그릴 것은 View의 Canvas에 그려진다. Application들이 가지고 있는 각 Surface들은 각각 BufferQueue에 연결되어 있으며 Surface에서 생성되는 화면의 정보가 BufferQueue에 축적되게 되면 이후 SurfaceFlinger에서 BufferQueue에 있는 Surface의 정보를 수신하게 된다. 각 Surface로부터 화면을 받은 SurfaceFlinger는 수신된 화면의 정보를 합성하게 되고 이를 디스플레이를 담당하는 HAL에 정보를 전달하게 되면 해당 화면이 안드로이드 기반 디바이스의 Display에 출력된다.

아래의 세 링크는 뷰가 그려지는 과정을 보다 원론적으로 설명하고 있는 블로그들의 링크이다. Choreographer, ViewRootImpl, Surface 등의 개념과 원리를 보다 자세하게 알고 싶으면 참고해야겠다.

[https://lastyouth.tistory.com/24](https://lastyouth.tistory.com/24)

[자유로운날개]

[https://elecs.tistory.com/131](https://elecs.tistory.com/131)

[늦깎이 공대생의 좌충우돌 이야기]

[https://openparadigm.tistory.com/49](https://openparadigm.tistory.com/49)

[OpenParadigm]

사실 Inflate하는 과정은 Activity에서 View 객체가 어떻게 눈에 보이게 되는지에 대한 내용이었다. 그렇다면 개별적인 View 객체들은 어떻게 화면에 **그려지고 배치되는** 것일까?
