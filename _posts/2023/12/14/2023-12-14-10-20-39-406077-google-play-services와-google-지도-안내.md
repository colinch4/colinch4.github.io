---
layout: post
title: "[android] Google Play Services와 Google 지도 안내"
description: " "
date: 2023-12-14
tags: [android]
comments: true
share: true
---

안녕하세요! 안드로이드 앱 개발자 여러분, **Google Play Services**와 **Google 지도**를 활용하여 앱에 지도 기능을 추가하는 방법에 대해 알아보겠습니다.

## Google Play Services란?

[Google Play Services](https://developers.google.com/android/guides/overview)는 안드로이드 플랫폼을 위한 Google의 백엔드 API 라이브러리입니다. Google Play Services를 통해 Google의 여러 서비스 및 API를 사용할 수 있으며, 이를 통해 지도, 위치, 인증, 게임 등 다양한 기능들을 앱에 추가할 수 있습니다.

## Google 지도 추가하기

Google 지도 API를 사용하여 앱에 유동적이고 상호작용이 가능한 지도 인터페이스를 통합할 수 있습니다.

### Google Play 서비스 및 지도 API 추가

먼저 앱의 `build.gradle` 파일에 Google Play 서비스 및 지도 API의 종속성을 추가해야 합니다.

```gradle
implementation 'com.google.android.gms:play-services-maps:17.0.0'
```

또한, **Google Cloud Console**에서 앱에 대한 API 키를 발급받아야 합니다.

### 지도 표시하기

앱의 레이아웃 XML 파일에 `MapView`를 추가하고, 액티비티에서 지도를 초기화하고 표시합니다.

```xml
<com.google.android.gms.maps.MapView
    android:id="@+id/mapView"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_maps);
    MapView mapView = findViewById(R.id.mapView);
    mapView.onCreate(savedInstanceState);
    mapView.getMapAsync(googleMap -> {
        // 지도 초기화 및 설정
        // ...
    });
}
```

### 위치 및 마커 추가

사용자의 현재 위치를 표시하거나, 특정 위치에 마커를 추가하는 등의 작업을 수행할 수 있습니다.

```java
googleMap.setMyLocationEnabled(true);
googleMap.addMarker(new MarkerOptions().position(latLng).title("My Marker"));
```

## 마치며

Google Play Services를 사용하여 Google 지도를 앱에 쉽게 통합할 수 있습니다. 이를 통해 사용자에게 위치 기반의 서비스를 제공하고, 사용자 경험을 더욱 향상시킬 수 있습니다.

Happy Coding!

[Google Play Services 문서 바로가기](https://developers.google.com/android/guides/overview)\
[Google Maps Android API 문서 바로가기](https://developers.google.com/maps/documentation/android-sdk/overview)