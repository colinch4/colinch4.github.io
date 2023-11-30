---
layout: post
title: "[java] JFreeChart에서 Multiple Series 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java 기반의 오픈 소스 라이브러리로서, 다양한 유형의 차트를 생성할 수 있는 강력한 기능을 제공합니다. 이러한 라이브러리를 사용하여 Multiple Series(다중 시리즈) 차트를 그리는 방법을 알아보겠습니다.

## 1. JFreeChart 라이브러리 추가하기

먼저, 프로젝트에 JFreeChart 라이브러리를 추가해야 합니다. 이를 위해 Maven이나 Gradle 등의 의존성 관리 도구를 사용하거나, JFreeChart의 공식 웹사이트에서 JAR 파일을 다운로드하여 직접 추가할 수 있습니다.

## 2. 데이터 설정하기

다중 시리즈 차트를 그리기 위해서는 그래프에 표시될 데이터를 설정해야 합니다. 각 시리즈는 X축 값과 Y축 값을 가지며, 이러한 값들을 데이터셋에 추가해야 합니다.

```java
DefaultCategoryDataset dataset = new DefaultCategoryDataset();
dataset.addValue(10, "Series 1", "Category 1");
dataset.addValue(15, "Series 1", "Category 2");
dataset.addValue(20, "Series 2", "Category 1");
dataset.addValue(25, "Series 2", "Category 2");
```

위의 예시에서는 "Series 1"과 "Series 2"라는 두 개의 시리즈를 설정하고, 각 시리즈에 대한 X축 카테고리 값과 Y축 값들을 추가했습니다.

## 3. 차트 생성하기

데이터셋을 생성한 후에는 JFreeChart 객체를 생성하여 차트를 그릴 준비를 해야 합니다. `ChartFactory.createBarChart()` 메서드를 사용하여 바 차트를 생성할 수 있습니다.

```java
JFreeChart chart = ChartFactory.createBarChart(
   "Multiple Series Chart",  // 차트 제목
   "Category",  // X축 라벨
   "Value",  // Y축 라벨
   dataset,  // 데이터셋
   PlotOrientation.VERTICAL,  // 차트 방향
   true,  // 범례 사용 여부
   true,  // 툴팁 사용 여부
   false  // URL 사용 여부
);
```

## 4. 차트 스타일 설정하기

생성한 차트에 대해 필요한 스타일 설정을 할 수 있습니다. 다중 시리즈 차트의 경우, 각 시리즈별로 다른 색상을 사용하여 구분할 수 있습니다.

```java
CategoryPlot plot = chart.getCategoryPlot();
CategoryItemRenderer renderer = plot.getRenderer();
renderer.setSeriesPaint(0, Color.red);  // 첫 번째 시리즈 색상
renderer.setSeriesPaint(1, Color.blue);  // 두 번째 시리즈 색상
```

위의 예시에서는 첫 번째 시리즈를 빨간색으로, 두 번째 시리즈를 파란색으로 설정하였습니다.

## 5. 차트 출력하기

마지막으로, 생성한 차트를 출력하여 화면에 표시할 수 있습니다.

```java
ChartPanel chartPanel = new ChartPanel(chart);
chartPanel.setPreferredSize(new java.awt.Dimension(500, 300));
```

위의 예시는 차트를 JPanel에 추가하고, 차트 패널의 크기를 설정한 것입니다. 이렇게 설정한 차트 패널을 원하는 컨테이너에 추가하면 차트가 출력됩니다.

## 결론

이렇게 JFreeChart를 사용하여 Multiple Series 차트를 그릴 수 있습니다. 데이터셋을 설정하고, 차트를 생성하며, 필요한 스타일을 적용하여 다양한 차트를 만들 수 있습니다. JFreeChart의 다양한 기능과 옵션을 활용하여 프로젝트에 맞는 멋진 차트를 구현해보세요.

## 참고 자료

- [JFreeChart 공식 웹사이트](https://www.jfree.org/jfreechart/)
- [JFreeChart 다중 시리즈 차트 예제](https://www.jfree.org/jfreechart/samples.html)