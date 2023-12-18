---
layout: post
title: "[ios] PhotoKit을 사용하여 Live Photo 및 Burst Mode 이미지 다루는 방법"
description: " "
date: 2023-12-18
tags: [ios]
comments: true
share: true
---

iOS 앱을 개발하다 보면 사용자의 사진 라이브러리에서 Live Photo나 Burst Mode로 촬영된 이미지를 처리해야 하는 경우가 있습니다. iOS의 PhotoKit 프레임워크를 사용하면 이러한 이미지를 다루는 것이 가능합니다. 이번 포스트에서는 PhotoKit을 사용하여 Live Photo와 Burst Mode 이미지를 다루는 방법에 대해 알아보겠습니다.

## Live Photo 다루기

Live Photo는 사실적인 동적 효과를 담아낸 이미지로, 정적인 JPEG 이미지와 함께 촬영된 짧은 동영상으로 구성됩니다. Live Photo를 다루기 위해선 다음의 단계를 따릅니다.

1. **PHAsset 가져오기:** PhotoKit을 사용하여 Live Photo를 나타내는 `PHAsset`을 가져옵니다.

    ```swift
    let options = PHFetchOptions()
    options.predicate = NSPredicate(format: "mediaSubtype == %ld", PHAssetMediaSubtype.photoLive.rawValue)
    let fetchResult = PHAsset.fetchAssets(with: options)
    ```

2. **Live photo 컨텐츠 가져오기:** `PHAsset`을 사용하여 Live Photo의 사진 및 동영상 컨텐츠를 가져옵니다.

    ```swift
    let imageManager = PHCachingImageManager()
    imageManager.requestLivePhoto(for: phAsset, targetSize: targetSize, contentMode: .aspectFit, options: nil) { (livePhoto, _) in
        // livePhoto 사용
    }
    ```

3. **Live Photo 플레이백:** Live Photo를 플레이백하거나 썸네일 이미지를 생성합니다.

    ```swift
    PHLivePhotoView.livePhoto = livePhoto
    ```

## Burst Mode 이미지 다루기

Burst Mode는 연속적으로 촬영된 여러 사진을 하나의 그룹으로 묶은 형태로, 각 그룹은 하나의 `PHAsset`으로 표현됩니다. Burst Mode 이미지를 다루는 방법은 다음과 같습니다.

1. **PHAsset 가져오기:** PhotoKit을 사용하여 Burst Mode 이미지를 나타내는 `PHAsset`을 가져옵니다.

    ```swift
    let options = PHFetchOptions()
    options.predicate = NSPredicate(format: "mediaSubtype == %ld", PHAssetMediaSubtype.photoBurst.rawValue)
    let fetchResult = PHAsset.fetchAssets(with: options)
    ```

2. **Burst Mode 이미지 그룹 가져오기:** `PHAsset`을 사용하여 해당 Burst Mode 이미지 그룹을 가져옵니다.

    ```swift
    PHAsset.fetchAssets(in: burstAsset, options: nil)
    ```

3. **Burst Mode 이미지 처리:** Burst Mode 이미지 그룹을 순회하면서 필요한 처리를 수행합니다.

    ```swift
    imageManager.startCachingImages(for: assetsArray, targetSize: targetSize, contentMode: .aspectFit, options: nil)
    ```

이러한 방법을 통해 PhotoKit을 사용하여 Live Photo와 Burst Mode 이미지를 효과적으로 다룰 수 있습니다. iOS 앱에서 사용자의 사진들을 다루거나 사용하는 경우, 이러한 기능을 적절히 활용하여 더 다양하고 풍부한 사용자 경험을 제공할 수 있습니다.

참고 자료:
- [Apple Developer Documentation - PhotoKit](https://developer.apple.com/documentation/photokit)
- [Apple Developer Documentation - PHAsset](https://developer.apple.com/documentation/photokit/phasset)