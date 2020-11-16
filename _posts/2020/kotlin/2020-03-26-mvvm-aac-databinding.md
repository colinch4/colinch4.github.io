---
layout: post
title: "MVVM AAC Databinding 사용법"
date: 2020-03-26 14:36
category: 
author: kskim2
tags: [kotlin, mvvm]
description: "해당 문서는 안드로이드 공식 문서를 기반으로 만들어졌습니다. "
summary: 
---


> 해당 문서는 안드로이드 공식 문서를 기반으로 만들어졌습니다.  
> 공식문서:  [https://developer.android.com/topic/libraries/data-binding/?hl=ko](https://developer.android.com/topic/libraries/data-binding/?hl=ko)

최종적으로는 사용자의 프로필을 출력하는 앱을 만들어보도록 하겠습니다.

Jetpack AAC(Android Architecture Components 이하 AAC)를 이용하기 위해서는 기본 안드로이드 개발지식이 필요합니다. 때문에  **안드로이드에 대한 기본 지식이 있다는 가정하에**  포스팅을 진행하도록 하겠습니다.

개발의 절반은 세팅이라고 했습니다.  
1편에서는 데이터바인딩을 이용하기 위한 세팅을 진행하고,  
2편 이후에는 상세 구현방법을 설명하도록 하겠습니다.

안드로이드 라이브러리를 사용할때는 **최소 호환버전을 확인하는게 매우 중요**합니다. 구현을 해놓고 최소 호환 버전이 맞지 않으면 모두 제거해야 되는 경우가 부지기수로 발생합니다.

데이터 바인딩 라이브러리는 유연성과 폭넓은 호환성을 모두 제공하는 지원 라이브러리로,  **Android 2.1**(API 레벨 7 이상)까지 Android 플랫폼의 모든 이전 버전에서 사용할 수 있으므로 거의 모든버전에 사용 가능하다고 볼 수 있습니다.(저는 7.0 이하 기기 본적도 없습니다.)

또한 Android Plugin for Gradle  **1.5.0-alpha1**  이상이 필요합니다.

----------

# _1. 안드로이드 개발의 시작! Gradle Setting_

//코틀린 사용자의 경우(해당세팅 하지 않을경우 어뎁터 사용 불가)  
apply plugin: 'kotlin-kapt'android {  
    ....  
    dataBinding {  
        enabled = true  
    }  
}

생각보다 매우 간단합니다.

AAC중 거의 유일하게 implementation 코드가 필요 없습니다. 그 이유는 databinding enabled를 true로 변경하면 컴파일러가 컴파일될때 자동으로 필요한 바인딩 클래스를 작성해주기 때문입니다. 이와 비슷한 라이브러리는  [Butterknife](https://github.com/JakeWharton/butterknife)가 있습니다.(버터나이프는 라이브러리를 이용을 합니다.)

----------

# 2. 레이아웃 세팅

<?xml version="1.0" encoding="utf-8"?>  
<layout xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:app="http://schemas.android.com/apk/res-auto"  
        xmlns:tools="http://schemas.android.com/tools">  
  
    <data>  
        <variable  
                name="user"  
                type="com.hyun.android.databindingsample.User"/>  
    </data>  
  
    <FrameLayout  
            android:layout_width="match_parent"  
            android:layout_height="match_parent">  
        <TextView  
            android:id="@+id/tv_sample"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:text="@{user.name}"  
            android:layout_gravity="center"/>  
    </FrameLayout>  
</layout>

![](https://miro.medium.com/max/60/1*A_gR_ZkXZixUARNDdZXiHA.png?q=20)

![](https://miro.medium.com/max/556/1*A_gR_ZkXZixUARNDdZXiHA.png)

우리가 프로잭트를 처음 만들면 생성되는 Hello world에 데이터바인딩 세팅을 하였습니다.(코드 간소화를 위하여 레이아웃을 FrameLayout으로 변경하였습니다.)

기존 코드와의 변경점이 보이시나요???

<layout xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:app="http://schemas.android.com/apk/res-auto"  
        xmlns:tools="http://schemas.android.com/tools">  
...</layout>

**첫번째**는 ViewGroup에 속해있는 레이아웃(FrameLayout 등)을 루트태그로 사용하는것이 아니라 layout을 루트태그로 사용하고 있다는 점입니다.  
layout 태그는  **하나의 레이아웃만 자식 뷰로 가질 수 있으며**(NestedScrollView와 비슷)두개이상의 레이아웃을 자식뷰로 선언 할 경우 아래와 같은 오류를 내뱉습니다.

> data binding error ****msg:**Only one layout element**  and one data element are allowed.

**오류가 나는 레이아웃구조**는 아래와 같습니다.

//오류 발생  
<layout>  
    <Framelayout/>  
    <Framelayout/></layout>

**두번째**는 data태그입니다. (세팅이라고 하기는 좀 그렇지만 데이터바인딩을 사용하는 가장 큰 이유이기 때문에 세팅으로 넣었습니다.)

<layout>  
  
    <data>  
        <variable  
                name="user"  
                type="com.hyun.android.databindingsample.User"/>  
    </data>  
...</layout>

User클래스는 간단한 데이터 클래스로 아래와 같습니다.

data class User(  
    var name: String = ""  
    , var address: String = ""  
)

data 태그는 레이아웃에서 사용하고 싶은 오브잭트의 구성요소들을 직접 사용할 수 있습니다. 코드가 이해하는데 더 빠르겠죠???

<TextView  
        android:id="@+id/tv_sample"  
        android:layout_width="wrap_content"  
        android:layout_height="wrap_content"  
        **android:text="@{user.name}"**  
        android:layout_gravity="center"/>

이로써 레이아웃 세팅도 끝이났습니다.

----------

# 3. 액티비티 세팅

**액티비티 세팅을 하기전에 Build->Rebuild Project를 해주어야 합니다.**(데이터바인딩의 거의 유일한 단점이지만 매우 귀찮습니다.) 그 이유는 위에 설명한것 처럼 컴파일러가 자동으로 생성해주는 바인딩 클래스가 컴파일할때 생성되기 때문입니다.

자동으로 생성된 Binding 클래스는 다음과 같은 규칙을 따릅니다.

1.  Binding 클래스는 레이아웃 파일의 이름을 기준으로 생성되어 파일 이름을 파스칼 표기법으로 변환하고 그 뒤에 “Binding”을 접미사로 붙입니다.
2.  컴포넌트아이디는 “_”를 기준으로 카멜 표기법으로 변환됩니다.

> xml이름이 activity_main인 경우 ActivityMainBinding으로 자동 생성됩니다.  
> 컴포넌트 id값이 tv_sample일 경우 tvSample로 자동 생성됩니다.

선언방식은 아래와 같으며 Activity, Fragment, Adapter의 선언방식은 각각 다릅니다.(예제는 Activity만 설명하도록 하겠습니다.)

class MainActivity : AppCompatActivity() {  
  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
  
        //setContentView(R.layout.activity_main)  
  
        var binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout._activity_main_)  
        **binding.tvSample._text_**  = "이종현의 개발블로그입니다."//id: tv_sample  
    }  
}

액티비티 세팅은 매우 간단합니다.

DataBindingUtil클래스를 통하여 레이아웃을 Binding 하고, binding 인스턴스를 통해 값을 세팅하면 됩니다.

# 4. 데이터 바인딩

이름에서 표현되듯이 데이터를 레이아웃에 바인딩을 해주는 것을 의미합니다. 먼저 코드와 결과 화면을 보고 설명을 드리도록 하겠습니다.

Activity 클래스의 코드입니다.

기존에 findViewById를 통하여 뷰를 바인딩하고, 데이터를 세팅해 주던 코드에서,  **variable에 선언한 user라는 객체값을 직접 설정해줌**으로써 값들을 세팅할 수 있습니다. 지금은 2개의 값만있는 데이터이기 때문에 코드의 간소화가 체감되지 않을 수 있지만, 서버로부터 받아오는 데이터값이 10개, 20개 이상이면 어마어마한 코드다이어트를 실현할 수 있습니다.(단 한줄이면 데이터세팅은 완료됩니다.)

var binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout._activity_main_)**binding._user_ = User("이종현", "서울시")**

그렇다면 xml코드에서 데이터세팅은 어떻게 이루어지는지 보겠습니다.

**별도의 컴포넌트 id값이 필요없이**  값을 세팅해주고 싶은 위치에 객체값을 넣어주면 그만입니다.

<TextView  
        android:layout_width="wrap_content"  
        android:layout_height="wrap_content"  
        **android:text="@{user.name}"**  
        android:layout_gravity="center"  
        android:textSize="30dp"  
        tools:text="이부분에 이름이 표시됩니다."/>  
  
<TextView  
        android:layout_width="wrap_content"  
        android:layout_height="wrap_content"  
        **android:text="@{user.address}"**  
        android:layout_gravity="center"  
        android:textSize="30dp"  
        tools:text="이부분에 주소가 표시됩니다."/>

우리가 원하는 이름과 주소가 나오는 화면이 결과로 나오네요.

그런데 뭔가 부족합니다. 프로필앱에 사진이 빠진다면 서운하니까 사진도 넣어보도록 하겠습니다.

![](https://miro.medium.com/max/30/1*0oV-dGiy9tlCsLUI9gNL4w.jpeg?q=20)

![](https://miro.medium.com/max/467/1*0oV-dGiy9tlCsLUI9gNL4w.jpeg)

# 5. 커스텀 바인딩 어댑터

이미지를 넣기위해 저는  [Picaaso](https://github.com/square/picasso)  혹은  [Glide](http://glide/)라이브러리를 이용합니다. 하지만 매번 Activity, Fragment등 에서 Glide를 이용해서 프로필 사진을 세팅하기 귀찮습니다. 뭔가 객체로 한번에 세팅을 하고 싶습니다. 그럴때 사용하는 방법이 커스텀 바인딩 어댑터입니다. 데이터 바인딩 프레임워크에는 값을 설정하기 위해 호출할 함수를 사용자 지정하는 방법이 있습니다.

먼저 User클래스에 profileURL이라는 변수를 선언해줍니다.  
drawable res을 이용할 것이기때문에 Int형으로 선언해주었습니다.

data class User(  
    var name: String = ""  
    , var address: String = ""  
    , var profileURL: Int = -1  
)

그에맞게 Activity에서 User값도 변경해보겠습니다.

binding._user_ = User("이종현", "서울시", R.drawable._profile_sample_)

그다음 xml파일도 수정해보록 하죠. 그전에 커스텀 바인딩 어뎁터를 작성하도록 하겠습니다. 해당 포스팅에서는 Glide사용법에 대하여 자세하게 기술하지는 않겠습니다.

@BindingAdapter("**bind_image**")  
fun bindImage(view: ImageView, res: Int?) {  
    Glide.with(view._context_)  
        .load(res)  
        .into(view)  
}

app:bind_image은 BindingAdapter에 의하여 바인딩 된 문자열 값(“bind_image”)을 따릅니다. 또한  **첫번째 인자값으로 뷰 객체를 받으며 해당 뷰(ImageView)에서만 사용 할 수 있습니다.**  이후의 인자값은 바인딩 어뎁터에 선언한 값들과 1:1로 bind_image는 Int형 값을 인자로 받을 수 있습니다.

xml입니다.

<ImageView android:layout_width="match_parent"  
           android:layout_height="wrap_content"  
           **app:bind_image="@{user.profileURL}"**/>

인자값이 2개인 경우는 아래와 같이 사용할 수 있습니다.

@BindingAdapter(**"bind_image", "bind_image_error"**)  
fun bindImage(view: ImageView, res: Int, error: Drawable) {  
    val options = RequestOptions()  
        .error(error)  
  
    Glide.with(view._context_)  
        .load(res)  
        .apply(options)  
        .into(view)  
}

xml은 아래와 같으며 **app:bind_image, app:bind_image_error 둘다 구현해주지 않으면 바인딩 어뎁터를 찾을수 없어서 오류가 발생**합니다.

> An exception occurred: android.databinding.tool.util.LoggedErrorException:  **Found data binding errors.**

//해당코드는 정상동작 코드입니다.  
<ImageView android:layout_width="match_parent"  
           android:layout_height="wrap_content"  
           app:bind_image="@{user.profileURL}"  
           app:bind_image_error="@{@drawable/error_sample}"/>//오류가 발생하는 코드입니다. setArribute가 하나만 있으면안됨  
<ImageView  
          ...  
          app:bind_image="@{user.profileURL}"/>

> **BindingAdapter는 메소드의 인자값을 알아서 찾아줍니다.**

그 이유는 컴파일될때 activity_main.xm기준으로 ActivityMainBindingImpl라는 클래스가 생성이되는데 여기서 세터메소드를 호출합니다. ActivityMainBindingImpl 코드중 일부입니다.

//개발자가 작성한 코드가 아닌 자동으로 작성된 코드입니다.  
private final android.widget.**ImageView** mboundView1;  
private final android.widget.**ImageView** mboundView2;  
...CustomBindingAdapterKt.bindImage(this._mboundView1_, userProfileURL, getDrawableFromResource(mboundView1, R.drawable._error_sample_));  
CustomBindingAdapterKt.bindImage(this._mboundView2_, userProfileURL);

자동생성 코드는 다음과 같은 규칙을 따릅니다.

-   맞춤 네임스페이스는 일치 확인 중에 무시됩니다.
-   Android 네임스페이스용 어댑터를 작성할 수도 있습니다.

# 6. 리스너 바인딩

안드로이드에는 여러가지 리스너가 있습니다. 대표적으로 View.OnClickListener가 있으며 이러한 SAM(Single Abstract Method)들은 함수 이름을 따라서 어트리뷰트 이름이 정해집니다. 추상메소드가 많은 리스너들은 변칙적으로 이름이 적용됩니다. 예를들어 TextWatcher의 경우 세가지의 추상메소드가 있지만 변칙적으로 하나의 메소드만 이용합니다.

android:onClick=""//OnClickListener  
android:onTextChanged=""//TextWatcher

저는 이미지 뷰를 클릭하면 이름과 주소가 토스트메시지로 출력되는걸 만들어보도록 하겠습니다.

일단 데이터를 처리하고 리스너로 받을 ViewModel을 구현하도록 하겠습니다.

> **AAC중 ViewModel과 LiveData가 추가로 사용되었으며 추후에 포스팅 하도록 하겠습니다. 참고용으로 봐주시기 바랍니다.**

class MainViewModel() : ViewModel() {  
    var clickConverter = MutableLiveData<Unit>()  
  
    //클릭 이벤트를 받아온다.  
    fun onClickHandler() {  
        clickConverter._value_ = Unit  
    }  
}

xml에 onClickHandler를 바인딩 해줍시다.

<import type="android.view.View"/><variable  
        name="viewModel"  
        type="com.hyun.android.databindingsample.MainViewModel"/>  
...<ImageView android:layout_width="match_parent"  
           android:layout_height="wrap_content"  
           android:onClick="@{()->viewModel.onClickHandler()}"  
           app:bind_image="@{user.profileURL}"  
           app:bind_image_error="@{@drawable/error_sample}"/>

이제 onClickHandler로 받은 이벤트를 activity에서 다뤄보도록 하겠습니다.

var factory = MainViewModelFactory()  
var viewModel: MainViewModel = ViewModelProviders.of(this, factory).get(MainViewModel::class._java_)  
  
viewModel.clickConverter.observe(this, _Observer_ **{** Toast.makeText(this, "${binding._user_?.name}, ${binding._user_?.address}", Toast._LENGTH_SHORT_).show()  
**}**)  
  
binding._user_ = User("이종현", "서울시", R.drawable._profile_sample_)  
binding._viewModel_ = viewModel  
binding.setLifecycleOwner(this)

결과화면입니다.

![](https://miro.medium.com/max/30/1*Rh5nWDxw9st0EgIUHx8GIQ.jpeg?q=20)

![](https://miro.medium.com/max/701/1*Rh5nWDxw9st0EgIUHx8GIQ.jpeg)

----------

주요파일들 전체 코드입니다. 참고로봐주시기 바랍니다.

# **MainActivity**

class MainActivity : AppCompatActivity() {  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
  
        //setContentView(R.layout.activity_main)  
  
        var binding: ActivityMainBinding = DataBindingUtil.setContentView(this, R.layout._activity_main_)  
//        binding.tvSample.text = "이종현의 개발블로그입니다."//id: tv_sample  
        subscribeUi(binding)  
    }  
  
    private fun subscribeUi(binding: ActivityMainBinding) {  
  
        var factory = MainViewModelFactory()  
        var viewModel: MainViewModel = ViewModelProviders.of(this, factory).get(MainViewModel::class._java_)  
  
        viewModel.clickConverter.observe(this, _Observer_ **{** Toast.makeText(this, "${binding._user_?.name}, ${binding._user_?.address}", Toast._LENGTH_SHORT_).show()  
        **}**)  
  
        binding._user_ = User("이종현", "서울시", R.drawable._profile_sample_)  
        binding._viewModel_ = viewModel  
        binding.setLifecycleOwner(this)  
    }  
}

# MainViewModel

class MainViewModel : ViewModel() {  
    var TAG = _javaClass_._simpleName_ var clickConverter = MutableLiveData<Unit>()  
  
    //클릭 이벤트를 받아온다.  
    fun onClickHandler() {  
        Log.d(TAG, "클릭을하면 이곳으로 옵니다.")  
        clickConverter._value_ = Unit  
    }  
}

# MainViewModelFactory

class MainViewModelFactory : ViewModelProvider.Factory {  
  
    override fun <T : ViewModel?> create(modelClass: Class<T>): T {  
        return MainViewModel() as T  
    }  
}

# CustomBindingAdapter.kt

@BindingAdapter("bind_image")  
fun bindImage(view: ImageView, res: Int?) {  
    Glide.with(view._context_)  
        .load(res)  
        .into(view)  
  
  
}  
  
@BindingAdapter("bind_image", "bind_image_error")  
fun bindImage(view: ImageView, res: Int, error: Drawable) {  
    val options = RequestOptions()  
        .error(error)  
  
    Glide.with(view._context_)  
        .load(res)  
        .apply(options)  
        .into(view)  
}

# activity_main.xml

<?xml version="1.0" encoding="utf-8"?>  
<layout xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:app="http://schemas.android.com/apk/res-auto"  
        xmlns:tools="http://schemas.android.com/tools">  
  
    <data>  
        <import type="android.view.View"/>  
        <variable  
                name="user"  
                type="com.hyun.android.databindingsample.User"/>  
        <variable  
                name="viewModel"  
           type="com.hyun.android.databindingsample.MainViewModel"/>  
    </data>  
  
    <LinearLayout  
            android:layout_width="match_parent"  
            android:layout_height="match_parent"  
            android:gravity="center"  
            android:orientation="vertical">  
  
        <ImageView android:layout_width="match_parent"  
                   android:layout_height="wrap_content"  
                   android:onClick="@{()->viewModel.onClickHandler()}"  
                   app:bind_image="@{user.profileURL}"  
                   app:bind_image_error="@{@drawable/error_sample}"/>  
        <TextView  
                android:layout_width="wrap_content"  
                android:layout_height="wrap_content"  
                android:text="@{user.name}"  
                android:layout_gravity="center"  
                android:textSize="30dp"  
                tools:text="이부분에 이름이 표시됩니다."/>  
  
        <TextView  
                android:layout_width="wrap_content"  
                android:layout_height="wrap_content"  
                android:text="@{user.address}"  
                android:layout_gravity="center"  
                android:textSize="30dp"  
                tools:text="이부분에 주소가 표시됩니다."/>  
    </LinearLayout>  
</layout>

# gradle.properties(이거 빼먹는경우 많습니다.)

_저도 포스팅하다가 이거 깜빡해서 좀 해맸습니다._

android.useAndroidX = true  
android.enableJetifier = true  
org.gradle.jvmargs=-Xmx1536m  
kotlin.code.style=official


# 7. 데이터바인딩 준비

1.  아키택쳐 가이드에 준하는 패키지 구조 확립
2.  Room을 이용한 데이터베이스 세팅

![](https://miro.medium.com/max/60/1*-yY0l4XD3kLcZz0rO1sfRA.png?q=20)

![](https://miro.medium.com/max/960/1*-yY0l4XD3kLcZz0rO1sfRA.png)

MVVM 권장 앱 아키텍쳐

3. 최초 데이터를 입력시켜줄 Worker클래스 작성

4. assets에 샘플 데이터 입력

준비가 완료된 코드는 아래와 같으며 깃허브에 태그로 남겨두겠습니다.  
_태그명:Android-Jetpack-Databinding-사용법(3.상세편-준비하기)_

준비된 패키지들의 구조는 아래와 같습니다. 최대한 간단하게 구성하도록 노력했습니다.

![](https://miro.medium.com/max/54/1*CAQYdiIB0UZS-jiKdWV54Q.png?q=20)

![](https://miro.medium.com/max/506/1*CAQYdiIB0UZS-jiKdWV54Q.png)

MVVM 패키지 구조

----------

# 8. 데이터바인딩(Fragment, Adapter)

Fragment 에서의 데이터 바인딩은 Activty에서의 데이터 바인딩과 조금 다르지만 기존에 inflater로 inflate하는 방식과 상당히 유사합니다. 또한 어뎁터로 리스트를 넘겨주는 방법또한 다릅니다. 먼저 코드를 보고 설명하겠습니다.

override fun onCreateView(  
    inflater: LayoutInflater, container: ViewGroup?,  
    savedInstanceState: Bundle?  
): View? {  
    //inflater.inflate(R.layout.fragment_cat_list, container, false)  
    binding = **DataBindingUtil.inflate(inflater, R.layout._fragment_cat_list_, container, false)**  
    subscribeUi()  
  
    return binding._root  
_}...var catListAdapter = CatListAdapter()  
**catListAdapter.submitList(it)  
**binding.rvCatList._adapter_ = catListAdapter

> 구버전: inflater.inflate(R.layout.fragment_cat_list, container, false)  
> 신버전:  **DataBindingUtil.inflate(inflater, R.layout._fragment_cat_list_, container, false)**

기존에 생성자 혹은 setData, updateData등등의 메소드를 개발자가 직접 만들어서 데이터를 세팅해주는 방식에서 androidx.recyclerview에서 지원해주는  **submitList에 데이터만 입력해주면 어뎁터에서 활용이 가능합니다.** 활용예는 아래와 같습니다.

override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CatListAdapter.ViewHolder {  
    return              ViewHolder(**RvItemCatListBinding.inflate(LayoutInflater.from(parent._context_), parent, false)**)  
}  
  
override fun onBindViewHolder(holder: CatListAdapter.ViewHolder, position: Int) {  
    var cat = **getItem(position)**  
    **holder.bind(cat)**  
  
}  
  
class ViewHolder(val binding: RvItemCatListBinding) : RecyclerView.ViewHolder(binding._root_) {  
    **fun bind(mCat: Cat) {  
        binding._apply_ {  
            _cat_ = mCat  
            executePendingBindings()  
        }  
    }**  
}

1.  onCreateViewHolder에서 ViewHolder를 생성하여 넘겨줍니다.
2.  onBindViewHolder에서 getItem으로 현재 포지션의 아이템을 가져와 holder.bind를 이용하여 바인딩 해줍니다.

3. executePendingBindings 을 이용하여 뷰를 강제로 업데이트 합니다.  
notifyDataSetChanged()와 기능적으로 유사합니다.

데이터바인딩을 이용하니 어뎁터의 코드가 굉장히 깔끔해 진것을 알 수 있습니다.

> 제가 이용해봤을때 가장 효용가치가 높다고 판단된 부분이 어뎁터 입니다.

----------

# 9. 레이아웃에 자바클래스 import

자바와 마찬가지로 import구문을 사용하여 xml레벨에서 해당 클래스를 이용 가능합니다. 복잡한 활용은 피해야 하며 최대한 직관적이고 간단하게 구현해야 합니다.

이미지뷰에 이미지가 제대로 세팅되지 않았을경우 이미지뷰를 보여주지 않는 코드를 작성해보겠습니다.

<data>  
    **<import type="android.view.View"/>**  
    <variable  
            name="user"  
            type="com.hyun.android.databindingsample.model.User"/>  
    <variable  
            name="viewModel"  
            type="com.hyun.android.databindingsample.viewmodel.MainViewModel"/>  
</data>...<ImageView android:layout_width="wrap_content"  
           android:layout_height="150dp"  
           android:onClick="@{()->viewModel.onClickHandler()}"  
           **android:visibility="@{user.profileURL != -1 ? View.VISIBLE : View.GONE}"**  
           tools:srcCompat="@drawable/profile_sample"  
           app:bind_image="@{user.profileURL}"  
           app:bind_image_error="@{@drawable/error_sample}"/>

----------

# 10. 식 언어

식 언어는 Java 식과 매우 흡사해 보입니다. 다음 사항은 Java 식과 똑같습니다.( 식언어는 간단한 예만 작성하고 따로 설명하지는 않겠습니다. 편의상 i와 j로 표기하겠습니다.)

-   수학  `**+ - / * % (ex> @{i + j} ... @{i % j})**`
-   문자열 연결  `**+ (ex> @{i.toString() + j.toString()})**`
-   논리  `**&& || (ex> @{i && j})**`
-   이항  `**& | ^ (ex> @{i & j})**`
-   단항  `**+ - ! ~ (ex> @{+i} ... @{~i})**`
-   시프트  `**>> >>> << (ex> @{i << 32})**`
-   비교  `**== > < >= <= (ex> @{i == j} ... @{i <= j})**`
-   `**instanceof (ex> @{i instanceof String})**`
-   그룹화  `**() (ex> @{(i + 1) + (j + 1)})**`
-   리터럴 — 문자, 문자열, 숫자,  `**null**`
-   형변환  `**(ex> @{(String)i})**`
-   함수 호출  `**(ex> @{i.toString()})**`
-   필드 액세스  `**(ex> @{i.field})**`
-   배열 액세스  `**[] (ex> @{i[0]})**`
-   삼항 연산자  `**?: (ex> @{i > j ? i : j})**`

한가지 특이한 연산자는 널 병합 연산잔가 있습니다.

null 병합 연산자(`**??**`)는 왼쪽 피연산자가 null이 아니면 왼쪽 피연산자를 선택하고, null이면 오른쪽 피연산자를 선택합니다. 두식은 기능적으로 같은 의미입니다.

**android:text="@{user.displayName ?? user.lastName}"  
android:text="@{user.displayName != null ? user.displayName : user.lastName}"**

----------

# 11.바인딩 어댑터 오버로딩

예를들어 이미지를 세팅할때, 이미지값이 Int타입 drawable, color ID값이 되거나, 서버로부터 이미지를 받아 String타입 URL이 될수도 있습니다. 이때 바인딩 어댑터를 어떤식으로 오버로딩 하는지 살펴보겠습니다.

//Int타입 drawable, color ID값이 되는경우  
@BindingAdapter("bind_image")  
fun bindImage(view: ImageView, res: Int?) {  
    Glide.with(view._context_)  
        .load(res)  
        .into(view)  
  
  
}//서버로부터 이미지를 받아 String타입 URL이 되는경우  
@BindingAdapter("bind_image")  
fun bindImage(view: ImageView, url: String?) {  
    Glide.with(view._context_)  
        .load(url)  
        .into(view)  
  
  
}//Int타입 drawable, color ID값이 되는경우에 오류처리를 하고 싶은경우  
@BindingAdapter("bind_image", "bind_image_error")  
fun bindImage(view: ImageView, res: Int, error: Drawable) {  
    val options = RequestOptions()  
        .error(error)  
  
    Glide.with(view._context_)  
        .load(res)  
        .apply(options)  
        .into(view)  
}

이런식으로 오버로딩을 지원하며 사용법은 아래와 같으며 매개변수 타입에 맞는 메소드에서 동작을 하며 매개변수 타입이 일치하는게 없을 경우 컴파일오류가 발생합니다.

//Int타입 drawable, color ID값이 되는경우  
<ImageView app:bind_image="@{Resource ID}"/>//서버로부터 이미지를 받아 String타입 URL이 되는경우  
<ImageView app:bind_image="@{String URL}"/>//Int타입 drawable, color ID값이 되는경우에 오류처리를 하고 싶은경우  
<ImageView app:bind_image="@{Resource ID}"  
           app:bind_image_error="@{@Resource ID for ERROR}"/>

> e: [kapt] An exception occurred: android.databinding.tool.util.LoggedErrorException: Found data binding errors.

----------

최종 결과 화면입니다.(이쁘진 않네요 :)

![](https://miro.medium.com/max/30/1*EmqeugTTMaq77n1sV6So1A.jpeg?q=20)

![](https://miro.medium.com/max/1080/1*EmqeugTTMaq77n1sV6So1A.jpeg)

# 12.개인적인 의견

1.  자동완성이 되지않는 경우가 있어 오타에 매우 주의해야 합니다.
2.  android:id값을 바꾸거나 새로운 컴포넌트를 추가하면 컴파일을 다시 해줘야 하기 때문에 매우 귀찮습니다.
3.  권장사항을 따르지않고 layout에 코딩을 하는 실수를 주의해야 합니다.
4.  object를 바로 입력하는 개념이기때문에 실무에서는 서버 개발자와 의견조율이 필요해 보입니다. 그렇지 않으면 비효율적일 수 있습니다.
5.  코드다이어트에 매우 효과적입니다.(단적으로, 20개의 컴포넌트를 셋팅하기 위하여 40줄의 코드가 필요한데, 데이터바인딩을 이용하면 한줄이면 세팅이 가능합니다.)
6.  다른 AAC들에 비해서 스터디양이 굉장히 많습니다.(가장 중요하다는 의미로 긍정적으로 받아들입시다.)