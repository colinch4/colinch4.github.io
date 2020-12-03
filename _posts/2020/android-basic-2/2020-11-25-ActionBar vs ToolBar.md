---
layout: post
title: "[안드로이드] ActionBar vs ToolBar"
description: " "
date: 2020-11-25
tags: [Android]
comments: true
share: true
---


  
  액션바에 여러 기능들이 추가되면서 os에 따라 다르게 동작하는 문제가 생겼다.
  
  그래서 툴바에 최신 피쳐들이 추가되어 액션바의 문제를 해결할 수 있다. 
  
  액션바는 object를 상속받으며, 툴바는 viewGroup을 상속 받는다.
  
  그래서 툴바는 어디든지 붙이기 쉽고, 뷰이기 때문에 애니메이션의 적용이 쉽다.
  
  요즘엔 대부분 툴바를 사용한다.
  

## 기본 액션 바를 툴바로 교체하기

  1. style.xml에서 AppTheme의 parent를 NoActionBar로 변경
  
  ```
    <style name="AppTheme" parent="Theme.AppCompat.Light.NoActionBar">
        <!-- Customize your theme here. -->
        <item name="colorPrimary">@color/colorPrimary</item>
        <item name="colorPrimaryDark">@color/colorPrimaryDark</item>
        <item name="colorAccent">@color/colorAccent</item>
    </style>
  ```
  
  2. 액티비티의 xml에 Toolbar 추가
  
  ```
  <androidx.appcompat.widget.Toolbar
        android:id="@+id/my_toolbar"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_alignParentTop="true"
        android:background="?attr/colorPrimary"
        android:minHeight="?attr/actionBarSize"
        android:theme="@style/ThemeOverlay.AppCompat.Dark.ActionBar"
        app:popupTheme="@style/ThemeOverlay.AppCompat.Light"/>
  ```
  
  3. 액티비티에서 세팅
  
  ```
    Toolbar toolbar = (Toolbar) findViewById(R.id.my_toolbar);    
    setSupportActionBar(toolbar); //툴바를 액션바와 같게 만들어 준다.
    ActionBar actionBar = getSupportActionBar();
    actionBar.setTitle("타이틀");
    actionBar.setDisplayHomeAsUpEnabled(true);  // 뒤로가기 버튼을 추가
  ```
