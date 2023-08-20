---
layout: post
title: "[git] 커밋 수정하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

## 커밋 수정하기

## 최근 커밋 수정

작업 후 이미 커밋을 작성했는데 조금 더 수정되거나, 커밋 메시지를 변경하고싶은 경우가 있다. 

커밋 메시지를 수정하는 명령어는 아래와 같다.

```bash
$ git commit --amend
```

이 명령은 가장 최근에 작성한 마지막 커밋 메시지를 편집할 수 있도록 텍스트 편집기를 열어준다. 여기에 메시지를 수정하고 편집기를 닫으면 편집기는 수정한 메시지로 마지막 커밋을 수정해준다.

커밋 후 수정된 파일을 마지막 커밋에 포함하는 방법도 기본적으로는 위와 같다.

```bash
$ git add <file-path>
```

위 명령어로 수정된 파일을 스테이징 한 후, 위의 `git commit —amend`로 커밋한다. 

 주의할 점은 이미 원격 저장소에 `push` 한 후에는 커밋 내역을 수정해서는 안된다. 다른 작업자들이 내가 올린 사항을 가져갔을 경우 작업 내역이 꼬이게 되기 때문이다. 커밋 수정은 원격 저장소에 올리기 전, 로컬에서 이루어져야 한다.

 만약 혼자 작업하는 저장소라면 커밋 히스토리를 깔끔하게 만들기 위해 아래와 같이  `-f` 옵션으로 올릴 수 있다.

```bash
$ git push -f origin master
```

## 이전 커밋 메시지 수정

최근 커밋이 아니라 예전 커밋을 수정하려면 다른 방법이 필요하다. git에 히스토리를 수정하는 방법은 없지만 `rebase` 를 이용해 수정할 수 있다. 대화형 `rebase`도구를 사용해 특정 시점부터 HEAD까지의 커밋을 한번에 수정할 수 있다.

HEAD를 기준으로 수정하고자 하는 특정 커밋까지 되돌아가는 명령어를 작성한다.

```bash
$ git rebase -i HEAD~3
```

위의 경우 현재 HEAD를 기준으로 3개 이전의 커밋까지 수정 가능하게 된다.

```bash
pick f7f3f6d changed my name a bit
pick 310154e updated README formatting and added blame
pick a5f4a0d added cat-file

## Rebase 710f0f8..a5f4a0d onto 710f0f8
#
## Commands:
##  p, pick = use commit
##  r, reword = use commit, but edit the commit message
##  e, edit = use commit, but stop for amending
##  s, squash = use commit, but meld into previous commit
##  f, fixup = like "squash", but discard this commit's log message
##  x, exec = run command (the rest of the line) using shell
#
## These lines can be re-ordered; they are executed from top to bottom.
#
## If you remove a line here THAT COMMIT WILL BE LOST.
#
## However, if you remove everything, the rebase will be aborted.
#
## Note that empty commits are commented out
```

이 내용은 `git log` 명령어와는 반대로 HEAD 기준 역순으로 커밋을 나열해 보여준다.`rebase`는 명령에 입력된대로  `HEAD~3` 부터 적용하기 때문이다.

위 메시지에서 `pick` 이라는 단어를 `edit` 으로 수정하면 그 커밋을 수정할 수 있다. 가장 오래된 커밋을 수정하려면 아래와 같이 편집한다.

```bash
edit f7f3f6d changed my name a bit
pick 310154e updated README formatting and added blame
pick a5f4a0d added cat-file
```

`:wq` 명령어로 내용을 저장하고 편집기를 종료하면 git은 `edit` 설정된 커밋으로 이동하고, 아래와 같은 메시지를 보여준다.

```bash
$ git rebase -i HEAD~3
Stopped at 7482e0d... updated the gemspec to hopefully work better
You can amend the commit now, with

       git commit --amend

Once you’re satisfied with your changes, run

       git rebase --continue
```

우리는 아래와 같은 명령어를 실행해 커밋 메시지를 수정하고

```bash
$ git commit --amend
```

수정이 완료되면 아래 명령어로 `rebase` 를 진행해준다.

```bash
$ git rebase --continue
```



---

참고자료: [Git - 히스토리 단장하기]([https://git-scm.com/book/ko/v1/Git-%EB%8F%84%EA%B5%AC-%ED%9E%88%EC%8A%A4%ED%86%A0%EB%A6%AC-%EB%8B%A8%EC%9E%A5%ED%95%98%EA%B8%B0](https://git-scm.com/book/ko/v1/Git-도구-히스토리-단장하기))

