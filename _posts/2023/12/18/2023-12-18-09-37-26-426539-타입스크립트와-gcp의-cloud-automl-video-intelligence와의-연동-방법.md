---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud AutoML Video Intelligence와의 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

본 포스트에서는 타입스크립트와 Google Cloud Platform(GCP)의 Cloud AutoML Video Intelligence를 연동하는 방법에 대해 소개합니다.

## 목차
1. [Cloud AutoML Video Intelligence 소개](#cloud-automl-video-intelligence-소개)
2. [GCP 프로젝트 설정](#gcp-프로젝트-설정)
3. [타입스크립트에서의 Cloud AutoML Video Intelligence 사용](#타입스크립트에서의-cloud-automl-video-intelligence-사용)
4. [결론](#결론)

## Cloud AutoML Video Intelligence 소개
**Cloud AutoML Video Intelligence**는 비디오 콘텐츠를 분석하고 탐색하기 위한 머신 러닝 기반의 서비스로, 사용자가 자체적으로 사용자 지정 비디오 분류 모델을 만들고 훈련시킬 수 있습니다.

## GCP 프로젝트 설정
먼저 GCP 콘솔에서 새로운 프로젝트를 생성하고 Cloud AutoML API를 활성화합니다. 활성화한 후에는 서비스 계정 키를 생성하여 해당 키를 사용해 인증 및 권한 부여를 할 수 있습니다.

## 타입스크립트에서의 Cloud AutoML Video Intelligence 사용
다음으로, 타입스크립트 프로젝트를 생성하고 필요한 패키지와 모듈을 설치합니다. 

```typescript
npm install @google-cloud/automl
```

그런 다음, Cloud AutoML Video Intelligence를 사용하여 비디오를 분석하고 분류하는 TypeScript 코드를 작성합니다.

```typescript
import { PredictionServiceClient } from '@google-cloud/automl';

// 인증 및 권한
const client = new PredictionServiceClient();

async function predictVideo() {
  // 비디오 예측 수행
  const response = await client.predict({
    name: 'projects/PROJECT_ID/locations/us-central1/models/MODEL_ID',
    payload: {
      video: {
        // 비디오 데이터
        video: {
          // 비디오 파일 경로
          name: 'projects/PROJECT_ID/locations/us-central1/models/MODEL_ID/datasets/DATASET_ID/files/VIDEO_FILE'
        }
      }
    }
  });

  console.log('Prediction results:', response);
}

predictVideo();
```

## 결론
본 포스트에서는 타입스크립트와 GCP의 Cloud AutoML Video Intelligence를 연동하는 방법에 대해 알아보았습니다. Cloud AutoML Video Intelligence를 사용하면 비디오 데이터를 분석하고 분류하는 작업을 타입스크립트에서 손쉽게 수행할 수 있습니다.

더 자세한 정보는 [Cloud AutoML Video Intelligence 문서](https://cloud.google.com/video-intelligence/automl/docs)에서 확인할 수 있습니다.