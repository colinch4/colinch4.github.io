---
layout: post
title: "팀 개발을 위한 Git, GitHub 시작하기 - 0"
description: " "
date: 2020-08-12
tags: [git]
comments: true
share: true
---


<hr/>

## CHAPTER 0 : 빠른 실습으로 Git, GitHub 감 익히기

**🖊01.Git, 그리고 GitHub**
- Git은 소스코드 버전 사이를 오고가는 시간 여행이상의 기능을 제공
- 이렇게 Git 으로 관리하는 프로젝트를 올려둘 수 있는 Git 호스팅 사이트 중 하나가 바로 GitHub
- 누구든지 기여할 수 있는 공개저장소 프로젝트 > 오픈소스

**🖊02.Git을 설치하고 로컬저장소에서 커밋 관리하기**
- git 설치하는 페이지로 들어갔는데, homebrew 를 설치해야 할 것 같아서 [homebrew](https://brew.sh/index_ko) 에서 설치함
- 책과는 약간 달라서 이 [주소](https://nillk.tistory.com/1) 코드를 참고하였다.
- 그랬더니 책과 같이 git 을 쳤을때 화면이 같아짐!
- 터미널에서 파일 경로로 들어갈때 커맨드누르면서 폴더를 드래그 하면 경로가 자동으로 입력!
- bash 에서 실행 : 

<pre><code> - git init
- git config --global user.email "내이메일"
- git config --global user.name "내이름"
</pre></code>

- 위에 부분에서 해맸다.. user.email 이후에 내 이메일을 넣어야함!

<pre><code> - git add README.text
- git commit -m "사이트 설명 추가"
**파일의 내용을 수정한다.**
- git add README.text
- git commit -m "설명 업데이트"
</pre></code>


<pre><code>- git log </pre></code>

- 하면 위에 커밋한 두개를 확인할 수있고 앞의 아이디를 복사해서 

<pre><code>- git checkout 8081393(아이디 전체 넣어도 됨) 
- git checkout -
</pre></code>

- 첫번째 처럼 하면 해당 아이디, 즉 책에서 말하는 시간여행이 가능하다 (해당하는 아이디의 상태로 돌아갈 수 있다.)
- 두번째처럼 하면 최신커밋으로 돌아간다.

>> 하지만 나는 여기서 첫번째 커밋했던 사이트 설명 추가 로 돌아가긴 하지만, 파일은 보이지 않는다 (첫번째에 text > rtf 여서 그런가..)
>> 그래도 최신커밋으로 돌아가기는 한다!

**🖊03.GitHub 원격저장소에 커밋 올리기**
- new repository 를 파고 첫 페이지에서 주소를 복사한뒤 bash 로 돌아간다.
- 올릴 폴더에서 

<pre><code>- git remote add origin 주소 
- git push origin master
</pre></code>

- 여기까지 따라오면 암호를 입력하라고 뜨는데, 맥의 암호였다!
- 그 이후 내가 폴더에 만들었던 파일(README)이 해당 repository 에 올라온걸 확인 할 수있었다.

>> 하지만 저번 오류때문인지 잘 업로드 되었지만 안에 내용물이 이상하게 써져있었다 ;;

**🖊04.GitHub 원격저장소의 커밋을 로컬저장소에 내려받기**
- 해당 repository 의 파일을 클론해 오고싶을때는, 클론 주소를 복사한 뒤 해당 폴더로 이동(bash)

<pre><code>- git clone 주소 .
</pre></code>

**한칸 뛰고 마침표필수**
- 이렇게 하면 파일이 그대로 받아진것을 확인 할 수 있다.
- 여기서 한칸 뛰고 마침표를 하는 이유는 해당 폴더 안에 또 해당 레파지토리 폴더가 생긴 뒤 파일들이 만들어지는 것을 막기위해!

>> 이렇게 하면 .git 폴더가 확인된다는데, 나는 확인할 수 없었다 ㅠㅠ

- 새로운 폴더에서 수정후 커밋하는 방법은 

<pre><code>- git add 파일(ex README.text).
- git commit -m "커밋설명내용"
- git push origin master
</pre></code>

- 하지만 이렇게 하면 원본 폴더의 파일은 바뀌지않는데, 새로운 커밋이 있다면 받아오라는 명령어는 

<pre><code>- git pull origin master
</pre></code>


**용어정리👉**
- GUI : 그래픽 유저 인터페이스, 마우스로 클릭해서 사용하는 방식
- CLI : 커맨드 라인 인터페이스, 명령어를 하나씩 입력하는 방식
- log 명령어 : 지금까지 만든 커밋을 모두 확인
- 체크아웃한다 : checkout 으로 원하는 지점으로 파일을 되돌릴 수 있다.
- 로컬저장소 : Git 으로 버전 관리하는 내 컴퓨터 안의 폴더
- 원격저장소 : GitHub 에서 협업하는 공간(폴더)
- 레퍼지토리 : 원격저장소
- 풀 : 원격저장소의 커밋을 로컬저장소로 내려받는 것.


