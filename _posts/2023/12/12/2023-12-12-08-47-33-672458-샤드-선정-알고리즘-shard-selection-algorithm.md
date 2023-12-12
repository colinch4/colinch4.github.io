---
layout: post
title: "[sql] 샤드 선정 알고리즘 (Shard Selection Algorithm)"
description: " "
date: 2023-12-12
tags: [sql]
comments: true
share: true
---

데이터베이스에서 샤딩은 대규모 데이터를 처리하기 위한 효율적인 방법 중 하나로, 데이터를 여러 조각으로 나누어 분산 저장 및 처리하는 기술이다. 이때, 클라이언트가 어떤 샤드(Shard)에 데이터를 쓰거나 읽을지 선택하는 과정이 Shard Selection Algorithm이다. 이번 포스트에서는 대표적인 Shard Selection Algorithm 두 가지를 살펴보고자 한다.

## 1. Round-robin algorithm

Round-robin 알고리즘은 간단하고 효과적인 샤드 선택 알고리즘이다. 여러 샤드 중에서 순서대로 선택하고, 마지막에 도달하면 다시 처음으로 돌아가는 방식이다. 이 알고리즘의 장점은 Overhead가 적고 구현이 간단하다는 것이다. 단점은 각 샤드에 대한 부하나 처리 속도와 무관하게 균일하게 노출된다는 것이다.

다음은 Round-robin 알고리즘을 이용한 샤드 선택의 예시이다.
```sql
shardCount = 3
selectedShard = (lastSelectedShard + 1) % shardCount
```

## 2. Consistent hashing algorithm

Consistent hashing 알고리즘은 각 샤드를 원 형태의 범위로 나타내어 일정 범위의 키들을 해당 샤드에 할당하는 방식이다. 이때, 새로운 샤드가 생성되거나 제거될 경우 기존에 할당된 키들에 대한 영향을 최소화할 수 있다. 이러한 특징은 Consistent hashing이 확장성과 유연성을 갖도록 도와준다.

다음은 Consistent hashing 알고리즘을 이용한 샤드 선택의 예시이다.
```sql
hash(node + ":" + key) % shardCount
```

두 알고리즘은 각자의 장단점을 갖고 있으며, 상황에 맞게 적절한 알고리즘을 선택해야 한다. 확장성과 범용성이 중요한 경우에는 Consistent hashing 알고리즘이 유용하며, 간단하고 빠른 구현이 필요한 경우에는 Round-robin 알고리즘이 적절할 것이다.