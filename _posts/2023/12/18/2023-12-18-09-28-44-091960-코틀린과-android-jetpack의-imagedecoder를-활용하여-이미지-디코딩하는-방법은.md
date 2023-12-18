---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 ImageDecoder를 활용하여 이미지 디코딩하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

# ImageDecoder 사용하기

Android Jetpack의 ImageDecoder는 Android 9 Pie(API 레벨 28)부터 도입된 이미지 디코딩 라이브러리입니다. ImageDecoder를 사용하면 비트맵을 로드하고 디코딩할 때 발생하는 일반적인 문제를 해결할 수 있습니다.

다음은 Kotlin에서 ImageDecoder를 사용하여 이미지를 디코딩하는 간단한 예제입니다.

```kotlin
import android.graphics.ImageDecoder
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val imageView: ImageView = findViewById(R.id.imageView)
        val uri = Uri.parse("your_image_uri_here")

        if (Build.VERSION.SDK_INT < 28) {
            val bitmap = ImageDecoder.decodeBitmap(ImageDecoder.createSource(contentResolver, uri))
            imageView.setImageBitmap(bitmap)
        } else {
            val source = ImageDecoder.createSource(contentResolver, uri)
            val drawable = ImageDecoder.decodeDrawable(source)
            imageView.setImageDrawable(drawable)
        }
    }
}
```
위의 예제에서는 `ImageDecoder`를 사용하여 이미지를 디코딩하고, 안드로이드 버전에 따라 `decodeBitmap` 또는 `decodeDrawable`을 호출하는 방법을 보여줍니다.

이제 ImageDecoder를 사용하여 안드로이드 앱에서 이미지를 디코딩하는 방법을 이해하셨을 것입니다. 추가 질문이 있으시면 언제든지 물어보세요!