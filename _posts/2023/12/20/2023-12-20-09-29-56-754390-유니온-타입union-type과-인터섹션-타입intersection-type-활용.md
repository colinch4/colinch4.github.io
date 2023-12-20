---
layout: post
title: "[typescript] 유니온 타입(union type)과 인터섹션 타입(intersection type) 활용"
description: " "
date: 2023-12-20
tags: [typescript]
comments: true
share: true
---

TypeScript는 JavaScript에 정적 타입을 추가한 언어로, 코드의 안정성을 높이고 실수를 줄일 수 있습니다. 이번 글에서는 유니온 타입과 인터섹션 타입을 사용하여 TypeScript 코드를 작성하는 방법에 대해 알아보겠습니다.

## 유니온 타입(Union Types)

유니온 타입은 파이프(|)를 사용하여 두 개 이상의 타입을 허용하는 방법입니다. 이를 통해 변수가 여러 타입을 가질 수 있도록 지정할 수 있습니다.

```typescript
function displayEmployeeId(employeeId: string | number) {
    console.log(employeeId);
}

displayEmployeeId("E123"); // string
displayEmployeeId(456); // number
```

위 예제에서 `displayEmployeeId` 함수는 `string` 또는 `number` 타입을 매개변수로 받을 수 있습니다. 이를 통해 코드의 유연성을 높일 수 있습니다.

## 인터섹션 타입(Intersection Types)

인터섹션 타입은 앰퍼샌드(&)를 사용하여 두 개 이상의 타입을 결합하는 방법입니다. 이를 통해 두 개 이상의 타입을 가진 새로운 타입을 생성할 수 있습니다.

```typescript
interface Employee {
    empId: string;
    empName: string;
}

interface Department {
    deptId: string;
    deptName: string;
}

type EmployeeWithDepartment = Employee & Department;

const emp: EmployeeWithDepartment = {
    empId: "E123",
    empName: "John Doe",
    deptId: "D001",
    deptName: "Engineering"
};
```

위 예제에서 `EmployeeWithDepartment` 타입은 `Employee`와 `Department` 인터페이스의 속성을 모두 가지고 있습니다.

## 결론

유니온 타입과 인터섹션 타입은 TypeScript에서 코드를 작성할 때 유용하게 활용할 수 있는 기능입니다. 유니온 타입은 여러 타입을 허용함으로써 유연성을 높이고, 인터섹션 타입은 여러 타입을 결합하여 새로운 타입을 생성할 수 있습니다.

이를 통해 코드의 가독성과 안정성을 높일 수 있으며, JavaScript 개발을 보다 안정적이고 효율적으로 할 수 있습니다.

참고 문헌:
- [TypeScript 공식 문서](https://www.typescriptlang.org/docs/)
- [TypeScript 핸드북](https://typescript-kr.github.io/)

이상으로 TypeScript의 유니온 타입과 인터섹션 타입에 대해 알아보았습니다. 감사합니다.