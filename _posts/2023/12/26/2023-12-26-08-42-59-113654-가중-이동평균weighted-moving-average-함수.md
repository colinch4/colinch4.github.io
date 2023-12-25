---
layout: post
title: "[sql] 가중 이동평균(WEIGHTED MOVING AVERAGE) 함수"
description: " "
date: 2023-12-26
tags: [sql]
comments: true
share: true
---

가중 이동평균(Weighted Moving Average)은 일련의 수치 데이터에서 특정 기간의 평균을 계산하는 방법 중 하나로, 각 관측치에 가중치를 부여하여 평균을 계산합니다.

보통 시계열 데이터 분석이나 경제학, 금융 등의 분야에서 많이 사용되며, 데이터 패턴의 부드러운 감소를 볼 수 있기 때문에 특히나 추세(Trend)를 분석하는 데 유용합니다.

## 가중 이동평균 계산 방법

가중 이동평균은 다음과 같이 계산됩니다.

1. 각 관측치에 가중치를 곱합니다.
2. 가중치를 총합으로 나누어 가중 산술 평균을 계산합니다.

예를 들어, n일 간의 관측치가 있다고 할 때 균등한 가중치를 사용한다면, 가장 최근 값은 n에 해당하는 가중치를 받고, 그로부터 n-1일 전의 값은 1에 해당하는 가중치를 받게 됩니다.

## SQL에서 가중 이동평균 계산

가중 이동평균은 SQL 쿼리를 이용하여 계산할 수 있습니다. 아래는 T-SQL을 사용하여 가중 이동평균을 계산하는 예제 코드입니다.

```sql
SELECT date, value,
   AVG(value) OVER (ORDER BY date ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS weighted_moving_average
FROM your_table
```

위의 코드에서 `AVG` 함수와 `OVER` 절을 사용하여 현재 행과 직전 4개 행을 포함하여 이동평균을 계산하고 있습니다. 실제 사용할 때에는 `your_table`을 해당 테이블 이름으로 변경하여 사용하시면 됩니다.

가중 이동평균은 데이터 시각화, 데이터 예측 및 분석 등 다양한 분야에서 유용하게 활용될 수 있으므로, 데이터 관련 작업을 수행하는 경우 유용한 기법 중 하나로 고려할 수 있습니다.

## 참고 자료
- [Microsoft Docs - T-SQL Window Functions](https://docs.microsoft.com/en-us/sql/t-sql/functions/window-functions)

이상으로 SQL에서 가중 이동평균을 계산하는 방법에 대해 알아보았습니다.