---
layout: post
title: "[android] 안드로이드 Content Provider와 Content Resolver"
description: " "
date: 2023-12-22
tags: [android]
comments: true
share: true
---

안드로이드 앱에서는 **Content Provider**와 **Content Resolver**를 사용하여 데이터를 관리하고 다른 앱과 데이터를 공유하는 기능을 구현할 수 있습니다. 

## Content Provider

**Content Provider**는 앱의 데이터를 다른 앱에 제공하기 위한 인터페이스를 제공합니다. 데이터베이스, 파일 또는 네트워크를 통해 얻은 데이터 등을 관리하고 다른 앱에 안전하게 노출할 수 있습니다. 

앱의 데이터에 접근하기 위해서는 URI(Uniform Resource Identifier)를 사용하여 Content Provider에 쿼리를 수행합니다. 

```java
Cursor cursor = getContentResolver().query(Uri, projection, selection, selectionArgs, sortOrder);
```

## Content Resolver

**Content Resolver**는 Content Provider를 통해 다른 앱의 데이터에 접근하고 관리하는 인터페이스를 제공합니다. Content Resolver를 사용하여 데이터를 추가, 수정, 삭제하고 다른 앱에서 제공하는 데이터에 접근할 수 있습니다.  

앱에서 Content Resolver를 사용하여 다른 앱의 Content Provider에 액세스할 수 있으며, URI를 통해 데이터를 식별하고 쿼리 또는 조작할 수 있습니다.

```java
ContentResolver contentResolver = context.getContentResolver();
contentResolver.insert(Uri, values);
```

Content Provider와 Content Resolver는 안드로이드 시스템에서 제공하는 메커니즘으로 두 앱 간 데이터 공유를 용이하게 합니다.

앱을 개발하거나 안드로이드 데이터 관리에 대해 더 알아보려면 공식 안드로이드 개발자 문서를 참고하시기 바랍니다.

[안드로이드 공식 개발자 문서 - Content Provider](https://developer.android.com/guide/topics/providers/content-providers)

[안드로이드 공식 개발자 문서 - Content Resolver](https://developer.android.com/reference/android/content/ContentResolver)

---

위 내용은 안드로이드 개발에 있어서 중요한 데이터 관리 기능에 대한 개념과 예시 코드를 제시하였습니다. Content Provider와 Content Resolver를 통해 안드로이드 앱 간 또는 시스템 간 데이터 공유 기능을 활용할 수 있습니다.