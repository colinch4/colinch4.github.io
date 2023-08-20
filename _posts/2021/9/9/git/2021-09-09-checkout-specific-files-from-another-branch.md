---
layout: post
title: "[git] Git에서 다른 브랜치의 특정 파일 체크아웃하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

## Git에서 다른 브랜치의 특정 파일 체크아웃하기

git-checkout 명령은 워킹 트리의 파일이나 디렉토리를 전체 병합하지 않고 다른 브랜치의 특정 파일이나 디렉토리로 업데이트하는데 사용할 수 있습니다. 이 기능은 여러 브랜치를 사용하고 있을 때 유용하게 사용될 수 있습니다.

사용 방법은 아래와 같습니다

```
git checkout <branch> -- <path>
```



## 📖 Reference

* [git-checkout 매뉴얼 페이지](http://schacon.github.io/git/git-checkout.html)
* [Quick tip: git-checkout specific files from another branch](http://nicolasgallagher.com/git-checkout-specific-files-from-another-branch/)

