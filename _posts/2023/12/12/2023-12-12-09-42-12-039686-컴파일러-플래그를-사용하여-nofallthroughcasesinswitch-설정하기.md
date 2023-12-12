---
layout: post
title: "[typescript] 컴파일러 플래그를 사용하여 noFallthroughCasesInSwitch 설정하기"
description: " "
date: 2023-12-12
tags: [typescript]
comments: true
share: true
---

이제 어떻게 `noFallthroughCasesInSwitch` 플래그를 사용하는지 자세히 알아보겠습니다.

1. **tsconfig.json 파일 수정**
   
   먼저, 프로젝트의 루트 디렉토리에 있는 `tsconfig.json` 파일을 엽니다.

2. **플래그 추가**

   다음과 같이 `compilerOptions` 섹션에 `noFallthroughCasesInSwitch` 플래그를 추가합니다.

   ```json
   {
     "compilerOptions": {
       "noFallthroughCasesInSwitch": true
     }
   }
   ```

   이제 TypeScript 컴파일러는 switch 문에서의 각 case가 명시적으로 종료되지 않을 경우 경고를 표시합니다.

이제 `noFallthroughCasesInSwitch` 플래그를 사용하여 TypeScript의 switch 문에서의 코드 품질을 더욱 향상시킬 수 있습니다.

자세한 내용은 [TypeScript 공식 문서](https://www.typescriptlang.org/tsconfig#noFallthroughCasesInSwitch)를 참조하세요.