---
layout: post
title: "[git] Merge 충돌 발생시 취소하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---


## Merge 충돌 발생시 취소하기

Merge 도중 충돌이 발생했으나, 예상했던 일도 아니고 지금 당장 처리할 일도 아니라면 아래의 명령어로 Merge 이전으로 되돌릴 수 있다

```bash
$ git merge --abort
```

Merge이전에 워킹 디렉토리에서 stash하지 않았거나 커밋하지 않은 파일이 있는 경우에는 이전으로 되돌아가지 않는다. 이런 경우 처음부터 다시 하고 싶다면 아래의 명령어를 통해 강제로 되돌릴 수 있다.

```bash
$ git reset --hard HEAD
```

단, 워킹 디렉토리를 이전 시점으로 완전히 되돌리기 때문에 저장하지 않은 내용은 사라진다는 점을 주의해야한다.