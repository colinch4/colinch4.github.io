---
layout: post
title: "[javascript] BehaviorSubject와 ReplaySubject의 차이는?"
description: " "
date: 2023-11-21
tags: [javascript]
comments: true
share: true
---

1. BehaviorSubject: BehaviorSubject는 현재 값과 함께 초기화됩니다. 구독(subscribe) 시점에서 가장 최신 값을 받습니다. 중요한 점은 BehaviorSubject는 새로운 값을 받는 것뿐만 아니라 이전 값들도 저장합니다. 따라서 새로운 구독자(subscriber)에게 최신 값을 즉시 전달할 수 있습니다. BehaviorSubject는 현재 상태 관리에 유용한 도구입니다.

   예시 코드:

   ```javascript
   import { BehaviorSubject } from 'rxjs';

   const subject = new BehaviorSubject('Initial value');

   subject.subscribe(value => console.log(value)); // 'Initial value' 출력

   subject.next('New value'); // 'New value' 출력

   subject.subscribe(value => console.log(value)); // 'New value' 출력
   ```

2. ReplaySubject: ReplaySubject는 구독 시점에 이전에 발생한 모든 값을 전달합니다. ReplaySubject의 생성자에 전달하는 인자로 버퍼 크기를 지정할 수 있습니다. 버퍼 크기를 지정하지 않으면 모든 값을 저장하며, 지정한 크기보다 작은 수의 값만 저장합니다.

   예시 코드:

   ```javascript
   import { ReplaySubject } from 'rxjs';

   const subject = new ReplaySubject(2); // 마지막 2개의 값만 저장하는 ReplaySubject

   subject.next('Value 1');
   subject.next('Value 2');
   subject.next('Value 3');

   subject.subscribe(value => console.log(value)); // 'Value 2', 'Value 3' 출력
   ```

BehaviorSubject와 ReplaySubject는 서로 다른 용도와 동작을 가지고 있습니다. BehaviorSubject는 현재 상태 관리에 적합하며, ReplaySubject는 이전 값들에 대한 접근이 필요한 경우 유용합니다. 이에 맞춰 사용 시에 적합한 서브젝트를 선택하여 활용하시면 됩니다.

참조: 
- RxJS BehaviorSubject 문서: https://rxjs.dev/api/index/class/BehaviorSubject
- RxJS ReplaySubject 문서: https://rxjs.dev/api/index/class/ReplaySubject