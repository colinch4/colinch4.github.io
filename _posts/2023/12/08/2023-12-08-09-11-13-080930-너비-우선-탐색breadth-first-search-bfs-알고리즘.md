---
layout: post
title: "[c++] 너비 우선 탐색(Breadth First Search, BFS) 알고리즘"
description: " "
date: 2023-12-08
tags: [c++]
comments: true
share: true
---

너비 우선 탐색(Breadth First Search, BFS) 알고리즘은 그래프 탐색에 사용되는 대표적인 알고리즘 중 하나입니다. 이 알고리즘은 특정 노드에서 시작하여 인접한 모든 노드를 우선적으로 탐색하는 방법을 기반으로 합니다.

## 알고리즘 개요
BFS 알고리즘은 큐(queue)를 사용하여 구현됩니다. 아래는 간단한 BFS 알고리즘의 개요입니다.

1. 시작 노드를 큐에 넣고 방문 여부를 확인합니다.
2. 큐가 빌 때까지 다음 작업을 반복합니다.
   - 큐에서 노드를 하나 꺼내고 방문 여부를 확인합니다.
   - 해당 노드의 인접 노드 중 방문하지 않은 노드를 큐에 넣고 방문 여부를 확인합니다.

이 알고리즘을 통해 너비 우선으로 그래프를 탐색할 수 있습니다.

## 예시 코드
```c++
#include <iostream>
#include <vector>
#include <queue>

void bfs(std::vector<std::vector<int>>& graph, int start) {
    std::vector<bool> visited(graph.size(), false);
    std::queue<int> q;

    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int current = q.front();
        q.pop();
        std::cout << current << " ";

        for (int next : graph[current]) {
            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
            }
        }
    }
}

int main() {
    std::vector<std::vector<int>> graph = {{1, 2}, {0, 3, 4}, {0, 5, 6}, {1}, {1}, {2}, {2}};
    bfs(graph, 0);

    return 0;
}
```

위 코드는 인접 리스트를 사용하여 그래프를 나타내고, BFS 알고리즘을 구현한 예시입니다.

## 결론
너비 우선 탐색(BFS) 알고리즘은 그래프 내의 노드들을 너비 방향으로 탐색하는 효율적인 알고리즘입니다. 이를 통해 특정 노드에서 출발하여 해당 노드와 연결된 모든 노드를 탐색할 수 있습니다.

[BFS 알고리즘 - 위키피디아](https://ko.wikipedia.org/wiki/너비_우선_탐색)