---
layout: post
title: "[java] 아파치 플링크의 스트림 파티셔닝(Stream partitioning in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

스트림 처리 시스템에서 병렬 처리는 매우 중요한 요소입니다. 병렬 처리를 효과적으로 수행하기 위해 스트림을 여러 파티션으로 분할하는 파티셔닝 기능을 사용할 수 있습니다. 아파치 플링크는 대량의 데이터를 처리하는 데 특화된 스트림 처리 엔진으로, 다양한 파티셔닝 전략을 제공합니다.

## 파티셔닝 전략

아파치 플링크에서는 다음과 같은 파티셔닝 전략을 제공합니다.

1. **랜덤 파티셔닝(Random Partitioning)**: 입력 스트림의 각 이벤트를 임의의 파티션에 할당합니다. 이 방식은 데이터의 균형을 유지하기 위해 가장 많이 사용되는 방법입니다.

2. **라운드 로빈 파티셔닝(Round Robin Partitioning)**: 입력 스트림의 이벤트를 순서대로 파티션에 할당합니다. 이 방식은 입력 순서를 유지하면서 데이터를 분산시키는 데 사용됩니다.

3. **리소스 파티셔닝(Resource Partitioning)**: 논리적인 파티션과 물리적인 리소스 간에 일대일 매핑을 수행합니다. 이 방식은 일부 리소스가 과부하되는 상황을 방지하고 데이터 처리량을 균형있게 조절하기 위해 사용됩니다.

4. **키 파티셔닝(Key Partitioning)**: 입력 스트림의 이벤트를 특정 키에 따라 파티션에 할당합니다. 이 방식은 같은 키 값을 가진 이벤트를 한 파티션에 모아서 처리하기 위해 사용됩니다.

## 파티셔닝 설정하기

아파치 플링크에서 파티셔닝 전략을 설정하려면 `DataStream` 객체의 `partitionCustom()` 메서드를 사용해야 합니다. 이 메서드는 파티셔닝 전략을 정의하고 적용할 수 있도록 도와줍니다.

다음은 랜덤 파티셔닝을 설정하는 예제 코드입니다.

```java
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class PartitioningExample {
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        DataStream<String> inputData = env.fromElements("Apple", "Banana", "Cherry");

        DataStream<String> partitionedStream = inputData.partitionCustom(new RandomPartitioner(), "key");

        partitionedStream.print();

        env.execute("Partitioning Example");
    }
}
```

위 코드에서 `partitionCustom()` 메서드에 전략으로 `RandomPartitioner` 클래스를 사용하고 있습니다. `RandomPartitioner` 클래스는 랜덤하게 파티션을 선택하는 파티셔닝 기능을 제공합니다. `key`는 입력 데이터의 키 값을 나타냅니다.

이와 같은 방식으로 다양한 파티셔닝 전략을 설정할 수 있으며, 이를 통해 아파치 플링크를 이용한 스트림 처리의 병렬성과 효율성을 높일 수 있습니다.

## 참고 자료

- [아파치 플링크 공식 문서](https://flink.apache.org/)