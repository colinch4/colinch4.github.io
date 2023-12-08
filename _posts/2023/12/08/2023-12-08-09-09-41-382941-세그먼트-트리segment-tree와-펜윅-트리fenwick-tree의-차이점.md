---
layout: post
title: "[kotlin] 세그먼트 트리(Segment Tree)와 펜윅 트리(Fenwick Tree)의 차이점"
description: " "
date: 2023-12-08
tags: [kotlin]
comments: true
share: true
---

세그먼트 트리와 펜윅 트리는 둘 다 효율적으로 범위 쿼리(range query)를 처리하는 데 사용되는 자료 구조입니다. 그러나 두 트리의 구현 방법과 특성에는 몇 가지 차이가 있습니다. 이 블로그에서는 세그먼트 트리와 펜윅 트리의 주요 차이점에 대해 알아보겠습니다.

### 1. 구조적 차이점

- **세그먼트 트리**: 이진 트리를 기반으로 범위 쿼리를 처리하는 자료 구조로, 주로 배열 형태로 구현됩니다. 구간 트리라고도 불립니다. 각 노드는 자식 노드의 값을 병합하여 부모 노드를 업데이트합니다.

- **펜윅 트리**: 또는 Binary Indexed Tree로 알려진 트리 구조로, 배열을 기반으로 하는 간단한 데이터 구조입니다. 각 원소가 다른 원소들의 합을 나타내며, 각 항목의 인덱스를 보고 적절한 원소를 찾아 부분 합을 계산하는 데 사용됩니다.

### 2. 구현 및 사용 용도의 차이점

- **세그먼트 트리**: 주로 범위 조작(query)이 많이 필요한 경우에 사용됩니다. 특히 최소값, 최대값과 같은 쿼리나 새로운 값으로 배열 요소를 업데이트할 때 사용됩니다.

```kotlin
// Kotlin 세그먼트 트리 예시
class SegmentTree(private val input: IntArray) {
    // 구현 내용 생략
}
```

- **펜윅 트리**: 주로 누적 합(prefix sum)을 구하는 데 사용됩니다. 특히 특정 인덱스의 값을 수정하거나 특정 구간의 누적 합을 계산할 때 유용합니다.

```kotlin
// Kotlin 펜윅 트리 예시
class FenwickTree(private val input: IntArray) {
    // 구현 내용 생략
}
```

두 트리는 각자의 장단점이 있으며, 사용하고자 하는 구체적인 상황에 따라 적절히 선택하는 것이 중요합니다. 각각의 트리를 이해하고 활용할 수 있으면, 데이터 구조와 알고리즘을 더 효과적으로 다룰 수 있을 것입니다.

참고 자료:
- [세그먼트 트리 - 위키백과](https://en.wikipedia.org/wiki/Segment_tree)
- [펜윅 트리 - 위키백과](https://en.wikipedia.org/wiki/Fenwick_tree)