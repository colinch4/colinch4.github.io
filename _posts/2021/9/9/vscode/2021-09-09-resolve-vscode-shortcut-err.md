---
layout: post
title: "[VSCode] vscode 단축키 오류 해결하기"
description: " "
date: 2021-09-09
tags: [ide]
comments: true
share: true
---


## vscode 단축키 오류 해결하기

현재 커서가 있는 한 줄을 선택하는 단축키가 분명히 있을 것 같았다. vscode shortcut select line... 와 같은 검색어로 서칭했을 때 아래와 같은 결과가 나온다.

> **Select** Entire **Line**: Command + L.

하지만 내 vscode에서 `cmd+L` 를 수행하면, 화면 왼쪽 아래에 `(단축키) was pressed. Waiting for second key of chord...` 와 같은 메시지가 나오고 실행되지 않았다.

![vhcode-short-cut-err](/onlyeon/TIL/raw/master/@images/vhcode-short-cut-err1.png)

`cmd+L` 뒤에 다른 키를 더 누를것으로 인지하고 대기하고 있다는 의미이다.

즉 해당 단축키에 복합적인 단축키가 설정되어있어 발생하는 문제였다. Keyboard Shortcuts 설정 페이지로 이동해 `cmd + L` 을 검색하면 해당 키를 사용하고 있는 명령어들이 나타나며, 그 중 복합 단축키를 제거하거나 다른 키로 바꿔주면 `cmd+L` 이 정상적으로 작동하게된다.

![vhcode-short-cut-err2](/onlyeon/TIL/raw/master/@images/vhcode-short-cut-err2.png)

Live Server를 켜고 끄는 단축키때문에 꼬여있었다.

Live server는 우측 아래 Go Live 버튼으로 켜고 끄는 경우가 훨씬 많기 때문에 단축키는 제거해주었다.

