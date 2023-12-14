---
layout: post
title: "[java] 자바의 너비 우선 탐색(Breadth First Search, BFS) 알고리즘 이해하기"
description: " "
date: 2023-12-14
tags: [java]
comments: true
share: true
---

이 포스트에서는 자바에서 **너비 우선 탐색(BFS)** 알고리즘의 구현과 이해에 대해 다루겠습니다. BFS는 그래프나 나무와 같은 자료 구조를 탐색할 때 가장 직관적인 방법 중 하나로, 시작 노드에서 가장 가까운 이웃 노드부터 모두 탐색하는 알고리즘입니다.

## BFS의 구현

아래는 자바에서 BFS 알고리즘을 구현한 간단한 예제입니다.

```java
import java.util.LinkedList;
import java.util.Queue;

public class BFS {
    public void breadthFirstSearch(Node root) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            System.out.println(current.value);

            for (Node neighbor : current.neighbors) {
                if (!neighbor.visited) {
                    queue.add(neighbor);
                    neighbor.visited = true;
                }
            }
        }
    }
}

class Node {
    int value;
    List<Node> neighbors;
    boolean visited;

    public Node(int value) {
        this.value = value;
        this.neighbors = new ArrayList<>();
        this.visited = false;
    }
}
```

이 예제에서는 `Node` 클래스를 정의하고, 이웃 노드들을 저장하기 위한 `neighbors` 리스트를 포함합니다. `BFS` 클래스는 `breadthFirstSearch` 메서드를 통해 BFS를 구현하고, `Queue`를 사용하여 너비 우선으로 탐색을 수행합니다.

## BFS 알고리즘의 이해

BFS 알고리즘은 너비를 기준으로 먼저 탐색을 진행하기 때문에, 더 깊은 단계의 노드들은 나중에 탐색됩니다. 이 알고리즘을 통해 특정 노드로부터 시작하여 해당 노드와 연결된 모든 노드를 발견할 수 있습니다.

BFS는 큐(queue)를 활용하여 구현되며, 각 노드를 `visited`로 표시하여 이미 방문한 노드를 추가적으로 탐색하지 않도록 합니다.

## 마무리

이 포스트에서는 자바에서의 BFS 알고리즘의 구현과 이해에 대해 간략히 살펴보았습니다. BFS는 그래프 탐색 및 최단 경로 찾기 등 다양한 문제에 활용되며, 이를 이해하고 활용할 수 있다면 다양한 알고리즘 문제를 해결하는 데 도움이 될 것입니다.

참고 문헌 : [GeeksforGeeks - Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

이상으로 "자바의 너비 우선 탐색(Breadth First Search, BFS) 알고리즘 이해하기"를 마치도록 하겠습니다.