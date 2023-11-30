---
layout: post
title: "[java] JFreeChart에서 Custom Legend 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 다양한 차트를 생성하기 위한 Java 기반의 오픈 소스 라이브러리입니다. 이 라이브러리를 사용하면 다양한 유형의 차트를 손쉽게 생성하고 커스터마이징할 수 있습니다. 이 글에서는 JFreeChart에서 차트의 범례(Legend)를 커스터마이징하는 방법에 대해 알아보겠습니다.

## 범례(Legend)란?

범례는 차트에서 각 시리즈(series)에 대한 식별을 제공하는 역할을 합니다. 보통 범례는 차트의 오른쪽에 위치하며, 시리즈의 색상/마커와 해당 시리즈의 이름을 표시합니다. 하지만 때로는 범례를 더욱 자유롭게 디자인하고 싶을 수 있으며, 이를 위해 JFreeChart에서 제공하는 기본 범례 스타일 이외에도 사용자 정의 범례를 만들 수 있습니다.

## Custom Legend 만들기

JFreeChart에서 Custom Legend를 만들기 위해서는 LegendItemSource 인터페이스를 구현해야 합니다. 이 인터페이스는 범례 아이템(LegendItem)의 목록을 반환하는 메소드를 제공합니다. 다음은 Custom Legend를 만들기 위한 간단한 예제 코드입니다.

```java
import org.jfree.chart.LegendItem;
import org.jfree.chart.LegendItemSource;
import java.awt.Color;
import java.util.ArrayList;
import java.util.List;

public class CustomLegend implements LegendItemSource {

    @Override
    public LegendItemCollection getLegendItems() {
        LegendItemCollection legendItems = new LegendItemCollection();
        
        // Custom Legend 아이템 추가
        legendItems.add(new LegendItem("시리즈 1", new Color(255, 0, 0)));
        legendItems.add(new LegendItem("시리즈 2", new Color(0, 255, 0)));
        legendItems.add(new LegendItem("시리즈 3", new Color(0, 0, 255)));
        
        return legendItems;
    }
}
```

위 코드에서 CustomLegend 클래스는 LegendItemSource 인터페이스를 구현합니다. getLegendItems() 메소드에서는 Custom Legend에 표시할 범례 아이템을 생성하고 LegendItemCollection에 추가합니다. 이 예제에서는 시리즈 이름과 색상을 직접 지정하였습니다.

## Custom Legend 적용하기

Custom Legend를 적용하기 위해서는 JFreeChart 생성 후 setLegend() 메소드를 사용하여 CustomLegend 객체를 설정해야 합니다. 다음은 Custom Legend를 적용하는 예제 코드입니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public class CustomLegendExample {

    public static void main(String[] args) {
        XYSeries series1 = new XYSeries("시리즈 1");
        series1.add(1, 2);
        series1.add(2, 3);
        series1.add(3, 4);
        
        XYSeries series2 = new XYSeries("시리즈 2");
        series2.add(1, 1);
        series2.add(2, 2);
        series2.add(3, 3);
        
        XYSeries series3 = new XYSeries("시리즈 3");
        series3.add(1, 5);
        series3.add(2, 4);
        series3.add(3, 3);
        
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(series1);
        dataset.addSeries(series2);
        dataset.addSeries(series3);
        
        // CustomLegend 객체 생성
        CustomLegend customLegend = new CustomLegend();
        
        // JFreeChart 생성 후 CustomLegend 적용
        JFreeChart chart = ChartFactory.createXYLineChart(
                "Custom Legend Example",
                "X",
                "Y",
                dataset,
                PlotOrientation.VERTICAL,
                true,
                false,
                false
        );
        XYPlot plot = (XYPlot) chart.getPlot();
        plot.setRangeGridlinesVisible(true);
        plot.setDomainGridlinesVisible(true);
        chart.getLegend().setFrame(BlockBorder.NONE);
        
        // CustomLegend 적용
        chart.setLegend(customLegend);
        
        // 차트 출력
        ChartFrame frame = new ChartFrame("Custom Legend Example", chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위 예제 코드에서는 JFreeChart를 사용하여 XY Line 차트를 생성합니다. 각 시리즈의 데이터를 설정하고, CustomLegend 객체를 생성한 후 chart.setLegend() 메소드를 사용하여 Custom Legend를 적용합니다.

## 결론

JFreeChart에서 Custom Legend를 사용하면 차트의 범례를 자유롭게 디자인할 수 있습니다. CustomLegend 클래스를 구현하여 범례 아이템을 직접 정의한 후 JFreeChart에 적용하는 방식으로 Custom Legend를 사용할 수 있습니다. 이를 통해 차트의 가독성과 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료

- [JFreeChart 공식 웹사이트](http://www.jfree.org/jfreechart/)
- [JFreeChart GitHub 저장소](https://github.com/jfree/jfreechart)
- [JFreeChart CustomLegend Example](https://github.com/jfree/jfreechart/blob/master/source/org/jfree/chart/CustomLegendDemo1.java)