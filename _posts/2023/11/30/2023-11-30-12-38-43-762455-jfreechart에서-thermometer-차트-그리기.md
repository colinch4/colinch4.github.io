---
layout: post
title: "[java] JFreeChart에서 Thermometer 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java에서 사용할 수 있는 강력한 차트 라이브러리입니다. 이 라이브러리를 사용하면 다양한 종류의 차트를 그릴 수 있으며, 그 중 하나인 Thermometer 차트에 대해 알아보겠습니다.

## Thermometer 차트란?

Thermometer 차트는 열량, 온도 등과 같이 측정 값을 시각적으로 나타내기 위해 사용되는 차트입니다. 이 차트는 일반적으로 온도 계량기와 유사한 모양을 가지고 있으며, 값을 나타내는 색 바 또는 막대가 채워집니다.

## JFreeChart에서 Thermometer 차트 그리기

아래는 JFreeChart를 사용하여 Thermometer 차트를 그리는 예제입니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.ThermometerPlot;
import org.jfree.data.general.DefaultValueDataset;

public class ThermometerChartExample {
    public static void main(String[] args) {
        // 데이터셋 생성
        DefaultValueDataset dataset = new DefaultValueDataset(25.0);

        // ThermometerPlot 생성
        ThermometerPlot plot = new ThermometerPlot(dataset);
        plot.setSubrangeInfo(ThermometerPlot.NORMAL, 0.0, 50.0, 0.0, 40.0);
        plot.setSubrangeInfo(ThermometerPlot.CRITICAL, 50.0, 70.0, 40.0, 45.0);
        plot.setSubrangeInfo(ThermometerPlot.WARNING, 70.0, 100.0, 45.0, 50.0);

        // JFreeChart 생성
        JFreeChart chart = new JFreeChart("Thermometer Chart", plot);

        // 차트 프레임 생성 및 표시
        ChartFrame frame = new ChartFrame("Thermometer Chart", chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위의 예제 코드에서는 먼저 `DefaultValueDataset`을 사용하여 데이터셋을 생성합니다. 이 데이터셋은 Thermometer 차트에 표시할 값을 설정하는 데 사용됩니다.

그 다음 `ThermometerPlot`을 생성하고, `setSubrangeInfo` 메서드를 사용하여 차트의 각 색 구간과 범위 값을 설정합니다. 이 예제에서는 NORMAL, CRITICAL, WARNING 3가지 색 구간을 설정하였습니다.

마지막으로 `JFreeChart`를 생성하고, `ChartFrame`을 사용하여 차트를 프레임에 표시합니다.

## 실행 결과

위의 예제를 실행하면 Thermometer 차트가 생성되며, 데이터셋의 값을 기준으로 색 바의 높이가 변합니다.

![Thermometer 차트](thermometer_chart.png)

## 참고 자료

- [JFreeChart 공식 홈페이지](http://www.jfree.org/jfreechart/)