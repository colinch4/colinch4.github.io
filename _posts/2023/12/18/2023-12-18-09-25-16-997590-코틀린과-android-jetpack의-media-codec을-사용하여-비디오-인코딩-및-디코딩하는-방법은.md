---
layout: post
title: "[kotlin] 코틀린과 Android Jetpack의 Media Codec을 사용하여 비디오 인코딩 및 디코딩하는 방법은?"
description: " "
date: 2023-12-18
tags: [kotlin]
comments: true
share: true
---

비디오 인코딩 및 디코딩은 안드로이드 앱에서 중요한 기능입니다. 코틀린과 Android Jetpack을 사용하여 비디오를 인코딩하고 디코딩하는 방법을 알아봅시다.

## 1. MediaCodec을 사용한 비디오 인코딩

MediaCodec은 안드로이드에서 비디오 인코딩을 위한 강력한 도구입니다. 아래는 간단한 예제입니다.

```kotlin
val mimeType = "video/avc"
val videoWidth = 1280
val videoHeight = 720
val videoBitRate = 2000000
val videoFrameRate = 30

val mediaCodec = MediaCodec.createEncoderByType(mimeType)
val mediaFormat = MediaFormat.createVideoFormat(mimeType, videoWidth, videoHeight)
mediaFormat.setInteger(MediaFormat.KEY_BIT_RATE, videoBitRate)
mediaFormat.setInteger(MediaFormat.KEY_FRAME_RATE, videoFrameRate)

mediaCodec.configure(mediaFormat, null, null, MediaCodec.CONFIGURE_FLAG_ENCODE)
mediaCodec.start()
```

위 코드는 AVC(Advanced Video Coding) 비디오 코덱을 사용하여 비디오를 인코딩할 수 있는 MediaCodec 인스턴스를 생성하는 방법을 보여줍니다. 그 후에는 원하는 설정 값으로 MediaFormat을 생성하고, `configure` 및 `start`를 호출하여 인코더를 시작합니다.

## 2. MediaCodec을 사용한 비디오 디코딩

비디오 디코딩을 위해서도 MediaCodec을 사용할 수 있습니다.

```kotlin
val filePath = "path_to_your_video_file"
val surface = Surface(textureView.surfaceTexture)

val mediaExtractor = MediaExtractor()
mediaExtractor.setDataSource(filePath)

val trackIndex = getVideoTrackIndex(mediaExtractor)
mediaExtractor.selectTrack(trackIndex)

val mediaFormat = mediaExtractor.getTrackFormat(trackIndex)
val mimeType = mediaFormat.getString(MediaFormat.KEY_MIME)

val mediaCodec = MediaCodec.createDecoderByType(mimeType)
mediaCodec.configure(mediaFormat, surface, null, 0)
mediaCodec.start()
```

위 코드는 주어진 비디오 파일의 트랙에서 비디오를 추출하고, 해당 트랙의 MediaFormat을 얻어 디코더를 초기화하는 방법을 보여줍니다.

## 3. Android Jetpack을 활용한 비디오 인코딩 및 디코딩

Android Jetpack에서는 MediaCodec을 더 쉽게 사용할 수 있도록 AndroidX의 `VideoEncoder` 및 `VideoDecoder` 라이브러리를 제공합니다. 이를 사용하면 더 간편하게 비디오 인코딩 및 디코딩을 수행할 수 있습니다.

```kotlin
val encoder = VideoEncoder.Builder()
    .setOutputSize(1280, 720)
    .setBitRate(2000000)
    .setEncoderCallback(encoderCallback)
    .build()

encoder.start()

val decoder = VideoDecoder.Builder()
    .setSurface(surface)
    .setDecoderCallback(decoderCallback)
    .build()

decoder.start()
```

Android Jetpack의 VideoEncoder 및 VideoDecoder를 사용하면 더 간편하고 높은 수준의 추상화된 API를 통해 비디오 인코딩 및 디코딩을 수행할 수 있습니다.

이제, 코틀린과 Android Jetpack을 사용하여 안드로이드 앱에서 비디오 인코딩 및 디코딩을 수행하는 방법에 대해 간략하게 살펴보았습니다. 이를 통해 앱에서 비디오 처리 기능을 구현하는데 도움이 되길 바랍니다.

참고 문헌:
- [Android Developers - MediaCodec](https://developer.android.com/reference/android/media/MediaCodec)
- [Android Developers - VideoEncoder](https://developer.android.com/guide/topics/media/video-encoder)