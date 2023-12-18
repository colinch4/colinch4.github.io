---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud Natural Language API 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

구글 클라우드 플랫폼(GCP)의 Cloud Natural Language API는 자연어 처리 기능을 제공합니다. 이 API를 사용하여 텍스트에서 감정 분석, 개체명 인식, 구문 분석 등의 자연어 처리 작업을 수행할 수 있습니다. 이번 블로그에서는 타입스크립트를 사용하여 GCP의 Cloud Natural Language API를 어떻게 연동하는지 알아보겠습니다.

## 1. GCP 프로젝트 및 서비스 계정 설정

우선 GCP 콘솔에서 새로운 프로젝트를 만들고, 해당 프로젝트에 서비스 계정을 생성해야 합니다. 서비스 계정을 통해 API를 사용할 수 있도록 권한을 부여할 수 있습니다. 

1. GCP 콘솔에 로그인한 후, "프로젝트 선택" 메뉴를 클릭하여 새로운 프로젝트를 만듭니다.
2. 이어서 "IAM 및 관리" > "서비스 계정"으로 이동하여 새 서비스 계정을 만듭니다. 
3. 서비스 계정을 만든 후에는 해당 계정에 Cloud Natural Language API를 사용할 수 있는 권한을 부여해야 합니다.

## 2. 타입스크립트로 API 연동하기

타입스크립트에서 GCP의 Cloud Natural Language API를 사용하려면 먼저 해당 API를 호출하는 클라이언트 라이브러리를 설치해야 합니다.

```typescript
npm install @google-cloud/language
```

그런 다음, 타입스크립트 파일에서 해당 라이브러리를 임포트하여 API를 사용할 수 있습니다.

```typescript
import { LanguageServiceClient } from '@google-cloud/language';

// 클라이언트 인스턴스 생성
const client = new LanguageServiceClient();

// 텍스트 분석 요청
const document = {
  content: '이 문장에 대해 감정 분석을 해주세요.',
  type: 'PLAIN_TEXT',
};

// API 호출
const [result] = await client.analyzeSentiment({ document: document });

// 결과 출력
console.log('감정 점수:', result.documentSentiment.score);
console.log('감정 매치:', result.documentSentiment.magnitude);
```

이제 해당 타입스크립트 파일을 빌드하고 실행하여 GCP의 Cloud Natural Language API를 연동한 후, 텍스트 분석 결과를 확인할 수 있게 됩니다.

위에서 설명한 방법을 통해 타입스크립트와 GCP의 Cloud Natural Language API를 연동하는 방법을 살펴보았습니다. 이를 통해 효과적으로 자연어 처리를 수행할 수 있는 웹 애플리케이션 또는 기타 솔루션을 개발할 수 있을 것입니다.

## 참고 자료
- [Google Cloud Natural Language API 공식 문서](https://cloud.google.com/natural-language)
- [Google Cloud Language 클라이언트 라이브러리](https://www.npmjs.com/package/@google-cloud/language)
- [Google Cloud 프로젝트 및 서비스 계정 설정 가이드](https://cloud.google.com/docs/authentication/getting-started)