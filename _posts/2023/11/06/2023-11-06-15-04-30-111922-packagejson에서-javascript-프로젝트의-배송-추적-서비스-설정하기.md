---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 배송 추적 서비스 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

작업 중인 JavaScript 프로젝트에 배송 추적 서비스를 추가하고 싶습니다. 이를 위해 package.json에서 설정을 변경해야 합니다. 이 문서에서는 package.json 파일을 사용하여 프로젝트에서 배송 추적 서비스를 설정하는 방법을 알려드리겠습니다.

## Step 1: Package.json 파일 열기

프로젝트 루트 디렉토리에서 package.json 파일을 엽니다. 이 파일에는 프로젝트에 대한 메타 정보와 종속성이 포함되어 있습니다.

## Step 2: 배송 추적 서비스 종속성 설치

배송 추적 서비스를 사용하기 위해 프로젝트에 종속성을 설치해야 합니다. npm을 사용하여 이 작업을 수행할 수 있습니다. 다음 명령을 터미널에서 실행하세요:

```bash
npm install delivery-tracker
```

이 명령은 `delivery-tracker` 모듈을 프로젝트에 설치합니다.

## Step 3: 배송 추적 서비스 설정 추가

package.json 파일을 열어 `"scripts"` 항목을 찾습니다. 해당 항목에 `"track-delivery"`라는 새로운 스크립트를 추가합니다. 스크립트는 배송 추적 서비스를 실행하는 데 사용됩니다.

```json
"scripts": {
  "start": "node index.js",
  "track-delivery": "delivery-tracker track <tracking-number>"
}
```

위 코드에서 `<tracking-number>`는 실제로 사용하는 배송 추적 번호로 바꾸어야 합니다. 이 스크립트를 사용하면 다음과 같이 배송 추적 서비스를 실행할 수 있습니다:

```bash
npm run track-delivery
```

## Step 4: 배송 추적 서비스 실행

이제 배송 추적 서비스를 실행할 준비가 되었습니다. 다음 명령을 터미널에서 실행하세요:

```bash
npm run track-delivery
```

위 명령은 프로젝트에 설치된 `delivery-tracker` 모듈을 사용하여 배송 추적 서비스를 실행합니다. 유효한 추적 번호를 사용하면 해당 배송의 상태를 확인할 수 있습니다.

## 요약

이제 JavaScript 프로젝트에서 배송 추적 서비스를 설정하는 방법을 알았습니다. package.json 파일을 열고 배송 추적 서비스 종속성을 설치한 후, 스크립트를 추가하여 배송 상태를 추적할 수 있습니다. 이를 통해 사용자는 프로젝트에 쉽게 배송 추적 기능을 추가할 수 있습니다.

#### References:
- [npm Documentation](https://docs.npmjs.com/)