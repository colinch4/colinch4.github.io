---
layout: post
title: "[Go] Setup environment  "
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

## Setup environment  
Go 컴파일러를 설치해보자. (for Mac User)
## Install Go
download link : https://golang.org/dl/  
For Mac User : Choose darwin

## Add PATH
go/bin 에서 PATH 환경 변수 설정하기
> <small>**PATH :** 리눅스와 유닉스 계통의 OS에서 쓰이는 환경변수 <code>PATH</code>는 shell 에게 어느 directory 에서 실행가능한 파일을 찾아야 하는지 알려준다.</small> 

```
export PATH=/usr/local/go/bin:$PATH
```

## Setup Workspace
Go 작업 공간 설정  
1. Git  
git 작업공간 설정
2. GOPATH  
```
mkdir -p ~/work/go
cd ~/work/go
go get golang.org/x/tools/cmd/...
```

원하는 Directory<code>(work/go)</code>로 GOPATH 환경 변수 설정.  
설정된 경로에 <code>bin, pkg, src</code> Directory가 생겼다면 성공.

* PATH가 알맞게 설정되었는지 확인 
```
goimports --help
```
성공시 보이는 Message는 아래와 같다.
```
usage: goimports [flags] [path ...]
  -cpuprofile string
    	CPU profile output
  -d	display diffs instead of rewriting files
  -e	report all errors (not just the first 10 on different lines)
  -format-only
    	if true, don't fix imports and only format. In this mode, goimports is effectively gofmt, with the addition that imports are grouped into sections.
  -l	list files whose formatting differs from goimport's
  -local string
    	put imports beginning with this string after 3rd-party packages; comma-separated list
  -memprofile string
    	memory profile output
  -memrate int
    	if > 0, sets runtime.MemProfileRate
  -srcdir dir
    	choose imports as if source code is from dir. When operating on a single file, dir may instead be the complete file name.
  -trace string
    	trace profile output
  -v	verbose logging
  -w	write result to (source) file instead of stdout
```
만약 <code>goimports</code> 라는 명령어를 찾을수 없다고 한다면 PATH 설정을 다시 해주어야 한다.
> command not found: goimports
