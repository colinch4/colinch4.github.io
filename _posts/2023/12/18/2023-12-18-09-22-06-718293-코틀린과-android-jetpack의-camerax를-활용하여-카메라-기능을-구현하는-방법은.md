---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 CameraX를 활용하여 카메라 기능을 구현하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

안녕하세요! 안드로이드 앱 개발에서 카메라 기능을 구현하고 싶으시군요. 코틀린과 Android Jetpack의 CameraX를 사용하여 카메라 기능을 구현하는 방법을 알려드리겠습니다.

## 필수 라이브러리 추가

먼저, **build.gradle** 파일에 CameraX와 관련된 필수 라이브러리를 추가해야 합니다.

```kotlin
dependencies {
    def camerax_version = "1.0.0-beta15"
    implementation "androidx.camera:camera-camera2:$camerax_version"
    implementation "androidx.camera:camera-lifecycle:$camerax_version"
    implementation "androidx.camera:camera-view:1.0.0-alpha25"
}
```

## 카메라 뷰 레이아웃 추가

카메라를 미리보기하기 위한 레이아웃을 추가합니다.

```xml
<androidx.camera.view.PreviewView
    android:id="@+id/previewView"
    android:layout_width="match_parent"
    android:layout_height="match_parent" />
```

## CameraX 초기화 및 사용

이제 Kotlin 코드를 사용하여 CameraX를 초기화하고 카메라를 사용할 수 있습니다.

```kotlin
val cameraProviderFuture = ProcessCameraProvider.getInstance(context)

cameraProviderFuture.addListener({
    val cameraProvider: ProcessCameraProvider = cameraProviderFuture.get()
    val preview = Preview.Builder().build().also {
        it.setSurfaceProvider(previewView.createSurfaceProvider())
    }
    val cameraSelector = CameraSelector.DEFAULT_BACK_CAMERA
    try {
        cameraProvider.unbindAll()
        cameraProvider.bindToLifecycle(
            lifecycleOwner, cameraSelector, preview
        )
    } catch(exc: Exception) {
        Log.e(TAG, "카메라 사용 중 에러 발생", exc)
    }
}, ContextCompat.getMainExecutor(context))
```

위의 코드는 카메라 미리보기를 설정하고 기기의 후면 카메라를 사용하는 방법을 보여줍니다.

이제 코틀린과 CameraX를 사용하여 안드로이드 카메라 앱을 만드는 방법을 알게 되셨습니다. 원하는 다른 기능들을 추가하여 더욱 풍부한 앱을 만들어보세요!