---
layout: post
title: "[java] JFreeChart에서 Custom Marker 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 자바에서 사용할 수 있는 강력한 차트 라이브러리입니다. 이 라이브러리를 사용하면 다양한 종류의 차트를 생성하고, 데이터를 시각적으로 표현할 수 있습니다. 이번에는 JFreeChart에서 Custom Marker를 사용하는 방법에 대해 알아보겠습니다.

Custom Marker는 사용자가 원하는 특정 위치에 표식을 표시하는 기능입니다. 예를 들어, 특정 값 이상이나 이하일 때 그래프에 세로선이나 가로선을 그리는 등의 작업을 할 수 있습니다.

먼저 JFreeChart를 사용하기 위해서는 JFreeChart 라이브러리를 다운로드하고 프로젝트에 추가해야 합니다. JFreeChart의 최신 버전은 [공식 웹사이트](http://www.jfree.org/jfreechart/)에서 다운로드할 수 있습니다.

Custom Marker를 사용하기 위해서는 `Marker` 클래스와 `XYPlot` 클래스를 사용해야 합니다. 다음은 Custom Marker를 생성하고 그래프에 추가하는 예제 코드입니다.

```java
import org.jfree.chart.*;
import org.jfree.chart.plot.*;
import org.jfree.data.xy.*;

// 데이터 생성
XYSeries series = new XYSeries("Data");
series.add(1, 10);
series.add(2, 15);
series.add(3, 20);
series.add(4, 25);

XYSeriesCollection dataset = new XYSeriesCollection(series);

// 그래프 생성
JFreeChart chart = ChartFactory.createXYLineChart("Custom Marker Example", "X", "Y", dataset);

// XYPlot 객체 가져오기
XYPlot plot = (XYPlot) chart.getPlot();

// Custom Marker 생성
Marker marker = new ValueMarker(15);
marker.setPaint(Color.RED);

// Custom Marker 추가
plot.addDomainMarker(marker);

// 차트 출력
ChartFrame frame = new ChartFrame("Custom Marker Example", chart);
frame.setVisible(true);
frame.pack();
```

위 코드에서는 `ValueMarker`를 사용하여 Custom Marker를 생성합니다. `ValueMarker`의 생성자에는 Marker를 표시할 값(여기서는 15)을 전달합니다. 그리고 `setPaint()` 메서드를 사용하여 Marker의 색상을 설정합니다.

마지막으로, `plot` 객체의 `addDomainMarker()` 메서드를 사용하여 Custom Marker를 그래프에 추가합니다. 이렇게 하면 X축에서 지정한 값을 가지는 위치에 Marker가 표시됩니다.

위 코드를 실행하면 "Custom Marker Example"라는 제목의 그래프 창이 열리며, X축에서 값이 15인 위치에 빨간색 Marker가 표시됩니다.

이처럼 JFreeChart를 사용하여 Custom Marker를 생성하고 그래프에 추가하는 것은 매우 간단합니다. 자신의 데이터에 맞게 Marker를 조정하여 데이터의 경계나 특정 값을 시각적으로 표현하는 데 활용할 수 있습니다.

자세한 내용은 [JFreeChart 공식 문서](http://www.jfree.org/jfreechart/api/javadoc/)를 참고하시기 바랍니다.