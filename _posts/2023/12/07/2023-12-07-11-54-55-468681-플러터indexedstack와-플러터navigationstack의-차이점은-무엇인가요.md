---
layout: post
title: "[flutter] 플러터(IndexedStack)와 플러터(NavigationStack)의 차이점은 무엇인가요?"
description: " "
date: 2023-12-07
tags: [flutter]
comments: true
share: true
---

플러터(IndexedStack)는 여러 위젯을 중첩하여 화면에 보여줄 때 사용됩니다. 이 위젯은 인덱스를 사용하여 현재 보여줄 위젯을 선택하고 화면에 표시합니다. 인덱스가 바뀔 때마다 이전에 보여지던 위젯은 숨겨지고 새로운 위젯이 나타납니다. 이러한 동작 방식으로 인해 IndexedStack은 여러 위젯 중 하나의 위젯만 화면에 보여주는데 사용됩니다. 예를 들어 화면에 다른 상태를 나타내는 여러 위젯을 중첩하여 보여줘야 하는 경우 IndexedStack을 사용할 수 있습니다.

플러터(NavigationStack)는 화면 간의 이동을 관리하기 위해 사용됩니다. 이 위젯은 여러 화면(라우트)을 스택으로 관리하며, 화면 간의 전환을 쉽게 할 수 있습니다. 일반적으로 앱의 네비게이션 구조를 관리하고 사용자의 상호작용에 따라 화면을 변경하는 데 사용됩니다. 예를 들어, 앱에서 화면 간에 이동할 때 플러터(NavigationStack)을 사용하여 스택에 새로운 화면을 추가하고, 뒤로가기 버튼을 누르면 스택에서 이전 화면을 꺼내와서 보여줄 수 있습니다.

플러터(IndexedStack)은 여러 위젯 중에서 하나의 위젯을 보여주는 데 사용되고, 플러터(NavigationStack)은 화면 간의 이동을 관리하는 데 사용됩니다. 즉, IndexedStack은 다양한 상태 관리에 사용되며, NavigationStack은 앱의 네비게이션 구조를 관리하는 데 사용됩니다.