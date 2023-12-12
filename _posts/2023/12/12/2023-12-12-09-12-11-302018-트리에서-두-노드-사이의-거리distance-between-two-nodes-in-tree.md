---
layout: post
title: "[c++] 트리에서 두 노드 사이의 거리(Distance Between Two Nodes in Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이번에는 **트리** 자료 구조에서 두 노드 사이의 거리를 구하는 방법에 대해 알아보겠습니다.

## 트리에서 두 노드 사이의 거리

트리에서 두 노드 사이의 거리란 두 노드를 연결하는 경로 상의 간선 수를 의미합니다. 여러 알고리즘을 활용하여 효율적으로 두 노드 사이의 거리를 계산할 수 있습니다. 가장 널리 사용되는 방법은 **최소 공통 조상(Lowest Common Ancestor, LCA)**를 활용하는 방법입니다.

### 최소 공통 조상(LCA) 알고리즘

최소 공통 조상 알고리즘은 두 노드의 공통 조상 중 가장 가까운 조상을 찾는 알고리즘입니다. 여러 방법으로 LCA를 계산할 수 있지만, 일반적으로 **최대 깊이 테이블**과 **이진 끝방(Ancestor) 배열**을 사용하여 LCA를 미리 계산합니다.

```cpp
// LCA 미리 계산
void precomputeLCA(int node, int parent) {
    depth[node] = depth[parent] + 1;
    ancestor[node][0] = parent;
    for (int i = 1; i < MAX_LOG; ++i) {
        ancestor[node][i] = ancestor[ancestor[node][i - 1]][i - 1];
    }
    for (int next : tree[node]) {
        if (next != parent) {
            precomputeLCA(next, node);
        }
    }
}

// 최소 공통 조상(LCA) 계산
int findLCA(int u, int v) {
    if (depth[u] < depth[v]) std::swap(u, v);
    for (int i = MAX_LOG - 1; i >= 0; --i) {
        if (depth[u] - depth[v] >= (1 << i)) {
            u = ancestor[u][i];
        }
    }
    if (u == v) return u;
    for (int i = MAX_LOG - 1; i >= 0; --i) {
        if (ancestor[u][i] != ancestor[v][i]) {
            u = ancestor[u][i];
            v = ancestor[v][i];
        }
    }
    return ancestor[u][0];
}
```

### 두 노드 사이의 거리 계산

LCA를 계산한 후, 두 노드 사이의 거리는 다음과 같이 계산할 수 있습니다.

```cpp
// 두 노드 사이의 거리 계산
int distanceBetweenNodes(int u, int v) {
    int lca = findLCA(u, v);
    return depth[u] + depth[v] - 2 * depth[lca];
}
```

이제 위의 방법을 활용하여 트리에서 두 노드 사이의 거리를 효과적으로 구할 수 있습니다.

## 마치며

이렇게 트리 자료 구조에서 두 노드 사이의 거리를 계산하는 방법을 알아보았습니다. **최소 공통 조상(LCA)** 알고리즘을 사용하여 두 노드 사이의 거리를 효율적으로 구할 수 있으며, 여러 문제 해결에 활용될 수 있는 유용한 방법입니다.

참고문헌: [GeeksforGeeks](https://www.geeksforgeeks.org/lca-n-ary-tree-constant-query-o1/), [CP-Algorithms](https://cp-algorithms.com/graph/lca_binary_lifting.html)