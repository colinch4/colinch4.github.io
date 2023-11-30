---
layout: post
title: "[java] JFreeChart에서 Custom Title 추가하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java 기반의 무료 차트 라이브러리입니다. 이 라이브러리를 사용하면 다양한 종류의 차트를 생성하고 사용자 정의할 수 있습니다. 이번 포스트에서는 JFreeChart에서 커스텀 타이틀을 추가하는 방법에 대해 알아보겠습니다.

## 1. JFreeChart 커스텀 타이틀 클래스 만들기

먼저, JFreeChart에서 사용할 커스텀 타이틀 클래스를 만들어야 합니다. 이 클래스는 TextTitle 클래스를 상속받아 구현됩니다.

```java
import org.jfree.chart.title.TextTitle;
import java.awt.Font;

public class CustomChartTitle extends TextTitle {

    public CustomChartTitle(String text) {
        super(text);
        setFont(new Font("Arial", Font.BOLD, 14));
    }
}
```

위 예제에서는 CustomChartTitle 클래스를 생성하고, 생성자에서 타이틀 텍스트를 받아와 TextTitle의 생성자를 호출합니다. 그리고 글꼴을 Arial, 굵게, 크기 14로 설정합니다.

## 2. JFreeChart에 커스텀 타이틀 추가하기

이제 JFreeChart 객체에 위에서 만든 커스텀 타이틀을 추가해보겠습니다. JFreeChart 객체에는 제목을 설정하는 setTitle() 메소드가 있습니다.

```java
import org.jfree.chart.ChartFactory;
import org.jfree.chart.JFreeChart;
import org.jfree.ui.ApplicationFrame;

public class Main extends ApplicationFrame {

    public Main(String title) {
        super(title);

        JFreeChart chart = ChartFactory.createBarChart(
                "차트 제목",
                "X축",
                "Y축",
                null);

        CustomChartTitle customTitle = new CustomChartTitle("커스텀 타이틀");
        chart.setTitle(customTitle);

        // 차트 그리기 등 추가 작업
    }

    public static void main(String[] args) {
        Main main = new Main("JFreeChart 커스텀 타이틀");
        main.pack();
        main.setVisible(true);
    }
}
```

위 예제에서는 Main 클래스가 ApplicationFrame을 상속받아 생성자에서 JFreeChart 객체를 생성합니다. 그리고 커스텀 타이틀을 생성하고, JFreeChart 객체에 setTitle() 메소드를 사용하여 커스텀 타이틀을 설정합니다.

## 3. 실행 결과 확인하기

위 코드를 실행하면 차트 제목 영역에 지정한 커스텀 타이틀이 표시됩니다.

![커스텀 타이틀 예제](custom_chart_title_example.png)

이처럼 JFreeChart에서 커스텀 타이틀을 추가하는 방법에 대해 알아보았습니다. 차트에 특별한 메시지나 추가 정보를 표시하고 싶을 때, 이러한 커스텀 타이틀을 사용할 수 있습니다.

## 참고 자료
- JFreeChart 공식 홈페이지: [https://www.jfree.org/jfreechart/](https://www.jfree.org/jfreechart/)
- JFreeChart 사용 예제: [https://www.tutorialspoint.com/jfreechart/index.htm](https://www.tutorialspoint.com/jfreechart/index.htm)