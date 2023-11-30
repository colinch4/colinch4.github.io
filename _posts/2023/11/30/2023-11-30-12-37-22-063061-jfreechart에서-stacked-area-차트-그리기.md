---
layout: post
title: "[java] JFreeChart에서 Stacked Area 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java에서 사용할 수 있는 강력한 차트 라이브러리입니다. 이 라이브러리를 사용하여 Stacked Area 차트를 그리는 방법에 대해 알아보겠습니다.

## 1. JFreeChart 라이브러리 가져오기

먼저, 프로젝트에 JFreeChart 라이브러리를 추가해야 합니다. Maven을 사용하는 경우 `pom.xml` 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.jfree</groupId>
    <artifactId>jfreechart</artifactId>
    <version>1.5.3</version>
</dependency>
```

## 2. Stacked Area 차트 생성하기

다음은 Stacked Area 차트를 생성하는 예제 코드입니다:

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.data.category.DefaultCategoryDataset;

public class StackedAreaChartExample {
    public static void main(String[] args) {
        // 데이터셋 생성
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();

        // 데이터 추가
        dataset.addValue(1, "Series 1", "Category 1");
        dataset.addValue(2, "Series 1", "Category 2");
        dataset.addValue(3, "Series 1", "Category 3");
        dataset.addValue(4, "Series 1", "Category 4");

        dataset.addValue(2, "Series 2", "Category 1");
        dataset.addValue(4, "Series 2", "Category 2");
        dataset.addValue(6, "Series 2", "Category 3");
        dataset.addValue(8, "Series 2", "Category 4");

        dataset.addValue(3, "Series 3", "Category 1");
        dataset.addValue(6, "Series 3", "Category 2");
        dataset.addValue(9, "Series 3", "Category 3");
        dataset.addValue(12, "Series 3", "Category 4");

        // 차트 생성
        JFreeChart chart = ChartFactory.createStackedAreaChart(
                "Stacked Area Chart", // 차트 타이틀
                "Category", // X축 레이블
                "Value", // Y축 레이블
                dataset // 데이터셋
        );

        // 차트를 화면에 보여주기
        ChartFrame frame = new ChartFrame("Stacked Area Chart Example", chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위의 코드는 Stacked Area 차트를 생성하고 데이터를 추가하는 간단한 예제입니다. `DefaultCategoryDataset` 클래스를 사용하여 데이터셋을 생성하고, `ChartFactory.createStackedAreaChart` 메소드를 호출하여 차트를 생성합니다. 마지막으로, `ChartFrame`을 사용하여 차트를 화면에 보여줍니다.

이제 코드를 실행하면 Stacked Area 차트가 생성되며 화면에 표시됩니다.

## 참고 자료

- [JFreeChart 공식 홈페이지](https://www.jfree.org/jfreechart/)
- [JFreeChart API 문서](https://www.jfree.org/jfreechart/api/)