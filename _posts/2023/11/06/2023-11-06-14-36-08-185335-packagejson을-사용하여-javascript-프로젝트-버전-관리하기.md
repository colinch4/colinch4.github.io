---
layout: post
title: "Package.json을 사용하여 JavaScript 프로젝트 버전 관리하기"
description: " "
date: 2023-11-06
tags: [JavaScript]
comments: true
share: true
---

## 소개

JavaScript 프로젝트를 개발하다보면 코드의 변경사항을 추적하고 프로젝트 버전을 효과적으로 관리해야하는 경우가 많습니다. 이를 위해 우리는 `package.json` 파일을 사용할 수 있습니다. `package.json`은 프로젝트의 의존성 모듈 정보뿐만 아니라 버전 정보, 작성자, 라이선스 등의 메타데이터를 포함할 수 있는 파일입니다.

## package.json 파일 생성하기

`package.json` 파일을 생성하려면 프로젝트 루트 디렉토리에서 다음 명령을 실행합니다:

```shell
npm init
```

이 명령은 단계별로 프로젝트 정보를 입력하도록 안내합니다. 프로젝트 이름, 버전, 설명, 저장소 URL 등을 입력할 수 있습니다. 모든 정보를 입력한 후 `package.json` 파일이 생성됩니다.

## 프로젝트 버전 지정하기

프로젝트 버전을 관리하기 위해서는 `package.json` 파일의 `version` 항목을 업데이트해야 합니다. 버전은 [시맨틱 버전](https://semver.org/lang/ko/) 형식에 맞게 지정하는 것이 좋습니다. 버전은 일반적으로 `Major.Minor.Patch` 형식으로 표현되며, 각 세그먼트는 숫자로 구성됩니다.

예를 들어, 버전이 `1.0.0`인 프로젝트의 첫 번째 버전을 출시한다면 버전을 `2.0.0`으로 업데이트할 수 있습니다. 코드에 큰 변경이 있다면 `Major` 버전을 업데이트하고, 새로운 기능이 추가되거나 버그가 수정되면 `Minor` 버전을 업데이트합니다. 버그 수정이나 작은 변경 사항들을 포함하는 경우에는 `Patch` 버전을 업데이트합니다.

버전을 변경하려면 `package.json` 파일의 `version` 항목을 직접 수정하면 됩니다.

## 버전 관리 도구

프로젝트 버전을 관리하는 것은 중요하지만, 수동으로 버전을 업데이트하는 것은 번거로울 수 있습니다. 이를 해결하기 위해 자동으로 버전을 관리해주는 여러 도구들이 있습니다. 대표적인 도구로는 [npm version](https://docs.npmjs.com/cli/version.html), [semantic-release](https://semantic-release.gitbook.io/semantic-release/) 등이 있습니다. 이러한 도구들은 Git 커밋 메시지를 분석하여 자동으로 적절한 버전을 지정하고, Git 태그를 생성하여 버전을 관리해줍니다.

## 결론

`package.json` 파일을 사용하여 JavaScript 프로젝트의 버전을 관리하는 방법에 대해 알아보았습니다. `package.json`을 활용하여 프로젝트의 메타데이터와 버전을 관리하면 코드의 변경사항을 추적하고 프로젝트를 손쉽게 관리할 수 있습니다. 만약 자동으로 버전을 관리하고 싶다면, 버전 관리 도구를 활용하는 것을 고려해보세요.

*이 기사는 #JavaScript #버전관리를 다루고 있습니다.*