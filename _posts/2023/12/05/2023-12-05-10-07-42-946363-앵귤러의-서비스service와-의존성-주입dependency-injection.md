---
layout: post
title: "[javascript] 앵귤러의 서비스(Service)와 의존성 주입(Dependency Injection)"
description: " "
date: 2023-12-05
tags: [javascript]
comments: true
share: true
---

앵귤러(Angular)는 자바스크립트 기반의 프런트엔드 개발 프레임워크로, 컴포넌트 기반 아키텍처를 기반으로 한다. 앵귤러에서는 서비스(Service)와 의존성 주입(Dependency Injection)이라는 개념을 사용하여 코드를 모듈화하고 재사용성을 높일 수 있다.

### 서비스(Service)

서비스는 앵귤러에서 비즈니스 로직이나 데이터를 공유하기 위해 사용되는 객체이다. 주로 HTTP 통신, 데이터 처리, 상태 관리 등의 역할을 수행한다. 앵귤러에서는 서비스를 바로 사용하기 위해 @Injectable() 데코레이터가 필요하다. 이 데코레이터를 사용하면 앵귤러가 서비스의 의존성을 관리해준다.

서비스는 아래와 같이 생성할 수 있다:

```javascript
import { Injectable } from '@angular/core';

@Injectable()
export class DataService {
  getData() {
    // 데이터를 가져오는 로직
  }

  saveData(data) {
    // 데이터를 저장하는 로직
  }
}
```

### 의존성 주입(Dependency Injection)

의존성 주입은 앵귤러에서 서비스를 사용할 때 필요한 다른 객체를 주입하는 개념이다. 의존성 주입을 사용하면 앵귤러가 자동으로 의존하는 객체를 생성하고 주입해준다.

예를 들어, 컴포넌트에서 DataService를 사용하려면 다음과 같이 의존성 주입을 할 수 있다:

```javascript
import { Component } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-my-component',
  template: '<button (click)="getData()">Get Data</button>',
})
export class MyComponent {
  constructor(private dataService: DataService) {}

  getData() {
    const data = this.dataService.getData();
    // 데이터 처리 로직
  }
}
```

위의 코드에서 DataService를 생성자 파라미터로 선언하면 앵귤러가 자동으로 DataService 인스턴스를 생성하고 주입해준다.

### 결론

앵귤러의 서비스와 의존성 주입을 적절하게 사용하면 코드의 모듈화와 재사용성을 높일 수 있다. 서비스를 통해 비즈니스 로직과 데이터 처리를 분리하고 의존성 주입을 통해 필요한 객체를 쉽게 주입받을 수 있다. 이를 통해 개발 효율성을 높이고 유지보수를 용이하게 할 수 있다.

### 참고 자료

- [앵귤러 공식 문서](https://angular.io/guide/architecture-services)
- [앵귤러로 응용 프로그램 개발](https://developer.mozilla.org/ko/docs/Glossary/Angular)
- [Dependency Injection in Angular](https://angular.io/guide/dependency-injection)