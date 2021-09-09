---
layout: post
title: "[git] git 레파지토리 히스토리까지 복제하기"
description: " "
date: 2021-09-09
tags: [git]
comments: true
share: true
---

# git 레파지토리 히스토리까지 복제하기

github 계정을 2개로 운영하면서 기존에 사용하던 TIL(Today I Learned) 레파지토리를 방치하고 있었는데, 새로 만든 계정에서도 이와 유사한 레파지토리를 운영하고 있어 두개의 내용을 합치고 싶었다.
기존 레파지토리에 있던 내용을 신규 레파지토리에 복제한 후 Add 커밋 으로 내용을 합칠 수 있으나, 이 경우 그간 기존 레파지토리에 남긴 커밋 히스토리가 사라지고 Add 커밋 하나로 남겨지는걸 원하지 않았다.
그래서 구글링을 하니  `--mirror` 옵션으로 커밋 히스토리와 브랜치 내역까지 전체를 통째로 복제하는 방법이 있다는걸 알게되었다.

일단 기존 레파지토리를 mirror 옵션으로 복제한다.
```bash
$ git clone --mirror https://github.com/exampleuser/repository-to-mirror.git
```
이후 위에 복제한 경로로 이동해 push 할 저장소에 신규 레파지토리를 등록해준다
```bash
$ cd repository-to-mirror.git
$ git remote set-url --push origin https://github.com/exampleuser/mirrored
```
마지막으로, 위에서 설정한 주소로 push 한다
```bash
$git push --mirror
```

위 과정으로 TIL 레파지토리의 커밋 히스토리가 무사히 복제되었다.
다만, 이 과정의 단점은 그간 신규 레파지토리에 작업해온 내용은 날아간다는 점이었다.
이번 경우에는 신규 레파지토리에 별로 중요한 히스토리가 없었기 때문에 내용이 사라지는것에 대해 큰 신경쓰지 않고 새로 커밋을 올려 해결했지만, 신규로 작성한 히스토리도 보존이 필요한 경우에는 적합하지 않은 방법이다.

`git clone --mirror https://github.com/exampleuser/repository-to-mirror.git` 명령어로 생긴 디렉토리를 통해 지속적으로 원본 레파지토리에서 신규 레파지토리로 PUSH해 내용을 동일하게 유지할 수 있다고 한다.
```bash
$ git fetch -p origin
$ git push --mirror
```

이번 경우에는 신규 레파지토리에서 다시 히스토리를 쌓아가야 하기 때문에 로컬에 생긴 기존 레파지토리 디렉토리는 삭제 했다.
[Duplicating a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository) 문서의 첫 번째 방법 만으로도 충분 할 것 같다.

## 📖 Reference
- [[Git] 저장소 히스토리까지 전체 복사](https://wrjeoung.tistory.com/15)
- [Duplicating a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)