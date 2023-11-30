---
layout: post
title: "[python] PyYAML로 YAML 파일을 읽어와서 그래프로 시각화하기 (ggplot, plotnine 등 사용)"
description: " "
date: 2023-11-30
tags: [python]
comments: true
share: true
---

여러분은 YAML 형식의 파일을 읽어와서 그래프로 시각화할 수 있는 Python 라이브러리인 PyYAML을 사용해보고 싶으신가요? 이 블로그 포스트에서는 PyYAML을 활용하여 YAML 파일을 읽어온 후, 그래프를 생성하기 위해 ggplot이나 plotnine과 같은 라이브러리를 사용하는 방법에 대해 알아보겠습니다.

## YAML 파일 읽어오기

먼저, PyYAML 패키지를 설치해야 합니다. 아래 명령어를 사용하여 설치할 수 있습니다:

```python
pip install PyYAML
```

다음으로, YAML 파일을 읽어와서 데이터로 저장하는 방법을 알아보겠습니다. 예를 들어, 다음과 같은 YAML 파일이 있다고 가정해봅시다:

```yaml
- name: John
  age: 25
  city: Seoul
- name: Amy
  age: 30
  city: Busan
- name: Mike
  age: 35
  city: Incheon
```

아래의 코드를 사용하여 YAML 파일을 읽어옵니다:

```python
import yaml

with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)
```

`data` 변수에는 YAML 파일의 내용이 딕셔너리의 리스트 형태로 저장됩니다.

## 그래프 생성하기

YAML 파일에서 읽어온 데이터를 그래프로 시각화하기 위해 ggplot이나 plotnine과 같은 라이브러리를 사용할 수 있습니다. 이 예제에서는 plotnine을 사용하도록 하겠습니다.

먼저, 필요한 패키지를 설치해야 합니다:

```python
pip install plotnine
```

다음과 같이 코드를 작성하여 데이터를 그래프로 시각화할 수 있습니다:

```python
from plotnine import *

df = pd.DataFrame(data)

(ggplot(df)
 + aes(x='name', y='age', fill='city')
 + geom_bar(stat='identity')
 + theme_minimal()
)
```

위 코드에서는 데이터프레임을 생성하고, `ggplot`을 사용하여 x축에는 이름, y축에는 나이, 색깔로는 도시를 사용하는 막대 그래프를 생성합니다. `theme_minimal()`을 사용하여 그래프의 테마를 설정합니다.

## 결론

PyYAML을 사용하여 YAML 파일을 읽어와서 데이터를 그래프로 시각화하는 방법에 대해 알아봤습니다. 이를 통해 YAML 포맷으로 저장된 데이터를 효과적으로 시각화할 수 있습니다. PyYAML 뿐만 아니라 다른 유용한 라이브러리들도 활용하여 데이터 분석 및 시각화를 한 단계 더 발전시킬 수 있습니다.

이 블로그 포스트가 여러분에게 도움이 되었기를 바랍니다. 더 많은 기술적인 내용을 공부하고 싶다면 공식 문서 및 관련 자료들을 참고해보세요.

---

**참고 자료:**

- [PyYAML 공식 문서](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [plotnine 공식 문서](https://plotnine.readthedocs.io/en/stable/)
- [ggplot 공식 문서](http://ggplot.yhathq.com/)