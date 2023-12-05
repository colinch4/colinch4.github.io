---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트 배포 자동화"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

## 목차

1. 소개
2. 배포 자동화의 이점
3. Package.json 설정
4. 배포 스크립트 작성
5. GitHub Actions 사용하기
6. 결론

## 1. 소개

현대의 JavaScript 개발 프로젝트에서 배포는 필수적인 작업입니다. 프로젝트가 커지면서 복잡한 구성 요소를 가질 수 있고, 배포 프로세스를 자동화하여 개발자의 시간과 노력을 절약할 수 있습니다. Package.json 파일은 npm (Node Package Manager)에서 프로젝트의 의존성 관리 외에도 다양한 작업을 자동화하기 위해 사용될 수 있습니다.

이 블로그 포스트에서는 Package.json 설정을 사용하여 JavaScript 프로젝트 배포를 자동화하는 방법을 알아보겠습니다.

## 2. 배포 자동화의 이점

배포 자동화는 다음과 같은 이점을 제공합니다:

- 일관된 배포 프로세스: 자동화된 배포 스크립트를 사용하면 개발자들이 프로젝트를 배포할 때 항상 일관된 방식으로 수행되도록 할 수 있습니다.
- 시간 절약: 수동으로 작업을 반복하는 대신 배포 작업을 자동화하면 개발자들이 시간을 절약할 수 있습니다.
- 실수 감소: 자동화된 배포 프로세스를 사용하면 실수를 줄일 수 있고, 실수로 인한 문제를 사전에 방지할 수 있습니다.

## 3. Package.json 설정

Package.json 파일은 JavaScript 프로젝트의 구성 요소를 정의하는 데 사용됩니다. 이 파일을 사용하여 프로젝트의 의존성 관리뿐만 아니라 스크립트 작성과 배포 자동화에도 활용할 수 있습니다.

```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "build": "webpack",
    "test": "jest",
    "deploy": "npm run build && aws s3 sync dist/ s3://my-bucket"
  },
  "devDependencies": {
    "webpack": "^5.0.0",
    "jest": "^27.0.0"
  }
}
```

위의 예시에서, Package.json 파일은 "scripts" 속성을 가지고 있습니다. 이 속성은 프로젝트에서 사용할 수 있는 스크립트 명령어들을 정의합니다. 이중 "deploy" 스크립트는 프로젝트를 빌드한 후 생성된 파일들을 AWS S3 버킷으로 동기화시키는 명령어입니다.

## 4. 배포 스크립트 작성

Package.json 파일에서 정의된 스크립트를 사용하여 배포 스크립트를 작성할 수 있습니다. 보통 배포 스크립트는 프로젝트의 빌드와 배포 단계를 포함합니다.

아래는 예시로 주어진 배포 스크립트입니다:

```bash
#!/bin/bash

echo "Building project..."
npm run build

echo "Deploying project to AWS S3..."
aws s3 sync dist/ s3://my-bucket

echo "Deployment completed!"
```

위의 예시에서, 스크립트는 프로젝트를 빌드하고, 빌드된 파일들을 AWS S3 버킷으로 동기화시킵니다. 또한 각 단계에서 메시지를 출력하여 진행 상황을 보여줍니다.

## 5. GitHub Actions 사용하기

GitHub Actions를 사용하여 JavaScript 프로젝트를 자동으로 빌드하고 배포할 수 있습니다. GitHub Actions는 CI/CD(Continuous Integration/Continuous Deployment) 파이프라인을 구축하기 위한 도구입니다.

아래는 예시로 주어진 GitHub Actions 설정 파일입니다:

```yaml
{% raw %}
name: Deploy to AWS S3

on:
  push:
    branches:
      - main

jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
        
      - name: Install dependencies
        run: npm ci
      
      - name: Build project
        run: npm run build
      
      - name: Deploy to AWS S3
        run: |
          aws configure set aws_access_key_id ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws configure set aws_secret_access_key ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws s3 sync dist/ s3://my-bucket
{% endraw %}
```

위의 예시에서, GitHub Actions는 "push" 이벤트를 감지하고, "main" 브랜치로 push 되었을 때 "deploy" 작업을 실행합니다. 이 작업은 프로젝트를 빌드하고, AWS S3에 배포합니다. 배포를 위해 AWS 액세스 키와 비밀 액세스 키를 Secrets로부터 가져옵니다.

## 6. 결론

Package.json 설정을 활용하여 JavaScript 프로젝트를 자동으로 빌드하고 배포하는 방법을 알아보았습니다. 이를 통해 일관된 배포 프로세스를 구축하고, 개발자들의 시간과 노력을 절약할 수 있습니다. 또한 GitHub Actions를 사용하여 자동화된 배포를 구현할 수도 있습니다.

빠르고 안정적인 배포 프로세스는 프로젝트의 성공과 지속적인 개선을 위해 필수적입니다. 따라서 Package.json 설정과 배포 자동화를 통해 효율적인 프로젝트 관리를 실현할 수 있습니다.

## 참고 자료

- [npm Documentation](https://docs.npmjs.com/)
- [AWS CLI Documentation](https://aws.amazon.com/cli/documentation/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)