---
layout: post
title: "[java] JFreeChart에서 Custom Renderer 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java 기반의 오픈 소스 라이브러리로, 다양한 그래프를 생성하고 표시하는 기능을 제공합니다. 이번 글에서는 JFreeChart에서 Custom Renderer를 사용하여 그래프를 커스터마이징하는 방법에 대해 알아보겠습니다.

### Custom Renderer란?

Custom Renderer는 JFreeChart에서 그래프의 요소들을 사용자 정의하여 그려주는 역할을 합니다. 기본적으로 제공되는 Renderer를 사용하여 그래프를 그리는 것도 가능하지만, Custom Renderer를 사용하면 그래프를 더욱 다양하고 개성있게 표현할 수 있습니다.

### Custom Renderer 생성하기

Custom Renderer를 생성하기 위해서는 다음과 같은 과정을 따를 수 있습니다:

1. `AbstractXYItemRenderer` 클래스를 상속하는 새로운 클래스를 생성합니다.
2. `drawItem()` 메서드를 오버라이딩하여 그래프 요소들을 원하는 대로 그립니다.
3. 필요한 설정 및 데이터를 처리하기 위해 `getItemRendererState()` 메서드를 오버라이딩할 수도 있습니다.

다음은 Custom Renderer 클래스의 예시입니다:

```java
import org.jfree.chart.renderer.xy.AbstractXYItemRenderer;
import org.jfree.chart.renderer.xy.XYItemRendererState;
import org.jfree.chart.plot.PlotRenderingInfo;
import org.jfree.chart.axis.ValueAxis;
import org.jfree.chart.plot.XYPlot;
import org.jfree.data.xy.XYDataset;
import java.awt.*;
import java.awt.geom.*;

public class CustomRenderer extends AbstractXYItemRenderer {

    public void drawItem(Graphics2D g2, XYItemRendererState state, Rectangle2D dataArea, PlotRenderingInfo info, XYPlot plot, ValueAxis domainAxis, ValueAxis rangeAxis, XYDataset dataset, int series, int item, CrosshairState crosshairState, int pass) {
        // 그래프 그리기 로직을 작성합니다.
        // 여기에 원하는 그래프 스타일 및 요소들을 그립니다.
    }

    public XYItemRendererState getItemRendererState() {
        // 필요한 설정 및 데이터 처리 로직을 작성합니다.
        // 필요한 경우, 유지할 상태 정보를 반환할 수도 있습니다.
        // 예: new XYItemRendererState();
    }
}
```

### Custom Renderer 적용하기

Custom Renderer를 사용하여 그래프를 그리기 위해서는 다음과 같은 과정을 따를 수 있습니다:

1. JFreeChart 객체를 생성합니다.
2. 사용할 Custom Renderer 객체를 생성합니다.
3. 생성한 Custom Renderer 객체를 JFreeChart 객체에 설정합니다.

다음은 Custom Renderer를 적용하는 예시입니다:

```java
import org.jfree.data.xy.DefaultXYDataset;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.plot.PlotOrientation;

// Custom Renderer 생성
CustomRenderer customRenderer = new CustomRenderer();

// JFreeChart 그래프 생성
JFreeChart chart = ChartFactory.createXYLineChart("My Chart", "X", "Y",
        new DefaultXYDataset(), PlotOrientation.VERTICAL, true, true, false);

// Custom Renderer 설정
chart.getXYPlot().setRenderer(customRenderer);

// 그래프를 출력하는 패널 생성
ChartPanel chartPanel = new ChartPanel(chart);

// 프레임에 패널 추가
frame.getContentPane().add(chartPanel);
```

위의 예시를 통해 Custom Renderer를 사용하여 JFreeChart에서 그래프를 커스터마이징하는 방법을 알아보았습니다. Custom Renderer를 사용하면 그래프의 다양한 스타일과 요소를 개별적으로 컨트롤할 수 있게 되므로, 원하는 그래프 출력을 구현하는 데 유용합니다.

### 참고 자료

- JFreeChart 공식 문서: [https://www.jfree.org/jfreechart/](https://www.jfree.org/jfreechart/)
- JFreeChart 예제 코드: [https://www.jfree.org/jfreechart/samples.html](https://www.jfree.org/jfreechart/samples.html)