---
layout: post
title: "[kotlin] 코틀린 집합(Set)을 이용한 DFS(Depth-First Search)"
description: " "
date: 2023-12-08
tags: [kotlin]
comments: true
share: true
---

DFS(Depth-First Search)는 그래프의 깊이를 우선적으로 탐색하는 알고리즘입니다. 즉, 한 노드에서 시작하여 다음 분기로 넘어가기 전에 해당 분기를 완전히 탐색하는 방법입니다. 이 방법은 스택(Stack) 자료구조나 재귀(Recursion)를 이용하여 구현할 수 있습니다.

## Set을 이용한 DFS

코틀린에서 DFS를 구현하는 방법 중 하나는 Set을 사용하여 방문한 노드를 관리하는 것입니다. 아래는 Set을 이용하여 DFS를 구현한 예제입니다.

```kotlin
class Graph(private val adjacencyList: Map<Int, List<Int>>) {
    private val visited = mutableSetOf<Int>()

    fun dfs(node: Int) {
        visited.add(node)
        println(node)

        adjacencyList[node]?.forEach {
            if (it !in visited) {
                dfs(it)
            }
        }
    }
}

fun main() {
    val graph = Graph(
        mapOf(
            1 to listOf(2, 3),
            2 to listOf(4, 5),
            3 to listOf(6),
            4 to emptyList(),
            5 to listOf(7),
            6 to emptyList(),
            7 to emptyList()
        )
    )
    graph.dfs(1)
}
```

위 예제에서 `Graph` 클래스는 주어진 인접 리스트를 사용하여 그래프를 표현하고, `dfs` 함수는 DFS를 수행합니다. 방문한 노드는 `visited` Set에 저장되며 `dfs` 함수 내에서 방문 여부를 확인하여 탐색을 진행합니다.

DFS 알고리즘을 위한 기본적인 구현이며, 실제 응용에 따라 보다 다양한 기능을 추가할 수 있습니다.

## 결론

Set을 이용하여 DFS를 구현하는 방법은 그래프 알고리즘에서 유용하게 활용될 수 있습니다. 코틀린의 집합(Set)은 중복을 허용하지 않고, 빠른 조회 속도를 제공하여 DFS 알고리즘을 효율적으로 구현할 수 있습니다.

위 예제를 통해 실제 그래프 구조에서 DFS를 구현하는 방법을 이해할 수 있습니다.

[참고](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)