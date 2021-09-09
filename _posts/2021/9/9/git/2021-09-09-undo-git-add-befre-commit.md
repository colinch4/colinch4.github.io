---
layout: post
title: "[git] Add 취소하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

# Add 취소하기

작업 도중 실수로 수정내역을 Add했을 때 Add 상태를 되돌릴 수 있다. 

```bash
$ git reset HEAD [file]
```

이렇게 특정 파일을 `reset`하면 추가Stage 상태에 추가(Add)되어 Commit을 기다리던 파일이 Unstaged 상태가 되며, 수정했던 내용은 그대로 워킹디렉토리에 보존된다.

