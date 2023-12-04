---
layout: post
title: "[javascript] Jasmine을 사용하여 TDD(Test-driven development)를 적용하는 방법"
description: " "
date: 2023-12-04
tags: [javascript]
comments: true
share: true
---

## 개요
Test-driven development (TDD)는 개발 프로세스에서 테스트를 작성하고 실행함으로써 코드 품질을 향상시키는 방법론입니다. 이를 도와주는 도구 중 하나가 Jasmine입니다. 이번 기사에서는 Jasmine을 사용하여 TDD를 적용하는 방법에 대해 알아보겠습니다.

## Jasmine 소개
Jasmine은 자바스크립트에서 사용 가능한 오픈 소스 테스트 프레임워크입니다. Jasmine은 테스트 스펙을 작성하고 실행할 수 있으며, 테스트 결과를 확인할 수 있습니다.

## Jasmine 설치 및 설정
Jasmine을 사용하기 위해서는 먼저 Jasmine을 다운로드하고 설정해야 합니다. 다음은 Jasmine을 설치하는 방법입니다.

1. Jasmine을 다운로드합니다. [Jasmine 다운로드 링크](https://github.com/jasmine/jasmine/releases)에서 최신 버전을 내려받으세요.
2. 다운로드한 Jasmine을 프로젝트 폴더에 압축 해제합니다.
3. `SpecRunner.html` 파일을 생성합니다. 이 파일에서 테스트 결과를 확인할 수 있습니다.

## Jasmine 테스트 스펙 작성하기
Jasmine에서는 `describe`와 `it` 함수를 사용하여 테스트 스펙을 작성합니다. `describe` 함수는 특정 작업의 컨텍스트를 정의하고, `it` 함수는 작업 단위의 테스트 스펙을 정의합니다.

다음은 간단한 예제를 통해 Jasmine 테스트 스펙을 작성하는 방법을 보여줍니다.

```javascript
// Calculator.js
class Calculator {
  add(a, b) {
    return a + b;
  }

  subtract(a, b) {
    return a - b;
  }
}

// CalculatorSpec.js
describe('Calculator', function() {
  let calculator;

  beforeEach(function() {
    calculator = new Calculator();
  });

  it('should add two numbers correctly', function() {
    expect(calculator.add(2, 3)).toEqual(5);
  });

  it('should subtract two numbers correctly', function() {
    expect(calculator.subtract(5, 2)).toEqual(3);
  });
});
```

위의 예제에서 `Calculator.js`는 `Calculator` 클래스를 정의하고 있습니다. `CalculatorSpec.js`는 `Calculator` 클래스를 테스트하는 스펙을 작성한 것입니다. `describe` 함수를 사용하여 `Calculator`에 대한 컨텍스트를 정의하고, `it` 함수를 사용하여 각각의 테스트 스펙을 정의했습니다.

## Jasmine 실행하기
Jasmine 테스트를 실행하기 위해서는 `SpecRunner.html` 파일을 브라우저에서 열어야 합니다. `SpecRunner.html` 파일은 Jasmine 설정과 테스트 스펙을 로드하고, 테스트 결과를 HTML로 표시하는 역할을 합니다.

`SpecRunner.html` 파일을 브라우저에서 열면 Jasmine은 설정된 테스트 스펙을 실행하고, 테스트 결과를 보여줍니다. 통과한 테스트는 초록색으로 표시되고, 실패한 테스트는 빨간색으로 표시됩니다.

## 결론
Jasmine을 사용하여 TDD를 적용하는 방법에 대해 알아보았습니다. TDD를 사용하면 개발 프로세스에서 테스트를 먼저 작성하고 실행함으로써 코드 품질을 향상시킬 수 있습니다. Jasmine은 테스트 스펙 작성과 실행, 결과 확인을 도와주는 유용한 도구입니다.

더 자세한 정보와 Jasmine의 다양한 기능을 알아보려면 [Jasmine 공식 문서](https://jasmine.github.io/)를 참고하시기 바랍니다.