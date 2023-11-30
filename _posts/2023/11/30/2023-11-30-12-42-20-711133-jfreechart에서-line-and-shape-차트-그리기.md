---
layout: post
title: "[java] JFreeChart에서 Line And Shape 차트 그리기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java를 사용하여 다양한 종류의 그래프를 생성하는 데 사용되는 라이브러리입니다. 이 글에서는 JFreeChart를 사용하여 Line and Shape 차트를 그리는 방법을 알아보겠습니다.

## 필요한 라이브러리 가져오기

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.data.xy.DefaultXYDataset;
import org.jfree.data.xy.XYDataset;
```

## 데이터 준비

```java
double[][] data = {{1, 5, 9, 13, 17}, {3, 8, 10, 15, 12}};
```

위의 예시로 사용할 데이터는 2차원 배열로 나타내며, x와 y 좌표의 값을 포함합니다. 아래와 같이 데이터를 준비할 수 있습니다.

## Line and Shape 차트 생성

```java
DefaultXYDataset dataset = new DefaultXYDataset();
dataset.addSeries("Series 1", data);

JFreeChart chart = ChartFactory.createXYLineChart(
        "Line And Shape Chart", // 차트 제목
        "X", // x축 레이블
        "Y", // y축 레이블
        dataset // 데이터셋
);
```

위의 코드는 DefaultXYDataset를 사용하여 데이터셋을 생성하고, ChartFactory를 사용하여 Line and Shape 차트를 생성합니다. 차트의 제목과 x축, y축의 레이블을 설정하고 데이터셋을 추가합니다.

## 차트 이미지로 저장

```java
int width = 800;
int height = 600;
String fileName = "line_and_shape_chart.png";

try {
    ChartUtilities.saveChartAsPNG(new File(fileName), chart, width, height);
    System.out.println("차트 이미지가 성공적으로 저장되었습니다.");
} catch (IOException e) {
    e.printStackTrace();
}
```

위의 코드는 생성한 차트를 이미지 파일로 저장하는 방법을 보여줍니다. ChartUtilities 클래스의 saveChartAsPNG 메서드를 사용하여 차트를 PNG 파일로 저장할 수 있습니다.

## 결과 확인

위의 코드를 실행하고 나면 "line_and_shape_chart.png"라는 파일이 생성됩니다. 해당 파일을 열어서 Line and Shape 차트를 확인할 수 있습니다.

## 참고 자료

- [JFreeChart 공식 홈페이지](https://www.jfree.org/jfreechart/)
- [JFreeChart API 문서](https://www.jfree.org/jfreechart/api/)
- [JFreeChart 예제 코드](https://github.com/jfree/jfreechart/tree/master/source/org/jfree/chart/demo)