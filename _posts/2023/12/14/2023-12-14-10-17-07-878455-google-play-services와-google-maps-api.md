---
layout: post
title: "[android] Google Play Services와 Google Maps API"
description: " "
date: 2023-12-14
tags: [android]
comments: true
share: true
---

# 소개
안드로이드 앱에 지도 기능을 추가하려면 Google Play Services 및 Google Maps API를 사용해야 합니다. 이 기술을 사용하면 사용자 위치 추적, 지도 표시, 장소 검색 및 기타 지도 관련 기능을 쉽게 구현할 수 있습니다.

# Google Play Services 설정
Google Play Services를 사용하려면 먼저 안드로이드 프로젝트에 Google Play Services 라이브러리를 추가해야 합니다. 
1. **build.gradle** 파일에 다음 의존성을 추가합니다.
   ```gradle
   implementation 'com.google.android.gms:play-services-location:18.0.0'
   implementation 'com.google.android.gms:play-services-maps:18.0.0'
   ```

2. Manifest 파일에 다음 permission을 추가하여 위치 권한을 요청합니다.
   ```xml
   <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
   <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
   ```

# Google Maps API 설정
Google Maps API를 사용하려면 API 키를 발급받아 프로젝트에 설정해야 합니다.
1. [Google Cloud Console](https://console.cloud.google.com/)에 로그인하여 새 프로젝트를 만듭니다.
2. "API 및 서비스" > "라이브러리"에서 "Maps SDK for Android"를 활성화합니다.
3. "API 및 서비스" > "사용자 인증 정보"에서 "API 키 만들기"를 선택하여 API 키를 발급받습니다.

# 지도 표시하기
앱의 화면에 지도를 표시하려면 **MapFragment**나 **MapView**를 사용합니다. 
1. **activity_main.xml**에 MapView를 추가합니다.
   ```xml
   <com.google.android.gms.maps.MapView
       android:id="@+id/mapView"
       android:layout_width="match_parent"
       android:layout_height="match_parent" />
   ```

2. **MainActivity.kt**에서 MapView를 초기화하고 지도를 표시합니다.
   ```kotlin
   val mapView = findViewById<MapView>(R.id.mapView)
   mapView.onCreate(savedInstanceState)
   mapView.getMapAsync { googleMap ->
       // 지도 초기화 및 설정
   }
   ```

지금까지 안드로이드 앱에 Google Play Services와 Google Maps API를 통합하는 방법에 대해 알아보았습니다. 이를 통해 사용자에게 편리하고 강력한 지도 기능을 제공할 수 있습니다.