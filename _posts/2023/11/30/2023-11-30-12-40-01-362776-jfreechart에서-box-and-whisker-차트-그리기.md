---
layout: post
title: "[java] JFreeChart에서 Box And Whisker 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

## 개요
이 문서에서는 Java 프로그래밍 언어를 사용하여 JFreeChart 라이브러리를 이용하여 Box And Whisker 차트를 그리는 방법에 대해 알아보겠습니다.

## JFreeChart 라이브러리
JFreeChart는 Java에서 사용할 수 있는 오픈 소스 차트 그리기 라이브러리입니다. 다양한 차트 형식을 지원하며, 사용하기 쉬운 인터페이스를 제공합니다. JFreeChart는 많은 사람들에게 널리 사용되고 있으며, 다양한 환경에서 사용할 수 있습니다.

## Box And Whisker 차트란?
Box And Whisker 차트는 데이터의 분포를 시각적으로 나타내는 차트입니다. 상자는 데이터의 중앙값을 가리키며, 상자의 윗부분은 75%의 데이터를 나타냅니다. 상자의 아랫부분은 25%의 데이터를 나타냅니다. 상자의 위 아래로 그어진 선은 최솟값과 최댓값을 나타냅니다. 차트에는 이상치(outlier)가 있는 경우 좀 더 쉽게 파악할 수 있도록 표시됩니다.

## JFreeChart에서 Box And Whisker 차트 그리기
JFreeChart에서 Box And Whisker 차트를 그리기 위해서는 `BoxAndWhiskerChart` 클래스를 사용합니다. 다음은 Box And Whisker 차트를 그리는 예제 코드입니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.statistics.BoxAndWhiskerCategoryDataset;
import org.jfree.data.statistics.DefaultBoxAndWhiskerCategoryDataset;

public class BoxAndWhiskerChartExample {
    public static void main(String[] args) {
        // 데이터 생성
        DefaultBoxAndWhiskerCategoryDataset dataset = new DefaultBoxAndWhiskerCategoryDataset();
        dataset.add(BoxAndWhiskerValues, Category, Series);

        // 차트 생성
        JFreeChart chart = ChartFactory.createBoxAndWhiskerChart(
                Chart Title,
                Category Axis Label,
                Value Axis Label,
                BoxAndWhiskerCategoryDataset dataset,
                Show Legend);

        // 차트 프레임에 추가
        ChartFrame frame = new ChartFrame(Chart Title, chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위의 코드에서 `BoxAndWhiskerValues`, `Category`, `Series`, `Chart Title`, `Category Axis Label`, `Value Axis Label`, `Show Legend`에는 각각 필요한 값들을 지정해주어야 합니다. 데이터를 추가하고 차트를 생성한 후, `ChartFrame`을 사용하여 차트를 화면에 표시할 수 있습니다.

## 참고 자료
- [JFreeChart 공식 홈페이지](https://www.jfree.org/jfreechart/)
- [JFreeChart - BoxAndWhiskerChart 문서](https://www.jfree.org/jfreechart/api/javadoc/org/jfree/chart/ChartFactory.html#createBoxAndWhiskerChart(java.lang.String,%20java.lang.String,%20java.lang.String,%20org.jfree.data.statistics.BoxAndWhiskerCategoryDataset,%20boolean))
- [JFreeChart - DefaultBoxAndWhiskerCategoryDataset 문서](https://www.jfree.org/jfreechart/api/javadoc/org/jfree/data/statistics/DefaultBoxAndWhiskerCategoryDataset.html)