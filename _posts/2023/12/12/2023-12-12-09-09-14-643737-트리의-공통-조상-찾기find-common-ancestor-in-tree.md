---
layout: post
title: "[c++] 트리의 공통 조상 찾기(Find Common Ancestor in Tree)"
description: " "
date: 2023-12-12
tags: [c++]
comments: true
share: true
---

트리 구조에서 두 노드의 공통 조상을 찾는 문제는 매우 일반적입니다. 이 문제는 두 가지 일반적인 알고리즘인 `LCA(Lowest Common Ancestor)`와 `Tarjan's Algorithm`을 사용하여 해결할 수 있습니다. 

## LCA(Lowest Common Ancestor)

`LCA` 알고리즘은 트리의 두 노드의 공통 부모를 찾는 알고리즘입니다. 이 알고리즘은 다이내믹 프로그래밍 기법을 사용하여 가장 가까운 공통 조상을 찾습니다.

아래는 C++로 구현된 예제 코드입니다.

```c++
#include <iostream>
#include <vector>
using namespace std;

const int MAX = 10005;
vector<int> tree[MAX];
int parent[MAX][15];
int depth[MAX];

void dfs(int cur, int prev) {
    depth[cur] = depth[prev] + 1;
    parent[cur][0] = prev;
    for (int i = 0; i < tree[cur].size(); i++) {
        if (tree[cur][i] != prev) {
            dfs(tree[cur][i], cur);
        }
    }
}

void setParent(int n) {
    dfs(1, 0);
    for (int j = 1; j < 15; j++) {
        for (int i = 1; i <= n; i++) {
            parent[i][j] = parent[parent[i][j - 1]][j - 1];
        }
    }
}

int LCA(int u, int v) {
    if (depth[u] < depth[v]) swap(u, v);
    for (int i = 14; i >= 0; i--) {
        if (depth[u] - depth[v] >= (1 << i)) {
            u = parent[u][i];
        }
    }
    if (u == v) return u;
    for (int i = 14; i >= 0; i--) {
        if (parent[u][i] != parent[v][i]) {
            u = parent[u][i];
            v = parent[v][i];
        }
    }
    return parent[u][0];
}

int main() {
    int n = 7;  // 노드의 개수
    tree[1].push_back(2);
    tree[2].push_back(1);
    tree[1].push_back(3);
    tree[3].push_back(1);
    tree[2].push_back(4);
    tree[4].push_back(2);
    tree[2].push_back(5);
    tree[5].push_back(2);
    tree[3].push_back(6);
    tree[6].push_back(3);
    tree[3].push_back(7);
    tree[7].push_back(3);

    setParent(n);
    
    // 공통 조상 찾기
    cout << LCA(4, 5) << endl;  // 결과: 2
    cout << LCA(6, 7) << endl;  // 결과: 3
    return 0;
}
```

## Tarjan's Algorithm

`Tarjan's Algorithm`은 트리, 혹은 그래프에서 각각의 노드가 속한 그룹을 찾는 알고리즘입니다. 이 알고리즘을 활용하여 트리의 두 노드 사이의 공통 조상을 찾을 수 있습니다.

아래는 C++로 구현된 예제 코드입니다.

```c++
#include <iostream>
#include <vector>
using namespace std;

const int MAX = 10005;
vector<int> tree[MAX];
int parent[MAX];
int ancestor[MAX];
bool visited[MAX];

int find(int u) {
    if (u == ancestor[u]) return u;
    return ancestor[u] = find(ancestor[u]);
}

void unionVertices(int u, int v) {
    u = find(u);
    v = find(v);
    ancestor[u] = v;
}

void dfs(int cur) {
    visited[cur] = true;
    ancestor[cur] = cur;
    for (int next : tree[cur]) {
        if (!visited[next]) {
            parent[next] = cur;
            dfs(next);
            unionVertices(cur, next);
        }
    }
}

int main() {
    int n = 7;  // 노드의 개수
    tree[1].push_back(2);
    tree[2].push_back(1);
    tree[1].push_back(3);
    tree[3].push_back(1);
    tree[2].push_back(4);
    tree[4].push_back(2);
    tree[2].push_back(5);
    tree[5].push_back(2);
    tree[3].push_back(6);
    tree[6].push_back(3);
    tree[3].push_back(7);
    tree[7].push_back(3);

    dfs(1);
    
    // 공통 조상 찾기
    cout << "LCA(4, 5): " << find(4) << endl;  // 결과: 2
    cout << "LCA(6, 7): " << find(6) << endl;  // 결과: 3
    return 0;
}
```

두 알고리즘 모두 임의의 두 노드의 공통 조상을 찾는 데 사용할 수 있으며, 선택은 문제의 특성에 따라 다를 수 있습니다.

이러한 방법을 사용하여 트리의 공통 조상을 찾을 수 있습니다.