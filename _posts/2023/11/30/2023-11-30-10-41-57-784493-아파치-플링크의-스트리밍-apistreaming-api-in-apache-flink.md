---
layout: post
title: "[java] 아파치 플링크의 스트리밍 API(Streaming API in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대규모 실시간 스트리밍 및 배치 데이터 처리를 위한 분산 처리 프레임워크입니다. 이 프레임워크는 데이터 스트림 처리를 위한 강력한 스트리밍 API를 제공합니다.

## 스트리밍 API 개요

스트리밍 API는 아파치 플링크에서 실시간 스트림 데이터 처리를 위한 핵심 기능을 제공합니다. 이 API를 사용하면 데이터 스트림을 처리하고 분석하는 다양한 연산을 수행할 수 있습니다.

스트리밍 API의 핵심 개념 중 하나는 `DataStream`입니다. `DataStream`은 무제한의 데이터 스트림을 나타내는 추상화된 데이터 형식입니다. 이 데이터 스트림은 시간 순서대로 계속해서 업데이트될 수 있으며, 사용자는 `DataStream`을 통해 연산을 적용하고 원하는 결과를 얻을 수 있습니다.

## 스트리밍 API 예제

다음은 아파치 플링크의 스트리밍 API를 사용한 예제 코드입니다:

```java
import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.util.Collector;

public class WordCount {

    public static void main(String[] args) throws Exception {

        // 아파치 플링크 실행 환경 생성
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // 데이터 스트림 생성
        DataStream<String> text = env.socketTextStream("localhost", 9999);

        // 공백을 기준으로 단어 분리하고 각 단어의 개수 계산
        DataStream<Tuple2<String, Integer>> counts = text
                .flatMap(new Tokenizer())
                .keyBy(0)
                .sum(1);

        // 결과 출력
        counts.print();

        // 아파치 플링크 실행
        env.execute("WordCount");
    }

    public static final class Tokenizer implements FlatMapFunction<String, Tuple2<String, Integer>> {
        @Override
        public void flatMap(String value, Collector<Tuple2<String, Integer>> out) {
            // 공백을 기준으로 단어 분리
            String[] words = value.toLowerCase().split("\\s+");

            // 각 단어와 1로 이루어진 Tuple 생성
            for (String word : words) {
                if (word.length() > 0) {
                    out.collect(new Tuple2<>(word, 1));
                }
            }
        }
    }
}
```

이 예제는 소켓을 통해 들어오는 텍스트 데이터의 단어를 분리하고, 각 단어의 등장 횟수를 계산하는 WordCount 애플리케이션입니다. `socketTextStream` 메소드를 사용하여 데이터 스트림을 생성하고, `Tokenizer` 함수를 사용하여 입력 문자열을 단어로 분리합니다. 그리고 `keyBy`와 `sum` 메소드를 사용하여 단어의 등장 횟수를 계산합니다. 마지막으로, 결과를 출력하고 아파치 플링크를 실행합니다.

## 참고 자료

- [Apache Flink Documentation](https://flink.apache.org/documentation.html)
- [Apache Flink Streaming API](https://ci.apache.org/projects/flink/flink-docs-stable/dev/datastream_api.html)