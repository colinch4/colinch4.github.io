---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud Text-to-Speech API 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

GCP(Cloud Text-to-Speech API)의 기능을 활용하여 타입스크립트 프로젝트에 텍스트를 음성으로 변환하는 기능을 추가할 수 있습니다. 이 기능을 사용하면 사용자에게 텍스트 기반의 정보를 음성으로 제공할 수 있으며, 웹 애플리케이션이나 모바일 애플리케이션에 음성 기능을 쉽게 통합할 수 있습니다.

## 1. GCP 프로젝트 및 서비스 계정 설정

먼저, GCP 콘솔에서 새로운 프로젝트를 생성하고, Cloud Text-to-Speech API를 활성화합니다. 그런 다음, 서비스 계정을 생성하여 해당 프로젝트에 대한 인증 정보를 받습니다.

## 2. 타입스크립트 프로젝트 설정

타입스크립트 프로젝트의 루트 디렉토리에서 GCP의 클라이언트 라이브러리를 설치합니다.

```typescript
npm install @google-cloud/text-to-speech
```

그런 다음, GCP의 서비스 계정 인증 정보를 포함하는 JSON 파일을 프로젝트 내에 추가하고, 해당 파일의 경로를 환경 변수로 설정합니다.

## 3. 음성 합성 기능 구현

GCP의 클라이언트 라이브러리를 사용하여 타입스크립트 코드에서 음성 합성을 수행합니다.

```typescript
import textToSpeech from '@google-cloud/text-to-speech';
import fs from 'fs';

const client = new textToSpeech.TextToSpeechClient();

async function synthesizeTextToSpeech(text: string, outputFile: string) {
  const request = {
    input: {text: text},
    voice: {languageCode: 'en-US', ssmlGender: 'NEUTRAL'},
    audioConfig: {audioEncoding: 'MP3'},
  };

  const [response] = await client.synthesizeSpeech(request);
  const writeFile = util.promisify(fs.writeFile);
  await writeFile(outputFile, response.audioContent, 'binary');
}
```

## 4. 음성 파일 재생

생성된 음성 파일을 웹 애플리케이션 등에서 재생할 수 있도록 설정합니다.

## 요약

위의 방법을 통해 GCP의 Cloud Text-to-Speech API를 타입스크립트 프로젝트에 통합하여 텍스트를 음성으로 변환하는 기능을 추가할 수 있습니다. 이를 통해 사용자 경험을 향상시키고, 웹 및 모바일 애플리케이션에 음성 기능을 쉽게 통합할 수 있습니다.

더 자세한 정보는 [GCP 공식 문서](https://cloud.google.com/text-to-speech)를 참고하세요.