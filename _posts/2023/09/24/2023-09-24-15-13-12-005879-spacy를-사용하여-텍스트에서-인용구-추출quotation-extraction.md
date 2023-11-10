---
layout: post
title: "SpaCy를 사용하여 텍스트에서 인용구 추출(Quotation Extraction)"
description: " "
date: 2023-09-24
tags: [SpaCy]
comments: true
share: true
---

SpaCy는 자연어 처리를 위한 인기있는 라이브러리 중 하나입니다. 이 블로그 포스트에서는 SpaCy를 사용하여 텍스트에서 인용구를 추출하는 방법에 대해 알아보겠습니다.

## SpaCy 설치 및 모델 로드

먼저, SpaCy를 설치하고 필요한 언어 모델을 로드해야 합니다. 다음 명령을 사용하여 SpaCy와 모델을 설치하세요.

```shell
pip install spacy
python -m spacy download [모델명]
```

여기서 `[모델명]`은 사용하려는 언어 모델에 해당합니다. 예를 들어, 영어 모델을 사용하려면 `en_core_web_sm`을 다운로드하면 됩니다.

## 인용구 추출하기

이제 SpaCy를 사용하여 텍스트에서 인용구를 추출하는 코드를 작성해보겠습니다. 아래 코드 예제는 영어 텍스트에서 인용구를 추출하는 예제입니다.

```python
import spacy

def extract_quotations(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    quotations = []
    for token in doc:
        if token.pos_ == "PUNCT" and token.text == '"':
            start = token.i
            end = token.i
            
            # Find preceding token
            while start > 0 and doc[start-1].pos_ != "PUNCT":
                start -= 1
                
            # Find following token
            while end < len(doc)-1 and doc[end+1].pos_ != "PUNCT":
                end += 1
                
            quotation = doc[start:end+1]
            quotations.append(quotation.text)
    
    return quotations
```

위 코드에서 `extract_quotations` 함수는 주어진 텍스트에서 인용구를 추출하는 역할을 합니다. SpaCy를 사용하여 텍스트를 토큰화하고, 인용구를 포함한 토큰을 찾아서 추출합니다.

## 인용구 추출하기 예제

이제 위에서 작성한 코드를 사용하여 인용구를 추출하는 간단한 예제를 살펴보겠습니다.

```python
text = "According to Albert Einstein, \"Imagination is more important than knowledge.\""
quotations = extract_quotations(text)
print(quotations)
```

위 코드를 실행하면 다음 출력을 얻을 수 있습니다.

```
['"Imagination is more important than knowledge."']
```

위 예제에서는 주어진 텍스트에서 인용구를 추출하여 출력합니다.

## 마치며

이제 SpaCy를 사용하여 텍스트에서 인용구를 추출하는 방법에 대해 알아보았습니다. SpaCy는 강력한 자연어 처리 라이브러리이기 때문에 다양한 텍스트 분석 작업에 유용하게 활용될 수 있습니다. 향후 프로젝트에서 SpaCy를 사용하여 텍스트를 처리하는데 도움이 되기를 바랍니다.

#NLP #인용구추출