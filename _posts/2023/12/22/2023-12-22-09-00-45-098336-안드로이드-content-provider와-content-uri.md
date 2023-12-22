---
layout: post
title: "[android] 안드로이드 Content Provider와 Content URI"
description: " "
date: 2023-12-22
tags: [android]
comments: true
share: true
---

안드로이드 앱은 다양한 데이터를 관리하고 공유하는데 Content Provider가 중요한 역할을 합니다. Content Provider는 데이터베이스나 파일 시스템과 같은 다양한 데이터 저장소를 추상화하고, 다른 앱이 이러한 데이터에 안전하게 접근할 수 있도록 합니다. Content URI는 이러한 데이터에 접근하기 위한 주소를 나타냅니다.

## Content Provider

Content Provider는 안드로이드 시스템의 중심이며, 데이터를 관리하고 다른 앱에 데이터 접근 권한을 부여하는 역할을 수행합니다. 다른 앱은 Content Resolver를 통해 Content Provider에서 데이터를 쿼리하거나 조작할 수 있습니다.

예를 들어, 주소록 앱의 Content Provider를 통해 다른 앱이 연락처 정보를 읽거나 변경할 수 있습니다.

## Content URI

Content URI는 Content Provider의 데이터에 접근하기 위한 주소를 나타냅니다. Content URI는 다음과 같이 구성되어 있습니다.

**content://authority/path/id**

- `content://` : Content URI의 scheme으로 항상 작성되어야 합니다.
- `authority` : Content Provider의 고유 이름을 나타내며, 독특한 문자열이어야 합니다.
- `path` : Content Provider 내에서 특정 데이터를 식별하는 데 사용되는 경로입니다.
- `id` : 옵션으로, 특정 데이터 항목을 식별하는 데 사용됩니다.

예를 들어, 주소록 Content Provider의 전체 연락처 목록은 다음과 같은 Content URI를 사용하여 접근할 수 있습니다.

```java
content://contacts/all
```

## Content Resolver와 ContentProviderClient

Content Resolver는 앱 간의 데이터 공유를 관리하는 중요한 클래스입니다. Content Resolver를 사용하여 Content Provider로 쿼리를 수행하거나 데이터를 변경할 수 있습니다.

ContentProviderClient는 Content Provider를 효율적으로 사용하기 위한 유틸리티 클래스로, Content Provider에 대한 안전한 접근과 데이터 조작을 제공합니다.

안드로이드 앱 개발에서 Content Provider와 Content URI는 데이터 관리와 공유에 있어 매우 중요한 부분을 담당합니다.

## 참고 자료
- [Android Developer - Content Providers](https://developer.android.com/guide/topics/providers/content-providers)
- [Medium - Understanding Content Providers in Android](https://medium.com/@raziul.alam/understanding-content-providers-in-android-75b205fb82f8)