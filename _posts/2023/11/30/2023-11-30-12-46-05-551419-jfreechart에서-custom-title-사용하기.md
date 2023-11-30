---
layout: post
title: "[java] JFreeChart에서 Custom Title 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 자바로 작성된 오픈 소스 차트 라이브러리입니다. 이 라이브러리를 사용하면 다양한 종류의 차트를 생성하고 커스터마이징할 수 있습니다. 이번에는 JFreeChart에서 Custom Title을 사용하는 방법에 대해 알아보겠습니다.

## Custom Title

JFreeChart의 Title 클래스는 차트의 제목을 표시하는 역할을 합니다. 기본적으로 제공되는 Title 클래스를 사용할 수도 있지만, 때로는 자신만의 Custom Title을 만들어 사용해야 할 때가 있습니다.

## Custom Title 만들기

Custom Title을 만들기 위해서는 Title 클래스를 상속받아 새로운 클래스를 만들어야 합니다. 이 클래스에서는 render() 메서드를 오버라이딩하여 원하는 형태의 제목을 표시할 수 있습니다.

```java
import org.jfree.chart.title.TextTitle;

public class CustomTitle extends TextTitle {

    public CustomTitle(String text) {
        super(text);
    }

    @Override
    public void render(Graphics2D g2, Rectangle2D area) {
        // Title을 그리는 로직을 작성합니다.
        // 예시: 원하는 위치에 텍스트를 출력하는 코드
        g2.drawString(getText(), (float) area.getX()+10, (float) area.getY()+20);
    }
}
```

위의 코드에서는 TextTitle을 상속받아 CustomTitle 클래스를 만들었습니다. render() 메서드를 오버라이딩하여 그리는 로직을 구현하였습니다. 예시로는 getTitle() 메서드로 가져온 텍스트를 원하는 위치에 출력하는 코드를 작성하였습니다.

## Custom Title 사용하기

Custom Title을 사용하기 위해서는 JFreeChart의 setTitle() 메서드에 CustomTitle 인스턴스를 전달해주면 됩니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

public class ChartDemo {

    public static void main(String[] args) {
        // 데이터 생성
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        dataset.addValue(100, "Series 1", "Category 1");
        dataset.addValue(200, "Series 1", "Category 2");
        dataset.addValue(300, "Series 1", "Category 3");

        // 차트 생성
        JFreeChart chart = ChartFactory.createBarChart(
                "Chart Title",    // 제목
                "Category",       // x축 레이블
                "Value",          // y축 레이블
                dataset,          // 데이터셋
                PlotOrientation.VERTICAL,
                true,             // 범례 표시 여부
                true,             // 도구 팁 표시 여부
                false             // URL 생성 여부
        );

        // Custom Title 생성
        CustomTitle customTitle = new CustomTitle("Custom Title");

        // 차트에 Custom Title 설정
        chart.setTitle(customTitle);

        // 차트 프레임 생성
        ChartFrame frame = new ChartFrame("Chart Demo", chart);
        frame.pack();
        frame.setVisible(true);
    }
}
```

위의 코드에서는 JFreeChart를 사용하여 Bar Chart를 생성하는 예제입니다. CustomTitle 클래스를 생성하여 차트의 제목으로 설정한 후, 차트를 생성하고 프레임에 출력합니다.

## 결론

JFreeChart에서 Custom Title을 사용하는 방법에 대해 알아보았습니다. Custom Title을 사용하면 제목을 원하는 형태로 표시할 수 있으며, 차트의 커스터마이징에 도움을 줄 수 있습니다.