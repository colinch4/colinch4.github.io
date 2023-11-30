---
layout: post
title: "[java] JFreeChart에서 Time Series Bar 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java에서 사용할 수 있는 강력한 차트 라이브러리입니다. 이 라이브러리를 사용하여 시계열 바 차트를 그리는 방법을 소개하겠습니다.

## 1. JFreeChart 라이브러리 추가하기
먼저, JFreeChart 라이브러리를 프로젝트에 추가해야합니다. 

Maven을 사용하는 경우, `pom.xml`에 다음 종속성을 추가하세요:

```xml
<dependencies>
    <dependency>
        <groupId>org.jfree</groupId>
        <artifactId>jfreechart</artifactId>
        <version>1.5.3</version>
    </dependency>
    <dependency>
        <groupId>org.jfree</groupId>
        <artifactId>jcommon</artifactId>
        <version>1.0.23</version>
    </dependency>
</dependencies>
```

Maven을 사용하지 않는 경우, JFreeChart를 [공식 웹사이트](https://www.jfree.org/jfreechart/)에서 다운로드하여 프로젝트 빌드 경로에 추가하세요.

## 2. Time Series Bar 차트 그리기

JFreeChart를 사용하여 Time Series Bar 차트를 그리려면 다음 단계를 따르세요:

### 2.1. 데이터 준비하기
시계열 데이터를 준비해야합니다. 이 예제에서는 일일 매출 데이터를 사용합니다.

```java
TimeSeries series = new TimeSeries("Daily Sales");
series.add(new Day(1, 1, 2022), 100);
series.add(new Day(2, 1, 2022), 150);
series.add(new Day(3, 1, 2022), 200);
// 추가 데이터 추가...

TimeSeriesCollection dataset = new TimeSeriesCollection();
dataset.addSeries(series);
```

### 2.2. 차트 생성하기
```java
JFreeChart chart = ChartFactory.createXYBarChart(
        "Time Series Bar Chart", // 차트 제목
        "Date", // X축 레이블
        false, // 레이블 타이틀의 가로 표시 여부
        "Sales", // Y축 레이블
        dataset, // 데이터셋
        PlotOrientation.VERTICAL, // 차트 방향
        true, // 범례 표시 여부
        true, // 툴팁 표시 여부
        false // URL 링크 표시 여부
);
```

### 2.3. 차트 커스터마이징하기
생성한 차트를 커스터마이징할 수 있습니다. 예를 들어, X축 레이블의 폰트를 변경하고, 차트 배경색을 설정하고, 그래프의 색상을 변경하는 등의 작업을 수행할 수 있습니다.

```java
CategoryPlot plot = (CategoryPlot) chart.getPlot();
plot.setBackgroundPaint(Color.WHITE);
plot.setRangeGridlinePaint(Color.BLACK);
plot.getDomainAxis().setTickLabelFont(new Font("SansSerif", Font.PLAIN, 12));

BarRenderer renderer = (BarRenderer) plot.getRenderer();
renderer.setSeriesPaint(0, Color.BLUE);
```

### 2.4. 차트 출력하기
```java
ChartFrame frame = new ChartFrame("Time Series Bar Chart", chart);
frame.pack();
frame.setVisible(true);
```

위 코드를 실행하면, Time Series Bar 차트가 생성되고 출력됩니다.

## 결론
JFreeChart를 사용하여 Java에서 Time Series Bar 차트를 그리는 방법을 배웠습니다. 이제 이 기술을 활용하여 다양한 시계열 데이터에 대한 차트를 만들 수 있습니다.

더 자세한 정보를 원하신다면, JFreeChart의 [공식 문서](https://www.jfree.org/jfreechart/api/)를 참고하세요.