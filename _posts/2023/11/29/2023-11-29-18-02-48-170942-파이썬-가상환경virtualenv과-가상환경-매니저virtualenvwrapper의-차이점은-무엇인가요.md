---
layout: post
title: "[python] 파이썬 가상환경(virtualenv)과 가상환경 매니저(virtualenvwrapper)의 차이점은 무엇인가요?"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

1. 기능: virtualenv는 파이썬 가상환경을 생성하는 기본 도구입니다. 가상환경을 만들고 관리하는 명령어를 제공하며, 필요한 패키지를 설치할 수 있습니다. virtualenvwrapper는 virtualenv를 좀 더 편리하게 사용하기 위한 래퍼(wrapper) 도구로, 가상환경을 관리하는 명령어를 좀 더 직관적이고 간편하게 사용할 수 있도록 도와줍니다.

2. 명령어의 간편성: virtualenv는 명령어를 통해 가상환경을 생성하고 활성화하는 등의 작업을 수행해야 합니다. 반면에 virtualenvwrapper는 추가적인 환경 변수 설정을 통해 기존 명령어를 좀 더 직관적으로 사용할 수 있습니다. 예를 들어, 가상환경을 생성할 때는 "mkvirtualenv" 명령어를 사용하는데, 이는 virtualenv의 "virtualenv" 명령어를 간략화한 것입니다.

3. 명령어의 통일성: virtualenv와 virtualenvwrapper는 기능적으로 중복되는 명령어가 있지만, virtualenvwrapper는 일관된 명령어를 제공하여 사용자들이 통일된 방식으로 가상환경을 관리할 수 있도록 도와줍니다. 예를 들어, 가상환경을 활성화할 때는 "workon" 명령어를 사용하는데, 이는 언제나 동일한 방식으로 사용할 수 있습니다.

가상환경을 사용하는 방법에 대해 자세히 알고 있다면 virtualenv만으로도 충분히 개발환경을 구성할 수 있습니다. 그러나 편의성과 일관성을 더 중요시하는 경우에는 virtualenvwrapper를 사용하여 가상환경을 더 편리하게 관리할 수 있습니다.

참고 자료:
- virtualenv 공식 문서: https://virtualenv.pypa.io/en/latest/
- virtualenvwrapper 공식 문서: https://virtualenvwrapper.readthedocs.io/en/latest/