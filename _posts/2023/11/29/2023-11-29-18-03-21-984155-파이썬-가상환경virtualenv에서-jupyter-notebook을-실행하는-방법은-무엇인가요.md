---
layout: post
title: "[python] 파이썬 가상환경(virtualenv)에서 Jupyter Notebook을 실행하는 방법은 무엇인가요?"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

1. 우선 파이썬 가상환경(virtualenv)을 생성합니다. 이를 위해 터미널(Command Prompt 또는 Terminal)에서 다음 명령어를 실행합니다:

   ```
   python -m venv myenv
   ```

   위 명령어에서 `myenv`는 가상환경의 이름으로 원하는 이름을 사용할 수 있습니다.

2. 가상환경을 활성화합니다. 터미널에서 다음 명령어를 실행합니다:

   - Windows:

     ```
     myenv\Scripts\activate
     ```

   - macOS/Linux:

     ```
     source myenv/bin/activate
     ```

3. 활성화된 가상환경에서 Jupyter Notebook을 설치합니다. 터미널에서 다음 명령어를 실행합니다:

   ```
   pip install notebook
   ```

4. Jupyter Notebook을 실행합니다. 터미널에서 다음 명령어를 실행합니다:

   ```
   jupyter notebook
   ```

   이제 브라우저에서 Jupyter Notebook이 실행될 것입니다. 새로운 노트북 파일을 만들어 파이썬 코드를 작성하고 실행할 수 있습니다.

가상환경에서 Jupyter Notebook을 사용하면 프로젝트별로 분리된 환경에서 작업할 수 있어 유용합니다. 가상환경을 종료하려면 터미널에서 `deactivate` 명령어를 실행하면 됩니다.