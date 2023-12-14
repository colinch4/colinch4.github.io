---
layout: post
title: "[flutter] get_storage와 SharedPreferences의 차이점은 무엇인가요?"
description: " "
date: 2023-12-15
tags: [flutter]
comments: true
share: true
---

`SharedPreferences`는 안드로이드 및 iOS 모바일 플랫폼에서 사용되는 기본 로컬 저장소 메커니즘입니다. 이것은 키-값 쌍의 형태로 간단한 데이터를 저장하고 검색할 수 있습니다. 주로 사용자 환경 설정, 앱 상태, 사용자에 대한 기본 정보 등을 저장하는 데에 사용됩니다.

반면에 `get_storage`는 Flutter 앱에서 보다 간단하고 빠른 로컬 데이터 저장를 위한 패키지입니다. `get_storage`는 디스크에 데이터를 저장하고 필요할 때 메모리에 로드하여 사용하는 방식으로 동작하며, `SharedPreferences` 보다 대량의 데이터 저장 및 빠른 액세스에 유리합니다.

따라서, 간단한 키-값 쌍 데이터 저장에는 `SharedPreferences`가 적합하고, 보다 복잡하고 대량의 데이터를 저장 및 빠른 액세스가 필요한 경우에는 `get_storage`를 사용하는 것이 좋습니다.

이제, 각각의 사용 예시를 통해 더 자세히 살펴보겠습니다.