---
layout: post
title: "[git] Git Submodule"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

# Git Submodule

Git 저장소에 다른 저장소를 추가하는 도구다. 예를들어, 라이브러리를 가져다 쓸 때 소스코드를 프로젝트로 직접 복사해 사용할 수 있지만 이 경우 라이브러리를 프로젝트에 맞게 수정해서 사용하고 배포하기 어렵다. 이러한 문제를 해결할 수 있는 도구이다.

하위 프로젝트를 추가할 저장소를 부모 저장소, 추가될 저장소를 자식 저장소라고 칭한다.

## 서브모듈 시작하기

```bash
$ git submodule add 자식저장소주소 <디렉토리 이름>
$ git submodule add https://github.com/user-name/repository-name core-style
```

자식 저장소를 서브 모듈로 추가하는 명령어다. <디렉토리 이름>은 생략 가능하며, 생략시 자동으로 자식 저장소 이름으로 디렉토리가 생성된다.

서브모듈 추가하는 명령어를 수행하면 `.gitsubmodules` 파일과 `core-style` 디렉토리가 생성된 것을 확인할 수 있다.

- `.gitcusbodules` 파일은 `.gitignore` 파일과 마찬가지로 버전을 관리한다
- 부모 저장소는 자식 저장소 파일의 변경내역을 추적하지 않으며, 서브모듈 디렉토리를 통째로 특별한 커밋으로 취급한다.

## 커밋 남기기

```bash
$ git commit -m 'Add core-style module'
```

이제 자식 저장소를 포함하는 커밋을 생성한 후 Upstream에 Push 해준다.

## 서브모듈을 포함한 프로젝트 클론

서브모듈을 포함한 저장소를 클론하면 위에서 추가한 `core-style` 디렉토리는 있지만 내용물은 비어있는 상태다.

```bash
$ git clone https://github.com/user-name/repository-name
```

이 경우 아래 두 명령어를 실행해 서브모듈 디렉토리의 내용을 가져와야한다.

```bash
$ git submodule init
$ git submodule update
```

위와 같이 두 단계에 걸쳐 진행되는 클론 과정에 `--recurse-submodules` 옵션을 추가해 한 단계로 줄일 수 있다.

```bash
$ git clone --recurse-submodules https://github.com/user-name/repository-name
```

## 서브모듈을 포함한 프로젝트 작업

### 서브모듈 업데이트 하기

서브모듈을 최신으로 업데이트 하려면 서브모듈 디렉토리에서 `git fetch` 명령을 실행하고 `git merge` 명령으로 upstream 브랜치를 병합한다.

```bash
$ git fetch
$ git merge upstream/master
```

부모 프로젝트 디렉토리로 돌아와서 `git diff --submodule` 명령어를 실행하면 서브모듈에 추가된 커밋 목록을 확인할 수 있다.

이 상태에서 커밋하면 부모 저장소가 포함된 서브모듈은 자식 저장소에 업데이트된 내용으로 메인 프로젝트에 적용된다.

### 더 쉬운 방법

디렉토리를 왔다갔다 하지 않아도 알아서 서브모듈 프로젝트를 Fetch하고 업데이트 해줄 수 있다.

```bash
$ git submodule update --remote core-style
```

이 명령어는 기본적으로 서브모듈 (자식 저장소)의 `main` 브랜치를 확인하고 업데이트해온다. 이 때, 업데이트 대상 브랜치를 변경할 수 있다.

`.gitmodules` 파일에 설정해 모든 작업자에게 동일하게 적용하거나 개인 설정 파일인 `.git/config` 에 설정할 수 있다.

```bash
# .gitmodules에 설정하기
$ git config -f .gitmodules submodule.core-style.branch dev

# .git/config에 설정하기
$ git config submodule.core-style.branch dev
```

모든 서브모듈을 업데이트 하는것도 가능하다.

```bash
$ git submodule update --remote
```

## 추가적인 기능들

### 서브모듈 디렉토리에 변경내역 확인하기

업데이트된 서브모듈에 추가되어있는 변경내역 (커밋) 목록을 확인할 수 있다.

```bash
$ git diff --submodule
```

매번 `--submodule` 옵션 주는게 귀찮다면 config에 설정해둘 수 있다.

```bash
$ git config --global diff.submodule log
```

### `git status` 수행시 서브모듈 파일 변경내역 확인하도록 설정하기

```bash
$ git config status.submodulesummary
```

위 명령어를 설정한 후 `git status` 수행시 서브모듈의 변경된 파일 내역을 간단히 확인할 수 있다

### 참고 자료

[Git 도구 - 서브모듈](https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-%EC%84%9C%EB%B8%8C%EB%AA%A8%EB%93%88)

[서브모듈 업데이트시 발생하는 에러 해결](https://leveloper.tistory.com/176)

[Git: Subtree basics](https://newfivefour.com/git-subtree-basics.html)