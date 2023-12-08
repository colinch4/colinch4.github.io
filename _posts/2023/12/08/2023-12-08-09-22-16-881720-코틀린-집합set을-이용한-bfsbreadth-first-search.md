---
layout: post
title: "[kotlin] 코틀린 집합(Set)을 이용한 BFS(Breadth-First Search)"
description: " "
date: 2023-12-08
tags: [kotlin]
comments: true
share: true
---

이번 포스트에서는 코틀린의 집합(Set)을 이용하여 BFS(Breadth-First Search) 알고리즘을 구현하는 방법에 대해 알아보겠습니다.

## BFS(Breadth-First Search)란?

BFS(Breadth-First Search)는 그래프를 탐색하는 알고리즘 중 하나로, 시작 정점으로부터 근접한 정점들을 먼저 탐색하는 방법입니다. 이 알고리즘은 가까운 정점들을 먼저 방문하기 때문에 너비 우선 탐색이라고 불립니다. BFS는 최단 경로를 찾는 문제나 상태 공간 탐색 문제 등에 활용됩니다.

## 코틀린 집합(Set)을 이용한 BFS 구현

다음은 코틀린을 사용하여 그래프를 나타내고 BFS 알고리즘을 구현하는 간단한 예제입니다.

```kotlin
import java.util.*

class Graph(val adjacencyList: Map<Int, List<Int>>) {
    fun bfs(start: Int) {
        val visited = HashSet<Int>()
        val queue: Queue<Int> = LinkedList()

        visited.add(start)
        queue.add(start)

        while (!queue.isEmpty()) {
            val vertex = queue.poll()
            print("$vertex ")

            for (v in adjacencyList[vertex]!!) {
                if (!visited.contains(v)) {
                    visited.add(v)
                    queue.add(v)
                }
            }
        }
    }
}

fun main(args: Array<String>) {
    val adjacencyList = mapOf(
        0 to listOf(1, 2),
        1 to listOf(2),
        2 to listOf(0, 3),
        3 to listOf(3)
    )

    val graph = Graph(adjacencyList)
    graph.bfs(2)
}
```

위 예제에서는 `Graph` 클래스를 정의하여 그래프와 BFS 알고리즘을 포함하고 있습니다. `bfs` 메서드는 주어진 시작 정점으로부터 BFS를 수행하는 역할을 합니다.

## 마무리

이번 포스트에서는 코틀린 집합(Set)을 이용하여 BFS 알고리즘을 구현하는 방법에 대해 살펴보았습니다. BFS 알고리즘은 너비 우선 탐색을 통해 그래프를 효율적으로 탐색할 수 있게 해주며, 코틀린의 집합(Set)을 이용하여 구현하는 것은 간단하면서도 효과적인 방법입니다. 해당 알고리즘을 활용하여 다양한 문제를 해결하는 데 도움이 될 것입니다.

참고 문헌: [Kotlin Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-set/index.html)