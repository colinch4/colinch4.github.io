---
layout: post
title: "[java] 아파치 플링크의 샘플 애플리케이션(Sample applications in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 대규모 데이터 처리를 위한 오픈 소스 분산 처리 프레임워크로, 다양한 샘플 애플리케이션을 제공합니다. 이번 블로그 포스트에서는 아파치 플링크의 샘플 애플리케이션에 대해 알아보겠습니다.

## WordCount 애플리케이션

WordCount 애플리케이션은 아파치 플링크의 가장 기본적인 예제입니다. 이 애플리케이션은 텍스트 파일을 읽어와 각 단어의 등장 횟수를 계산하는 기능을 제공합니다.

```java
import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.util.Collector;

public class WordCount {

    public static void main(String[] args) throws Exception {
        // Execution Environment 설정
        final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // 입력 데이터를 읽어올 DataStream 생성
        DataStream<String> text = env.readTextFile("input.txt");

        // 입력 데이터를 단어 단위로 분할하고 단어와 1을 Tuple 형태로 매핑하는 FlatMap 함수 정의
        DataStream<Tuple2<String, Integer>> counts = text
                .flatMap(new Tokenizer())
                .keyBy(0)
                .sum(1);

        // 결과를 출력
        counts.print();

        // Job 실행
        env.execute("WordCount");
    }

    public static final class Tokenizer implements FlatMapFunction<String, Tuple2<String, Integer>> {
        @Override
        public void flatMap(String value, Collector<Tuple2<String, Integer>> out) {
            // 공백을 기준으로 단어 분리
            String[] words = value.toLowerCase().split("\\W+");

            // 각 단어와 1을 Tuple로 매핑하여 Collector에 추가
            for (String word : words) {
                if (word.length() > 0) {
                    out.collect(new Tuple2<>(word, 1));
                }
            }
        }
    }
}
```

위의 예제 코드는 WordCount 애플리케이션을 실행하는 간단한 Java 코드입니다. 이 코드는 입력 데이터를 텍스트 파일로부터 읽어와 단어 단위로 분할하고, 각 단어와 1을 Tuple 형태로 매핑한 다음, 단어를 기준으로 그룹화하고 등장 횟수를 합산합니다. 마지막으로 결과를 출력하며, 아파치 플링크의 실행 환경을 설정하여 Job을 실행합니다.

## 참고 자료

- [아파치 플링크 공식 사이트](https://flink.apache.org/)
- [아파치 플링크 핵심 개념 및 아키텍처 소개 블로그 포스트](https://www.cubrid.org/blog/understanding-apache-flink-core-concepts-and-architecture)

이 블로그 포스트에서는 아파치 플링크의 샘플 애플리케이션인 WordCount를 소개했습니다. 아파치 플링크에 대한 추가적인 정보는 공식 사이트와 핵심 개념 및 아키텍처에 대한 블로그 포스트에서 확인할 수 있습니다.