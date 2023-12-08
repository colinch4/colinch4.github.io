---
layout: post
title: "[c++] 최단 경로 알고리즘(Shortest Path Algorithms)"
description: " "
date: 2023-12-08
tags: [c++]
comments: true
share: true
---

최단 경로 알고리즘은 그래프 내의 노드 사이의 최단 경로를 찾는 알고리즘입니다. 이 글에서는 대표적인 최단 경로 알고리즘인 다익스트라(Dijkstra) 알고리즘과 벨만-포드(Bellman-Ford) 알고리즘에 대해 알아보겠습니다.

## 목차
- [다익스트라 알고리즘](#다익스트라-알고리즘)
- [벨만-포드 알고리즘](#벨만-포드-알고리즘)

---

## 다익스트라 알고리즘

다익스트라 알고리즘은 하나의 시작 노드로부터 모든 다른 노드까지의 최단 경로를 찾는 알고리즘입니다. 이 알고리즘은 음이 아닌 가중치를 갖는 그래프에서 사용됩니다.

```c++
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

#define INF 1e9

int n, m; // 노드의 수, 간선의 수
vector<pair<int, int>> graph[100001]; // 각 노드에 연결된 노드(노드, 가중치)

vector<int> dijkstra(int start) {
    vector<int> distance(n + 1, INF);
    priority_queue<pair<int, int>> pq; // (최단 거리, 노드)

    pq.push({0, start});
    distance[start] = 0;

    while (!pq.empty()) {
        int dist = -pq.top().first;
        int now = pq.top().second;
        pq.pop();

        if (distance[now] < dist) continue;

        for (int i = 0; i < graph[now].size(); i++) {
            int cost = dist + graph[now][i].second;
            if (cost < distance[graph[now][i].first]) {
                distance[graph[now][i].first] = cost;
                pq.push({-cost, graph[now][i].first});
            }
        }
    }

    return distance;
}
```

위 코드는 다익스트라 알고리즘을 C++로 구현한 예시입니다.

## 벨만-포드 알고리즘

벨만-포드 알고리즘은 음수 가중치가 있는 그래프에서 최단 경로를 찾는 알고리즘입니다. 다익스트라 알고리즘과는 달리 음수 가중치를 허용합니다.

```c++
#include <iostream>
#include <vector>
using namespace std;

#define INF 1e9

struct Edge {
    int from, to, cost;
};

int n, m; // 노드의 수, 간선의 수
vector<Edge> edges;
vector<int> dist(n + 1, INF);

bool bellman_ford(int start) {
    dist[start] = 0;

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int from = edges[j].from;
            int to = edges[j].to;
            int cost = edges[j].cost;
            if (dist[from] != INF && dist[to] > dist[from] + cost) {
                dist[to] = dist[from] + cost;
            }
        }
    }

    for (int i = 0; i < m; i++) {
        int from = edges[i].from;
        int to = edges[i].to;
        int cost = edges[i].cost;
        if (dist[from] != INF && dist[to] > dist[from] + cost) {
            return false; // 음수 사이클 존재
        }
    }

    return true;
}
```

위 코드는 벨만-포드 알고리즘을 C++로 구현한 예시입니다.

각 알고리즘의 구체적인 동작 방식과 시간 복잡도 등에 대한 이해를 바탕으로 최적의 상황에 맞게 적절한 알고리즘을 선택하여 사용할 수 있습니다.

## 참고 자료
- [Dijkstra's algorithm - Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Bellman–Ford algorithm - Wikipedia](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)

---