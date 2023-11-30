---
layout: post
title: "[python] PyYAML로 YAML 파일을 읽어와서 그래프로 시각화하기 (networkx, graph-tool 등 사용)"
description: " "
date: 2023-11-30
tags: [python]
comments: true
share: true
---

PyYAML은 Python에서 YAML 파일을 쉽게 파싱하고 생성하는 데 사용되는 라이브러리입니다. 이 블로그 포스트에서는 PyYAML를 사용하여 YAML 파일을 읽어와서 그래프로 시각화하는 방법을 알아보겠습니다. 그래프 시각화에는 networkx, graph-tool 등 여러 라이브러리를 사용할 수 있습니다.

## 1. PyYAML 설치

먼저 PyYAML을 설치해야 합니다. 다음 명령을 사용하여 PyYAML을 설치할 수 있습니다.

```python
pip install pyyaml
```

## 2. YAML 파일 읽기

다음은 YAML 파일을 읽어오는 예제 코드입니다.

```python
import yaml

with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data)
```

위 코드에서 'data.yaml' 대신 실제 YAML 파일의 경로를 사용해야 합니다. 파일을 열고 `yaml.safe_load` 함수를 사용하여 데이터를 로드합니다. 로드된 데이터는 Python의 딕셔너리 형태로 반환됩니다.

## 3. 그래프로 시각화

여기서는 networkx 라이브러리를 사용하여 데이터를 그래프로 시각화하는 방법을 알아보겠습니다.

```python
import networkx as nx
import matplotlib.pyplot as plt

# 그래프 생성
G = nx.Graph()

# YAML 데이터를 그래프에 추가
for node, neighbors in data.items():
    G.add_node(node)
    G.add_edges_from([(node, neighbor) for neighbor in neighbors])

# 그래프 그리기
nx.draw(G, with_labels=True)
plt.show()
```

위 코드에서는 `nx.Graph()`를 사용하여 빈 그래프를 생성한 후, 데이터를 그래프에 추가합니다. 마지막으로 `nx.draw` 함수를 사용하여 그래프를 그려줍니다.

## 참고 자료

- [PyYAML 공식 문서](https://pyyaml.org/)
- [networkx 공식 문서](https://networkx.org/)
- [matplotlib 공식 문서](https://matplotlib.org/)