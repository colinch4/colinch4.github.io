---
layout: post
title: "[android] Google Play Services와 Google Fit API"
description: " "
date: 2023-12-14
tags: [android]
comments: true
share: true
---

Google Play Services는 안드로이드 앱에서 Google의 다양한 서비스 및 기능을 이용할 수 있도록 지원하는 라이브러리입니다. 이 라이브러리를 사용하여 Google Fit API를 통해 사용자의 건강 및 운동 데이터를 가져오고 저장할 수 있습니다. 이를 통해 안드로이드 앱에 강력한 피트니스 기능을 추가할 수 있습니다.

## Google Play Services 및 Google Fit API 구성

안드로이드 프로젝트에서 Google Play Services 및 Google Fit API를 사용하기 위해서는 먼저 이러한 라이브러리를 프로젝트에 추가해야 합니다. `build.gradle` 파일에 다음과 같이 종속성을 추가합니다.

```gradle
implementation 'com.google.android.gms:play-services-fitness:20.0.0'
```

Google Play Services 및 Google Fit API를 사용하려면 안드로이드마다 해당 서비스를 사용하기 위한 권한을 얻어야 합니다. 필요한 권한을 요청하는 방법에 대한 자세한 내용은 [Google Play Services 문서](https://developers.google.com/fit/android/get-api-key)를 확인하세요.

## Google Fit API 사용하기

Google Fit API를 사용하여 사용자의 건강 및 운동 데이터를 읽고 쓸 수 있습니다. 다음은 Google Fit API를 사용하여 달리기 활동을 기록하고 거리, 시간, 칼로리 등을 얻는 예제 코드입니다.

```java
// 필요한 권한 확인 및 요청
GoogleSignInAccount account = GoogleSignIn.getAccountForExtension(this, fitnessOptions);

// Google API Client 초기화
GoogleApiClient googleApiClient = new GoogleApiClient.Builder(this)
        .addApi(Fitness.SENSORS_API)
        .addScope(new Scope(Scopes.FITNESS_ACTIVITY_READ_WRITE))
        .addConnectionCallbacks(...).addOnConnectionFailedListener(...)
        .build();

// 센서 데이터 구독
Fitness.getSensorsClient(this, account)
        .add(new SensorRequest.Builder()
                .setDataType(DataType.TYPE_DISTANCE_DELTA)
                .setSamplingRate(1, TimeUnit.SECONDS)
                .build(), new OnDataPointListener() {
            @Override
            public void onDataPoint(DataPoint dataPoint) {
                // 데이터 처리
            }
        });

// 활동 기록
DataWriteRequest request = new DataWriteRequest.Builder()
        .setDataType(DataType.TYPE_ACTIVITY_SEGMENT)
        .setActivityField(Field.FIELD_ACTIVITY, "running")
        .setTimeInterval(startTime, endTime, TimeUnit.MILLISECONDS)
        .build();

Fitness.getHistoryClient(this, account)
        .insertData(request)
        .addOnSuccessListener(...).addOnFailureListener(...);
```

## 결론

Google Play Services와 Google Fit API를 사용하면 안드로이드 앱에 간단하게 피트니스 기능을 추가할 수 있습니다. 사용자의 건강 데이터를 안전하게 저장하고 관리하여 피트니스 관련 앱을 보다 효과적으로 구축할 수 있습니다. Google Play Services 및 Google Fit API를 통해 효과적인 피트니스 앱을 개발하는 방법에 대해 더 알아보려면 [Google Developers](https://developers.google.com/fit) 웹사이트를 방문하세요.