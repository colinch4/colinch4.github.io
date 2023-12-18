---
layout: post
title: "[typescript] 유니온 타입과 해체 할당(Destructuring Assignment)의 관계는 무엇인가요?"
description: " "
date: 2023-12-19
tags: [typescript]
comments: true
share: true
---

해체 할당은 객체나 배열을 비구조화하여 여러 개의 변수에 할당하는 과정을 말합니다. 유니온 타입과 함께 사용할 때, 변수에 할당된 값의 타입을 정확히 알 수 없는 상황에서도 사용될 수 있습니다.

예를 들어, 다음과 같이 유니온 타입과 해체 할당이 함께 사용될 수 있습니다.

```typescript
type ResultType = { success: boolean } | { error: string };

function processResult(result: ResultType) {
    if ('success' in result) {
        const { success } = result; // 해체 할당을 통해 success만을 추출하여 사용
        console.log('Success:', success);
    } else {
        const { error } = result; // 해체 할당을 통해 error만을 추출하여 사용
        console.log('Error:', error);
    }
}

const successResult: ResultType = { success: true };
const errorResult: ResultType = { error: 'Something went wrong' };

processResult(successResult);
processResult(errorResult);
```

위 예제에서 `ResultType`은 `success` 또는 `error` 프로퍼티 중 하나를 갖는 오브젝트 타입입니다. `processResult` 함수는 이 두 가지 타입을 받아서, 어떤 타입을 받았는지에 따라 처리하는 예시입니다. 각 타입에 맞게 실제 처리를 하기 위해 해체 할당을 사용하여 객체를 쉽게 다룰 수 있습니다.

이처럼 유니온 타입과 해체 할당은 TypeScript에서 변수의 타입이 고정되지 않거나, 여러 가지 타입을 다뤄야 하는 상황에서 유용하게 활용될 수 있습니다.