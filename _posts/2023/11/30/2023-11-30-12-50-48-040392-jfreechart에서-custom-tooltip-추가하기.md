---
layout: post
title: "[java] JFreeChart에서 Custom Tooltip 추가하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java에서 사용할 수 있는 강력한 차트 라이브러리입니다. 이 라이브러리를 사용하여 다양한 형태의 차트를 만들 수 있습니다. 이번 글에서는 JFreeChart에서 Custom Tooltip을 추가하는 방법에 대해 알아보겠습니다.

## 1. Custom Tooltip 클래스 만들기

우선 Custom Tooltip을 구현하기 위해 새로운 클래스를 만들어야 합니다. 이 클래스는 `org.jfree.chart.labels.StandardCategoryToolTipGenerator`를 상속받아야 합니다. 아래는 Custom Tooltip 클래스의 예제입니다.

```java
import org.jfree.chart.labels.StandardCategoryToolTipGenerator;
import org.jfree.data.category.CategoryDataset;

public class CustomTooltip extends StandardCategoryToolTipGenerator {
    public CustomTooltip() {
        super();
    }
    
    @Override
    public String generateToolTip(CategoryDataset dataset, int row, int column) {
        // Custom Tooltip 내용을 반환하는 로직을 작성합니다.
        // dataset, row, column을 활용하여 원하는 Tooltip 내용을 생성합니다.
        return "Custom Tooltip";
    }
}
```

CustomTooltip 클래스는 `StandardCategoryToolTipGenerator`를 상속받고, `generateToolTip` 메서드를 오버라이딩하여 Custom Tooltip 내용을 만듭니다.

## 2. JFreeChart에 Custom Tooltip 적용하기

이제 JFreeChart 객체에 Custom Tooltip을 적용하는 방법에 대해 알아보겠습니다. 아래는 Custom Tooltip을 적용하는 예제입니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.data.category.DefaultCategoryDataset;

public class Main {
    public static void main(String[] args) {
        // 데이터셋 생성
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        dataset.addValue(1, "Series 1", "Category 1");
        dataset.addValue(2, "Series 1", "Category 2");
        dataset.addValue(3, "Series 1", "Category 3");
        
        // Chart 생성
        JFreeChart chart = ChartFactory.createBarChart("Custom Tooltip Example", "Category", "Value", dataset);
        
        // Custom Tooltip 적용
        CustomTooltip tooltipGenerator = new CustomTooltip();
        chart.getCategoryPlot().setToolTipGenerator(tooltipGenerator);
        
        // 차트 프레임에 표시
        ChartFrame frame = new ChartFrame("Chart", chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위의 코드에서는 `ChartFactory.createBarChart`를 사용하여 차트를 생성하고, `chart.getCategoryPlot().setToolTipGenerator`를 이용하여 Custom Tooltip 객체를 적용합니다.

## 결론

이렇게 JFreeChart에서 Custom Tooltip을 추가하는 방법에 대해 알아보았습니다. Custom Tooltip을 사용하면 사용자가 차트의 데이터를 더 쉽게 이해할 수 있게 됩니다. 차트에 맞는 Custom Tooltip을 만들어서 보다 유용한 정보를 제공하도록 해보세요.