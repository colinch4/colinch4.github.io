---
layout: post
title: "[javascript] Prettier를 사용하여 코드 작성 시 일관적인 optional chaining 사용 방식을 유지하는 방법은 무엇인가?"
description: " "
date: 2023-12-26
tags: [javascript]
comments: true
share: true
---

먼저, `package.json` 파일 또는 별도의 Prettier 설정 파일을 만듭니다. 그리고 아래의 설정을 추가합니다.

```json
{
  "name": "your-project",
  "version": "1.0.0",
  "prettier": {
    "semi": false,
    "singleQuote": true,
    "overrides": [
      {
        "files": "*.js",
        "options": {
          "parser": "babel",
          "semi": true,
          "printWidth": 100,
          "proseWrap": "always",
          "plugins": ["prettier-plugin-optional-chaining"]
        }
      }
    ]
  }
}
```

위의 예시에서 `prettier-plugin-optional-chaining`은 optional chaining을 지원하는 Prettier 플러그인을 사용하는 것을 보여줍니다. 이와 함께 `overrides`를 활용하여 .js 파일에 대한 설정을 따로 지정할 수 있습니다.

이러한 Prettier 설정을 통해 코드 작성 시 일관적인 optional chaining 사용을 유지할 수 있습니다.