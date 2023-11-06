---
layout: post
title: "Package.json에서 JavaScript 프로젝트의 소스 맵 설정하기"
description: " "
date: 2023-11-06
tags: []
comments: true
share: true
---

소스 맵(Source Maps)은 JavaScript 코드에서 디버깅을 용이하게 하기 위해 사용되는 파일입니다. 이 파일은 웹 브라우저가 압축되거나 난독화된 JavaScript 파일을 원래의 소스 코드와 매핑할 수 있도록 도와줍니다. 이를 통해 디버그 모드에서도 원본 소스 코드로 디버깅할 수 있습니다.

Package.json 파일에서 JavaScript 프로젝트의 소스 맵을 설정하는 방법을 알아보겠습니다. 다음은 기본적인 설정 방법입니다.

1. Package.json 파일을 엽니다.

2. `"scripts"` 속성을 찾습니다. 이 속성은 프로젝트에 대한 스크립트 명령어를 정의하는 객체입니다.

3. `"scripts"` 객체에 `"dev"` 또는 `"start"`와 같은 사용자 정의 스크립트를 추가합니다. 이 스크립트는 개발 모드에서 프로젝트를 실행할 때 사용될 것입니다.

예시:
```json
"scripts": {
  "dev": "webpack --mode development --devtool eval-source-map",
  "start": "node server.js"
}
```

위의 예시에서 `"dev"` 스크립트는 Webpack을 사용하여 개발 모드로 프로젝트를 빌드하고, 소스 맵을 생성하도록 설정되어 있습니다. `--devtool eval-source-map` 옵션은 소스 맵을 생성하는 방법을 나타내는데, 여기서는 `eval-source-map`을 사용하였습니다.

4. 프로젝트를 개발 모드로 실행하려면 명령어를 실행합니다. 예를 들어, 위의 Package.json에서 `"dev"` 스크립트를 실행하기 위해 다음 명령어를 실행합니다.
```shell
npm run dev
```

5. 개발 모드로 프로젝트가 실행되면 소스 맵 파일(`.map` 확장자를 가진 파일)이 생성됩니다. 이 파일은 JavaScript 코드와 소스 코드 간의 매핑 정보를 담고 있습니다.

이제 Package.json에서 JavaScript 프로젝트의 소스 맵을 설정하는 방법을 알게 되었습니다. 소스 맵을 설정하면 디버깅 과정에서 원래의 소스 코드로 디버깅할 수 있어 개발 과정을 더욱 효과적으로 할 수 있습니다.

**참고 자료:**

- [웹팩(Webpack) 공식 문서](https://webpack.js.org/configuration/devtool/)
- [소스 맵에 관한 개념 설명 (Mozilla 개발자 네트워크 문서)](https://developer.mozilla.org/en-US/docs/Tools/Debugger/How_to/Use_a_source_map)