---
layout: post
title: "팀 개발을 위한 Git, GitHub 시작하기 - 6, 7"
description: " "
date: 2020-11-12
tags: [git]
comments: true
share: true
---

<h1 id="팀-개발을-위한-git-github-시작하기">팀 개발을 위한 Git, GitHub 시작하기</h1>
<hr>
<h2 id="chapter-6--part-1에서-수행했던-기본-명령어">CHAPTER 6 : PART 1에서 수행했던 기본 명령어</h2>
<p><strong>🖊01. 왜 CLI를 사용할까?</strong></p>
<p><strong>🖊02. Git Bash를 시작하자</strong></p>
<ul>
<li>$ 기호와 표시된 경로등을 합쳐서 : 프롬프트(prompt)</li>
<li><strong>프롬프트</strong>는 CLI에서 가장 기본적인 정보를 보여준다.</li>
<li>프롬프트 끝에 브랜치명이 보인다면 Git 작업 폴더임을 의미</li>
</ul>
<p><strong>Git Bash 명령어</strong></p>

<table>
<thead>
<tr>
<th>명령어</th>
<th>설명</th>
</tr>
</thead>
<tbody>
<tr>
<td>pwd</td>
<td>현재 폴더 위치 확인</td>
</tr>
<tr>
<td>ls -a</td>
<td>현재 폴더 위치 확인</td>
</tr>
<tr>
<td>cd</td>
<td>홈 폴더로 이동(홈 폴더는 사용자 이름과 폴더명이 같고 내 문서 폴더의 상위폴더)</td>
</tr>
<tr>
<td>cd 폴더이름</td>
<td>특정 위치의 디렉토리로 이동</td>
</tr>
<tr>
<td>cd …/</td>
<td>현재 폴더의 상위폴더로 이동</td>
</tr>
<tr>
<td>mkdir 새폴더이름</td>
<td>현재 폴더의 아래에 새 폴더를 만듬</td>
</tr>
<tr>
<td>echo “Hello Git”</td>
<td>메아리라는 뜻, 화면에 ""안의 문장인 "Hello Git"을 표시</td>
</tr>
<tr>
<td>git status</td>
<td>Git 워킹트리의 상태를 보는 명령으로, 매우 자주 사용 / 워킹트리가 아닌 폴더에서 사용하면 오류 발생</td>
</tr>
<tr>
<td>git status -s</td>
<td>git status 명령보다 짧게 요약해서 상태를 보여주는 명령으로, 변경된 파일이 많을 때 유용</td>
</tr>
<tr>
<td>git init</td>
<td>현재 폴더에 Git 저장소를 생성. 현재 폴더에는 [ .git ] 이라는 숨김 폴더가 생성되는데 사실 이 폴더가 로컬저장소이다.</td>
</tr>
<tr>
<td>git reset 파일명</td>
<td>스테이지 영역에 있는 파일을 스테이지에서 내린다.(언스테이징), 워킹트리의 내용은 변경되지 않으며 옵션을 생략할 경우 스테이지의 모든변경사항을 초기화한다.</td>
</tr>
<tr>
<td>git log</td>
<td>현재 브랜치의 커밋 이력을 보는 명령어(HEAD와 관련된 커밋이 자세히 나온다)</td>
</tr>
<tr>
<td>git log -n숫자</td>
<td>전체 커밋 중에서 최신 n개의 커밋만 살펴본다</td>
</tr>
<tr>
<td>git log --oneline</td>
<td>간단한 커밋 해시와 제목만 보고싶을때</td>
</tr>
<tr>
<td>git log --online --graph --decorate</td>
<td>HEAD와 관련된 커밋을 조금 더 자세히 보고싶을때</td>
</tr>
<tr>
<td>git log --online --graph --all --decorate</td>
<td>모든 브랜치를 보고 싶을때</td>
</tr>
<tr>
<td>git help 명령어</td>
<td>ex git help commit, git help status 처럼 명령어의 도움말이 표시함</td>
</tr>
<tr>
<td>git remote add 원격저장소이름 원격저장소주소</td>
<td>원격저장소 등록, 같은 별명의 원격저장소는 하나만 가질 수 있고 통상 첫번째는 원격저장소를 origin 으로 저장</td>
</tr>
<tr>
<td>git remote -v</td>
<td>원격저장소 목록을 살펴봄</td>
</tr>
</tbody>
</table><p><strong>Git 용어정리</strong></p>

<table>
<thead>
<tr>
<th>용어</th>
<th>설명</th>
</tr>
</thead>
<tbody>
<tr>
<td>워킹트리</td>
<td>워킹트리, 워킹 디렉토리, 작업 디렉토리, 작업 폴더 모두 같은 뜻으로 사용.일반적으로 사용자가 파일과 하위폴더를 만들고 작업 결과물을 저장하는 곳을 Git에서는 워킹트리라고 부름. 공식문서에서는 워킹트리를 '커밋을 체크아웃 하면 생성되는 파일과 디렉토리’로 정의. 정확하게는 작업 폴더에서 [ .git ] 폴더(로컬저장소)를 뺀 나머지 부분이 워킹트리 / <strong>일반적인 작업이 일어나는 곳</strong></td>
</tr>
<tr>
<td>로컬 저장소</td>
<td>Git init 명령으로 생성되는 [ .git ] 폴더가 로컬저장소. 커밋, 커밋을 구성하는 객체, 스테이지가 모두 이 폴더에 저장 / <strong>.git 폴더, 커밋은 여기에 들어있다.</strong></td>
</tr>
<tr>
<td>원격 저장소</td>
<td>로컬저장소를 업로드 하는곳을 원격저장소라고 함. 우리가 사용하고 있는 GitHub 저장소가 원격저장소</td>
</tr>
<tr>
<td>Git 저장소</td>
<td>Git 명령으로 관리할 수 있는 폴더 전체를 일반적으로 Git 프로젝트 혹은 Git 저장소라고 부름. 일반적으로 Git 저장소를 워킹트리 + 로컬저장소의 느낌으로 사용하지만 공식문서에서는 로컬저장소와 Git 저장소를 같은 뜻으로 사용. / <strong>엄밀하게는 로컬저장소를 의미하지만 넓은의미로 작업폴더를 의미하기도 함</strong></td>
</tr>
</tbody>
</table><ul>
<li>작업폴더 = 워킹트리 + 로컬저장소</li>
</ul>
<p><strong>Git 로컬저장소를 위한 새폴더 만들기</strong></p>
<pre><code>$ mkdir 폴더이름     # 새폴더를 만든다
$ cd 만든폴더이름/     # 만든 폴더로 이동한다
$ pwd     # 현재 어디에 있는지 확인</code></pre>
<p><strong>Git 저장소 초기화</strong></p>
<pre><code>$ git init     # git 저장소를 생성
$ ls -a     # 무슨 파일이 있는지 목록 확인
$ git status     # 워킹트리 상태 확인</code></pre>
<ul>
<li>git init 을 하기전에 status 를 했을때는 에러가 떳었다. 단, 기존 git 폴더 밑 하위폴더라면 status 에러가 뜨지 않는다.</li>
</ul>
<p><strong>Git 전역옵션 설정</strong></p>
<pre><code>$ git config --global user.name     
#기존에 나는 설정을 해놔서 이렇게 치면 내 이름이 뜨는데 안 뜰 경우엔 
$ git config --global user.name "이름"   # 로 설정해줘야한다.</code></pre>
<p><strong>Git 기본에디터 확인</strong></p>
<pre><code>$ git config core.editor     
$ git config  --global core.editor   
$ git config  --system core.editor       </code></pre>
<blockquote>
<p>-비쥬얼 스튜디오 코드랑 git 이 연결이 안되서 헤맸는데 vscode 에서 보기 &gt; 명령팔레트 &gt; shell command &gt; 셸 명령 PATH에 ‘code’ 명령 설치를 눌러주고 나서는 해결되었다</p>
</blockquote>
<p><strong>🖊03. 기본 CLI 명령어 살펴보기</strong></p>
<p><strong>간단한 텍스트 파일 생성하고 확인하기</strong></p>
<pre><code>$ echo "hello git"     # 화면에 큰 따옴표("")안에 텍스트를 보여준다.     
$ echo "hello git" &gt; file1.md     # 큰 따옴표 안의 텍스트로 파일 생성
$ ls     # 현재폴더 파일 목록 확인
$ git status     # 상태를 확인할 수 있다
#현재는 위에서 파일이 생성됬지만, 스테이지에 올라가지 않은것을 알 수 있다.     </code></pre>
<p><strong>생성한 파일 스테이지에 추가하기</strong></p>
<pre><code>$ git add file1.md     
$ git status     # 파일이 스테이지 영역에 추가 된 것을 알 수 있다.     </code></pre>
<p><strong>스테이지에서 파일 언스테이징 하기</strong></p>
<pre><code>$ git status     # 현재 파일이 올라간 상태라면     
$ git reset file1.md     # 언스테이징
$ git status     # 파일이 내려간것을 볼 수있다.
$ cat file1.md     # cat 을 앞에 붙여주면 뒤에 파일을 터미널 화면에 뿌려준다.   </code></pre>
<p><strong>첫번째 커밋 생성</strong></p>
<pre><code>$ git commit     # 커밋 실행, vscode가 열리면 커밋메세지 입력후 저장&amp;닫기   </code></pre>
<ul>
<li>vscode 가 열리고 첫째줄에는 작업내용의 요약(제목), 다음줄에는 자세하게 작업내용을 기록(본문)하는데 첫번째 줄과 둘째줄 사이에는 반드시 한줄을 비워야 한다.</li>
<li>vscode 종료</li>
<li>만약 vscode가 열렸는데 커밋하고 싶지 않아진다면, 그냥 vscode를 종료해도 된다 (커밋 취소됨)</li>
</ul>
<p><strong>커밋 확인해보기</strong></p>
<pre><code>$ git status     #깨끗한상태임을 알려준다
$ git log --oneline --graph --all --decorate </code></pre>
<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/book-git/images/%EB%8F%84%EC%84%9C/git%20log.png" width="60%">
<p><strong>좋은 커밋 메세지의 7가지 규칙</strong></p>
<ol>
<li>제목과 본문을 빈 줄로 분리한다.</li>
<li>제목은 50자 이내로 쓴다.</li>
<li>제목을 영어로 쓴 경우 첫 글자는 대문자로 쓴다.</li>
<li>제목에는 마침표를 넣지 않는다.</li>
<li>제목을 영어로 쓴 경우 동사원형(현재형)으로 시작한다.</li>
<li>본문을 72자단위로 줄바꿈한다.</li>
<li>어떻게 보다 무엇과 왜를 설명한다.</li>
</ol>
<p><strong>🖊04. 원격저장소 관련 CLI 명령어</strong></p>
<p><strong>원격저장소 등록 및 push</strong></p>
<pre><code>$ git remote add origin 주소     
$ git remote -v
$ git push </code></pre>
<ul>
<li>위와 같이 push를 하게 되면 밑에와 같은 에러가 뜬다.</li>
</ul>
<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/book-git/images/%EB%8F%84%EC%84%9C/git%20push%20error.png" width="60%">
<ul>
<li>업스트림 브랜치는 로컬저장소와 연결된 원격저장소를 일컫는 단어이다.</li>
<li>업스트림 브랜치 설정을 위해 에러메세지가 알려준대로 --set-upstream 을 쓰거나 단축 명령인 -u 옵션을 사용</li>
<li>이후에는 origin 저장소의 master 브랜치가 로컬저장소의 master 브랜치의 업스트림으로 지정되어 에러없이 push 가능해진다.</li>
</ul>
<p><strong>git push 재시도</strong></p>
<pre><code>$ git push -u origin master      # push 와 동시에 업스트림 지정     
$ git log --oneline -n1
$ git push </code></pre>
<p><strong>git clone 사용해보기</strong></p>
<pre><code>$ pwd     
$ cd ../     # 반드시 상위 디렉토리로 이동할 것!
$ git clone 클론할주소 새로운폴더명
$ ls
$ cd 새로운폴더명
$ git log --oneline
$ git remote -v     # 원격저장소 목록 확인</code></pre>
<p><strong>추가 commit and push</strong></p>
<pre><code>$ echo "second" &gt; file1.md     # 파일에 내용 한 줄 추가    
$ cat file1.md   
$ git commit -a     # 스테이징 없이 바로 커밋
$ git push
$ git log --oneline </code></pre>
<p><strong>git pull</strong></p>
<pre><code># 처음저장소로 이동     
$ git log --oneline      # 결과물을 보면 커밋은 하나뿐  
$ git pull
$ git log --oneline     # 첫번째, 두번째 커밋 확인 가능
$ cat file1.md     # 클론, 기존 내용이 합쳐진 것을 확인할 수 있다.
</code></pre>


  

## CHAPTER 7 : 브랜치 생성 및 조작하기

  

**🖊01. CLI로 브랜치 생성하기**

 - 커밋을 하면 커밋 객체가 생긴다. 커밋 객체에는 부모 커밋에 대한 참조와 실제 커밋을 구성하는 파일 객체가 들어있다.
 - 브랜치는 논리적으로는 어떤 커밋과 그 조상들을 묶어서 뜻하지만, 사실은 단순히 커밋 객체를 가리킬 뿐이다.
 
 **브랜치는 언제 사용 되는가?**
 
 - 새로운 기능 추가
 - 버그수정 ( ex hotFix, bugFix )
 - 병합과 리베이스 테스트
 - 이전코드 개선
 - 특정 커밋으로 돌아가고 싶을때  

**브랜치 생성하기**
|명령어 | 설명  |
|--|--|
| git branch -v | 로컬저장소의 브랜치 목록을 보는 명령, -v를 입력하면 마지막 커밋도 함께 표시, 표시된 브랜치 중에서 이름 왼쪽에 *가 붙어있으면 HEAD 브랜치 |
| git branch -f 브랜치이름 커밋체크섬 | 새로운 브랜치 생성, 커밋체크섬값을 주지 않으면 HEAD로 부터 생성, 이미 있는 브랜치를 다른 커밋으로 옮기고 싶을때는 옵션 -f를 줘야 함 |
| git branch -r v | 원격저장소에 있는 브랜치를 보고싶을 때 사용, -v 옵션을 추가하여 커밋 요약도 볼 수 있음 |
| git checkout 브랜치이름 | 특정 브랜치로 체크아웃때 사용, 브랜치 이름대신 커밋체크섬을 쓸수 있지만 브랜치이름을 사용하는것을 강력히 권장함 |
| git checkout -b 브랜치이름 커밋체크섬 | 특정 커밋에서 브랜치를 생성하고 동시에 체크아웃까지 함, 두 명령어를 하나로 합쳤기 때문에 자주 사용 |
| git merge 대상 브랜치 | 현재 브랜치와 대상 브랜치를 병합할때 사용, 병합 커밋이 새로생기는 경우가 많음 | 
| git rebase 대상 브랜치 | 내 브랜치의 커밋들을 대상 브랜치에 재배치 시킴, 히스토리가 깔끔해져서 자주 사용하지만 주의 필요 |
| git branch -d 브랜치이름 | 특정 브랜치를 삭제할때사용, HEAD 브랜치나 병합하지 않은 브랜치는 삭제할 수 없음 | 
| git branch -D 브랜치이름 | 브랜치 강제삭제 명령어, -d 로 지울수 없는 브랜치를 지우는데 주의 필요 | 
| git tag -a -m 간단한메세지 태그이름 브랜치또는체크섬 | -a 로 주석이 있는 태그를 생성, 메세지와 태그이름은 필수이며 브랜치 생략하면 HEAD에 태그 생성 |
| git push 원격저장소별명 태그이름 | 원격저장소에 태그를 업로드 |

**브랜치 만들기**
<pre><code> $ git log --oneline     # 커밋 로그 보기
$ git branch     # 현재 브랜치 확인 
$ git branch mybranch1     # 새로운 브랜치 생성
$ git branch     # 현재 브랜치 확인
$ git branch --oneline --all     # 변경된 브랜치 확인 </code></pre>

 - *master 이라는 의미는 HEAD -> master 와 동일한 의미 

**HEAD에 대해 반드시 기억할 점**

 1. HEAD는 현재 작업중인 브랜치를 가리킴
 2. 브랜치는 커밋을 가리키기 때문에 HEAD도 커밋을 가리킴
 3. 결국 HEAD는 현재 작업중인 브랜치의 최근 커밋을 가리킴

- **revert를 이용해 커밋을 되돌릴 경우는 최신 커밋부터 취소해주는것이 좋다 ex C1 <- F1 <- C2 <- F2 <- C3 (master)

<pre><code>$ git revert F2
$ git revert F1 </code></pre>


**🖊02. CLI로 checkout 하기**

- checkout  명령은 브랜치의 내용을 워킹트리에 반영할때 사용. 정확히는 브랜치가 가르키는 커밋의 내용을 워킹트리에 반영

**브랜치 만들기**
<pre><code>$ git checkout mybranch1     # 브랜치 체크아웃
$ git branch     # 현재 브랜치 확인
$ git log --oneline --all     # HEAD 변경 확인
$ cat file1.md     # 파일 내용 확인
$ echo "third - my branch" >> file1.md     # 파일에 내용추가
$ cat file1.md     # 파일 내용 확인
$ git status      # 스테이지 상태 확인
$ git add file1.md     # 스테이지에 변경사항 추가
$ git commit      # 커밋
$ git log --oneline --all     # 변경된 브랜치 확인 </code></pre>

**커밋 후 빨리감기 병합**
<pre><code>## mybranch1 에 새로운 커밋을 추가해주고
$ git checkout master    # 마스터 브랜치 체크아웃
$ cat file1.md     # 파일이 이전으로 돌아갔는지 확인
$ git merge mybranch1      # 병합, fast-forward
$ git log --oneline --all --graph    # 로그 확인
$ cat file1.md     # 파일 상태 재확인 </code></pre>

- 이번 병합은 작업의 흐름이 하나였기 때문에 빨리감기(fast-forward)병합으로 완료

**reset --hard 로 브랜치 되돌리기**
- reset 은 현재브랜치를 특정 커밋을 되돌릴때 사용
- git reset --hard 이동할 커밋체크섬: 현재 브랜치를 지정한 커밋으로 옮긴 후 해당 커밋의 내용을 작업폴더에도 반영
- 커밋체크섬은 git log 를 통해 확인 가능, 그러나 번거롭기 때문에 HEAD~ || HEAD^ 로 시작하는 약칭 사용 가능!

**HEAD~, HEAD^**
|  |  |
|--|--|
| HEAD~숫자 | HEAD~는 헤드의 부모 커밋, HEAD~2 는 헤드의 할아버지 커밋을 말한다. HEAD~n 은 헤드의 n 번째 위쪽 조상이라는 뜻 |
| HEAD^숫자 | HEAD^는 똑같은 부모 커밋, 반면 HEAD^2 는 두번째 부모 커밋을 가리킴. 병합커밋처럼 부모가 둘 이상의 커밋에서만 의미있음. |

**현재브랜치를 두 단계 이전을 되돌리기**
<pre><code>$ git reset --hard --HEAD~2   # 브랜치 되돌리기
$ git log --oneline --all   #  로그 확인</code></pre>

- 위에서 사용한 reset은 hard reset

**빨리감기 병합 상황에서 rebase 해보기**
- git rebase 대상브랜치 : 현재 브랜치에만 있는 새로운 커밋을 대상 브랜치 위로 재배치 시킴. 빨리감기 병합이 가능한 경우에는 rebase 명령을 수행하면 빨리감기병합을 한다. 

**rebase, push, branch 제거**
<pre><code>$ git checkout mybranch1    # 브랜치 변경
$ git rebase master     # rebase 시도
- current branch mybranch1 is up to date.
$ git log --oneline --all     # 로그 확인, 변한게 없다.
$ git checkout master     # 다시 master 브랜치 체크아웃
$ git rebase mybranch1     # 반대방향에서 rebase
$ git log --oneline --all     # 변경사항을 확인해보면 빨리감기 병합이 되었다.
$ git push     # push
$ git branch -d mybranch1     # 브랜치 삭제
$ git log --oneline --all -n2     # 로그 확인 </code></pre>

**tag 작성**
<pre><code>$ git log --oneline    # 로그 확인
$ git tag -a -m "첫번째태그생성" v0.1     # 주석있는 태그 작성
$ git log --oneline     # 태그생성확인
$ git push origin v0.1     # 태그 푸시</code></pre>



**🖊03. CLI로 3-way 병합하기**

 - 긴급한 버그 처리 시나리오
 1.  오류가 없는 버전(주로 tag가 있는 커밋)으로 롤백
 2. master브랜치로부터 hotfix 브랜치 생성
 3. 빠르게 소스 코드 수정 / 테스트 완료
 4. master 브랜치로 병합 (fast-forward) 및 배포
 5. 개발중인 브랜치에도 병합(충돌가능성 높음)

 **새로운 브랜치 및 커밋 생성**
<pre><code>$ git checkout master    # master 로 체크아웃
$ git checkout -b feature1    # feature1 브랜치 생성 및 체크아웃
$ echo "기능 1 추가" >> file1.md      # 파일내용수정
$ git add file1.md     # 스테이징
$ git commit     # 커밋
$ git log --oneline --graph --all --n2     # 로그확인</code></pre>

**hotfix 브랜치생성 및 커밋, master에 병합**
<pre><code>$ git checkout -b hotfix master     # master 로 부터 hotfix 브랜치 생성, 체크아웃
$ git log --oneline --all --n2     # 2개의 커밋 로그만 보기
$ echo "som hot fix" >> file1.md
$ git add file1.md
$ git commit 
$ git log --oneline -n1
$ git checkout master 
$ git merger hotfix     # 빨리감기 병합
$ git push     # 원격저장소로 push </code></pre>

- 이제 feature1 브랜치에도 병합을 해야하는데, feature1 과 master는 다른분기로 진행되고 있기 때문에 이경우에는 빨리감기 병합이 불가능 하다. > 이럴때는 3-way 병합!

**병합 및 충돌해결하기1**
<pre><code>$ git checkout feature1     # feature1로 체크아웃
$ git log --oneline --all
$ git merge master     # master와 병합을 시도하지만 실패한다.
$ git status     # 실패 원인 파악 </code></pre>

- 이렇게 됬을때 결과메세지에서 볼 수있는 것 처럼 git merge --abort 명령을 통해 merge를 취소할수도있다.
- 이때 vscode를 들어가면 충돌부분을 확인할 수 있다!

**병합 및 충돌해결하기2**
<pre><code>$ cat file1.md     # 최종 변경내용 확인
$ git add file1.md     # 스테이징
$ git status
$ git commit 
$ git log --oneline --all --graph -n4 </code></pre>

<img src="https://github.com/colinch4/colinch4.github.io/blob/master/_posts/2020/book-git/images/%EB%8F%84%EC%84%9C/3way%EB%B3%91%ED%95%A9.png" width="80%">

**🖊04. CLI로 rebase 해보기**

- 3-way 병합을 하면 병합 커밋이 생성되기 때문에 다소 지저분해지는데, 이때 트리를 깔끔하게 하고 싶다면 rebase를 사용할 수 있다!
- rebase === 재배치 (브랜치의 커밋들을 재배치 한다)
- **원격에 푸시한 브랜치를 rebase 할때는 조심해야한다. 여러 Git 가이드에서는 원격저장소에 존재하는 브랜치에 대해서는 rebase를 하지말 것 이라고 권하고 있음. ( rebase 전과 후의 커밋체크섬이 다름, 즉 이전의 커밋과 다른 커밋임)**

**reset --hard 및 rebase 시도**
<pre><code> ## feature1 브랜치로 전환
$ git reset --hard HEAD~    # 현재 브랜치를 한단계 되돌린다.(병합 커밋 사라짐)
$ git log --oneline --graph --all -n3
$ git rebase master     # HEAD 브랜치의 커밋들을 master 로 재배치
$ git push     # 원격에 push </code></pre>

- 하지만 위에와 같이 하면 에러가 뜬다.
 - 병합 전으로 돌아가기 때문에 충돌로 rebase에 실패하는데, 수동으로 충돌을 해결한 뒤 스테이지에 추가할 것을 알려줌. 
 - 이후 git rebase --continue 명령을 수행할 것도 알려줌.

**충돌 해결 및 rebase 이어서 하기**
<pre><code>$ git status     # 충돌 대상 확인 및 수동으로 충돌 해결 (vscode 이용)
$ git add file1.md     # 변경사항 스테이징 및 상태 확인
$ git status
$ git rebase --continue     # 리베이스 계속 진행
$ git log --oneline --graph --all -n2     
$ git checkout master 
$ git merger feature1     # 빨리감기 병합 </code></pre>

- merge 는 마지막 단계에서 $ git commit 을 이용하지만, rebase 는 $ git rebase --continue 명령어를 사용!!!

**3-way병합**
- 머지커밋생성한다. 한번만 충돌 발생한다는 장점이 있지만 트리가 지저분해진다는 단점이 있다.

**rebase**
- 현재커밋을 수정하면서 대상 브랜치 위로 재배치한다. 깔끔한 히스토리가 되는 장점이 있지만 여러번 충돌이 발생할 수도 있다.

**유용한 rebase의 사용법 : 뻗어나온 가지 없애기**

**보통 커밋 만들기**
<pre><code>$ echo "master1" > master1.md  
$ git add master1.md
$ git commit -m "master 커밋 1"
$ git push origin/master 
$ git log --oneline -n1 </code></pre>

**가지 커밋 만들기**
<pre><code>$ git reset --hard HEAD~     # HEAD를 한단계 되돌리기 
$ echo "master2" > master2.md
$ git commit -m "master 커밋 2"
$ git log --oneline --graph -n3 </code></pre>

**git pull 수행결과**
<pre><code>$ git pull     # git pull 수행
$ git log --oneline --graph --all -n4     # 병합커밋생성확인 </code></pre>

**rebase로 가지 없애기**
<pre><code>$ git reset --hard HEAD~ 
$ git rebase origin/master     # rebase 수행으로 현재 커밋 재배치
$ git log --oneline --all  --graph -n3  
$ git push </code></pre>

**임시브랜치 사용하기**
- 원래 작업하려고 했던 브랜치의 커밋으로 임시브랜치를 만들고 나면 해당 브랜치에서는 아무작업이나 막 해도 상관 없다!
- 이후 그 브랜치를 삭제하기만 하면 원상복구 되기 때문이다.
- 브랜치가 필요 없어지는 시점에서  $ git branch -D 브랜치이름  명령으로 삭제 가능하다.

**임시 브랜치 생성 사용 및 삭제**
<pre><code>$ git branch test feature1     # feature1 브랜치에서 임시 브랜치 생성
$ git checkout test
$ echo "아무말대잔치" > test.md
$ git add .
$ git commit -m "임시 커밋"     # 새로운 커밋 생성
$ git log --oneline --graph --all -n4
$ git checkout master
$ git branch -D test     # 임시브랜치 삭제
$ git log --oneline --graph --all -n3 </code></pre>






 
