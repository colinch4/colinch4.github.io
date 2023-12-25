---
layout: post
title: "[sql] 지수이동평균(EXPONENTIAL MOVING AVERAGE) 함수"
description: " "
date: 2023-12-26
tags: [sql]
comments: true
share: true
---

SQL에서 지수이동평균(EMA)은 과거 데이터 포인트의 가중 평균을 사용하여 데이터의 추세를 분석하는 데 사용되는 통계적 기법입니다. 이 기법은 시계열 데이터에서 주로 사용되며, 데이터의 평균 값을 계산하는 간단한 방법과 달리, EMA는 최근 데이터 포인트에 더 큰 가중치를 부여하여 빠르게 변화하는 추세를 포착할 수 있습니다.

## EMA 함수 구현하기

다음은 SQL에서 EMA 함수를 구현하는 예시입니다. 아래 예제에서는 `LAG` 함수를 사용하여 이전 기간의 EMA 값을 가져와서 새로운 EMA 값을 계산합니다.

```sql
WITH RECURSIVE ema_data AS (
  SELECT 
    id, 
    date, 
    value, 
    value AS ema
  FROM 
    your_table
  WHERE 
    date = (SELECT MIN(date) FROM your_table)
  UNION ALL
  SELECT 
    t.id, 
    t.date, 
    t.value, 
    (t.value * 2.0 / (1 + :alpha)) + (p.ema * (1 - (2.0 / (1 + :alpha)))) AS ema
  FROM 
    your_table t
  JOIN 
    ema_data p
  ON 
    t.id = p.id + 1
)
SELECT 
  id, 
  date, 
  value, 
  ema
FROM 
  ema_data;
```

```sql
-- :alpha는 EMA의 smoothing factor로, 보통 12일을 기간으로 하는 경우 smoothing factor는 2 / (12 + 1)이 됩니다.
```

위의 코드에서 `:alpha`는 EMA의 smoothing factor로, 데이터의 특성에 따라 조정할 수 있습니다. 대부분의 경우에는 12일을 기간으로 하는 경우 smoothing factor는 `2 / (12 + 1)`로 설정됩니다.

이 예에서  `your_table`은 EMA를 계산하려는 데이터가 있는 테이블을 대표합니다. `id`, `date`, `value`는 각각 데이터의 식별자, 날짜 및 값을 나타냅니다.

## EMA 함수의 활용

EMA 함수는 주식시장 데이터, 주가 예측, 경제학적 추세 분석 및 기타 시계열 데이터에서 널리 사용됩니다. 데이터 분석가 및 트레이더들은 EMA를 사용하여 장기 및 단기 추세를 식별하고 거래 결정에 활용합니다.

더 자세한 내용은 [이 링크](https://ko.wikipedia.org/wiki/%EC%A7%80%EC%88%98_%EC%9D%B4%EB%8F%99_%ED%8F%89%EA%B7%A0)를 참조하세요.

이와 같이 SQL에서 EMA 함수를 구현하고 활용하는 방법을 알아보았습니다. EMA를 사용하여 시계열 데이터의 추세를 예측하고 분석하는 과정에서 이를 유용하게 활용할 수 있을 것입니다.