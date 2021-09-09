---
layout: post
title: "[git] Git에서 Untracked 상태인 파일 삭제하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

# Git에서 Untracked 상태인 파일 삭제하기

프로젝트를 진행하다보면 워킹 디렉토리에 Git에서 관리하지 않을 파일들이 생성된다. 저장소에 넣고 버전 관리 할 필요가 없는 build된 CSS파일이나(내가 진행하는 프로젝트는 배포시에 최종 빌드된 CSS만 버전을 관리하기 때문에), 테스트용 이미지등이 생긴다. 이런 파일들은 `git checkout <file path>`로도 지워지지 않는 Untracked 상태이다.

이런 임시 파일들은 `.gitignore`에 등록해도 되지만, 깃에서 관리할 필요가 없는 `.psd`파일 외에 임시로 작성한 `.png`파일은 전부 깃에서 관리되어야하기에 등록할 수 없다.

이렇게 임시로 쌓인 Untracked 상태의 파일은 직접 디렉토리에 들어가 파일을 휴지통에 버리는 방법도 있지만, [git의 clean](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Stashing%EA%B3%BC-Cleaning)으로 워킹 디렉토리에서 청소할 수 있다.

```bash
git clean -f
```

강제로 `git clean`하기 전에 `git clean`이 어떤 파일을 지울지 확인하는 명령어는 아래와 같다

```bash
git clean -n
```

추가로, 디렉토리를 지우거나 `.gitignore`에 등록해둔 무시된 파일을 지우는 옵션도 있다.

* 디렉토리를 지울 때는 `git clean -f -d` 또는 `git clean -fd` 를 사용
* 무시된 파일을 지울 때는 `git clean -f -x` 또는 `git clean -fx` 를 사용
* 대화형으로 파일을 하나씩 확인하며 지울때는 `git clean -i`를 사용