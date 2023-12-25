---
layout: post
title: "[clojure] Clojure의 map, filter, reduce 등을 이용한 지능형 프로그래밍"
description: " "
date: 2023-12-26
tags: [clojure]
comments: true
share: true
---

Clojure는 함수형 프로그래밍 언어로, map, filter, reduce 같은 함수들을 사용하여 데이터를 처리하는데 강점이 있습니다. 이번에는 Clojure에서의 이들 함수들을 이용한 지능형 프로그래밍에 대해 알아보도록 하겠습니다.

## 1. map

`map` 함수는 시퀀스(리스트, 벡터, 맵 등)의 각 요소에 함수를 적용하여 새로운 시퀀스를 반환합니다. 간단한 예제를 통해 살펴보겠습니다.

```clojure
(def numbers '(1 2 3 4 5))
(def squared (map #(* % %) numbers))
```

위 예제에서 `map` 함수는 `numbers` 시퀀스의 각 요소에 제곱 함수를 적용하여 `squared`라는 새로운 시퀀스를 생성합니다.

## 2. filter

`filter` 함수는 주어진 조건에 맞는 요소만을 선택하여 새로운 시퀀스를 반환합니다. 예제를 통해 살펴보도록 하겠습니다.

```clojure
(def numbers '(1 2 3 4 5))
(def even-numbers (filter even? numbers))
```

위 예제에서 `filter` 함수는 `numbers` 시퀀스에서 짝수인 요소만을 선택하여 `even-numbers` 시퀀스를 생성합니다.

## 3. reduce

`reduce` 함수는 시퀀스의 각 요소에 누적 연산을 수행하여 단일값을 반환합니다. 예제를 통해 살펴보겠습니다.

```clojure
(def numbers '(1 2 3 4 5))
(def sum (reduce + numbers))
```

위 예제에서 `reduce` 함수는 `numbers` 시퀀스의 각 요소를 더하여 `sum`이라는 단일값을 반환합니다.

Clojure의 `map`, `filter`, `reduce` 함수를 이용하면 간결하고 가독성 좋은 지능형 프로그래밍을 구현할 수 있습니다. 이러한 함수들은 함수형 프로그래밍의 핵심이며, 데이터 처리와 변환을 쉽게 수행할 수 있도록 도와줍니다.

더 많은 정보를 원하시면 [Clojure 공식 문서](https://clojure.org/)를 참조해 주세요.