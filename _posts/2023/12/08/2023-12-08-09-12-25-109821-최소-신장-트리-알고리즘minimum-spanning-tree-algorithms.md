---
layout: post
title: "[c++] 최소 신장 트리 알고리즘(Minimum Spanning Tree Algorithms)"
description: " "
date: 2023-12-08
tags: [c++]
comments: true
share: true
---

최소 신장 트리 (MST, Minimum Spanning Tree)는 가중치 그래프에 대한 개념으로, 그래프의 모든 정점을 포함하면서 사이클을 형성하지 않는 부분 그래프 중에서 간선의 가중치 합이 최소인 트리를 의미합니다. 대표적인 최소 신장 트리 알고리즘으로는 Kruskal과 Prim 알고리즘이 있습니다.

## 1. [Kruskal 알고리즘](#kruskal-algorithm)

## 2. [Prim 알고리즘](#prim-algorithm)

## Kruskal 알고리즘
Kruskal 알고리즘은 **간선을 기준으로** MST를 만들어가는 그리디 알고리즘입니다. 이 알고리즘은 가능한 모든 간선을 가중치에 따라 오름차순으로 정렬한 후, 가장 작은 가중치부터 차례대로 MST에 포함시킵니다. 이때, 새로운 간선을 추가할 때 사이클이 형성되는지 확인하고, 사이클이 형성되지 않는 경우에만 간선을 추가합니다.

Kruskal 알고리즘의 **시간 복잡도**는 O(E log E)로, E는 간선의 수를 나타냅니다.

```c++
// Kruskal 알고리즘 예제 코드
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Edge {
    int start, end, weight;
};

vector<int> parent;

int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

void merge(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) parent[b] = a;
}

bool compare(Edge a, Edge b) {
    return a.weight < b.weight;
}

int main() {
    int V, E;  // 정점의 개수와 간선의 개수
    cin >> V >> E;
    vector<Edge> edges(E);
    for (int i = 0; i < E; i++) {
        cin >> edges[i].start >> edges[i].end >> edges[i].weight;
    }
    sort(edges.begin(), edges.end(), compare);
    parent.resize(V);
    for (int i = 0; i < V; i++) {
        parent[i] = i;
    }
    
    int answer = 0;
    for (int i = 0; i < E; i++) {
        if (find(edges[i].start) != find(edges[i].end)) {
            merge(edges[i].start, edges[i].end);
            answer += edges[i].weight;
        }
    }
    cout << answer << endl;
    return 0;
}
```

### 참고문헌
- [Kruskal's algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)

## Prim 알고리즘
Prim 알고리즘은 **정점을 기준으로** MST를 만들어가는 그리디 알고리즘으로, 임의의 시작 정점을 선택한 후 해당 정점과 연결된 간선 중에서 최소 가중치 간선을 선택하여 트리를 확장해가는 방식입니다. 선택된 정점들과 연결된 간선 중에서 가장 작은 가중치의 간선을 선택하고, 해당 간선으로 연결된 정점을 트리에 포함시킵니다.

Prim 알고리즘의 **시간 복잡도**는 O(V^2) 또는 O(E log V)로, V는 정점의 개수, E는 간선의 개수를 나타냅니다.

```c++
// Prim 알고리즘 예제 코드
#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

vector<vector<pair<int, int>>> graph;  // (연결된 정점, 가중치) 쌍으로 표현된 그래프
vector<bool> visited;

int main() {
    int V, E;  // 정점의 개수와 간선의 개수
    cin >> V >> E;
    graph.resize(V);
    visited.resize(V, false);
    for (int i = 0; i < E; i++) {
        int start, end, weight;
        cin >> start >> end >> weight;
        graph[start].push_back(make_pair(end, weight));
        graph[end].push_back(make_pair(start, weight));
    }

    int answer = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;  // (가중치, 정점) 쌍으로 표현된 우선순위 큐
    pq.push(make_pair(0, 0));  // 시작 정점과 해당 정점의 가중치 0 추가
    while (!pq.empty()) {
        int weight = pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        if (visited[cur]) continue;
        visited[cur] = true;
        answer += weight;
        for (int i = 0; i < graph[cur].size(); i++) {
            int next = graph[cur][i].first;
            int nextWeight = graph[cur][i].second;
            if (!visited[next]) {
                pq.push(make_pair(nextWeight, next));
            }
        }
    }
    cout << answer << endl;
    return 0;
}
```

### 참고문헌
- [Prim's algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)