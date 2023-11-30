---
layout: post
title: "[java] JFreeChart에서 Single Series 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java 언어로 작성된 오픈 소스 라이브러리로, 다양한 유형의 그래프와 차트를 생성할 수 있습니다. 이번 포스트에서는 JFreeChart를 사용하여 Single Series 차트를 그리는 방법을 알아보겠습니다.

## JFreeChart 설치하기

JFreeChart를 사용하려면 먼저 JFreeChart 라이브러리를 다운로드하고 설치해야 합니다. 아래는 Maven을 사용하여 JFreeChart를 추가하는 예시입니다. 필요한 경우 다른 의존성 관리 도구를 사용할 수도 있습니다.

```xml
<dependency>
    <groupId>org.jfree</groupId>
    <artifactId>jfreechart</artifactId>
    <version>1.5.3</version>
</dependency>
```

## Single Series 차트 그리기

Single Series 차트는 하나의 데이터 시리즈에 대한 그래프를 나타내는 차트입니다. 아래는 JFreeChart를 사용하여 Single Series 차트를 그리는 간단한 예제 코드입니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.data.general.DefaultPieDataset;
import javax.swing.JFrame;

public class SingleSeriesChartExample {
    public static void main(String[] args) {
        // 데이터 생성
        DefaultPieDataset dataset = new DefaultPieDataset();
        dataset.setValue("Apple", 60);
        dataset.setValue("Banana", 30);
        dataset.setValue("Orange", 10);
        
        // 차트 생성
        JFreeChart chart = ChartFactory.createPieChart("Fruit Distribution", dataset);
        
        // 차트를 화면에 표시
        ChartFrame frame = new ChartFrame("Single Series Chart", chart);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위의 코드에서는 `DefaultPieDataset`을 사용하여 데이터를 생성하고, `ChartFactory.createPieChart`를 통해 Pie 차트를 생성합니다. 마지막으로 `ChartFrame`을 사용하여 차트를 화면에 표시합니다.

## 차트 커스터마이징하기

JFreeChart는 다양한 방법을 제공하여 차트를 커스터마이징할 수 있습니다. 예를 들어, 차트의 색상, 레이블, 범례 등을 변경할 수 있습니다. 또한, 여러 유형의 차트를 선택할 수도 있습니다.

자세한 내용은 JFreeChart 문서나 예제 코드를 참고하시기 바랍니다.

## 참고 자료

- JFreeChart 공식 사이트: [https://www.jfree.org/jfreechart/](https://www.jfree.org/jfreechart/)
- JFreeChart 예제 코드: [https://github.com/jfree/jfreechart](https://github.com/jfree/jfreechart)

위의 링크에서 JFreeChart에 대한 더 자세한 정보와 다른 차트 유형에 대한 예제 코드를 확인할 수 있습니다.