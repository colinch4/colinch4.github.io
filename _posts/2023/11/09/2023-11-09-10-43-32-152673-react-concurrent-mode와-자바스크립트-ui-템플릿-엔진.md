---
layout: post
title: "React Concurrent Mode와 자바스크립트 UI 템플릿 엔진"
description: " "
date: 2023-11-09
tags: []
comments: true
share: true
---

React Concurrent Mode는 React의 최신 기능 중 하나로, UI의 동시성을 향상시키는 것을 목표로 합니다. 이 모드는 UI를 더 적절하게 분할하여 작업을 수행하고, 응답성을 향상시키며, 사용자 경험을 향상시킬 수 있습니다.

# Concurrent Mode의 장점

Concurrent Mode는 여러 가지 장점을 가지고 있습니다.

1. 응답성 향상: Concurrent Mode는 프레임 우선 스케줄링을 통해 네트워크 요청, 계산 집약적인 작업 등과 같은 비동기 작업과 UI 업데이트를 동시에 처리할 수 있습니다. 이는 사용자가 앱이 응답하지 않는다고 느끼는 현상을 줄여줍니다.

2. 사용자 경험 개선: Concurrent Mode는 우선순위를 기반으로 작업을 세분화할 수 있으므로, 사용자가 중요한 작업에 먼저 응답을 받을 수 있습니다. 예를 들어, 느린 네트워크 연결하에서도 필수적인 컨텐츠가 먼저 나타나는 것을 보장할 수 있습니다.

3. 자원 효율성: Concurrent Mode는 작업의 우선순위 설정을 통해 자원 사용을 최적화할 수 있습니다. 자원을 효율적으로 사용하면서도 사용자 경험을 향상시킬 수 있습니다.

# 자바스크립트 UI 템플릿 엔진

자바스크립트 UI 템플릿 엔진은 웹 페이지나 애플리케이션의 동적으로 생성된 UI 컴포넌트를 생성하기 위한 도구입니다. 자바스크립트로 작성된 템플릿을 사용하여 간단하고 효율적으로 UI를 만들 수 있습니다.

대표적으로 React에서는 JSX라는 자바스크립트 확장 문법을 사용하여 UI를 작성합니다. JSX는 XML과 유사한 문법을 가지고 있어, 개발자가 직관적으로 UI를 작성할 수 있게 해줍니다.

React Concurrent Mode와 자바스크립트 UI 템플릿 엔진은 함께 사용하여 더 나은 사용자 경험을 제공할 수 있습니다. Concurrent Mode는 빠르고 반응성 있는 UI를 만들 수 있게 해주고, UI 템플릿 엔진은 간편한 UI 작성을 가능하게 해줍니다.

# 결론

React Concurrent Mode와 자바스크립트 UI 템플릿 엔진은 모두 개발자가 더 나은 사용자 경험을 제공할 수 있도록 돕는 첨단 기술입니다. Concurrent Mode는 UI의 동시성을 향상시켜 앱의 응답성을 향상시키고, UI 템플릿 엔진은 간단하고 효율적인 UI 작성을 가능하게 해줍니다.

중요한 차이점에 대해 디테일한 정보를 알고 싶다면 공식 React 문서[^1]를 참조해주세요.

[#react](react) [#ui-templating](ui-templating)

[^1]: https://reactjs.org/docs/concurrent-mode-intro.html