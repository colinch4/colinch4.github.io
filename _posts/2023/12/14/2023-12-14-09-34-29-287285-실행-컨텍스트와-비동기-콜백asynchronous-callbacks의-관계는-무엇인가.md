---
layout: post
title: "[javascript] 실행 컨텍스트와 비동기 콜백(asynchronous callbacks)의 관계는 무엇인가?"
description: " "
date: 2023-12-14
tags: [javascript]
comments: true
share: true
---

비동기 함수는 실행 컨텍스트가 생성된 후에나 실행되기 때문에, 비동기 콜백 함수는 자체적인 실행 컨텍스트를 갖게 됩니다. 이때 비동기 함수의 실행 컨텍스트는 해당 함수가 호출된 시점에서의 환경을 포함하게 됩니다. 따라서 비동기 콜백 함수는 자신만의 실행 컨텍스트를 가지며, 이를 통해 비동기 처리와 관련된 작업을 안전하게 수행할 수 있습니다.