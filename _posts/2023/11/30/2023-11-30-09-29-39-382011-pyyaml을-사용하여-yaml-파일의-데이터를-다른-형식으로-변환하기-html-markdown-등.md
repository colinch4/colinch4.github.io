---
layout: post
title: "[python] PyYAML을 사용하여 YAML 파일의 데이터를 다른 형식으로 변환하기 (HTML, Markdown 등)"
description: " "
date: 2023-11-30
tags: [python]
comments: true
share: true
---

YAML은 인간이 쉽게 읽고 쓸 수 있는 데이터 직렬화 형식입니다. PyYAML은 Python에서 YAML 파일을 다루기 위한 라이브러리로, 이를 활용하여 YAML 파일의 데이터를 다른 형식으로 변환할 수 있습니다. 이번 포스트에서는 PyYAML을 사용하여 YAML 파일의 데이터를 HTML과 Markdown 형식으로 변환하는 방법을 알아보겠습니다.

## PyYAML 설치하기

먼저, PyYAML을 설치해야 합니다. 아래의 명령어를 사용하여 PyYAML을 설치할 수 있습니다.

```python
pip install pyyaml
```

## YAML 파일 읽기

먼저, YAML 파일을 읽어와야 합니다. PyYAML을 사용하여 YAML 파일을 읽는 방법은 아래와 같습니다.

```python
import yaml

with open("data.yaml", "r") as file:
    yaml_data = yaml.safe_load(file)
```

위의 코드에서 `data.yaml`은 변환하고자 하는 YAML 파일의 경로입니다. `yaml.safe_load()` 함수를 사용하여 YAML 파일을 읽어옵니다.

## HTML로 변환하기

YAML 데이터를 HTML로 변환하는 방법은 여러 가지가 있지만, 가장 간단한 방법은 문자열 템플릿을 사용하는 것입니다. 아래의 코드는 YAML 데이터를 이용하여 간단한 HTML 템플릿을 적용하는 예시입니다.

```python
html_template = """
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
</head>
<body>
<h1>{title}</h1>
<ul>
{items}
</ul>
</body>
</html>
"""

title = yaml_data.get("title")
items = "\n".join(f"<li>{item}</li>" for item in yaml_data.get("items", []))

html_output = html_template.format(title=title, items=items)
```

위의 코드에서 `html_template`는 HTML의 템플릿으로, `{title}`과 `{items}`는 템플릿에서 치환될 부분입니다. `yaml_data`에서 `title`과 `items` 키를 이용하여 데이터를 추출한 다음, `{title}`과 `{items}`에 적용하여 최종적인 HTML을 생성합니다.

## Markdown으로 변환하기

PyYAML을 사용하여 YAML 데이터를 Markdown으로 변환하는 방법은 비슷합니다. 문자열 템플릿을 이용하여 Markdown 템플릿을 작성하고, YAML 데이터를 이용하여 템플릿을 적용합니다. 아래의 코드는 YAML 데이터를 Markdown으로 변환하는 예시입니다.

```python
markdown_template = """# {title}

{items}"""

title = yaml_data.get("title")
items = "\n".join(f"- {item}" for item in yaml_data.get("items", []))

markdown_output = markdown_template.format(title=title, items=items)
```

위의 코드에서 `markdown_template`은 Markdown의 템플릿으로, `{title}`과 `{items}`는 템플릿에서 치환될 부분입니다. 앞서 설명한 HTML 변환과 마찬가지로 `yaml_data`에서 데이터를 추출한 후, 템플릿에 치환하여 마지막 Markdown 결과를 생성합니다.

## 결과 출력하기

마지막으로, 변환된 HTML 또는 Markdown 결과를 출력하거나 파일로 저장할 수 있습니다. 아래의 코드는 결과를 화면에 출력하는 예시입니다.

```python
print(html_output)
print(markdown_output)
```

위의 코드는 변환된 HTML과 Markdown 결과를 화면에 출력합니다. 이를 파일로 저장하려면 `open()` 함수를 사용하여 파일을 열고, `write()` 함수를 사용하여 결과를 파일에 저장하면 됩니다.

## 마치며

PyYAML을 사용하여 YAML 파일의 데이터를 다른 형식으로 변환하는 방법을 알아보았습니다. 이를 활용하여 HTML, Markdown 외에도 다양한 형식으로 데이터를 변환할 수 있습니다. PyYAML은 YAML 파일을 다루는 다양한 기능을 제공하므로, 필요에 따라 활용해보시기 바랍니다.

## 참고 자료

- [PyYAML 공식 문서](https://pyyaml.org/)
- [Python 문자열 템플릿](https://docs.python.org/3/library/string.html#template-strings)
- [YAML 위키백과](https://en.wikipedia.org/wiki/YAML)
- [HTML 위키백과](https://en.wikipedia.org/wiki/HTML)
- [Markdown 위키백과](https://en.wikipedia.org/wiki/Markdown)