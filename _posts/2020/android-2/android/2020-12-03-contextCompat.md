---
layout: post
title: "[안드로이드] ContextCompat"
description: " "
date: 2020-12-03
tags: [android]
comments: true
share: true
---


ContextCompat은 Resource에서 값을 가져오거나 퍼미션을 확인할 때 사용할 때 SDK버전을 고려하지 않아도 되도록 (내부적으로 SDK버전을 처리해둔) 클래스입니다. 예를들면 아래와 같이 처리되어 있다.


```java
    public static int getColor(@NonNull Context context, @ColorRes int id) {
        if (Build.VERSION.SDK_INT >= 23) {
            return context.getColor(id);
        } else {
            return context.getResources().getColor(id);
        }
    }
```

이렇게 버전을 내부적으로 분기를 태워서 개발자는 특별하게 SDK버전을 신경쓰지 않아도 되도록 처리해둔 것이며 Color, Drawable, File, PermissionCheck 등 다양한 기능이 있다.

사용은 아래와 같이 사용하면 된다.

```java
//color
ContextCompat.getColor(this, available ? R.color.button_text_enabled : R.color.button_text_disabled)
```

```java
//drawable
ContextCompat.getDrawable(getContext(), R.color.delivery_list_offset)
```