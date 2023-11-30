---
layout: post
title: "[java] JFreeChart에서 Dual Axis Layered 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java 기반의 강력한 차트 그리기 라이브러리입니다. 이 라이브러리를 사용하면 다양한 유형의 차트를 생성할 수 있습니다. 이번 글에서는 JFreeChart를 사용하여 Dual Axis Layered 차트를 그리는 방법에 대해 알아보겠습니다.

## 1. JFreeChart 설치

JFreeChart를 사용하기 위해서는 먼저 JFreeChart 라이브러리를 다운로드하고 설치해야 합니다. 다음 링크를 통해 JFreeChart의 메인 페이지에 접속하여 라이브러리를 다운로드할 수 있습니다.

[JFreeChart 다운로드](https://www.jfree.org/jfreechart/download.html)

## 2. Dual Axis Layered 차트 그리기

Dual Axis Layered 차트는 두 가지 다른 데이터 유형을 함께 표시하는 차트입니다. 예를 들어, 한 축에는 온도 데이터를, 다른 축에는 습도 데이터를 나타낼 수 있습니다. 이러한 차트를 그리기 위한 코드 예제를 살펴보겠습니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.axis.ValueAxis;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.time.TimeSeries;
import org.jfree.data.time.TimeSeriesCollection;
import org.jfree.data.xy.XYDataset;
import org.jfree.ui.ApplicationFrame;

import java.awt.*;
import java.text.SimpleDateFormat;

public class DualAxisLayeredChartExample extends ApplicationFrame {

    public DualAxisLayeredChartExample(String title) {
        super(title);

        // 데이터 생성
        TimeSeries temperatureSeries = new TimeSeries("Temperature");
        temperatureSeries.add(new Minute(0, 0, 7, 12, 2003), 20.0);
        temperatureSeries.add(new Minute(30, 12, 7, 12, 2003), 25.0);
        temperatureSeries.add(new Minute(60, 22, 7, 12, 2003), 22.0);
        TimeSeriesCollection temperatureDataset = new TimeSeriesCollection();
        temperatureDataset.addSeries(temperatureSeries);

        TimeSeries humiditySeries = new TimeSeries("Humidity");
        humiditySeries.add(new Minute(0, 0, 7, 12, 2003), 50.0);
        humiditySeries.add(new Minute(30, 12, 7, 12, 2003), 55.0);
        humiditySeries.add(new Minute(60, 22, 7, 12, 2003), 45.0);
        TimeSeriesCollection humidityDataset = new TimeSeriesCollection();
        humidityDataset.addSeries(humiditySeries);

        // 차트 생성
        JFreeChart chart = ChartFactory.createTimeSeriesChart(
                "Dual Axis Layered Chart",  // 타이틀
                "Time",                     // X축 라벨
                "Temperature (°C)",         // 첫 번째 Y축 라벨
                temperatureDataset,         // 온도 데이터셋
                true,                       // 레전드 표시여부
                true,                       // 툴팁 표시여부
                false                       // URL 링크 표시여부
        );

        // 차트 스타일 설정
        XYPlot plot = chart.getXYPlot();
        plot.setDataset(1, humidityDataset);
        ValueAxis humidityAxis = new NumberAxis("Humidity (%)");  // 두 번째 Y축 라벨
        plot.setRangeAxis(1, humidityAxis);
        plot.mapDatasetToRangeAxis(1, 1);

        // 두 번째 데이터셋에 대한 라인과 포인트 설정
        XYLineAndShapeRenderer renderer2 = new XYLineAndShapeRenderer();
        renderer2.setSeriesPaint(0, Color.BLUE);
        plot.setRenderer(1, renderer2);

        // 차트 패널 생성
        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new Dimension(800, 400));
        setContentPane(chartPanel);
    }

    public static void main(String[] args) {
        DualAxisLayeredChartExample example = new DualAxisLayeredChartExample("Dual Axis Layered Chart Example");
        example.pack();
        example.setVisible(true);
    }
}
```

위 코드는 Dual Axis Layered 차트를 생성하는 Java 코드입니다. `Temperature` 데이터와 `Humidity` 데이터를 생성하여 각각의 Time Series 데이터셋에 추가하고, 다른 축에 대한 설정을 수행합니다.

## 3. 실행 결과

위의 코드를 실행하면 다음과 같은 Dual Axis Layered 차트를 그릴 수 있습니다.

![Dual Axis Layered Chart](chart.png)

위의 실행 결과에서는 온도 데이터를 나타내는 첫 번째 Y축과 습도 데이터를 나타내는 두 번째 Y축이 함께 표시되고 있습니다.

## 4. 결론

JFreeChart를 사용하여 Dual Axis Layered 차트를 그리는 방법에 대해 알아보았습니다. JFreeChart를 사용하면 간단하게 다양한 유형의 차트를 구현할 수 있으며, Dual Axis Layered 차트는 두 가지 다른 데이터 유형을 함께 표시하는데 유용합니다.