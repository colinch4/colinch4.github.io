---
layout: post
title: "[flutter] 플러터(Flutter)에서 상태 관리를 위해 Redux와 Redux Saga 중 어떤 것을 선택하는 것이 좋나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

Redux와 Redux Saga는 모두 상태 관리를 위한 효과적인 도구들입니다. 하지만 각각의 특징과 장단점을 고려하여 선택해야합니다.

Redux는 단방향 데이터 흐름 아키텍처를 제공하여 상태 변화를 예측 가능하고 관리하기 쉽게 만듭니다. 액션(Action)을 통해 상태를 변경하고, 리듀서(Reducer)를 통해 상태를 업데이트합니다. 이렇게 하면 애플리케이션의 상태를 일관성 있게 관리할 수 있습니다. Redux는 플러터의 Provider와 같은 다른 상태 관리 도구와 함께 사용할 수도 있습니다.

반면 Redux Saga는 Redux의 미들웨어로 애플리케이션의 비동기 로직을 관리하는 데 도움을 줍니다. Redux Saga는 제네레이터(Generator) 함수를 사용하여 비동기 작업을 처리하며, 액션을 모니터링하고 필요한 시점에 액션을 디스패치하여 상태를 업데이트합니다. 이를 통해 비동기 작업과 관련된 복잡성을 상태 관리 로직 밖으로 분리하여 코드를 더 깔끔하고 테스트하기 쉽게 만들 수 있습니다.

따라서 Redux를 선택하면 상태 관리에 더 집중할 수 있고, Redux Saga를 선택하면 비동기 작업을 효율적으로 관리할 수 있습니다. 어떤 도구를 선택할지는 프로젝트의 요구 사항과 팀의 선호도에 따라 다를 수 있으므로, 상황에 맞게 선택하는 것이 좋습니다.

참고 자료:
- Redux 공식 문서: https://redux.js.org/
- Redux Saga 공식 문서: https://redux-saga.js.org/