---
layout: post
title: "[java] JFreeChart에서 Custom Label 추가하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java에서 사용할 수 있는 강력한 그래프 생성 라이브러리입니다. 이 라이브러리를 사용하여 그래프를 그릴 때, 축 레이블에 사용자 정의 레이블을 추가할 수 있습니다.

## 1. 그래프 생성

먼저, JFreeChart를 사용하여 그래프를 생성해야 합니다. 아래의 예제 코드를 통해 그래프를 생성하는 방법을 알아보겠습니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

public class ChartExample {

    public static void main(String[] args) {
        // 데이터셋 생성
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        dataset.addValue(1, "Series1", "Label1");
        dataset.addValue(2, "Series2", "Label2");
        dataset.addValue(3, "Series3", "Label3");
        
        // 그래프 생성
        JFreeChart chart = ChartFactory.createBarChart(
            "Chart Title",
            "Category Axis Label",
            "Value Axis Label",
            dataset,
            PlotOrientation.VERTICAL,
            true,
            true,
            false
        );
        
        // 차트 프레임 생성
        ChartFrame frame = new ChartFrame("Chart Example", chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위의 코드는 JFreeChart를 사용하여 바차트를 생성하는 간단한 예제입니다. `ChartFactory.createBarChart` 메서드를 사용하여 그래프를 생성하고, `ChartFrame`을 통해 그래프를 표시합니다.

## 2. Custom Label 추가

이제, 그래프의 축 레이블에 Custom Label을 추가해보겠습니다. 아래의 코드를 참고하여 레이블을 추가할 수 있습니다.

```java
import org.jfree.chart.axis.CategoryAxis;
import org.jfree.chart.axis.NumberAxis;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

public class CustomLabelExample {

    public static void main(String[] args) {
        // 데이터셋 생성
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        dataset.addValue(1, "Series1", "Label1");
        dataset.addValue(2, "Series2", "Label2");
        dataset.addValue(3, "Series3", "Label3");
        
        // 그래프 생성
        CategoryAxis categoryAxis = new CategoryAxis("Category Axis Label");
        NumberAxis numberAxis = new NumberAxis("Value Axis Label");
        
        CategoryPlot plot = new CategoryPlot(dataset, categoryAxis, numberAxis, null);
        JFreeChart chart = new JFreeChart("Chart Title", JFreeChart.DEFAULT_TITLE_FONT, plot, true);
        
        // Custom Label 추가
        categoryAxis.setTickLabelsVisible(false);
        categoryAxis.setCategoryLabelPositions(CategoryLabelPositions.UP_90); // 90도 회전
        
        // 차트 프레임 생성
        ChartFrame frame = new ChartFrame("Custom Label Example", chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위의 코드에서는 `CategoryAxis` 객체를 사용하여 카테고리 축의 레이블을 커스터마이징합니다. `setTickLabelsVisible(false)`를 통해 레이블을 숨기고, `setCategoryLabelPositions(CategoryLabelPositions.UP_90)`를 통해 레이블을 90도로 회전시킬 수 있습니다.

이제 위 코드를 실행하면, 그래프의 축 레이블이 숨겨지고 90도로 회전된 것을 확인할 수 있습니다.

JFreeChart의 자세한 사용법은 JFreeChart 공식 문서를 참고하시기 바랍니다.

## 참고 자료

- [JFreeChart 공식 사이트](https://www.jfree.org/jfreechart/)
- [JFreeChart API 문서](https://www.jfree.org/jfreechart/api-docs/index.html)