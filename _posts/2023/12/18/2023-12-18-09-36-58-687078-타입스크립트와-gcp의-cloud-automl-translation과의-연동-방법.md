---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud AutoML Translation과의 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

본 포스트에서는 타입스크립트로 작성된 애플리케이션과 **Google Cloud Platform(GCP)**의 **Cloud AutoML Translation**을 연동하는 방법에 대해 설명합니다.

## Cloud AutoML Translation이란?

**Cloud AutoML Translation**은 사용자 지정된 텍스트 번역 모델을 구축하고 배포하는 데 도움을 주는 GCP의 서비스입니다. 머신러닝 기술을 사용하여 다양한 언어 간의 텍스트 번역을 지원합니다.

## 환경 설정

먼저, **GCP** 콘솔에서 프로젝트를 만들고, **Cloud AutoML Translation** API를 활성화합니다. 그 후, **서비스 계정 키**를 생성하여 프로젝트 ID를 포함한 JSON 파일을 다운로드합니다.

## 타입스크립트 프로젝트 설정

### 패키지 설치

먼저, **@google-cloud/translate** 패키지를 사용하여 GCP와 통신할 수 있도록 필요한 패키지를 설치합니다.

```bash
npm install @google-cloud/translate
```

### GCP와 연동

다음으로, GCP의 **서비스 계정 키**를 사용하여 **GCP**와 연동합니다.

```typescript
import { TranslationServiceClient } from '@google-cloud/translate';

const translationServiceClient = new TranslationServiceClient({
  keyFilename: 'path-to-service-account-key.json',
});
```

위 코드에서 `'path-to-service-account-key.json'`은 앞서 다운로드한 **서비스 계정 키** 파일의 경로로 대체되어야 합니다.

### 번역 요청

이제 번역하고자 하는 텍스트와 대상 언어를 지정하여 번역 요청을 보낼 수 있습니다.

```typescript
async function translateText(text: string, targetLanguage: string) {
  const request = {
    parent: `projects/${projectId}/locations/global`,
    contents: [text],
    mimeType: 'text/plain',
    sourceLanguageCode: 'en', // 원본 언어 코드
    targetLanguageCode: targetLanguage, // 대상 언어 코드
  };

  const [response] = await translationServiceClient.translateText(request);
  console.log('번역 결과:', response.translations);
}
```

위 코드에서 `text`는 번역하고자 하는 텍스트이고, `targetLanguage`는 번역할 대상 언어 코드입니다. 호출 결과는 `response.translations`로 확인할 수 있습니다.

이제 이 코드를 통해 타입스크립트 애플리케이션과 Cloud AutoML Translation을 연동할 수 있습니다. 

본 포스트에서는 타입스크립트로 GCP의 Cloud AutoML Translation과의 연동 방법에 대해 알아보았습니다. 이를 통해 사용자 정의 텍스트 번역 모델을 구축하고 활용하는 방법에 대한 기본적인 이해를 얻을 수 있습니다.

더 많은 정보는 [Cloud AutoML Translation 문서](https://cloud.google.com/translate/automl/docs)를 참고하시기 바랍니다.