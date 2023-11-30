---
layout: post
title: "[java] JFreeChart에서 Clustered Bar 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 자바에서 사용할 수 있는 강력한 차트 그리기 라이브러리입니다. 이 라이브러리를 사용하여 Clustered Bar 차트를 그릴 수 있습니다. Clustered Bar 차트는 막대 그래프의 모음으로, 각 막대 그래프는 여러 그룹으로 구성됩니다.

## JFreeChart 설정

먼저, JFreeChart를 사용하기 위해 프로젝트의 의존성에 JFreeChart 라이브러리를 추가해야 합니다. Maven을 사용하는 경우, pom.xml 파일에 다음 의존성을 추가합니다:

```xml
<dependency>
    <groupId>org.jfree</groupId>
    <artifactId>jfreechart</artifactId>
    <version>1.5.3</version>
</dependency>
```

## Clustered Bar 차트 그리기

다음은 JFreeChart를 사용하여 Clustered Bar 차트를 그리는 예제 코드입니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

public class ClusteredBarChartExample {
    public static void main(String[] args) {
        // 데이터셋 생성
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        dataset.addValue(10, "Series 1", "Category 1");
        dataset.addValue(15, "Series 1", "Category 2");
        dataset.addValue(20, "Series 1", "Category 3");
        dataset.addValue(25, "Series 2", "Category 1");
        dataset.addValue(30, "Series 2", "Category 2");
        dataset.addValue(35, "Series 2", "Category 3");
        
        // 차트 생성
        JFreeChart chart = ChartFactory.createBarChart(
            "Clustered Bar Chart",  // 제목
            "Category",             // x축 레이블
            "Value",                // y축 레이블
            dataset,                // 데이터셋
            PlotOrientation.VERTICAL,// 차트 방향
            true,                   // 범례 표시 여부
            true,                   // 툴팁 표시 여부
            false                   // URL 생성 여부
        );
        
        // 차트 프레임 생성
        ChartFrame frame = new ChartFrame("Clustered Bar Chart Example", chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

## 실행 결과

위의 예제 코드를 실행하면 Clustered Bar 차트가 그려진 차트 윈도우가 표시됩니다. 이 차트는 데이터셋에 포함된 값에 따라 여러 그룹으로 구성된 막대 그래프를 보여줍니다.

## 참고 자료

- [JFreeChart 공식 홈페이지](https://www.jfree.org/jfreechart/)
- [JFreeChart API 문서](https://www.jfree.org/jfreechart/api/index.html)

JFreeChart를 사용하여 Clustered Bar 차트를 그리는 방법을 알아보았습니다. 이러한 차트를 사용하면 데이터의 그룹별 비교를 시각적으로 쉽게 할 수 있습니다.