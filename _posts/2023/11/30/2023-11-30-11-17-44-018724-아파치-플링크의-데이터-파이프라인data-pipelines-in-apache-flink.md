---
layout: post
title: "[java] 아파치 플링크의 데이터 파이프라인(Data pipelines in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대규모 데이터 처리를 위한 오픈 소스 분산 처리 프레임워크입니다. 이러한 프레임워크는 실시간 스트림 처리 및 배치 처리에 사용되며, 데이터 파이프라인을 구축하는 데 매우 유용합니다.

## 데이터 스트림 처리와 배치 처리

플링크는 데이터 스트림 처리와 배치 처리를 모두 지원합니다. 데이터 스트림 처리는 실시간으로 데이터를 처리하는 것을 의미하며, 플링크는 이를 지원하기 위해 스트림 API를 제공합니다. 데이터 배치 처리는 대량의 데이터를 일괄적으로 처리하는 것을 의미하며, 플링크는 이를 지원하기 위해 배치 API를 제공합니다.

## 스트림 처리 파이프라인 구축하기

아파치 플링크를 사용하여 데이터 스트림 처리 파이프라인을 구축하는 것은 매우 간단합니다. 플링크의 스트림 API를 사용하면 데이터를 끊임없이 흐르는 스트림으로 처리할 수 있습니다. 다음은 이를 위한 간단한 예제 코드입니다.

```java
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;

public class StreamProcessingPipeline {
    public static void main(String[] args) throws Exception {
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        DataStream<String> inputDataStream = env.socketTextStream("localhost", 1234);

        DataStream<Tuple2<String, Integer>> wordCounts = inputDataStream
                .flatMap((String line, Collector<Tuple2<String, Integer>> out) -> {
                    for (String word : line.split(" ")) {
                        out.collect(new Tuple2<>(word, 1));
                    }
                })
                .keyBy(0)
                .sum(1);

        wordCounts.print();

        env.execute("Stream processing pipeline");
    }
}
```

위의 코드는 소켓으로부터 들어오는 문자열을 공백을 기준으로 단어로 분리하고, 각 단어의 출현 횟수를 계산하여 출력하는 간단한 스트림 처리 파이프라인을 구축하는 예제입니다.

## 배치 처리 파이프라인 구축하기

플링크를 사용하여 데이터 배치 처리 파이프라인을 구축하는 것도 매우 쉽습니다. 플링크의 배치 API를 사용하면 대량의 데이터를 효율적으로 처리할 수 있습니다. 다음은 이를 위한 간단한 예제 코드입니다.

```java
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.api.java.tuple.Tuple2;

public class BatchProcessingPipeline {
    public static void main(String[] args) throws Exception {
        final ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();

        DataSet<String> inputDataSet = env.readTextFile("input.txt");

        DataSet<Tuple2<String, Integer>> wordCounts = inputDataSet
                .flatMap((String line, Collector<Tuple2<String, Integer>> out) -> {
                    for (String word : line.split(" ")) {
                        out.collect(new Tuple2<>(word, 1));
                    }
                })
                .groupBy(0)
                .sum(1);

        wordCounts.print();

        env.execute("Batch processing pipeline");
    }
}
```

위의 코드는 텍스트 파일에서 읽어온 문자열을 공백을 기준으로 단어로 분리하고, 각 단어의 출현 횟수를 계산하여 출력하는 간단한 배치 처리 파이프라인을 구축하는 예제입니다.

## 결론

아파치 플링크를 사용하면 데이터 파이프라인을 간편하게 구축할 수 있습니다. 스트림 처리와 배치 처리를 모두 지원하기 때문에 실시간 처리와 대규모 데이터 처리를 모두 효율적으로 수행할 수 있습니다. 플링크의 다양한 API와 기능을 활용하여 데이터 파이프라인을 구축해 보세요.

## 참고 자료
- [Apache Flink 공식 홈페이지](https://flink.apache.org/)