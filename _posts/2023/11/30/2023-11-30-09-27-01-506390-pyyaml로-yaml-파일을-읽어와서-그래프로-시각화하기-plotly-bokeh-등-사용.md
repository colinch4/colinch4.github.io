---
layout: post
title: "[python] PyYAML로 YAML 파일을 읽어와서 그래프로 시각화하기 (plotly, bokeh 등 사용)"
description: " "
date: 2023-11-30
tags: [python]
comments: true
share: true
---

이번 포스트에서는 PyYAML 라이브러리를 사용하여 YAML 파일을 읽어와서 데이터를 그래프로 시각화하는 방법을 알아보겠습니다. 그래프 시각화에는 plotly, bokeh 등의 라이브러리를 사용할 수 있습니다.

## PyYAML이란?
PyYAML은 파이썬에서 YAML 파일을 파싱하고 생성하기 위한 라이브러리입니다. YAML은 사람이 쉽게 읽고 쓸 수 있는 데이터 표현 양식으로서, 설정 파일이나 데이터 저장에 많이 사용됩니다.

## YAML 파일 읽기
먼저 PyYAML을 설치해야 합니다. 다음 명령을 사용하여 설치할 수 있습니다.

```python
pip install pyyaml
```

다음은 YAML 파일을 읽어와서 내용을 출력하는 간단한 예제 코드입니다.

```python
import yaml

with open("data.yml", "r") as file:
    data = yaml.safe_load(file)

print(data)
```

위 코드에서 `data.yml`은 읽어올 YAML 파일의 경로를 나타냅니다. `yaml.safe_load()` 함수를 사용하여 YAML 파일의 내용을 파이썬 객체로 변환합니다.

## 그래프 시각화
PyYAML로 데이터를 읽어왔다면, 이제 그래프로 시각화하는 작업을 할 수 있습니다. 여기서는 plotly 라이브러리를 사용하여 그래프를 그려보겠습니다.

먼저, plotly를 설치해야 합니다. 다음 명령을 사용하여 설치할 수 있습니다.

```python
pip install plotly
```

다음은 PyYAML로 읽어온 데이터를 사용하여 plotly로 그래프를 그리는 예제 코드입니다.

```python
import yaml
import plotly.graph_objects as go

with open("data.yml", "r") as file:
    data = yaml.safe_load(file)

x_values = []  # x축 데이터
y_values = []  # y축 데이터

for item in data:
    x_values.append(item["x"])
    y_values.append(item["y"])

fig = go.Figure(data=go.Scatter(x=x_values, y=y_values))

fig.show()
```

위 코드에서는 YAML 파일에서 읽어온 데이터를 x축과 y축 데이터로 사용하여 scatter 그래프를 그리고 있습니다. `go.Figure`는 그래프 객체를 생성하고, `fig.show()`를 통해 그래프를 출력합니다.

## 마무리
이번 포스트에서는 PyYAML 라이브러리를 사용하여 YAML 파일을 읽어와서 데이터를 그래프로 시각화하는 방법을 알아보았습니다. PyYAML을 사용하면 YAML 파일을 파싱하는 작업이 간편해지고, plotly와 같은 라이브러리를 사용하면 데이터를 다양한 그래프로 시각화할 수 있습니다.