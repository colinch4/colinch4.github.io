---
layout: post
title: "[flutter] 플러터(Flutter) 개발에서 상태 관리를 위해 MobX를 사용하면 왜 라이브러리(Flutter Hooks)를 함께 사용하나요?"
description: " "
date: 2023-12-04
tags: [flutter]
comments: true
share: true
---

[링크1](https://mobx.netlify.app/faq/#how-do-i-work-with-reactive-widget-frameworks-like-flutter)
[링크2](https://pub.dev/packages/flutter_hooks) 

플러터(Flutter) 개발에서 MobX는 상태 관리를 위한 강력한 라이브러리입니다. MobX는 반응형 프로그래밍의 개념을 플러터 앱에 적용하여 효율적인 상태 관리를 가능하게 합니다. 

하지만 MobX만으로 상태 관리를 할 수 있지만, 함께 라이브러리(Flutter Hooks)를 사용하는 것이 여러 이점을 가집니다. 

1. 코드 간결화: Flutter Hooks는 MobX와 함께 사용되면 상태 업데이트 로직을 더 간결하게 작성할 수 있습니다. Hook을 사용하면 일반적인 상태 업데이트 로직을 다른 컴포넌트와 분리하여 재사용할 수 있습니다.

2. 편리한 상태 관리: MobX는 상태 변경을 감지하여 자동으로 업데이트합니다. 그러나 플러터(Flutter) 개발에서는 많은 비즈니스 로직을 수행하는 위젯이 존재하는 경우가 많습니다. Flutter Hooks는 이러한 경우에 상태 변경을 더욱 편리하게 처리할 수 있습니다.  

3. 성능 개선: MobX는 효율적인 상태 관리를 위해 내부적으로 옵저버 패턴을 사용합니다. 그러나 MobX의 변화를 감지하기 위해서는 리액트(React)와 같은 반응형 라이브러리가 필요합니다. Flutter Hooks는 이 역할을 수행하여 MobX와 함께 사용할 때 성능을 최적화할 수 있습니다.

따라서 플러터(Flutter) 개발에서 상태 관리를 위해 MobX를 사용하는 경우, Flutter Hooks와 함께 사용하면 코드의 간결성과 편리성, 그리고 성능 개선을 도모할 수 있습니다.