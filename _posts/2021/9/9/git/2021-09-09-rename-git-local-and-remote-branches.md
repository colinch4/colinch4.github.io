---
layout: post
title: "[git] 브랜치 이름 변경하고 리모트 저장소에 반영하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

## 브랜치 이름 변경하고 리모트 저장소에 반영하기

브랜치 이름을 변경하는 명령어는 아래와 같다.

```bash
$ git branch -m [oldbranch] [newbranch]
```

로컬의 `[oldbranch]`가` [newbranch]`로 변경된다. 

`[oldbranch]`가 리모트에 존재하는 경우, 새로 변경된 브랜치명을 리모트에 반영하기 위해 리모트에 있는 `[oldbranch]`의 삭제와 이름이 변경된`[newbranch]`를 올리는 작업이 필요햐다. 단계를 나눠 살펴본다.

리모트의 기존 브랜치를 삭제한다.

```shell
$ git push [remotename] :[oldbranch]
```

위 명령어는 `$ git push [remotename] [localbranch]:[remotebranch]` 로 기억하는 것이 좋다.  `[localbranch]` 부분이 공백으로 비어있으면 로컬에서 빈 내용을 리모트의 `[remotebranch]`에 채워 넣으라는 뜻이다. 즉 기존 브랜치가 삭제된 채 대체된다.

리모트에 변경한 브랜치를 올려준다.

```shell
$ git push [remotename] [newbranch]
```

