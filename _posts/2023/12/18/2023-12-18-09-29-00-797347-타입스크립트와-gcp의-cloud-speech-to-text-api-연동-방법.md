---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud Speech-to-Text API 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

이 기술 블로그에서는 타입스크립트로 개발된 애플리케이션에서 Google Cloud Platform(GCP)의 Cloud Speech-to-Text API를 사용하여 음성을 텍스트로 변환하는 방법에 대해 알아보겠습니다.

## 필수 요구사항

이 연동을 위해선 GCP의 프로젝트 및 서비스 계정이 설정되어 있어야 합니다. 타입스크립트 기반의 프로젝트가 미리 설정되어 있어야 합니다.

## Cloud Speech-to-Text API 설정

1. GCP 콘솔에서 프로젝트를 선택합니다.
2. Navigation 메뉴에서 APIs 및 서비스 > 라이브러리로 이동합니다.
3. Cloud Speech-to-Text API를 검색하고 활성화합니다.

## 서비스 계정 및 인증 설정

1. GCP 콘솔에서 프로젝트를 선택합니다.
2. Navigation 메뉴에서 IAM 및 관리 > 서비스 계정으로 이동합니다.
3. 새 서비스 계정을 생성하고, `Cloud Speech-to-Text API 사용자` 역할을 부여합니다.
4. 서비스 계정 키를 생성하고 JSON 형식으로 저장합니다.

## 타입스크립트 프로젝트 설정

1. GCP의 서비스 계정 키 파일을 프로젝트에 추가합니다.
2. `google-cloud/speech` 패키지를 사용하여 타입스크립트 프로젝트에 Cloud Speech-to-Text API를 연동합니다.

```typescript
import * as speech from '@google-cloud/speech';
import * as fs from 'fs';

const client = new speech.SpeechClient({
  keyFilename: 'path_to_service_account_key.json',
});

const audio = {
  content: fs.readFileSync('path_to_audio_file').toString('base64'),
};

const config = {
  encoding: '',
  sampleRateHertz: 16000,
  languageCode: 'en-US',
};

const request = {
  audio: audio,
  config: config,
};

const [response] = await client.recognize(request);
const transcription = response.results
  .map(result => result.alternatives[0].transcript)
  .join('\n');
console.log(`Transcription: ${transcription}`);
```

위 코드에서 `path_to_service_account_key.json`은 서비스 계정 키 파일의 경로를, `path_to_audio_file`은 변환하려는 오디오 파일의 경로를 나타냅니다.

이제 당신의 타입스크립트 프로젝트에서 Cloud Speech-to-Text API를 사용하여 음성을 텍스트로 변환할 수 있습니다.

## 결론

이 문서에서는 타입스크립트를 사용하여 GCP의 Cloud Speech-to-Text API를 연동하는 방법에 대해 알아보았습니다. 이를 통해 음성 처리와 텍스트 변환에 대한 기술적인 이해를 높일 수 있으며, 다양한 타입스크립트 기반 프로젝트에서 활용할 수 있습니다.

## 참고 자료

- [Google Cloud Speech-to-Text API 공식 문서](https://cloud.google.com/speech-to-text)
- [Google Cloud Speech-to-Text API 타입스크립트 클라이언트 라이브러리](https://www.npmjs.com/package/@google-cloud/speech)