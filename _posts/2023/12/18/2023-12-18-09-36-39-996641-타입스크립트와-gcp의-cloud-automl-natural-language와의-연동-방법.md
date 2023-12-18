---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud AutoML Natural Language와의 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

GCP(Cloud AutoML Natural Language)은 기계 학습(ML) 모델을 구축하는 것을 돕기 위한 Google Cloud의 기계 학습 플랫폼입니다. 타입스크립트를 사용하여 GCP의 AutoML Natural Language와 연동하여 효율적으로 ML 모델을 구축하고 활용할 수 있습니다.

이 블로그에서는 타입스크립트를 사용하여 GCP의 Cloud AutoML Natural Language와의 연동 방법에 대해 알아보겠습니다.

## 1. GCP 프로젝트 및 서비스 계정 설정

GCP 콘솔에서 새로운 프로젝트를 생성하고, Cloud AutoML Natural Language 서비스를 활성화합니다. 서비스 계정을 생성하여 JSON 형식의 인증 키를 다운로드 받습니다.

## 2. 타입스크립트 프로젝트 초기화

새로운 타입스크립트 프로젝트를 초기화합니다. `package.json` 파일을 생성하고 필요한 의존성 모듈을 설치합니다.

```typescript
npm init -y
npm install @google-cloud/automl
```

## 3. 인증 및 연결 설정

다운로드 받은 인증 키를 사용하여 GCP와 연결합니다. 타입스크립트 코드에서 인증 키를 로드하고 GCP와의 연결을 설정합니다.

```typescript
import { AutoMlClient } from '@google-cloud/automl';

const client = new AutoMlClient({ credentials: require('./path-to-credentials.json') });
```

## 4. 자연어 처리 모델 구축

Cloud AutoML Natural Language를 사용하여 자연어 처리 모델을 구축합니다. 이를 위해 데이터를 업로드하고 모델을 훈련시킵니다.

```typescript
async function createModel() {
  const projectId = 'your-project-id';
  const location = 'us-central1';
  const datasetId = 'dataset-id';
  const displayName = 'MyModel';

  const request = {
    parent: client.locationPath(projectId, location),
    model: {
      displayName: displayName,
      datasetId: datasetId,
      textClassificationModelMetadata: {},
    },
  };

  const [response] = await client.createModel(request);
  console.log(`Model name: ${response.name}`);
}
```

## 5. 모델 활용

구축한 모델을 활용하여 자연어 처리 작업을 수행합니다.

```typescript
async function predict(text: string) {
  const modelId = 'your-model-id';
  const input = {
    textSnippet: {
      content: text,
    },
  };

  const [response] = await client.predict({
    name: client.modelPath(projectId, location, modelId),
    payload: input,
  });

  console.log('Prediction results:');
  response.payload.forEach(result => {
    console.log(`Predicted class name: ${result.displayName}`);
    console.log(`Confidence: ${result.classification.score}`);
  });
}
```

위의 단계를 따라하면 타입스크립트로 GCP의 AutoML Natural Language와 연동하여 ML 모델을 구축하고 활용할 수 있습니다. 이를 통해 원하는 자연어 처리 작업에 대해 효율적으로 모델을 구성하고 활용할 수 있습니다.

[참조: Google Cloud AutoML Natural Language 공식 문서](https://cloud.google.com/natural-language/automl/docs)

이상으로 GCP의 Cloud AutoML Natural Language와의 연동 방법에 대한 타입스크립트 코드를 소개하였습니다. 감사합니다.