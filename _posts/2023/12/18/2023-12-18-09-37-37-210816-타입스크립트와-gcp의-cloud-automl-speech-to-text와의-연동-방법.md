---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud AutoML Speech-to-Text와의 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

이번 포스트에서는 타입스크립트를 사용하여 **Google Cloud Platform(GCP)**의 **Cloud AutoML Speech-to-Text** 서비스와의 연동 방법을 알아보겠습니다.

## 1. Cloud AutoML Speech-to-Text 설정

우선, GCP 콘솔에 로그인하여 **Cloud AutoML Speech-to-Text** 서비스를 활성화하고 모델을 작성합니다. 모델을 작성하는 과정에서 API 키 및 인증 정보를 가져올 수 있습니다.

## 2. 타입스크립트 프로젝트 설정

타입스크립트 프로젝트를 초기화하고, GCP 클라이언트 라이브러리를 설치합니다.

```bash
npm init -y
npm install @google-cloud/automl
```

## 3. 타입스크립트 코드 작성

아래는 Cloud AutoML Speech-to-Text 서비스를 사용하여 오디오 파일을 변환하는 간단한 예시 코드입니다.

```typescript
import { SpeechClient } from '@google-cloud/automl';

async function transcribeAudio() {
  // API 키와 인증 정보 설정
  const apiKey = 'your-api-key';
  const speechClient = new SpeechClient({ apiKey });

  // 오디오 파일 변환
  const inputConfig = {
    audioUri: 'gs://your-bucket/your-audio-file.wav',
  };

  const output = await speechClient.transcribeAudio(inputConfig);
  console.log('Transcription: ', output);
}

transcribeAudio();
```

위 코드에서 `your-api-key`와 `your-bucket/your-audio-file.wav`를 실제 값으로 대체해야 합니다.

## 4. 실행

코드를 실행하여 오디오 파일이 Cloud AutoML Speech-to-Text 서비스를 통해 텍스트로 변환되는지 확인합니다.

이렇게 타입스크립트를 사용하여 GCP의 Cloud AutoML Speech-to-Text와의 연동을 구현할 수 있습니다. 만약, 해당 서비스에 대한 API 사용 방법에 대해 더 알아보고 싶다면 공식 문서를 참고하시기 바랍니다.