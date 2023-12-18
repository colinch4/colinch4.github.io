---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 CameraX를 활용하여 이미지 캡처 기능을 구현하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

이미지 캡처 기능은 Android 앱에서 자주 사용되는 기능 중 하나입니다. CameraX는 Android Jetpack의 일부로 제공되며, 간편한 방식으로 디바이스 카메라에 접근하여 이미지 캡처 및 영상 녹화 기능을 구현할 수 있게 해줍니다. 

## CameraX 라이브러리 추가

먼저, Android Studio에서 CameraX 라이브러리를 프로젝트에 추가해야 합니다. `build.gradle` 파일의 `dependencies` 섹션에 다음 의존성을 추가하세요.

```gradle
implementation "androidx.camera:camera-camera2:1.1.0-alpha05"
```

## 이미지 캡처 기능 구현

이미지 캡처 기능을 구현하기 위해 다음과 같은 단계를 수행할 수 있습니다.

### 1. 카메라 미리보기 구성

카메라 미리보기를 구성하기 위해 `Preview` use case를 설정하세요.

```kotlin
val previewConfig = PreviewConfig.Builder().build()
val preview = Preview(previewConfig)

preview.setOnPreviewOutputUpdateListener {
    // 프리뷰를 화면에 표시
}
```

### 2. 이미지 캡처 구성

이미지 캡처를 위해 `ImageCapture` use case를 설정하세요.

```kotlin
val imageCaptureConfig = ImageCaptureConfig.Builder().build()
val imageCapture = ImageCapture(imageCaptureConfig)

// 이미지 캡처 요청
imageCapture.takePicture(executor, object : ImageCapture.OnImageCapturedListener() {
    override fun onCaptureSuccess(image: ImageProxy) {
        // 이미지 캡처 성공 시 동작
    }

    override fun onError(exception: ImageCaptureException) {
        // 오류 발생 시 동작
    }
})
```

### 3. 권한 요청

카메라를 사용하기 위해 적절한 권한을 요청하세요. manifest 파일에도 카메라 권한을 추가해야 합니다.

### 4. 이미지 캡처 버튼 추가

사용자가 이미지 캡처를 요청할 수 있는 버튼을 UI에 추가하세요.

### 5. 이미지 저장

`onCaptureSuccess` 콜백에서 이미지를 저장하는 코드를 추가하세요.

이제 CameraX를 사용하여 이미지 캡처 기능을 구현하고, 사용자가 카메라 인터페이스를 통해 이미지를 캡처할 수 있게 됩니다. 동작을 확인하고 필요에 따라 추가적인 기능을 구현하세요.

더 많은 자세한 내용 및 실제 구현 예제는 [Android Developers 사이트](https://developer.android.com/training/camerax)에서 찾아볼 수 있습니다.