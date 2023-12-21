---
layout: post
title: "[android] 안드로이드 Content Provider의 허가(permission)에 대해"
description: " "
date: 2023-12-22
tags: [android]
comments: true
share: true
---

안드로이드 앱은 사용자의 민감한 정보에 접근하기 전에 적절한 **허가(permission)**를 요구해야 합니다. 안드로이드 시스템은 앱이 허가를 획득하지 않은 경우, 해당 리소스 또는 기능에 접근할 수 없도록 막습니다. 안드로이드의 Content Provider도 그런 측면에서 허가를 요구합니다.

## Content Provider 허가 확인

안드로이드의 Content Provider를 사용하기 위해서는 해당 Content Provider가 요구하는 허가(permission)를 선언해야 합니다. 이는 앱의 `AndroidManifest.xml` 파일에 `<uses-permission>` 요소를 사용하여 표시됩니다.

```xml
<uses-permission android:name="android.permission.READ_CONTACTS" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
```

위의 예시는 연락처와 외부 저장소에 대한 접근 권한을 요청하는 예시입니다.

## 허가(permission) 획득

Content Provider에 접근하려면 허가(permission)를 요청하고, 사용자로부터 승인을 받아야 합니다. 이를 위해 일반적으로는 `ContextCompat.checkSelfPermission()`를 사용하여 해당 허가(permission)이 허용되어 있는지 확인하고, `ActivityCompat.requestPermissions()`를 사용하여 사용자에게 허용을 요청합니다.

```java
if (ContextCompat.checkSelfPermission(this, Manifest.permission.READ_CONTACTS) != PackageManager.PERMISSION_GRANTED) {
    ActivityCompat.requestPermissions(this, new String[] { Manifest.permission.READ_CONTACTS }, MY_PERMISSIONS_REQUEST_READ_CONTACTS);
}
```

허가(permission) 요청 후에는 사용자가 허용하거나 거부할 수 있으며, 이에 따라 콜백을 통해 처리해야 합니다.

## 결론

Content Provider를 안전하게 사용하기 위해서는 허가(permission)를 적절히 관리하고, 사용자의 프라이버시를 존중하는 것이 중요합니다.

자세한 내용은 [안드로이드 공식 문서](https://developer.android.com/guide/topics/providers/content-providers)를 참고하시기 바랍니다.