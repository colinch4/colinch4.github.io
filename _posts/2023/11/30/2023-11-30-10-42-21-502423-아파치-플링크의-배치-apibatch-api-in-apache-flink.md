---
layout: post
title: "[java] 아파치 플링크의 배치 API(Batch API in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크는 대규모 데이터 처리를 위한 분산 처리 시스템으로 유명한 오픈 소스 프레임워크입니다. 플링크는 실시간 스트리밍 처리를 위한 Streaming API뿐만 아니라 배치 처리를 위한 Batch API도 제공합니다. 이번 포스트에서는 아파치 플링크의 배치 API에 대해 알아보겠습니다.

## 배치 처리란?

배치 처리는 대량의 데이터를 한 번에 처리하는 작업을 의미합니다. 일반적으로 정해진 일련의 단계를 따라 일괄적으로 데이터를 처리하며, 스트리밍 처리와 달리 실시간 처리가 아닌 지연된 처리를 수행합니다. 예를 들어, 매일 밤에 대량의 데이터를 분석하거나 요약하는 작업은 배치 처리에 해당합니다.

## 아파치 플링크의 배치 API

아파치 플링크의 배치 API는 Java와 Scala로 작성된 프로그램으로 배치 처리 작업을 수행할 수 있습니다. 배치 API를 사용하려면 다음과 같은 단계를 따라야 합니다.

1. **환경 설정**: `ExecutionEnvironment`를 생성하여 실행 환경을 설정합니다.
2. **데이터 소스 설정**: `ExecutionEnvironment`에서 데이터를 읽어와 배치 작업의 입력 소스로 설정합니다.
3. **변환 및 연산**: 데이터에 대한 변환과 연산 로직을 구현합니다. 예를 들어, 데이터를 필터링하거나 그룹화하는 작업 등을 수행할 수 있습니다.
4. **데이터 결과 저장**: 처리된 데이터를 원하는 형식으로 저장합니다. 예를 들어, 파일이나 데이터베이스에 저장할 수 있습니다.
5. **작업 실행**: `ExecutionEnvironment`의 `execute` 메서드를 호출하여 배치 작업을 실행합니다.

다음은 아파치 플링크의 배치 API를 사용한 예제 코드입니다.

```java
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.api.java.DataSet;

public class BatchJob {
  public static void main(String[] args) throws Exception {
    // 환경 설정
    ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
    
    // 데이터 소스 설정
    DataSet<String> input = env.readTextFile("path/to/input/file.txt");
    
    // 변환 및 연산
    DataSet<String> filtered = input.filter(line -> line.contains("apple"));
    DataSet<Tuple2<String, Integer>> counts = filtered.map(line -> new Tuple2<>(line, 1))
                                                     .groupBy(0)
                                                     .sum(1);
    
    // 데이터 결과 저장
    counts.writeAsCsv("path/to/output/file.csv", "\n", ",");
    
    // 작업 실행
    env.execute("Batch Job");
  }
}
```

이 예제는 입력 파일에서 "apple"을 포함한 줄을 필터링하고, 각 단어의 출현 횟수를 계산한 후 결과를 CSV 파일로 저장하는 간단한 배치 작업을 수행합니다.

## 결론

아파치 플링크의 배치 API를 사용하면 대량의 데이터를 처리하는 작업을 효율적으로 수행할 수 있습니다. 배치 API는 데이터 소스 설정, 변환 및 연산, 데이터 결과 저장의 단계로 구성되어 있으며, 작업 실행을 통해 배치 작업을 실행할 수 있습니다. 이를 통해 아파치 플링크를 사용하여 배치 처리 작업을 수행할 수 있습니다.

참고 문서: [아파치 플링크 공식 문서](https://flink.apache.org/)