---
layout: post
title: "[java] JFreeChart에서 Interval Bar 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java로 작성된 무료 차트 라이브러리로, 다양한 종류의 차트를 만들 수 있습니다. 이번에는 JFreeChart를 사용하여 Interval Bar 차트를 그리는 방법에 대해 알아보겠습니다.

## JFreeChart 설정

우선 JFreeChart를 사용하기 위해 프로젝트에 JFreeChart 라이브러리를 추가해야 합니다. 아래는 Maven을 사용하는 경우, `pom.xml` 파일에 의존성을 추가하는 예시입니다.

```xml
<dependency>
    <groupId>org.jfree</groupId>
    <artifactId>jfreechart</artifactId>
    <version>1.5.3</version>
</dependency>
```

## 차트 데이터 생성

Interval Bar 차트를 그리기 위해서는 데이터를 생성해야 합니다. 각각의 막대는 시작과 끝 값을 가지고 있으며, 그 사이의 범위를 나타냅니다. 예를 들어, 한 주간의 온도 범위를 표현하는 차트를 그린다고 가정해봅시다.

```java
DefaultIntervalCategoryDataset dataset = new DefaultIntervalCategoryDataset();

// 데이터 추가
dataset.add(start, end, series, category);
```

위의 코드에서 `start`와 `end`는 각각 막대의 시작과 끝 값을 나타내며, `series`는 막대의 시리즈 이름, `category`는 막대의 카테고리(주로 x축 값)입니다. 차트에 표시할 데이터에 따라 데이터셋에 추가하여 사용할 수 있습니다.

## Interval Bar 차트 생성

데이터셋을 생성한 후에는 이를 사용하여 Interval Bar 차트를 생성할 수 있습니다. 아래는 차트의 기본 설정과 데이터셋을 사용하여 차트를 생성하는 예시입니다.

```java
CategoryAxis xAxis = new CategoryAxis(); // x축 객체 생성
NumberAxis yAxis = new NumberAxis(); // y축 객체 생성

IntervalBarRenderer renderer = new IntervalBarRenderer(); // 차트 렌더러 객체 생성

// 차트 객체 생성
JFreeChart chart = new JFreeChart("Interval Bar Chart", JFreeChart.DEFAULT_TITLE_FONT, 
    new CategoryPlot(dataset, xAxis, yAxis, renderer));
```

## 차트 출력

마지막으로 생성한 차트를 출력하는 방법에 대해 알아보겠습니다. JFreeChart는 다양한 형식의 출력을 지원하며, 여기서는 기본적인 이미지 파일로 출력하는 방법을 설명하겠습니다.

```java
ChartUtils.saveChartAsPNG(new File("chart.png"), chart, 800, 600);
```

위의 코드는 차트를 800x600 크기의 PNG 파일로 저장하는 예시입니다. ChartUtils 클래스는 JFreeChart에서 제공하는 유틸리티 클래스로, 다양한 형식으로 차트를 출력할 수 있는 기능을 제공합니다.

## 결론

이상으로 JFreeChart를 사용하여 Interval Bar 차트를 그리는 방법에 대해 알아보았습니다. JFreeChart는 다양한 차트 유형을 지원하므로, 필요한 경우 다른 유형의 차트도 생성할 수 있습니다. 자세한 사용법은 [JFreeChart 공식 문서](http://www.jfree.org/jfreechart/)를 참고하시기 바랍니다.