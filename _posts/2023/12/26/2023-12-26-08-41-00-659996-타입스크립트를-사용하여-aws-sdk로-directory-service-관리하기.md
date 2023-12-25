---
layout: post
title: "[typescript] 타입스크립트를 사용하여 AWS SDK로 Directory Service 관리하기"
description: " "
date: 2023-12-26
tags: [typescript]
comments: true
share: true
---

이번에는 **AWS SDK**와 **타입스크립트**를 사용하여 **AWS Directory Service**를 관리하는 방법에 대해 살펴보겠습니다.

## 목차

1. AWS Directory Service란?
2. AWS SDK 및 타입스크립트 설정
3. Directory Service 리스트 가져오기
4. 새로운 Directory 생성하기
5. Directory 삭제하기

## 1. AWS Directory Service란?

**AWS Directory Service**는 마이크로소프트 액티브 디렉터리(AD)와 Amazon Cognito Identity를 사용하는 애플리케이션을 위한 관리형 디렉터리를 제공합니다. 

## 2. AWS SDK 및 타입스크립트 설정

먼저, AWS SDK와 타입스크립트를 설정해야 합니다. 

```typescript
import * as AWS from 'aws-sdk';

AWS.config.update({
  region: 'YOUR_REGION',
  // 다른 설정들...
});
```

## 3. Directory Service 리스트 가져오기

```typescript
const ds = new AWS.DirectoryService();

ds.describeDirectories({}, (err, data) => {
  if (err) console.log(err, err.stack);
  else console.log(data);
});
```

## 4. 새로운 Directory 생성하기

```typescript
const params = {
  Name: 'NEW_DIRECTORY',
  Password: 'PASSWORD',
  Size: 'Small',
  // 다른 필수 및 옵션 파라미터들...
};

ds.createDirectory(params, (err, data) => {
  if (err) console.log(err, err.stack);
  else console.log(data);
});
```

## 5. Directory 삭제하기

```typescript
const params = {
  DirectoryId: 'YOUR_DIRECTORY_ID',
};

ds.deleteDirectory(params, (err, data) => {
  if (err) console.log(err, err.stack);
  else console.log(data);
});
```

## 마무리

지금까지 **AWS SDK**와 **타입스크립트**를 사용하여 **AWS Directory Service**를 관리하는 방법에 대해 알아보았습니다. 추가로 필요한 정보는 **AWS 공식 문서**를 참고하시기 바랍니다.

- 더 많은 정보: [AWS SDK for JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DirectoryService.html)
- [타입스크립트 공식 문서](https://www.typescriptlang.org/docs)