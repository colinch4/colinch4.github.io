---
layout: post
title: "[java] JFreeChart에서 Custom Marker 추가하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java 기반의 오픈소스 데이터 시각화 라이브러리로, 다양한 차트와 플롯을 생성할 수 있습니다. 이 라이브러리를 사용하면 데이터를 시각적으로 표현하여 분석 및 이해를 용이하게 할 수 있습니다. JFreeChart에는 데이터 포인트를 강조하기 위해 마커를 추가하는 기능이 제공되며, 이번 글에서는 JFreeChart에서 커스텀 마커를 추가하는 방법에 대해 알아보겠습니다.

## JFreeChart 마커

JFreeChart에서 마커(marker)는 특정한 데이터 포인트를 강조하기 위해 사용됩니다. 마커는 차트의 X축과 Y축에 위치하며, 이를 통해 특정 구간이나 이벤트 등을 시각적으로 표시할 수 있습니다. JFreeChart는 여러 종류의 마커를 제공하며, 사용자 정의 마커를 추가하는 것도 가능합니다.

## 커스텀 마커 추가하기

JFreeChart에서 커스텀 마커를 추가하는 방법은 다음과 같습니다.

1. Series 매개변수로 데이터를 포함하는 `XYSeries` 객체를 생성합니다.
2. `XYSeriesCollection` 객체를 생성하고, 앞서 생성한 `XYSeries` 객체를 추가합니다.
3. `XYLineAndShapeRenderer` 객체를 생성하고, 해당 객체에 커스텀 마커를 추가합니다.
4. `XYPlot` 객체를 생성하고, 앞서 생성한 `XYLineAndShapeRenderer` 객체를 설정합니다.
5. `JFreeChart` 객체를 생성하고, 앞서 생성한 `XYPlot` 객체를 설정합니다.
6. 생성한 `JFreeChart` 객체를 `ChartPanel`에 추가하고, 이를 `JFrame` 컨테이너에 추가합니다.

```java
import org.jfree.chart.*;
import org.jfree.chart.plot.*;
import org.jfree.data.xy.*;

public class CustomMarkerExample {

    public static void main(String[] args) {

        XYSeries series = new XYSeries("Data Series");
        series.add(1, 5);
        series.add(2, 3);
        series.add(3, 8);
        series.add(4, 2);
        series.add(5, 6);

        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(series);

        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();
        renderer.setSeriesShape(0, new Rectangle(-3, -3, 6, 6));

        XYPlot plot = new XYPlot(dataset, null, new NumberAxis("X Axis"), new NumberAxis("Y Axis"));
        plot.setRenderer(renderer);

        JFreeChart chart = new JFreeChart(plot);
        ChartPanel chartPanel = new ChartPanel(chart);
        JFrame frame = new JFrame("Custom Marker Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(chartPanel);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위 예제 코드는 `XYSeries`를 생성하고, 그래프에 커스텀 마커를 추가하는 방법을 보여줍니다. 마커 모양은 `Rectangle`로 설정되어 있으며, `-3`부터 `3`까지 좌표로 설정되어 있습니다.

이제 위 코드를 실행하면 차트에 커스텀 마커가 추가되어 데이터 포인트가 강조되는 것을 확인할 수 있습니다.

## 결론

JFreeChart는 데이터 시각화에 유용한 라이브러리로, 데이터 포인트를 강조하기 위해 커스텀 마커를 추가할 수 있습니다. 이를 통해 데이터를 보다 명확하게 표현하고 분석할 수 있습니다. 위에서 소개한 방법을 활용하여 JFreeChart에 커스텀 마커를 추가해보세요!