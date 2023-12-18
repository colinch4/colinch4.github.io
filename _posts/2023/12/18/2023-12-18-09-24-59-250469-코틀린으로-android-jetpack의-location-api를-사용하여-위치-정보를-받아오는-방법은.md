---
layout: post
title: "[kotlin] 코틀린으로 Android Jetpack의 Location API를 사용하여 위치 정보를 받아오는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

안녕하세요! 안드로이드 앱에서 위치 정보를 받아오는 방법에 대해 알아보겠습니다. Kotlin을 사용하여 안드로이드 Jetpack의 Location API를 활용하여 위치 정보를 받아올 수 있습니다.

## 1. Location 권한 설정

먼저, 앱이 위치에 접근하는 권한을 허용해야 합니다. `AndroidManifest.xml` 파일에 다음과 같이 위치 권한을 추가합니다:

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

API 레벨 29부터는 사용자의 현재 위치를 받아오기 위해 추가적인 권한을 요청해야 합니다. 이를 위해 다음과 같이 코드를 추가합니다:

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
    if (ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) ==
            PackageManager.PERMISSION_GRANTED) {
        // 위치 권한이 허용된 경우 위치 정보를 받아올 수 있습니다.
    } else {
        requestPermissions(arrayOf(Manifest.permission.ACCESS_FINE_LOCATION), LOCATION_PERMISSION_REQUEST_CODE)
    }
}
```

## 2. Location API 사용

이제 Location API를 사용하여 위치 정보를 받아오겠습니다. `FusedLocationProviderClient` 인스턴스를 사용하여 현재 위치를 받아올 수 있습니다. `LocationServices` 클래스를 사용하여 `FusedLocationProviderClient`를 얻을 수 있습니다:

```kotlin
val fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)
```

위 코드에서 `this`는 현재 액티비티나 애플리케이션 컨텍스트를 나타냅니다.

위치 정보를 요청하고 받아오기 위해서 다음과 같이 코드를 작성합니다:

```kotlin
fusedLocationClient.lastLocation
        .addOnSuccessListener { location : Location? ->
            // 위치 정보를 성공적으로 받아왔을 때 처리할 작업을 여기에 추가합니다.
            if (location != null) {
                // 위치 정보가 null이 아닌 경우
            }
        }
        .addOnFailureListener { e : Exception ->
            // 위치 정보를 받아오는데 실패했을 때의 처리를 여기에 추가합니다. 
        }
```

위 코드에서 `addOnSuccessListener` 함수의 람다 내부에 위치 정보를 받아왔을 때의 처리 작업을 추가합니다. `addOnFailureListener` 함수의 람다 내부에 위치 정보를 받아오는데 실패했을 때의 처리 작업을 추가합니다.

## 3. 위치 정보를 사용하여 작업하기

위치 정보를 받아왔다면, 해당 정보를 사용하여 필요한 작업을 수행할 수 있습니다. 예를들면, 지도에 현재 위치를 표시하거나 특정 위치 주변의 정보를 가져오는 등의 작업을 수행할 수 있습니다.

## 요약
이제 안드로이드 Jetpack의 Location API를 사용하여 위치 정보를 받아오는 방법을 알아보았습니다. 위치 권한을 설정하고, Location API를 사용하여 위치 정보를 받아온 뒤, 해당 정보를 사용하여 작업하는 방법에 대해 알아보았습니다. 내용이 도움이 되었기를 바랍니다!