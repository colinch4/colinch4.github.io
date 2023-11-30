---
layout: post
title: "[java] 아파치 플링크의 윈도우 함수(Window functions in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 분산 처리를 위한 오픈 소스 스트림 처리 프레임워크입니다. 플링크는 데이터 스트림 처리에서 윈도우 함수를 사용하여 데이터를 윈도우로 분할하고 집계하는 기능을 제공합니다. 이 기사에서는 플링크의 윈도우 함수에 대해 살펴보겠습니다.

## 1. 윈도우 함수란?

윈도우 함수는 데이터 스트림을 분할하고 해당 윈도우 내에서 집계 연산을 수행하는 함수입니다. 플링크에서는 다양한 윈도우 유형을 제공하며, 각 유형에 따라 윈도우 크기와 슬라이딩 정책을 설정할 수 있습니다.

플링크에서 지원하는 주요 윈도우 유형은 다음과 같습니다:
- Tumbling Windows: 고정 크기의 서로 겹치지 않는 윈도우를 생성합니다.
- Sliding Windows: 고정된 크기의 윈도우를 지정한 슬라이딩 간격으로 슬라이딩 시킵니다.
- Session Windows: 입력 스트림에서 윈도우의 시작과 끝을 기반으로 세션을 식별합니다.

## 2. 플링크에서 윈도우 함수 사용하기

플링크에서 윈도우 함수를 사용하기 위해서는 먼저 데이터 스트림을 KeyedStream으로 변환해야 합니다. KeyedStream은 키를 기준으로 데이터 스트림을 파티셔닝하며, 윈도우 함수를 적용할 수 있습니다.

윈도우 함수를 적용하려면 다음과 같은 단계를 따릅니다:

1. DataStream을 KeyedStream으로 변환합니다:
   ```java
   KeyedStream<Tuple2<String, Integer>, String> keyedStream = dataStream.keyBy(Tuple2::f0);
   ```

2. 원하는 윈도우 유형을 선택하고 크기 및 슬라이딩 간격을 설정합니다:
   ```java
   WindowedStream<Tuple2<String, Integer>, String, TimeWindow> windowedStream = keyedStream.window(TumblingEventTimeWindows.of(Time.seconds(5)));
   ```

3. 윈도우 함수를 적용하여 집계 연산을 수행합니다:
   ```java
   SingleOutputStreamOperator<Tuple2<String, Integer>> result = windowedStream.sum(1);
   ```

위 코드에서는 키드 스트림을 생성한 후, TumblingEventTimeWindows를 사용하여 5초 크기의 텀블링 윈도우를 생성하고, sum 함수를 사용하여 해당 윈도우 내에서 두 번째 필드를 기준으로 집계 연산을 수행합니다.

## 3. 윈도우 함수의 활용 예시

윈도우 함수는 데이터 스트림에서 다양한 분석 작업을 수행하는 데 사용될 수 있습니다. 예를 들어, 플링크를 사용하여 주요 키워드의 트렌드를 파악하기 위해 윈도우 함수를 활용할 수 있습니다.

주요 키워드의 트렌드를 파악하는 방법은 다음과 같습니다:
1. 데이터 스트림에서 키워드를 추출하고 키드 스트림으로 변환합니다.
2. 키드 스트림을 윈도우 함수로 변환하여 키워드를 특정 시간 간격으로 그룹화합니다.
3. 각 윈도우에서 키워드의 등장 횟수를 집계하여 트렌드를 분석합니다.

이렇게 하면 주요 키워드의 등장 횟수를 윈도우마다 확인할 수 있으며, 시간의 흐름에 따른 트렌드 변화를 파악할 수 있습니다.

## 4. 결론

아파치 플링크의 윈도우 함수를 사용하면 데이터 스트림을 윈도우로 분할하고 집계하는 강력한 기능을 제공합니다. 윈도우 함수를 적절하게 활용하면 데이터 스트림에서 다양한 분석 작업을 수행할 수 있으며, 플링크의 성능과 확장성을 극대화할 수 있습니다.

더 자세한 내용은 아파치 플링크 공식 문서를 참조하시기 바랍니다.

---

참고:
- [아파치 플링크 공식 문서](https://flink.apache.org/)