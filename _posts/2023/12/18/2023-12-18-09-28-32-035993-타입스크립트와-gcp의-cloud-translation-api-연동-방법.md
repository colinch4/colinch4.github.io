---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud Translation API 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

GCP의 Cloud Translation API는 다양한 언어 간 번역 기능을 제공하며, 타입스크립트를 사용하여 이 API를 손쉽게 연동할 수 있습니다. 이 블로그 포스트에서는 타입스크립트와 GCP의 Cloud Translation API를 연동하는 방법에 대해 알아보겠습니다.


## 1. 프로젝트 설정

먼저, 타입스크립트 프로젝트를 생성하고 GCP의 프로젝트를 설정해야 합니다. GCP 콘솔에서 프로젝트를 생성한 후, 해당 프로젝트의 인증 정보를 기반으로 서비스 계정을 생성할 수 있습니다.

### 1.1 GCP 프로젝트 생성

GCP 콘솔에 로그인한 후, 새 프로젝트를 생성합니다.

### 1.2 서비스 계정 생성

GCP 콘솔에서 서비스 계정을 생성하고, 해당 서비스 계정의 키를 JSON 형식으로 다운로드합니다.


## 2. 타입스크립트 프로젝트 설정

### 2.1 프로젝트 초기화

먼저 새로운 디렉토리를 만들고, 다음 명령어를 사용하여 타입스크립트 프로젝트를 초기화합니다.

```bash
mkdir translation-api
cd translation-api
npm init -y
npm install typescript @google-cloud/translate
```

### 2.2 서비스 계정 키 설정

프로젝트 루트 디렉토리에 GCP에서 다운로드한 서비스 계정 키를 `service-account-key.json`이라는 파일명으로 저장합니다.


## 3. Cloud Translation API 연동

### 3.1 인증 설정

Cloud Translation API를 사용하기 위해서는 서비스 계정 키를 사용하여 클라이언트를 생성해야 합니다. 타입스크립트에서는 다음과 같이 인증 정보를 설정할 수 있습니다.

```typescript
import { Translate } from '@google-cloud/translate';
import path from 'path';

const translate = new Translate({
  keyFilename: path.join(__dirname, 'service-account-key.json'),
});
```

### 3.2 번역 요청

이제 Cloud Translation API를 사용하여 번역 요청을 보낼 수 있습니다. 아래 예제는 영어를 한국어로 번역하는 예시입니다.

```typescript
async function translateText(text: string, targetLanguage: string) {
  const [translation] = await translate.translate(text, targetLanguage);
  return translation;
}

const translatedText = await translateText('Hello, world!', 'ko');
console.log(translatedText);
```

위와 같이 Cloud Translation API를 사용하여 텍스트를 다른 언어로 번역할 수 있습니다.


## 결론

이제 당신은 타입스크립트를 사용하여 GCP의 Cloud Translation API를 손쉽게 연동하는 방법을 배웠습니다. GCP와 타입스크립트를 함께 사용하여 언어 번역 기능을 구현할 수 있을 것입니다. GCP의 Cloud Translation API 공식 문서에서 더 자세한 정보를 얻을 수 있으니 참고해 보세요.

내용이 마음에 드셨다면, [여기](https://www.example.com)를 클릭하여 더 많은 정보를 얻어보세요.