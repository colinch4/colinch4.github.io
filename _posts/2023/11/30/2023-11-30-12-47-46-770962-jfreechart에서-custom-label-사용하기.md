---
layout: post
title: "[java] JFreeChart에서 Custom Label 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java 기반의 강력한 차트 생성 라이브러리로, 다양한 유형의 그래프와 차트를 생성할 수 있습니다. JFreeChart를 사용하면 축(Label)에 표시되는 값들을 사용자화할 수 있습니다.

이번 블로그 포스트에서는 JFreeChart를 사용하여 축에 사용자 정의 라벨을 표시하는 방법을 알아보겠습니다.

## 1. 축에 사용자 정의 라벨 추가하기

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.CategoryAxis;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.data.category.CategoryDataset;
import org.jfree.data.category.DefaultCategoryDataset;

public class CustomLabelExample {

    public static void main(String[] args) {
        // 데이터셋 생성
        CategoryDataset dataset = createDataset();

        // 차트 생성
        JFreeChart chart = ChartFactory.createBarChart(
                "Custom Label Example", // 차트 제목
                "Category", // x축 라벨
                "Value", // y축 라벨
                dataset, // 데이터셋
                PlotOrientation.VERTICAL, // 그래프 방향
                true, // 범례 표시 여부
                true, // 툴팁 표시 여부
                false // URL 링크 표시 여부
        );

        // x축에 사용자 정의 라벨 추가
        CategoryAxis domainAxis = ((XYPlot) chart.getPlot()).getDomainAxis();
        domainAxis.setTickLabelsVisible(false);
        domainAxis.setTickMarksVisible(false);
        domainAxis.setCategoryLabelPositions(CategoryLabelPositions.UP_45);

        // 차트를 패널에 추가
        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new java.awt.Dimension(500, 300));
        setContentPane(chartPanel);
    }

    private static CategoryDataset createDataset() {
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        dataset.addValue(1, "Series 1", "A");
        dataset.addValue(2, "Series 1", "B");
        dataset.addValue(3, "Series 1", "C");
        dataset.addValue(4, "Series 1", "D");
        dataset.addValue(5, "Series 1", "E");
        return dataset;
    }
}
```

## 2. 축에 라벨 관련 설정하기

위 예제에서는 x축에 사용자 정의 라벨을 추가하는 방법을 살펴보았습니다. 모든 라벨을 표시하지 않고, 가독성을 높이기 위해 일부 라벨만 표시하고 회전시켜 표시하도록 설정했습니다.

`domainAxis.setTickLabelsVisible(false)`를 사용하여 모든 라벨을 숨김 처리하고, `CategoryLabelPositions.UP_45`를 사용하여 라벨을 45도로 회전시킵니다. 이를 통해 그래프의 축에 가독성 높은 사용자 정의 라벨을 추가할 수 있습니다.

## 3. 결론

JFreeChart를 사용하면 축에 사용자 정의 라벨을 표시할 수 있습니다. 위 예제를 참고하여 필요한 라벨을 추가하고, 라벨 관련 설정을 변경하여 원하는 모양으로 그래프를 커스터마이징할 수 있습니다.

## 참고 자료

- [JFreeChart 공식 홈페이지](https://www.jfree.org/jfreechart/)