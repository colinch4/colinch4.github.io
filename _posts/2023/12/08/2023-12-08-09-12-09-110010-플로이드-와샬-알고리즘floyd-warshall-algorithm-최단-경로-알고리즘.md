---
layout: post
title: "[c++] 플로이드-와샬 알고리즘(Floyd-Warshall Algorithm) 최단 경로 알고리즘"
description: " "
date: 2023-12-08
tags: [c++]
comments: true
share: true
---

Floyd-Warshall 알고리즘은 다이내믹 프로그래밍을 활용하여 구현됩니다. 이 알고리즘의 핵심 아이디어는 정점을 하나씩 추가하면서 해당 정점을 거쳐 가는 최단 거리를 업데이트하는 것입니다.

아래는 C++로 플로이드-와샬 알고리즘을 구현한 간단한 예제 코드입니다.

```cpp
#include <iostream>
#include <climits>

#define V 4
#define INF 99999

void floydWarshall(int graph[][V]) {
    int dist[V][V];

    for (int i = 0; i < V; i++)
        for (int j = 0; j < V; j++)
            dist[i][j] = graph[i][j];

    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }

    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (dist[i][j] == INF)
                std::cout << "INF ";
            else
                std::cout << dist[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    int graph[V][V] = {{0, 5, INF, 10},
                       {INF, 0, 3, INF},
                       {INF, INF, 0, 1},
                       {INF, INF, INF, 0}};

    floydWarshall(graph);
    return 0;
}
```

이 코드는 4개의 정점과 특정 간선 가중치를 포함하는 그래프에 플로이드-와샬 알고리즘을 적용하여 모든 쌍의 최단 거리를 계산합니다.