---
layout: post
title: "[안드로이드] BottomNavigationView 란"
description: " "
date: 2020-11-25
tags: [android]
comments: true
share: true
---


  
  안드로이드 support Library 25 이상부터 지원한다.
  
  
## 적용하기
  
  1. menu.xml을 정의한다.
  2. 레이아웃 파일에 BottomNavigationView를 정의한다
  3. menu item click을 정의한다.
  
### menu.xml 정의
  
  아이템을 2개도 만들 수 있지만 가이드상 3개 이상을 사용해야 한다!
  
```
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
    <item
        android:id="@+id/action_menu1"
        android:icon="@drawable/ic_menu1"
        android:enabled="true"
        android:title="@string/menu1"/>
    <item
        android:id="@+id/action_menu2"
        android:icon="@drawable/ic_menu2"
        android:enabled="true"
        android:title="@string/menu2"/>
    <item
        android:id="@+id/action_menu3"
        android:icon="@drawable/ic_menu3"
        android:enabled="true"
        android:title="@string/menu3"/>
</menu>
```

### layout resource에 정의하기
  
  위에서 정의한 menu는 다음과 같이 추가할 수 있습니다.
  
  - app:menu="@menu/xml 파일명" 
  
  각각 이미지와 텍스트에 대한 색상은 아래 속성을 이용하면 된다.
  
  - app:itemIconTint="color code"
  - app:itemTextColor="color code"
  
  ```
 <com.google.android.material.bottomnavigation.BottomNavigationView
        android:id="@+id/bottom_navigation"
        android:layout_alignParentBottom="true"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="@color/colorWhite"
        app:itemIconTint="@color/bottom_section_color"
        app:itemTextColor="@color/bottom_section_color"
        app:menu="@menu/bottom_navigation_main"/>
  ```
 
 ### menu item click 정의하기
 
 bottomNavigationView를 액티비티나 프래그먼트에서 불러와 onNavigationItemSelectedListener를 설정해주면 된다.
   
   ```
   // 자바 
   bottomNavigationView.setOnNavigationItemSelectedListener(new BottomNavigationView.OnNavigationItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.action_one:
                        return true;
                    case R.id.action_two:
                        return true;
                    case R.id.action_three:
                        return true;
                }
                return false;
            }
        });
   ```
   
   ```
   // 코틀린으로 액티비티에서 오버라이딩
   
   override fun onNavigationItemSelected(item: MenuItem): Boolean {
        when(item.itemId){
            R.id.action_home -> {
                var detailViewFragment = DetailViewFragment()
                supportFragmentManager.beginTransaction()
                    .replace(R.id.main_content, detailViewFragment).commit()
                return true
            }
            R.id.action_search -> {
                var gridFragment = GridFragment()
                supportFragmentManager.beginTransaction()
                    .replace(R.id.main_content, gridFragment).commit()
                return true
            }
            
            ...
        }
        return false
    }
   ```
   
 ### 사용하면서 피해야할 스타일
   
   1. 아이템의 색상을 단색이 아닌 여러 색을 사용하는 것.
   
   2. 1줄 넘어가는 텍스트 사용하지 말 것
   
   3. 메뉴를 최소 3개이상!
   
   4. 4~5개 인경우 이미지로만 노출할 것
   
   5. 스크롤이 발생하는 경우 바텀 메뉴를 숨김처리하고 다시 위로 올라오면 노출시킬 것.
   

### Bottom Behavior 정의하기
  
  위의 5번에서 요구하는 행동을 쉽게 Behavior만 정의하여 해결할 수 있다.
  
  ```
  <android.support.design.widget.BottomNavigationView
		app:layout_behavior="tech.thdev.app.view.BottomNavigationBehavior" />
  ```
