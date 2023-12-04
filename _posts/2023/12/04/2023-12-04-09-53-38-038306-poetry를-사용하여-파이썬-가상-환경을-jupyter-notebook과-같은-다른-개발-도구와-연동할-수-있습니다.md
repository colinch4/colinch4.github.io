---
layout: post
title: "[python] Poetry를 사용하여 파이썬 가상 환경을 Jupyter Notebook과 같은 다른 개발 도구와 연동할 수 있습니다."
description: " "
date: 2023-12-04
tags: [python]
comments: true
share: true
---

Poetry는 파이썬 프로젝트의 의존성 관리와 패키징을 위한 도구입니다. Poetry를 사용하면 가상 환경을 손쉽게 설정하고 의존성을 관리할 수 있으며, 이를 Jupyter Notebook과 같은 다른 개발 도구와 연동할 수도 있습니다.

Poetry를 사용하여 파이썬 가상 환경을 설정하려면 다음과 같은 단계를 따를 수 있습니다.

### 단계 1: Poetry 설치

Poetry는 pip를 사용하여 설치할 수 있습니다. 아래의 명령어를 터미널에서 실행하여 Poetry를 설치합니다.

```python
pip install poetry
```

### 단계 2: 새로운 프로젝트 생성

Poetry를 사용하여 파이썬 가상 환경을 설정하려면 새로운 프로젝트를 생성해야 합니다. 아래의 명령어를 터미널에서 실행하여 새로운 프로젝트를 생성합니다.

```python
poetry new myproject
cd myproject
```

### 단계 3: 의존성 관리

Poetry는 `pyproject.toml` 파일을 사용하여 의존성을 관리합니다. 이 파일을 수정하여 필요한 패키지를 추가하거나 제거할 수 있습니다. 예를 들어, `numpy` 패키지를 추가하려면 아래의 명령어를 실행합니다.

```python
poetry add numpy
```

### 단계 4: 가상 환경 설정

Poetry는 가상 환경을 자동으로 생성하고 관리합니다. 가상 환경을 설정하려면 아래의 명령어를 실행합니다.

```python
poetry shell
```

### 단계 5: Jupyter Notebook과 연동하기

Poetry로 설정한 가상 환경은 Jupyter Notebook과 같은 다른 개발 도구와도 연동할 수 있습니다. 먼저, 아래의 명령어를 실행하여 Jupyter Notebook을 설치합니다.

```python
pip install jupyter
```

그리고 나서, 아래의 명령어를 실행하여 Jupyter Notebook을 시작합니다.

```python
jupyter notebook
```

이제 Jupyter Notebook에서 Python 커널을 선택할 때, Poetry로 설정한 가상 환경이 사용 가능한 옵션으로 나타날 것입니다. 이 옵션을 선택하면 Poetry로 설정한 가상 환경에서 코드를 실행할 수 있습니다.

Poetry를 사용하여 파이썬 가상 환경을 설정하고 Jupyter Notebook과 연동하는 방법에 대해 알아보았습니다. Poetry를 사용하면 의존성 관리와 패키지 설치가 훨씬 간편해지며, 프로젝트의 개발 환경을 효율적으로 관리할 수 있습니다. 자세한 내용은 [Poetry 공식 문서](https://python-poetry.org/docs/)를 참조하시기 바랍니다.