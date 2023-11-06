---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 캐시 패키지 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

JavaScript 프로젝트를 개발하는 동안, 종속성 패키지의 버전이나 업데이트가 변경될 수 있습니다. 이로 인해 필요한 패키지를 다시 설치하고 캐시를 지우는 작업을 해야할 수도 있습니다. 이런 작업은 시간이 많이 소요되고 번거로울 수 있습니다.

이 문제를 해결하기 위해, Package.json 파일에서 캐시 패키지 설정을 할 수 있습니다. 이를 통해 패키지를 다시 설치하는 대신 캐시된 패키지를 사용하여 바로 사용할 수 있습니다.

캐시 패키지 설정을 위해서는 Package.json 파일에서 "dependencies" 및 "devDependencies" 필드에 "_resolved" 키를 추가해야 합니다. 이 키는 패키지의 캐시된 버전을 지정합니다. 

아래는 Package.json에서 캐시 패키지 설정 예시입니다:

```json
{
  "dependencies": {
    "express": {
      "_resolved": "https://registry.npmjs.org/express/-/express-4.17.1.tgz"
    },
    "axios": {
      "_resolved": "https://registry.npmjs.org/axios/-/axios-0.21.1.tgz"
    }
  },
  "devDependencies": {
    "jest": {
      "_resolved": "https://registry.npmjs.org/jest/-/jest-27.2.5.tgz"
    },
    "eslint": {
      "_resolved": "https://registry.npmjs.org/eslint/-/eslint-7.32.0.tgz"
    }
  }
}
```

패키지의 "_resolved" 값을 해당 패키지의 정확한 버전을 가리키는 URL로 설정합니다. 이렇게 하면 패키지 매니저가 패키지를 다시 설치하는 대신 캐시된 패키지를 사용하여 프로젝트를 빌드하거나 실행할 수 있습니다.

이제 Package.json 파일에 캐시 패키지 설정을 추가하여 프로젝트 개발을 보다 효율적으로 진행할 수 있습니다.

### 참고 문서
- [NPM Documentation](https://docs.npmjs.com/files/package.json)
- [Yarn Documentation](https://classic.yarnpkg.com/lang/en/docs/package-json/)