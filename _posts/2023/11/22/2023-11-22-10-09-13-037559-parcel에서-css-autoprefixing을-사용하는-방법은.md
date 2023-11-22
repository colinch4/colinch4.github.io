---
layout: post
title: "[javascript] Parcel에서 CSS autoprefixing을 사용하는 방법은?"
description: " "
date: 2023-11-22
tags: [javascript]
comments: true
share: true
---

CSS autoprefixing은 CSS 프로퍼티를 다양한 브라우저 호환성을 위해 자동으로 접두사(prefix)를 붙여주는 작업입니다. 이를 통해 개발자는 수동으로 접두사를 추가할 필요 없이 브라우저 호환성을 유지할 수 있습니다.

Parcel에서 CSS autoprefixing을 사용하기 위해서는 `autoprefixer` 패키지를 설치해야 합니다. 아래는 사용 방법의 예시입니다:

1. 프로젝트 루트 디렉토리에서 다음 명령어를 실행하여 `autoprefixer`를 설치합니다:

```bash
npm install autoprefixer --save-dev
```

2. 이제 CSS 파일에 autoprefixing을 적용하기 위해 `.postcssrc` 또는 `package.json` 파일에 다음과 같이 설정합니다:

```json
{
  "postcss": {
    "plugins": {
      "autoprefixer": {}
    }
  }
}
```

위 설정에서 `plugins` 오브젝트 안에 `autoprefixer`를 추가함으로써 autoprefixing을 활성화할 수 있습니다.

3. 이제 Parcel을 실행하면 CSS 파일에 자동으로 autoprefixing이 적용됩니다.

위의 예시에서 `autoprefixer`는 프로젝트의 `package.json`에 설치되기 때문에 `npm run`을 사용하여 Parcel을 실행하면 됩니다. 프로젝트에 다른 CSS 전처리기를 사용하고 있다면, 해당 전처리기와 함께 `autoprefixer` 플러그인을 설정해야 할 수도 있습니다.

자세한 내용은 [Parcel 공식 문서](https://parceljs.org/css.html#postcss)에서 확인할 수 있습니다.