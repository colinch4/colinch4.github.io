---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud Deployment Manager와의 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

이 글에서는 타입스크립트 프로젝트를 GCP(Cloud Deployment Manager)와 연동하는 방법에 대해 설명하겠습니다.

## 1. GCP 프로젝트 설정

먼저 GCP (Google Cloud Platform) 콘솔에 로그인하여 프로젝트를 생성합니다. 생성한 프로젝트에서 Cloud Deployment Manager API를 활성화 합니다.

## 2. gcloud 설치 및 구성

로컬 개발 환경에서는 gcloud 명령줄 도구를 사용하여 GCP와 상호 작용합니다. gcloud CLI를 설치하고 프로젝트를 구성합니다.

```bash
gcloud init
```

## 3. 타입스크립트 프로젝트 생성

타입스크립트 프로젝트를 생성하고 의존성을 설치합니다.

```bash
mkdir my-ts-project
cd my-ts-project
npm init -y
npm install typescript @types/node
```

## 4. Deployment 스크립트 작성

GCP의 Cloud Deployment Manager는 Infrastructure as Code를 구현하기 위한 템플릿 엔진입니다. 타입스크립트 프로젝트 내에서 Deployment 스크립트를 작성합니다.

예를 들어 `deployment.ts` 파일을 생성하고 다음과 같이 작성합니다:

```typescript
import { Deployment, Resources } from '@google-cloud/deployment-manager';

const deployment = new Deployment({
  projectId: 'your-project-id',
});

const resources: Resources = {
  // define your resources here
  // ...
};

deployment.create('my-deployment', { resources });
```

## 5. 배포

마지막으로, 타입스크립트 프로젝트를 빌드하고 Deployment Manager를 사용하여 GCP에 배포합니다.

```bash
tsc deployment.ts
gcloud deployment-manager deployments create my-ts-deployment --config deployment.js
```

이제 타입스크립트 프로젝트를 GCP의 Cloud Deployment Manager와 연동하여 손쉽게 인프라를 관리할 수 있습니다.

참고문헌:
- [Google Cloud Deployment Manager Documentation](https://cloud.google.com/deployment-manager/docs)
- [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs)
- [Typescript Documentation](https://www.typescriptlang.org/docs)