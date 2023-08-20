---
layout: post
title: "Actions on Google"
description: " "
date: 2020-12-03
tags: [Google]
comments: true
share: true
---

## Actions on Google

## Overview
Actions on Google은 Google assistant 기반의 대화형 앱(3rd party action)을 생성할 수 있도록 해주는 플랫폼이라고 볼 수 있음.

Gooole assistant가 지원하는 prebuilt service(날씨, 맵, 주문 등)들을 내부적으로 action으로 관리되고 있고, 개발자들의 외부 서비스들을 추가할 수 있도록 해주는 것이 Actions on Google이라고 보면 됨

```
Actions on Google은 개발자가 자신들의 서비스를 Google Assistant에 통합하기 위한 플랫폼이다.
```

외부 서비스를 Google assistant에 통합하는 과정은 다음과 같음

```
먼저, Conversation action은 양방향 대화를 통해 사용자의 request을 처리할 수 있도록 해주는데, Alexa의 custom skill과 유사하다고
보면 된다.

1. 사용자가 action을 request하면, Google assistant가 request을 처리해서 가장 적합한 action을 찾아서 호출한다.
2. 그러면, 해당 action이 이후의 동작들(사용자를 어떻게 맞이하고, 사용자의 요청을 어떻게 처리 한 뒤, 어떻게 대화를 끝낼 것인지까지)를 
관리한다. 
```

### Example - Personal Chef Application
구글에서 Actions on Google을 설명하기 위해 사용한 action으로 사용자가 Google Home을 통해 '*조리법을 찾기 서비스*' 와 상호작용 할 수 있도록 해준다.  
사용자는 현재 어떤 기분인지, 어떤 재료를 가지고 있는지 명시함  
그러면, Conversational App은 사용자의 기분을 해석하고, 어떤 재료가 이용가능한 지 이해함

Action에서 의미를 찾아내는 것은 상당히 어렵기 때문에, 그 동안 이러한 유형의 application을 만드는 것 자체가 쉽지 않았음

Mehdi Samadi, co-founder and CTO at Solvvy, explains
> AI 기술 측면에서, "show me cheap Indian restaurants near me"와 같은 command나 instruction을 실행 가능한 명령어 셋으로 변환하는 것은 쉽지 않은 일이다. 사용자가 인도 요리가 있는 음식점을 보고 싶어한다는 것을 이해해야하며, "Cheap"으로 사용자가 무엇을 의도하는지 해석해서 개인화해야 합니다.

Conversation Action은 이러한 문맥 인식 문제(Contextually aware challenges)를 해결할 수 있는 대화형 앱을 개발하는데 도움이 되도록 구글이 개발함

![Extract meaning](https://cdn.infoq.com/statics_s2_20170228-0434_4/resource/news/2016/12/Google-AI-API/en/resources/conversation.png)

## Conversation Actions
Conversation Actions의 세 가지 주요 컴포넌트  

* **Invocation triggers** 사용자가 action을 어떻게 호출하고, 찾을지를 정의함. 한 번 trigger되고 나면, actions은 dialog에 의해 정의된 대화를 수행함
* **Dialogs** 사용자가 action과 어떻게 대화할 지를 정의함. actions을 위한 user interface 역할을 함
* **Fulfillment** user input을 처리하고 reponse를 돌려주는 코드로, recipes를 가져오거나 news를 읽어주는 등과 같은 외부 서비스의 로직을 구현함. REST endpoint로 노출됨

![Major components of a Conversation Action](https://developers.google.com/actions/images/conversation-action.png)

Conversation action을 호출하기 위한 세 가지 방법

* **Conversation APIs** Google Assistant와 통신하기 위해 사용되어야 하는 request/response format을 제공함
* **Actions SDK** NodeJS client library, Action Package definition, CLI and Web Simulator를 포함함. Google에서 deprecate하려는 분위기
* **API.AI**


## Conversation API
Conversation API는  Google Assistant와 통신하기 위해 반드시 사용해야하는 request/response format.
Action이 invoke되어 사용자와 상호작용 할 때도, Google Assistant는 action과 사용자 사이에서 브로커 역할을 하기 때문에 Conversation API를 사용해야 함

![Conversation API](https://developers.google.com/actions/images/conversation-api.png)

Actions SDK는 이러한 Conversation API request를 parsing하고, response를 생성하는 라이브러리를 제공함


## API.AI
API.AI는 구글이 최근에 인수한 것으로, 개발자들이 대화형 인터페이스를 만들 수 있도록 해서 Conversation API에서 요구하는 많은 양의 텍스트 문자를 줄여줌

Piekarsk highlights
> API.AI는 대화형 인터페이스를 생성하기 위한 직관적인 GUI를 제공하고, 대화 상태를 관리하고, slots과 forms을 채우는 측면에서 힘든 작업을 수행합니다.



![MacDown logo](https://cdn.infoq.com/statics_s2_20170228-0434_4/resource/news/2016/12/Google-AI-API/en/resources/apiai.png)


대화를 처리르 하기 위해서, 개발자들은 Develper console에서 intent들을 정의할 수 있음.  
Personal Chef 예제의 문맥에서 보면, 사용자로부터 재료와 온도, 음식 종류, 그리고 조리 시간 등이 필요하다는 정보를 정의해야 함  
다음으로, 개발자는 *user says*에 예제 문장을 제공해야 함. API.AI는 Machine Learning argorithm을 트레이닝 시키기 위해 이 에제 문장들을 이용함  

![API.AI Developer console](https://cdn.infoq.com/statics_s2_20170228-0434_4/resource/news/2016/12/Google-AI-API/en/resources/intents.png)


개발자들은 각각의 정보들을 위한 value를 설정할 수 있고, API.AI는 사용자 발화에서 의미를 추출하기 위해 이 정보들을 이용한다.  
예를 들어 Personal Chef app이 recipe의 일부로 protein이 필요하다면, 개발자들은 beef, lamb, tofu, chicken 등과 같은 동의어 리스트 포함할 수 있다. 

API.AI를 이용해 action을 만들어 배포할 때의 flow.

![](https://developers.google.com/actions/images/conversation-action-apiai.png)

* **API.AI NLU** Natural Language Understanding은 입력 대화를 처리함. 자연스러운 구문 확장 및 사용자 입력에서 파라미터를 쉽게 구별하고, 파싱할 수 있는 내장 기능을 제공
* **A GUI interface** dialogs나 invocation을 쉽게 정의하고 설정할 수 있음
* **Conversation building features** API.AI는 상태를 쉽게 유지하고, 사용자의 request를 문맥화할 수 있는 context와 같은 고급 기능을 제공함. 또한 내장 시뮬레이터와 ML algorithm을 통해 사용자 입력을 보다 잘 이해함


### Webhook
Intent를 backend webhook과 연결시킬 수 있는데, 이 webhook은 3rd party platform과의 연결을 통한 확장을 허용함  
**앞에서 언급한 외부 서비스 로직 코드인 fulfillment가 webhook과 연결딘 3rd party platform에 구현되어 있다고 보면 됨**


### References
* [Building Conversational Apps Using Actions on Google and API.AI](https://www.infoq.com/news/2016/12/Google-AI-API)
* [Actions on Google: Introduction to Conversation Actions(동영상)](https://www.youtube.com/watch?v=HNfE0uaKcfY)
* [Actions on Google: Building Assistant Actions using API.AI(동영상)](https://www.youtube.com/watch?v=9SUAuy9OJg4)
* [Actions on Google: Developer site](https://developers.google.com/actions/develop/conversation)