---
layout: post
title: "[typescript] 타입스크립트와 GCP의 Cloud Identity Platform 연동 방법"
description: " "
date: 2023-12-18
tags: [typescript]
comments: true
share: true
---

본 포스트에서는 Google Cloud Platform(GCP)의 Cloud Identity Platform과 타입스크립트를 연동하는 방법을 안내합니다. 

## 전제 조건
- GCP 프로젝트가 설정되어 있어야 합니다.
- Cloud Identity Platform이 활성화되어 있어야 합니다.
- GCP의 OAuth 2.0 클라이언트 ID가 생성되어 있어야 합니다.

## 스텝 1: GCP 프로젝트 설정
1. GCP 콘솔에 로그인합니다.
2. Cloud Identity Platform 페이지로 이동합니다.
3. "OAuth 클라이언트 ID 만들기"를 선택합니다.
4. 필요한 정보를 입력하고 "만들기"를 클릭합니다.

## 스텝 2: 타입스크립트 프로젝트 생성
```typescript
// index.ts
import * as express from 'express';
const app = express();
```

## 스텝 3: GCP 클라이언트 ID 연동
1. GCP 콘솔에서 OAuth 2.0 클라이언트 ID를 선택합니다.
2. "허용된 리디렉션 URI"에 타입스크립트 애플리케이션의 엔드포인트 경로를 추가합니다.

위 과정을 완료하면 타입스크립트 애플리케이션을 GCP의 Cloud Identity Platform과 연동할 수 있습니다.

더 자세한 정보는 [GCP 공식 문서](https://cloud.google.com/identity-platform/docs)에서 확인할 수 있습니다.