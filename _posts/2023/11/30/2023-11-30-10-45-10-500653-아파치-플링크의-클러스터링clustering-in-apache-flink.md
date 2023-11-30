---
layout: post
title: "[java] 아파치 플링크의 클러스터링(Clustering in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

아파치 플링크(Apache Flink)는 대규모 데이터 처리 및 분석을 위한 분산 처리 프레임워크입니다. 클러스터링은 플링크 애플리케이션을 실행하기 위해 여러 대의 컴퓨터를 사용하는 과정입니다. 이번 포스트에서는 아파치 플링크에서의 클러스터링에 대해 알아보겠습니다.

## 클러스터링 방식

아파치 플링크에서는 다양한 클러스터링 방식을 지원합니다. 가장 일반적인 방식은 스탠드얼론(Standalone) 클러스터링입니다. 이 방식은 플링크 애플리케이션을 실행하는 데 필요한 모든 리소스를 자체적으로 가지고 있는 독립적인 클러스터를 구성하는 것입니다.

또한 아파치 메소스(Mesos), 애니메시(Animesh)와 같은 분산 시스템 매니저와의 통합도 가능합니다. 이러한 방식은 플링크 애플리케이션을 실행하기 위해 클러스터 매니저를 사용하는 오픈 소스 프레임워크를 사용하는 경우에 유용합니다.

## 스탠드얼론 클러스터 설정

스탠드얼론 클러스터링을 사용하기 위해서는 다음과 같은 단계를 따라야 합니다.

1. 플링크가 설치된 컴퓨터에서 `start-cluster.sh` 스크립트를 실행하여 스탠드얼론 클러스터를 시작합니다.
2. 클러스터를 통제하는 웹 인터페이스인 Flink 대시보드에 접속하여 클러스터 상태를 모니터링할 수 있습니다.
3. 플링크 애플리케이션을 제출하기 위해 `flink run` 명령을 사용합니다.

```java
// 예시 플링크 애플리케이션 코드
import org.apache.flink.api.java.ExecutionEnvironment;
import org.apache.flink.api.java.DataSet;

public class WordCount {
    public static void main(String[] args) throws Exception {
        // 실행 환경 설정
        final ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();

        // 데이터 소스 읽기
        DataSet<String> text = env.fromElements("Apache", "Flink", "is", "awesome");

        // 단어 카운트
        DataSet<Tuple2<String, Integer>> counts = text.flatMap((String line, Collector<Tuple2<String, Integer>> out) -> {
            for (String word : line.split(" ")) {
                out.collect(new Tuple2<>(word, 1));
            }
        }).groupBy(0).sum(1);

        // 결과 출력
        counts.print();
    }
}
```

## 참고 자료

- [아파치 플링크 공식 문서](https://flink.apache.org/)
- [아파치 메소스 공식 사이트](http://mesos.apache.org/)
- [애니메시 공식 깃허브](https://github.com/animesh-project/animesh)