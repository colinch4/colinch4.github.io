---
layout: post
title: "[안드로이드] DataBinding 란"
description: " "
date: 2020-11-25
tags: [android]
comments: true
share: true
---

  
  데이터 바인딩을 사용하면 findViewById() 를 호출하지 않아도 자동으로 xml에 만든 view들을 만들어 준다.
  
  값이 바뀌면 알아서 바뀐 값으로 view를 변경하게 할 수도 있다.
  
  ## 지원 사항
  
  - 안드로이드 2.1(api 7) 이상
  - 안드로이드 플러그인 for Gradle 1.5.0-alpha 1 이상
  - 안드로이드 스튜디오 1.3 이상
  
  ## 설정
  
  build.gradle(Module.app) 에서 enable 하자.
  
  ```
  android {
    compileSdkVersion 29
    buildToolsVersion "29.0.3"
    defaultConfig {
        applicationId "com.an.myplace"
        minSdkVersion 21  
        targetSdkVersion 29
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
    dataBinding {
        enabled = true
    }
  }
  ```
  
  데이터 바인딩을 사용하기 위해서는 해당 xml의 최상위 태그를 layout으로 감싸준다.
  
  ```
  <layout>
    ...
    ....
    .....
  </layout>
  ```
  
  액티비티에서 항상 해주던 setContentView대신에 **DatabindingUtil.setContentView()**를 이용한다.
  
  이때 ActivityMainBinding 클래스는 layout으로 감싸면 자동으로 생성된다. 지금은 메인 액티비티의 레이아웃을 사용하였음.
  
  ```
  ActivityMainBinding binding = DataBindingUtil.setContentView(this,R.layout.activity_main);
  binding.setActivity(this);
  ```
  
  레이아웃의 뷰에 접근하려면 바인딩객체.뷰이름 으로 접근한다!
  
  ```
  binding.textView1.setText("123123");
  ```
  
  
  ## 장단점
  
  데이터 바인딩을 통해 MVVM 패턴 즉, View와 ViewModel의 의존성을 분리할 수 있고, 많은 로직들을 xml로 뺄 수 있다.
  
  findViewById를 사용하는 거 보다 빠르다! 근데 ViewHolder를 사용하면 각 뷰마다 id로 1번씩만 찾을텐데 성능차는 거의 없지 않나 싶다. 일반적으로는 빠르다고 한다.
  
  단점은 빌드시간이 오래 걸린다. 클래스들이 많이 만들어지기 때문!
  
  
  
  
  
