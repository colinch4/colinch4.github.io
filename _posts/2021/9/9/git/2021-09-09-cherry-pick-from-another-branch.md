---
layout: post
title: "[git] 다른 브랜치의 특정 commit 반영하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

## 다른 브랜치의 특정 commit 반영하기

 Cherry-pick은 다른 브랜치에 있는 특정 commit만 반영할 때 사용한다.

commit을 적용하고자 하는 브랜치로 체크아웃한 후 아래 명령어를 입력한다. 

```shell
$git cherry-pick [commit id]
```

 cherry-pick은 commit ID가 새롭게 생성된다. 즉 동일한 수정사항의 commit이 복수개 생기는 현상이 발생하며, 히스토리 관리에 불편함이 생길 수 있다.

`-n` 옵션을 사용하면 특정 commit을 가져와 add 상태까지만 수행한다.

```shell
$git cherry-pick -n [commit id]
```

여러개의 commit을 `-n`옵션으로 가져온 후 `-m` 옵션으로 commit message를 작성하면 하나의 새로운 commit이 작성된다.

```shell
$git commit -m "commit message"
```

