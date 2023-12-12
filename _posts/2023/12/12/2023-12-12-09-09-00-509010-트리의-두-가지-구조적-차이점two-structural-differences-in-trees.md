---
layout: post
title: "[c++] 트리의 두 가지 구조적 차이점(Two Structural Differences in Trees)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

트리(Tree)는 자료 구조에서 중요한 역할을 하는데, 이는 다양한 종류가 있고 각각의 특성이 다릅니다. 여기에서는 트리의 두 가지 구조적 차이점에 대해 알아보겠습니다.

### 1. 이진 트리(Binary Tree)와 이진 탐색 트리(Binary Search Tree)의 차이점

**이진 트리(Binary Tree)**는 각각의 노드가 최대 두 개의 자식 노드를 가지는 트리를 말합니다. 이진 트리는 좌우에 대한 정렬이 없으며, 각 노드가 0개, 1개 또는 2개의 자식 노드를 가질 수 있습니다.

반면에 **이진 탐색 트리(Binary Search Tree)**는 다음과 같은 성질을 만족합니다.
- 모든 왼쪽 서브트리 노드의 값은 부모 노드의 값보다 작습니다.
- 모든 오른쪽 서브트리 노드의 값은 부모 노드의 값보다 큽니다.
- 왼쪽과 오른쪽 서브트리도 이진 탐색 트리여야 합니다.

이 두 가지 구조 간의 주요 차이점은 *정렬*에 있습니다. 이진 탐색 트리는 데이터를 효율적으로 탐색할 수 있도록 정렬된 형태를 유지하는 반면, 일반 이진 트리는 그러지 않습니다.

### 2. 높이 균형 트리와 불균형 트리의 차이점

**높이 균형 트리(Balanced Tree)**는 모든 리프 노드의 깊이 차이가 1 이하인 트리를 말합니다. 이에 반해 **불균형 트리(Unbalanced Tree)**는 한쪽으로 치우쳐 있는 경우나 높이 차이가 큰 경우를 말합니다.

높이 균형 트리는 트리의 높이를 최소화하여 검색, 삽입, 삭제와 같은 연산을 효율적으로 수행할 수 있도록 돕습니다. 반면 불균형 트리는 연산의 성능이 떨어지는 경우가 많습니다.

트리의 구조적 차이점을 이해하면, 각 트리의 특징과 이에 따른 적절한 활용이 가능해집니다.

이러한 트리의 구조적 차이점을 직관적으로 이해하는 것은 자료 구조를 공부하는 데 매우 중요합니다.

### 참고 자료
- [GeeksforGeeks - Binary Tree](https://www.geeksforgeeks.org/binary-tree-data-structure/)
- [GeeksforGeeks - Binary Search Tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
- [GeeksforGeeks - Balanced Tree](https://www.geeksforgeeks.org/b-trees-introduction/)
- [GeeksforGeeks - Unbalanced Tree](https://www.geeksforgeeks.org/deletion-binary-tree/)