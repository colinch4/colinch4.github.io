---
layout: post
title: "[git] git stash drop 으로 사라진 변경사항 복구하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

# git stash drop 으로 사라진 변경사항 복구하기

비가 오고 싱숭생숭한 기분으로 stash 해둔 내용을 `git stash drop` 시켰을 때! 앞이 캄캄해져 다시 작업 해야하나 파일을 뒤적이다가 git stash drop 복구하기를 구글링했다. 천만 다행으로 drop 된 내용을 다시 복구하는 방법을 찾았다.

`git stash drop` 을 수행하고나면 터미널에 아래와 같은 메시지가 출력된다.

```bash
$ git stash drop
Dropped refs/stash@{0} (e61c278e8a8a00009999999994de70d289ceaef09)
```

이 메시지에서 오른쪽 `()` 괄호 안에 있는 것이 삭제된 stah의 hash 값이다.
해당하는 hash값을 복사해 아래 명령어를 수행한다.

```bash
git stash apply e61c278e8a8a00009999999994de70d289ceaef09
```
