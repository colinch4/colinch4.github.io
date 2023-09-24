---
layout: post
title: "파이썬 SpaCy를 활용하여 텍스트에서 중복된 내용 제거(Duplicate Removal)"
description: " "
date: 2023-09-24
tags: [python, spacy]
comments: true
share: true
---

중복된 내용을 제거하는 것은 텍스트 데이터 처리에서 중요한 과정입니다. 중복된 내용은 데이터 분석과 정보 추출에 영향을 미칠 수 있으며, 결과의 정확성과 효율성을 저하시킬 수 있습니다. 이를 해결하기 위해 파이썬의 SpaCy 라이브러리를 활용하여 텍스트에서 중복된 내용을 제거하는 방법을 알아보겠습니다.

## SpaCy 라이브러리 설치

먼저, SpaCy를 설치해야 합니다. 아래의 명령어를 사용하여 SpaCy를 설치할 수 있습니다.

```
pip install spacy
```

## 중복된 내용 제거하기

중복된 내용을 제거하기 위해서는 SpaCy의 문서 유사성 기능을 사용할 수 있습니다. 우선 SpaCy의 모델을 로드해야 합니다. 예를 들어, 영어 텍스트의 경우 다음과 같이 en_core_web_sm 모델을 로드할 수 있습니다.

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

SpaCy의 문서 유사성 기능을 활용하여 중복된 내용을 제거할 수 있습니다. 아래의 예제 코드를 참고해보세요.

```python
def remove_duplicates(documents):
    unique_documents = []
    
    for document in documents:
        is_duplicate = False
        
        for unique_doc in unique_documents:
            similarity = document.similarity(unique_doc)
            
            if similarity >= 0.9:  # 유사도 임계값을 설정하여 중복 여부를 판단합니다.
                is_duplicate = True
                break
        
        if not is_duplicate:
            unique_documents.append(document)
    
    return unique_documents

# 중복이 포함된 텍스트 문서들
documents = [
    "This is a sample document.",
    "This is another sample document.",
    "This is a sample document."  # 중복된 내용
]

# SpaCy의 문서 객체로 변환
spacy_docs = [nlp(doc) for doc in documents]

# 중복된 내용 제거
unique_docs = remove_duplicates(spacy_docs)

# 중복이 제거된 문서 출력
for doc in unique_docs:
    print(doc.text)
```

위의 코드에서 `remove_duplicates` 함수는 중복된 내용을 제거하기 위한 함수입니다. 입력으로 텍스트 문서들을 SpaCy의 문서 객체로 변환한 리스트를 받고, 중복된 내용을 제거한 결과를 반환합니다. 유사도 임계값을 설정하여 중복 여부를 판단하며, 유사도가 임계값보다 크거나 같으면 중복으로 판단합니다.

위 예제는 간단한 텍스트 예시를 사용하였지만, 실제 데이터에 적용할 수 있습니다. 중복된 내용을 제거함으로써 텍스트 데이터의 정확성을 높이고, 분석 및 정보 추출 과정을 효율적으로 진행할 수 있습니다.

#python #nlp #spacy #텍스트처리 #중복제거