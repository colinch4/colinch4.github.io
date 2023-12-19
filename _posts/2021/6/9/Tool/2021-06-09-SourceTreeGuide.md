---
layout: post
title: "[Tool] Git 소스트리 사용법 정리(모르는 내용 정리)"
description: " "
date: 2021-06-09
tags: [개발]
comments: true
share: true
---

Git 소스트리 사용법 정리(모르는 내용 정리)
==========================================

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

-	[브랜치 생성](#브랜치-생성)
-	[머지](#머지)
-	[커밋 되돌리기](#커밋-되돌리기)
-	[이 커밋으로 초기화](#이-커밋으로-초기화)
-	[채리픽](#채리픽)
-	[브랜치 삭제](#브랜치-삭제)

<!-- /code_chunk_output -->

### 브랜치 생성

1.	복제할 원본 브랜치로 체크아웃
2.	상단의 브랜 버튼 클릭
3.	브랜치명 입 후 브랜치 생성 버튼 클릭

### 머지

-	A 브랜치 <- B브랜치 로 머지시
	1.	머지 대상 브랜치(A 브랜치) 체크아웃
	2.	B 브랜치 마우스 우측 클릭
	3.	Merge B브랜치 into A브랜치 클릭

### 커밋 되돌리기

현재 commit 된 commit을 선택 후 이전 commit으로 되돌릴 수 있다. 순차적으로 되돌려야한다. 여러 단계를 건너 띄어서 되돌리기 하실 원치 않는 결과를 얻을 수 있고 되돌리기시 오류가 발생할 수 있다. 주의 필요. 최신 커밋 부터 순차적으로 되돌리기 한다.

1.	커밋 선택 마우스 우측 클릭
2.	커밋 되돌리기 선택
3.	'되돌리겠습니까?' 확인버튼 클릭

### 이 커밋으로 초기화

1.	커밋 선택 마우스 우측 클릭
2.	이 커밋으로 초기화 선택
3.	Mixed, Hard 선택 후 확인
	-	**Mixed** 는 선택한 커밋으로 초기화가 되어 선택한 커밋 이후의 commit 이력이 사라진다. 단. 이력만 초기화가 되고 그 이후 수정했던 파일은 그대로 남아서 새로운 커밋 파일로 뜬다.
	-	**Hard** 는 선택한 커밋으로 초기화가 되어 선택한 커밋 이후의 commit 이력이 사라진다. 단. 이력도 초기화 되고 이력 시점으로 파일이 돌아가 선택 커밋 이후 commit 한 파일들이 모두 삭제 된다.
	-	**Mixed** 와 **Hard** 상황에 맞춰 사용하자. 일반적으로 완전히 파일을 삭제하고 되돌릴 경우 **Hard** 를 사용하고 되돌려도 중요한 파일로 파일들을 살려서 봐야할 때 **Mixed** 를 이용해야겠다.

### 채리픽

-	체리픽(Cherry Pick)을 사용해야 하는 경우

	1.	여러 브랜치로 작업을 하는 중, 다른 브랜치에 있는 기능을 현재 브랜치에서 확인하고 싶을 때
	2.	누군가 작업도중 Commit Revert를 사용해 파일을 되돌린 경우

-	1번의 경우 사용법 ![채리픽](https://mblogthumb-phinf.pstatic.net/MjAxNzAzMjVfODAg/MDAxNDkwNDI4NTIyNTE4.rMTnMnYYIDjaGokZmLX3Rc-fVkvlSMyZV7jRwgCvG0wg.yfxCJGMel6j6C841QZ6QULVxCRhg4e_VECxP0KDNWLcg.PNG.kbh3983/스크린샷_2017-03-25_오후_4.54.45.png?type=w800)[위 이미지 출처](https://mblogthumb-phinf.pstatic.net/MjAxNzAzMjVfODAg/MDAxNDkwNDI4NTIyNTE4.rMTnMnYYIDjaGokZmLX3Rc-fVkvlSMyZV7jRwgCvG0wg.yfxCJGMel6j6C841QZ6QULVxCRhg4e_VECxP0KDNWLcg.PNG.kbh3983/스크린샷_2017-03-25_오후_4.54.45.png?type=w800)

	1.	3번에서 되돌리기로 2번을 갔을 경우 되돌리기전 3번 commit을 선택하여 마우스 우측을 클릭한다.
	2.	채리픽 선택한다.

-	2번의 경우 사용법

	-	소스트리로 하는 방법을 찾지 못했다.
	-	브랜치 1의 특정 commit을 브랜치2에 적용시
		1.	브랜치1 체크아웃
		2.	git checkout 브랜치1 SHA-1을 클립보드로 복사
		3.	브랜치2 체크아웃
		4.	터미널은 연다.
		5.	git cherry-pick {SHA1 ID}

### 브랜치 삭제

1.	삭제할 브랜치 마우스 오른쪽을 클릭
2.	브랜치명 삭제 클릭
3.	체크할 사항 체크하고 확인
