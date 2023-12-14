---
layout: post
title: "[javascript] 실행 컨텍스트와 비동기 처리(Asynchronous processing)의 관계는 무엇인가?"
description: " "
date: 2023-12-14
tags: [javascript]
comments: true
share: true
---

비동기 처리는 JavaScript에서 일어나는 일을 순차적으로 처리하지 않고, 코드의 실행을 멈추지 않고 다른 작업을 수행할 수 있게 하는 메커니즘입니다. 주로 콜백 함수, 프로미스, async/await 등을 사용하여 구현됩니다.

이 두 가지 개념은 밀접한 관계가 있습니다. 비동기 처리를 하는 동안에도 실행 컨텍스트는 계속해서 스택에 쌓이고 실행되며, 이로 인해 비동기 작업의 콜백 함수나 결과를 기다리는 동안에도 다른 코드들이 실행됩니다. 따라서 실행 컨텍스트는 비동기 처리와 함께 작동하여 JavaScript가 비동기 작업을 처리할 수 있게 합니다.