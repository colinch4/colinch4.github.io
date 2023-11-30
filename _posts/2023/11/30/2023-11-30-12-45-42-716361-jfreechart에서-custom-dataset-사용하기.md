---
layout: post
title: "[java] JFreeChart에서 Custom Dataset 사용하기"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

JFreeChart는 자바 기반의 오픈 소스 라이브러리로, 다양한 형식과 스타일의 그래프를 생성하는 데 사용됩니다. 이 라이브러리를 사용하면 막대 그래프, 선 그래프, 원 그래프 등 다양한 유형의 그래프를 생성할 수 있습니다. 이번 글에서는 JFreeChart에서 Custom Dataset을 사용하는 방법에 대해 알아보겠습니다.

### Custom Dataset이란?

JFreeChart에서 데이터셋(Dataset)은 그래프에 표시되는 데이터를 포함하는 객체입니다. 보통은 표준적인 데이터셋 구현체인 `DefaultCategoryDataset`, `DefaultPieDataset` 등을 사용하게 됩니다. 그러나 때로는 특정한 요구사항을 충족시키기 위해 Custom Dataset을 만들어야 할 수도 있습니다. Custom Dataset을 사용하면 그래프를 생성하고 제어하는 데 더 많은 유연성을 가질 수 있습니다.

### Custom Dataset 구현하기

Custom Dataset을 구현하기 위해서는 `org.jfree.data.general.Dataset` 인터페이스를 구현해야 합니다. 이 인터페이스에는 그래프 그릴 때 필요한 메소드들이 정의되어 있습니다.

아래는 Custom Dataset을 구현하는 간단한 예시입니다.

```java
public class CustomDataset implements Dataset {
    private List<String> categories;
    private List<Double> values;

    public CustomDataset(List<String> categories, List<Double> values) {
        this.categories = categories;
        this.values = values;
    }

    @Override
    public int getSeriesCount() {
        return 1;  // 하나의 시리즈만 사용
    }

    @Override
    public Comparable<?> getSeriesKey(int series) {
        return "Series 1";  // 시리즈의 이름
    }

    @Override
    public int getItemCount(int series) {
        return categories.size();  // 데이터 항목 개수
    }

    @Override
    public Number getX(int series, int item) {
        return item;  // X값은 데이터 항목의 인덱스로 표시
    }

    @Override
    public Number getY(int series, int item) {
        return values.get(item);  // Y값은 데이터 값으로 표시
    }

    @Override
    public int indexOf(Comparable<?> seriesKey) {
        return 0;  // 시리즈 인덱스
    }
}
```

위 예시에서는 카테고리와 값의 리스트를 생성자로 받아 Custom Dataset을 초기화합니다. `getSeriesCount()`, `getSeriesKey()`, `getItemCount()`, `getX()`, `getY()`, `indexOf()` 등의 메소드를 구현하여 데이터 값을 그래프에 표시할 수 있습니다.

### Custom Dataset 사용하기

Custom Dataset을 사용하여 JFreeChart에서 그래프를 생성하는 방법은 간단합니다. 아래는 Custom Dataset을 사용하여 막대 그래프를 생성하는 예시입니다.

```java
List<String> categories = Arrays.asList("Category 1", "Category 2", "Category 3");
List<Double> values = Arrays.asList(10.0, 20.0, 30.0);

CustomDataset dataset = new CustomDataset(categories, values);

JFreeChart chart = ChartFactory.createBarChart(
    "My Bar Chart",  // 그래프 제목
    "Category",  // X축 레이블
    "Value",  // Y축 레이블
    dataset,  // 사용할 Dataset
    PlotOrientation.VERTICAL,  // 그래프 방향
    true,  // 범례 표시 여부
    true,  // 도구 상자 표시 여부
    false  // URL 링크 사용 여부
);
```

위 예시에서는 Custom Dataset을 생성한 후, `ChartFactory.createBarChart()`를 사용하여 막대 그래프를 생성합니다. 생성된 그래프에는 Custom Dataset에 있는 데이터가 표시됩니다.

### 결론

JFreeChart에서 Custom Dataset을 사용하면 다양한 유연성을 가진 그래프를 생성하고 제어할 수 있습니다. Custom Dataset을 구현하여 원하는 형태와 스타일의 그래프를 만들어보세요. 더 자세한 정보는 JFreeChart 공식 문서를 참고하세요.

#### References

- [JFreeChart 공식 홈페이지](https://www.jfree.org/jfreechart/)
- [JFreeChart API 문서](https://www.jfree.org/jfreechart/api/javadoc/)
- [JFreeChart Custom Dataset 예제](https://github.com/jfree/jfreechart/blob/master/src/main/java/org/jfree/chart/dataset/custom/)