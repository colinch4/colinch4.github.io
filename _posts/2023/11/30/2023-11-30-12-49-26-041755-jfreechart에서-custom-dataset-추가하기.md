---
layout: post
title: "[java] JFreeChart에서 Custom Dataset 추가하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 데이터 시각화를 위한 강력한 도구입니다. 기본적으로 제공되는 데이터셋 이외에 사용자 정의 데이터셋을 추가할 수도 있습니다. 이번 포스트에서는 JFreeChart에서 Custom Dataset을 추가하는 방법에 대해 알아보겠습니다.

## 1. Custom Dataset 클래스 만들기
먼저, Custom Dataset을 위한 클래스를 만들어야 합니다. 이 클래스는 `org.jfree.data.general.Dataset` 인터페이스를 구현해야 합니다. 새로운 클래스를 생성하고 아래의 예제 코드를 작성해보세요.

```java
import org.jfree.data.general.Dataset;
import org.jfree.data.xy.XYDataset;

public class CustomDataset implements XYDataset {
    
    // 필요한 멤버 변수 및 메소드를 추가하세요
    
    @Override
    public int getSeriesCount() {
        // 데이터셋에 포함된 시리즈의 개수를 반환하는 코드를 작성하세요
    }
    
    @Override
    public Comparable<?> getSeriesKey(int series) {
        // 주어진 시리즈의 키를 반환하는 코드를 작성하세요
    }
    
    @Override
    public int getItemCount(int series) {
        // 주어진 시리즈에 포함된 항목의 개수를 반환하는 코드를 작성하세요
    }
    
    @Override
    public Number getX(int series, int item) {
        // 주어진 시리즈 및 항목에 대한 X값을 반환하는 코드를 작성하세요
    }
    
    @Override
    public Number getY(int series, int item) {
        // 주어진 시리즈 및 항목에 대한 Y값을 반환하는 코드를 작성하세요
    }
}
```

위의 코드에서 필요한 멤버 변수와 메소드를 추가하여 Custom Dataset 클래스를 구현하세요.

## 2. Custom Dataset을 사용하여 그래프 그리기
Custom Dataset 클래스를 작성했다면, 이를 사용하여 JFreeChart에서 그래프를 그릴 수 있습니다. 아래의 예제 코드를 참고하여 그래프를 그려보세요.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.data.xy.XYDataset;
import org.jfree.ui.ApplicationFrame;
import org.jfree.ui.RefineryUtilities;

public class ChartExample extends ApplicationFrame {

    public ChartExample(String title) {
        super(title);
        // 그래프를 생성하는 코드를 작성하세요
    }

    private static JFreeChart createChart(XYDataset dataset) {
        // JFreeChart를 생성하는 코드를 작성하세요
    }

    public static void main(String[] args) {
        XYDataset dataset = new CustomDataset();
        JFreeChart chart = createChart(dataset);

        ChartExample example = new ChartExample("Custom Dataset Example");
        example.pack();
        RefineryUtilities.centerFrameOnScreen(example);
        example.setVisible(true);
    }
}
```

위의 코드에서 `CustomDataset` 클래스를 생성하여 `XYDataset` 인터페이스로 초기화한 다음, `createChart()` 메소드를 호출하여 JFreeChart 객체를 생성합니다. 이후, `ChartExample` 클래스를 사용하여 그래프를 화면에 표시합니다.

## 3. 추가적인 작업
Custom Dataset 클래스를 작성하고 그래프를 그리는 기본 코드를 작성하였다면, 필요에 따라 추가적인 작업을 수행할 수 있습니다. 예를 들어, Custom Dataset에 데이터를 추가하거나, 그래프의 스타일을 변경하거나, 축의 레이블을 설정할 수 있습니다. JFreeChart의 문서와 예제를 참고하여 원하는 작업을 수행해보세요.

## 참고 자료
- [JFreeChart 공식 홈페이지](https://www.jfree.org/jfreechart/)
- [JFreeChart API 문서](https://www.jfree.org/jfreechart/api/javadoc/)
- [JFreeChart 개발자 가이드](https://www.jfree.org/jfreechart/api/javadoc/developer-guide.html)