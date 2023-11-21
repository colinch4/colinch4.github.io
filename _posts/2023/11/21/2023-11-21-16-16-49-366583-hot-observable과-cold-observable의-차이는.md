---
layout: post
title: "[javascript] Hot Observable과 Cold Observable의 차이는?"
description: " "
date: 2023-11-21
tags: [javascript]
comments: true
share: true
---

Hot Observable과 Cold Observable은 RxJS(Reactive Extensions for JavaScript)에서 사용되는 용어로, 두 가지 다른 종류의 옵저버블을 나타냅니다.

Hot Observable은 생성 시점과 상관없이 데이터를 방출하는 옵저버블입니다. 여러 개의 구독자가 하나의 Hot Observable을 동시에 구독할 수 있으며, 이미 생성된 데이터 스트림을 각각의 구독자들에게 전달합니다. 즉, Hot Observable은 데이터의 생산과 구독이 분리된 상태입니다. 주로 이벤트 스트림이나 센서 데이터와 같이 실시간으로 변화하는 데이터를 다룰 때 사용됩니다.

Cold Observable은 각각의 구독 시점에 데이터를 방출하는 옵저버블입니다. 구독자가 구독을 요청할 때마다 새로운 데이터 스트림을 생성하고, 이어서 그 데이터를 전달합니다. 따라서 Cold Observable은 구독 시점에 데이터의 생산이 시작되며, 각각의 구독자에게 독립된 데이터 스트림을 제공합니다. Cold Observable은 보통 정적인 데이터나 한 번에 계산 가능한 작업을 다룰 때 사용됩니다.

Hot Observable과 Cold Observable의 가장 큰 차이점은 데이터 생산과 구독의 관계입니다. Hot Observable은 데이터를 먼저 생성하고 여러 구독자에게 전달하는 반면, Cold Observable은 구독 시점에 데이터를 생성하고 개별적으로 전달합니다.

참고 자료:
- RxJS 공식 문서: [https://rxjs.dev/guide/overview](https://rxjs.dev/guide/overview)