---
layout: post
title: "[java] JFreeChart에서 Custom Legend 추가하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 자바를 기반으로한 오픈소스 라이브러리로, 다양한 종류의 차트를 생성하고 커스터마이징할 수 있습니다. 이번 포스트에서는 JFreeChart에서 Custom Legend(범례)를 추가하는 방법에 대해 알아보겠습니다.

## 1. Custom Legend 클래스 만들기

먼저, Custom Legend를 표시하기 위한 클래스를 생성해야 합니다. 이 클래스는 `org.jfree.chart.title.LegendTitle` 클래스를 상속받아야 합니다.

```java
import org.jfree.chart.title.LegendTitle;
import org.jfree.chart.title.TextTitle;
import org.jfree.ui.RectangleEdge;

public class CustomLegend extends LegendTitle {
    
    private String customText;

    public CustomLegend(String customText) {
        super(new CustomBlockContainer());
        this.customText = customText;
    }

    @Override
    public void setTitle(TextTitle title) {
        super.setTitle(new TextTitle(customText, title.getFont()));
    }

    private static class CustomBlockContainer extends BlockContainer {
      
        public CustomBlockContainer() {
            super(new BorderArrangement());
        }

        @Override
        public ArrangeResult arrange(Graphics2D g2, RectangleConstraint constraint) {
            ArrangeResult result = super.arrange(g2, constraint);
            double height = getHeight();
            double y = constraint.getAnchorY() + constraint.getHeight() / 2 - height / 2;
            result.setSize(constraint.getWidth(), height);
            result.setOffsetY(y);
            return result;
        }
    }
    
}
```

위의 코드에서 `CustomLegend` 클래스는 `customText` 변수를 가지고 있으며, 이는 사용자가 원하는 문구를 나타냅니다. `setTitle` 메소드는 제목을 설정하기 위해 오버라이드 되어 있습니다. `CustomBlockContainer` 클래스는 CustomLegend의 레이아웃을 설정하기 위해 사용됩니다.

## 2. JFreeChart에 Custom Legend 추가하기

Custom Legend를 생성하고 JFreeChart에 추가하기 위해 다음과 같은 단계를 따릅니다.

```java
// 1. Custom Legend 생성
CustomLegend customLegend = new CustomLegend("Custom Legend");

// 2. JFreeChart 생성
JFreeChart chart = createChart();

// 3. JFreeChart에 Custom Legend 추가
chart.addSubtitle(customLegend);
```

## 3. Custom Legend 스타일링하기

Custom Legend의 스타일을 변경하기 원한다면, `CustomLegend` 클래스에서 다양한 메소드를 사용할 수 있습니다. 예를 들어, Custom Legend의 폰트, 배경색, 범례 위치 등을 조절할 수 있습니다. 자세한 설정 방법은 JFreeChart 공식 문서를 참고하십시오.

## 마치며

이번 포스트에서는 JFreeChart에서 Custom Legend를 추가하는 방법에 대해 알아보았습니다. Custom Legend를 사용하면 JFreeChart 생성물에 개인적인 스타일을 부여할 수 있습니다. JFreeChart의 더 많은 기능과 사용법을 알고 싶다면, JFreeChart 공식 문서를 참고하시기 바랍니다.

## 참고 자료
- [JFreeChart 공식 홈페이지](https://www.jfree.org/jfreechart/)
- [JFreeChart GitHub 저장소](https://github.com/jfree/jfreechart)