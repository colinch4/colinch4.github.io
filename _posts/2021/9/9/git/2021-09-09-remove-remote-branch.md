---
layout: post
title: "[git] 원격 브랜치 삭제하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---


# 원격 브랜치 삭제하기

로컬에 있는 브랜치를 로컬과 원격에서 동시에 삭제하고자 하는 경우, [브랜치 삭제하기](https://github.com/onlyeon/TIL/blob/master/git/delete-branch.md) 를 먼저 수행한 후 아래의 명령어로 upstream에 반영한다.

```bash
$ git push origin :<branch_name>
```

원격 브랜치에만 존재하는 경우 아래의 명령어로 즉시 삭제 가능하다.

```bash
$ git push origin --delete <branch_name>
```



참고자료: [Git 브랜치 - 리모트 브랜치](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%A6%AC%EB%AA%A8%ED%8A%B8-%EB%B8%8C%EB%9E%9C%EC%B9%98)

