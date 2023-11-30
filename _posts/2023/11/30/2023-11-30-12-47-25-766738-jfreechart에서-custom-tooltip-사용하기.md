---
layout: post
title: "[java] JFreeChart에서 Custom Tooltip 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 Java로 작성된 오픈 소스 차트 라이브러리입니다. 이 라이브러리는 다양한 형식의 차트를 생성하고 사용자에게 시각적인 데이터 표시를 제공하는 데 도움을 줍니다.

JFreeChart를 사용하여 차트를 그리는 동안 일반적으로 데이터를 시리즈로 구성하고, X축과 Y축 레이블을 추가하며, 범례를 생성하는 등 여러 작업을 수행할 수 있습니다. 하지만 때로는 차트의 특정 요소에 대한 추가 정보를 표시해야 할 수도 있습니다. 이를 위해 JFreeChart에서는 툴팁(Tooltip)을 사용할 수 있습니다.

## JFreeChart 툴팁 사용하기

JFreeChart에서 툴팁을 사용하려면 다음 단계를 따라야 합니다.

1. `ChartPanel` 객체를 생성합니다.
2. `ChartPanel` 객체에 마우스 이벤트 리스너를 추가합니다.
3. `ChartMouseEvent`를 처리하여 툴팁을 표시하고 감춥니다.

```java
ChartPanel chartPanel = new ChartPanel(chart);

chartPanel.addChartMouseListener(new ChartMouseListener() {
    @Override
    public void chartMouseClicked(ChartMouseEvent event) {
        // 마우스 클릭 이벤트 처리
    }

    @Override
    public void chartMouseMoved(ChartMouseEvent event) {
        // 마우스 이동 이벤트 처리
        ChartEntity entity = event.getEntity();
        if (entity instanceof XYItemEntity) {
            // XYItemEntity의 추가 정보를 가져와 툴팁을 생성
            XYItemEntity xyEntity = (XYItemEntity) entity;
            int seriesIndex = xyEntity.getSeriesIndex();
            int item = xyEntity.getItem();
            XYDataset dataset = xyEntity.getDataset();
            // 툴팁 내용 생성
            String tooltipText = "Series: " + seriesIndex + ", Item: " + item;
            // 생성된 툴팁을 ChartPanel에 설정
            chartPanel.setToolTipText(tooltipText);
        } else {
            // XYItemEntity가 아닌 경우 툴팁을 감춤
            chartPanel.setToolTipText(null);
        }
    }
});
```

위의 코드에서 `chart`는 JFreeChart 객체를 나타냅니다.

## 툴팁 사용 예시

위의 코드를 사용하여 JFreeChart에 툴팁을 추가하면 다음과 같이 차트 요소에 대한 추가 정보를 표시할 수 있습니다.

![JFreeChart Custom Tooltip](https://example.com/image.png)

위의 이미지에서는 각 데이터 아이템에 대한 추가 정보가 툴팁으로 표시되고 있습니다.

## 결론

JFreeChart를 사용하여 자신만의 차트를 그리고 데이터를 시각화하는 데 도움이 되는 오픈 소스 라이브러리입니다. 이를 통해 데이터의 상세 정보를 사용자에게 쉽게 전달할 수 있는 툴팁 기능도 사용할 수 있습니다. 그러므로 JFreeChart를 사용하여 차트를 개발하는 경우, Custom Tooltip을 이용해 차트 요소에 대한 추가 정보를 표시해보는 것도 좋은 방법입니다.