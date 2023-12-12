---
layout: post
title: "[c++] 트리의 가장 작은 공통 조상(Find the Smallest Common Ancestor in Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

이번 포스트에서는 트리 구조에서 두 노드의 가장 작은 공통 조상을 찾는 알고리즘에 대해 다루어 보겠습니다. 가장 작은 공통 조상(Smallest Common Ancestor, LCA)을 찾는 것은 많은 그래프 알고리즘 문제에서 중요한 부분입니다. 트리의 구조에서 LCA를 찾는 알고리즘으로는 **최소 공통 조상 알고리즘(Lowest Common Ancestor Algorithm)**이 널리 알려져 있습니다.

## LCA 알고리즘의 기본 원리
가장 작은 공통 조상 알고리즘은 **트리 자료구조**에서 두 노드의 가장 가까운 공통 조상을 찾는 알고리즘으로, 주로 이진 트리나 일반 트리에서 사용됩니다. LCA 알고리즘은 주어진 두 노드의 **깊이(Depth)** 값을 이용하여 가장 가까운 조상을 찾습니다.

## 예시 코드
아래는 C++로 트리의 가장 작은 공통 조상을 찾는 예시 코드입니다.

```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 100001;
const int LOG = 20;

vector<int> tree[MAX];
int parent[MAX][LOG];
int depth[MAX];

void dfs(int cur, int prev) {
    depth[cur] = depth[prev] + 1;
    parent[cur][0] = prev;

    for (int i = 0; i < tree[cur].size(); i++) {
        int next = tree[cur][i];
        if (next != prev) {
            dfs(next, cur);
        }
    }
}

void setParent(int n) {
    dfs(1, 0);

    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= n; i++) {
            parent[i][j] = parent[parent[i][j - 1]][j - 1];
        }
    }
}

int lca(int a, int b) {
    if (depth[a] > depth[b]) {
        swap(a, b);
    }

    for (int i = LOG - 1; i >= 0; i--) {
        if (depth[b] - depth[a] >= (1 << i)) {
            b = parent[b][i];
        }
    }

    if (a == b) {
        return a;
    }

    for (int i = LOG - 1; i >= 0; i--) {
        if (parent[a][i] != parent[b][i]) {
            a = parent[a][i];
            b = parent[b][i];
        }
    }

    return parent[a][0];
}
```

위의 예시 코드는 트리의 각 노드의 깊이와 조상 노드를 저장한 후, 주어진 두 노드의 깊이를 맞추고 공통 조상을 찾는 **LCA 알고리즘**의 구현 예시입니다.


## 참고 자료
1. [TopCoder - Lowest Common Ancestor Review](https://www.topcoder.com/community/competitive-programming/tutorials/range-minimum-query-and-lowest-common-ancestor/)
2. [GeeksforGeeks - Lowest Common Ancestor in a Binary Tree](https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/)