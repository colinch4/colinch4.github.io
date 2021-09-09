---
layout: post
title: "[git] 브랜치 삭제하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

# 브랜치 삭제하기

임시 브랜치나, 이미 dev에 통합되어 더이상 필요없게 된 브랜치를 삭제하는 방법이다.

```bash
$ git branch -d <branchname>
```

브랜치 삭제 명령어를 입력했는데 아래와 같은 에러가 출력되는 경우가 있다. 

```bash
$ git branch -d <branchname>
error: The branch '<branchname>' is not fully merged.
If you are sure you want to delete it, run 'git branch -D <branchname>'.
```

위 메시지는 브랜치에서 수정한 내용을 병합(merge)하지 않아 작업 내용을 잃어버릴 수 있다는 경고 메시지다. 중요한 커밋이 누락되지 않는지 한번 다시 검토해 본 후, 브랜치가 삭제되어도 괜찮다면 강제로 브랜치를 삭제한다.

```bash
$ git branch -D <branchname>
```
