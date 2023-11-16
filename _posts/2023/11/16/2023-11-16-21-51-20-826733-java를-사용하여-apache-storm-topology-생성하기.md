---
layout: post
title: "[java] Java를 사용하여 Apache Storm Topology 생성하기"
description: " "
date: 2023-11-16
tags: [java]
comments: true
share: true
---

Apache Storm은 대규모 실시간 데이터 처리를 위한 분산 컴퓨팅 플랫폼입니다. Storm Topology는 Storm 클러스터에서 실행되는 데이터 처리 작업의 그래프입니다. 이 문서에서는 Java를 사용하여 간단한 Storm Topology를 생성하는 방법을 알아보겠습니다.

## 필요한 의존성 추가하기

먼저, Maven 또는 Gradle과 같은 빌드 도구를 사용하여 프로젝트에 Apache Storm 의존성을 추가해야 합니다. 다음은 Maven을 사용하는 경우의 예입니다.

```xml
<dependencies>
    <dependency>
        <groupId>org.apache.storm</groupId>
        <artifactId>storm-core</artifactId>
        <version>2.2.0</version>
    </dependency>
</dependencies>
```

## Topology 클래스 생성하기

다음으로, Topology 클래스를 생성해야 합니다. 이 클래스는 Storm Topology의 구조를 정의하고 처리 작업을 설정합니다. 아래는 간단한 Topology 클래스의 예입니다.

```java
import org.apache.storm.Config;
import org.apache.storm.LocalCluster;
import org.apache.storm.topology.TopologyBuilder;

public class MyTopology {

    public static void main(String[] args) throws Exception {
        // Topology 생성
        TopologyBuilder builder = new TopologyBuilder();

        // Bolt 및 Spout 추가
        builder.setSpout("spout", new MySpout());
        builder.setBolt("bolt", new MyBolt()).shuffleGrouping("spout");

        // Config 설정
        Config config = new Config();
        config.setDebug(true);

        // LocalCluster 생성 및 실행
        LocalCluster cluster = new LocalCluster();
        cluster.submitTopology("my-topology", config, builder.createTopology());

        // 종료 대기
        Thread.sleep(5000);

        // Topology 종료
        cluster.killTopology("my-topology");
        cluster.shutdown();
    }
}
```

이 코드에서는 `MySpout`와 `MyBolt`라는 사용자 정의 Spout와 Bolt를 생성하여 Topology에 추가하고 있습니다.

## Spout 및 Bolt 클래스 생성하기

마지막으로, 사용자 정의 Spout와 Bolt 클래스를 구현해야 합니다. Spout는 데이터를 생성하여 Bolt에 전달하는 역할을 하고, Bolt는 받은 데이터를 처리하는 역할을 합니다. 아래는 간단한 Spout와 Bolt 클래스의 예입니다.

```java
import org.apache.storm.spout.SpoutOutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichSpout;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Values;
import org.apache.storm.utils.Utils;

import java.util.Map;

public class MySpout extends BaseRichSpout {

    private SpoutOutputCollector collector;

    @Override
    public void open(Map conf, TopologyContext context, SpoutOutputCollector collector) {
        this.collector = collector;
    }

    @Override
    public void nextTuple() {
        Utils.sleep(1000);
        collector.emit(new Values("Hello, World!"));
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("message"));
    }
}

import org.apache.storm.task.OutputCollector;
import org.apache.storm.task.TopologyContext;
import org.apache.storm.topology.OutputFieldsDeclarer;
import org.apache.storm.topology.base.BaseRichBolt;
import org.apache.storm.tuple.Fields;
import org.apache.storm.tuple.Tuple;
import org.apache.storm.tuple.Values;

import java.util.Map;

public class MyBolt extends BaseRichBolt {

    private OutputCollector collector;

    @Override
    public void prepare(Map conf, TopologyContext context, OutputCollector collector) {
        this.collector = collector;
    }

    @Override
    public void execute(Tuple input) {
        String message = input.getStringByField("message");
        System.out.println("Received message: " + message);
        collector.emit(new Values(message.toUpperCase()));
        collector.ack(input);
    }

    @Override
    public void declareOutputFields(OutputFieldsDeclarer declarer) {
        declarer.declare(new Fields("message"));
    }
}
```

위의 코드에서는 `MySpout` 클래스가 "Hello, World!"라는 메시지를 생성하여 Bolt로 전달하고 있으며, `MyBolt` 클래스는 받은 메시지를 대문자로 변환한 후 출력합니다.

## Topology 실행하기

위에서 작성한 Topology를 실행하려면 다음 명령을 사용하면 됩니다.

```
$ storm jar my-topology.jar MyTopology
```

`my-topology.jar`는 Topology를 패키징한 JAR 파일의 경로입니다. 이 명령을 실행하면 Storm 클러스터에서 Topology를 실행하고 데이터 처리 과정을 확인할 수 있습니다.

## 결론

이 문서에서는 Java를 사용하여 Apache Storm Topology를 생성하는 방법에 대해 알아보았습니다. Storm를 사용하면 대규모 실시간 데이터 처리를 간편하게 수행할 수 있으며, Java를 통해 Topology를 생성하고 커스터마이징할 수 있습니다. 추가적인 자세한 내용은 [Apache Storm 공식 문서](https://storm.apache.org/documentation.html)를 참조하십시오.