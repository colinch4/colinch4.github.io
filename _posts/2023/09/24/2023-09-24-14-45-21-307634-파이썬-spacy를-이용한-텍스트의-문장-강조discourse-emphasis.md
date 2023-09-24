---
layout: post
title: "파이썬 SpaCy를 이용한 텍스트의 문장 강조(Discourse Emphasis)"
description: " "
date: 2023-09-24
tags: [SpaCy]
comments: true
share: true
---

텍스트를 처리하다보면, 특정 문장을 강조하여 표시하고 싶을 때가 있습니다. 예를 들어, 중요한 내용이나 강조하고 싶은 포인트를 텍스트 내에서 부각하고 싶을 때, 강조를 통해 가독성을 높일 수 있습니다. 파이썬의 SpaCy 라이브러리는 이러한 강조 기능을 제공합니다.

SpaCy는 자연어 처리를 위한 강력한 도구로, 문장을 구분하는 기능을 제공합니다. 강조하고자 하는 문장을 선택하여 SpaCy를 이용하면, 해당 문장을 쉽게 표시할 수 있습니다. 

```python
import spacy

def emphasize_sentence(text, sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    emphasized_text = ""
    for sent in doc.sents:
        if sent.text == sentence:
            emphasized_text += "**" + sent.text + "**" + " "
        else:
            emphasized_text += sent.text + " "
    
    return emphasized_text.strip()

text = "Hello, this is a sample text. I want to emphasize this sentence."
sentence = "I want to emphasize this sentence."

emphasized_text = emphasize_sentence(text, sentence)
print(emphasized_text)
```

위의 코드는 SpaCy를 사용하여 텍스트에서 특정 문장을 강조하는 예제입니다. 위의 코드에서 `emphasize_sentence()` 함수는 텍스트와 강조하고자 하는 문장을 전달받습니다. 이후 SpaCy를 이용하여 텍스트를 문장으로 구분하고, 강조하고자 하는 문장을 찾아 해당 문장을 강조하기 위해 앞뒤로 별표를 추가합니다.

위의 예제를 실행하면 다음과 같은 결과를 얻을 수 있습니다.

```
Hello, this is a sample text. **I want to emphasize this sentence**.
```

위의 예제에서는 SpaCy의 영어 모델을 이용하였지만, 다른 언어의 모델도 사용할 수 있습니다. SpaCy는 다양한 언어에 대한 모델을 제공하므로, 강조하고자 하는 텍스트의 언어에 맞는 모델을 선택하여 사용할 수 있습니다.

#NLP #SpaCy