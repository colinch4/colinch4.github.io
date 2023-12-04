---
layout: post
title: "[flutter] 플러터 geolocator와 Google Maps API를 이용한 지도 표시하기"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

이번 포스트에서는 Flutter를 사용해 Geolocator 패키지와 Google Maps API를 이용하여 지도를 표시하는 방법에 대해 알아보겠습니다.

## 목차
- Geolocator 패키지 소개
- Google Maps API 등록
- Geolocator를 통해 현재 위치 가져오기
- Google Maps 플러그인 설치
- 지도 위에 현재 위치 표시하기

## Geolocator 패키지 소개
Geolocator는 Flutter에서 사용할 수 있는 위치 정보 관련 패키지로, GPS, 네트워크 등 다양한 위치 프로바이더를 통해 현재 위치를 가져올 수 있습니다.

`pubspec.yaml` 파일에 Geolocator 패키지를 추가해야합니다.

```dart
dependencies:
  geolocator: ^7.0.1
```

## Google Maps API 등록
Google Maps를 사용하기 위해서는 먼저 Google Cloud Console에서 API 키를 발급받아야 합니다. 발급 후에는 해당 키를 사용하여 Google Maps를 사용할 수 있습니다.

## Geolocator를 통해 현재 위치 가져오기
Geolocator 패키지를 사용하여 현재 장치의 위치를 가져오는 방법은 다음과 같습니다.

```dart
import 'package:geolocator/geolocator.dart';

Position position = await Geolocator.getCurrentPosition(
  desiredAccuracy: LocationAccuracy.high,
);
```

`await Geolocator.getCurrentPosition()`을 호출하면 사용자의 현재 위치인 `Position` 객체가 반환됩니다.

## Google Maps 플러그인 설치
Google Maps를 사용하기 위해서는 flutter_google_maps 패키지를 설치해야합니다.

`pubspec.yaml` 파일에 flutter_google_maps 패키지를 추가해야합니다.

```dart
dependencies:
  flutter_google_maps: ^1.1.0
```

## 지도 위에 현재 위치 표시하기
Google Maps를 표시하고 현재 위치를 표시하는 방법은 아래와 같습니다.

```dart
import 'package:flutter_google_maps/flutter_google_maps.dart';

GoogleMap(
  initialPosition: GeoCoord(position.latitude, position.longitude),
  markers: {
    Marker(GeoCoord(position.latitude, position.longitude)),
  },
)
```

`GeoCoord` 객체를 사용하여 위도와 경도 정보를 지정합니다. `GoogleMap` 위젯을 사용하여 지도를 표시하고, `Marker`를 사용하여 현재 위치를 표시합니다.

이제 플러터에서 Geolocator와 Google Maps API를 사용하여 지도를 표시하는 방법을 알아보았습니다. 이를 활용하여 실제 앱 개발에 적용해보세요.

## 참고 자료
- [Geolocator 패키지](https://pub.dev/packages/geolocator)
- [Google Maps API 문서](https://developers.google.com/maps/documentation)