---
layout: post
title: "[java] JFreeChart에서 Custom Renderer 추가하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java로 작성된 강력한 차트 라이브러리입니다. 이 라이브러리를 사용하면 다양한 유형의 차트를 생성하고 사용자 정의를 적용할 수 있습니다.

여기서는 JFreeChart에서 Custom Renderer를 추가하는 방법에 대해 알아보겠습니다. Custom Renderer는 차트에 특정 데이터 요소를 사용자가 원하는 대로 그리는 데 사용됩니다.

## Custom Renderer 작성하기

Custom Renderer를 작성하려면 `org.jfree.chart.renderer.xy.AbstractXYItemRenderer` 클래스를 상속받는 클래스를 작성해야 합니다. 예를 들어, 선 그래프를 그리기 위한 Custom Renderer를 작성할 수 있습니다. 아래의 예제 코드를 참고해주세요.

```java
import org.jfree.chart.ChartRenderingInfo;
import org.jfree.chart.entity.EntityCollection;
import org.jfree.chart.plot.PlotRenderingInfo;
import org.jfree.chart.renderer.xy.AbstractXYItemRenderer;
import org.jfree.chart.renderer.xy.XYItemRendererState;
import org.jfree.chart.util.LineUtilities;
import org.jfree.data.xy.XYDataset;
import org.jfree.ui.RectangleEdge;

import java.awt.*;
import java.awt.geom.GeneralPath;
import java.awt.geom.Rectangle2D;

public class CustomLineRenderer extends AbstractXYItemRenderer {

    public CustomLineRenderer() {
        super();
    }

    @Override
    public void drawItem(Graphics2D g2, XYItemRendererState state, Rectangle2D dataArea, PlotRenderingInfo info, XYPlot plot,
                         ValueAxis domainAxis, ValueAxis rangeAxis, XYDataset dataset, int series, int item, CrosshairState crosshairState, int pass) {

        Paint paint = getItemPaint(series, item);
        Stroke stroke = getItemStroke(series, item);
        g2.setPaint(paint);
        g2.setStroke(stroke);

        // 데이터 점을 연결하는 선을 그립니다.
        if (item > 0) {
            double x1 = dataset.getXValue(series, item - 1);
            double y1 = dataset.getYValue(series, item - 1);
            double x2 = dataset.getXValue(series, item);
            double y2 = dataset.getYValue(series, item);
            RectangleEdge domainAxisEdge = plot.getDomainAxisEdge();
            RectangleEdge rangeAxisEdge = plot.getRangeAxisEdge();
            double transX1 = domainAxis.valueToJava2D(x1, dataArea, domainAxisEdge);
            double transY1 = rangeAxis.valueToJava2D(y1, dataArea, rangeAxisEdge);
            double transX2 = domainAxis.valueToJava2D(x2, dataArea, domainAxisEdge);
            double transY2 = rangeAxis.valueToJava2D(y2, dataArea, rangeAxisEdge);

            Shape line = LineUtilities.clipLine(new GeneralPath(transX1, transY1), new GeneralPath(transX2, transY2),
                    dataArea);
            if (line.intersects(dataArea)) {
                g2.draw(line);
            }

        }
    }
}
```

위의 코드에서 `drawItem` 메서드는 데이터 점을 연결하는 선을 그리는 로직을 담고 있습니다. 여기서는 간단한 선 그래프를 그리는 코드를 작성하였습니다.

## Custom Renderer 적용하기

Custom Renderer를 적용하려면 JFreeChart에서 사용하는 Renderer를 설정해야 합니다. `XYPlot` 객체를 가져온 후 `setRenderer` 메서드를 사용하여 Custom Renderer를 설정합니다. 예를 들어, 생성한 CustomLineRenderer를 사용하여 Line Chart에 Custom Renderer를 적용하려면 아래의 예제 코드를 참고해주세요.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.XYPlot;
import org.jfree.data.xy.XYDataset;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RefineryUtilities;

public class LineChartExample extends ApplicationFrame {

    public LineChartExample(String title) {
        super(title);
        XYDataset dataset = createDataset();
        JFreeChart chart = createChart(dataset);
        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new java.awt.Dimension(500, 270));
        setContentPane(chartPanel);
    }

    private XYDataset createDataset() {
        // 데이터셋 생성 로직
        // ...
    }

    private JFreeChart createChart(XYDataset dataset) {
        JFreeChart chart = ChartFactory.createXYLineChart(
                "Line Chart", "X", "Y", dataset);
        XYPlot plot = (XYPlot) chart.getPlot();
        plot.setRenderer(new CustomLineRenderer()); // Custom Renderer 적용
        return chart;
    }

    public static void main(String[] args) {
        LineChartExample example = new LineChartExample("Line Chart Example");
        example.pack();
        RefineryUtilities.centerFrameOnScreen(example);
        example.setVisible(true);
    }
}
```

위의 예제 코드에서 `createChart` 메서드에서 `plot.setRenderer(new CustomLineRenderer())`를 사용하여 Custom Renderer를 설정하였습니다.

## 결론

JFreeChart를 사용하면 Custom Renderer를 사용하여 차트에 원하는 대로 그리는 기능을 구현할 수 있습니다. Custom Renderer를 작성하고 적용함으로써 다양한 차트를 개발할 수 있습니다.

## 참고 문서
- [JFreeChart Custom Renderers](https://www.jfree.org/jfreechart/api/javadoc/org/jfree/chart/renderer/xy/AbstractXYItemRenderer.html)