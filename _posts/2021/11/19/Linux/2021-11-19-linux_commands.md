---
layout: post
title: "[Linux] Linux Commands"
description: " "
date: 2021-11-19
tags: [linux]
comments: true
share: true
---


## Linux Commands
리눅스 명령어에 대해 알아보자.

리눅스는 개발자 친화적이기에 많은 엔지니어들의 사랑을 받는다. 리눅스는 시스템을 운영을 위한 OS로써 제일 높은 점유율을 갖고 있다. 리눅스가 가진 특징을 꼽자면 오픈소스, 보안성, 신뢰성, 호환성, 그리고 안정성이라 할 수 있겠다.

[리눅스 관련 포스트](https://babytiger.netlify.com/posts/intro-linux/)

> 링크를 클릭하여 이동  

| [A](#A) | [B](#B) | [C](#C) | [D](#D) | [E](#E) | [F](#F) | [G](#G) | [H](#H) | [I](#H) | [G](#G) | [K](#K) | [L](#L) | [M](#M) | [N](#N) | [O](#O) |
 [P](#P) | [Q](#Q) | [R](#R) | [S](#S) | [T](#T) | [U](#U) | [V](#V) | [W](#W) | [X, Y, Z](#XYZ) |

## C
  * Change
    * Change to Home  
    ```cd```  
    단순히 ```cd```만 입력한다면 home 으로 이동.

    * Change directory  
    ```cd```  

    * Change file owner and group  
    ```chown```  

  * Clear
    * Clear terminal screen  
    ```clear```  

  * Compare
    * Compare two files  
    ```cmp <file1> <file2>```  
    ```file1``` 과 ```file2``` 를 비교.

    * Compare two sorted files line by line  
    ```comm <file1> <file2>```  
    ```file1``` 과 ```file2``` 를 라인별로 비교.

  * Copy  
    * Copy file  
    ```cp <fileA> <fileB>```  
    ```fileA``` 를 ```fileB``` 에 복사

  * Create
    * Create file  
    ```touch <file>```  
    ```file``` 생성

## D
  * Delete
    * Delete all file  
    ```rm *```  
    모든 파일 삭제

    * Delete file  
    ```rm <file>```  
    ```file``` 삭제.

    * Delete directory  
    ```rm -r <directory>```  
    ```directory``` 삭제.

    * Delete directory forcefully  
    ```rm -rf <directory>```  
    ```directory``` 를 강제로 삭제.

    * Delete a group  
    ```groupdel```  
    그룹 삭제.


  * Display
    * Display all running processes  
    ```top```  
    시스템 운용상황을 모니터링하기.  

    * Display contents of a file.  
    ```cat <file>```  
    ```file``` 내용 출력.
        * cat 은 concatenate 의 약자.

    * Display contents of files.  
    ```cat <file1> <file2>```  
    다수의 파일을 연속하여 출력.  

    * Display contents of file with line number.  
    ```cat -n <file>```  
    ```file```의 내용을 행 번호와 함께 출력.

    * Display help for a built-in command.  
    ```help```  
    리눅스 도움말 보기.

    * Display information about user  
    ```finger user```  
    사용자 정보 보기.  

    * Display who is online.  
    ```w```  
    시스템에 현재 접속해 있는 사용자 보기.  

    * Display your currently active processes.  
    ```ps```  
    현재 실행중인 프로세스 보기.


  * Divide
    * Divide a file unto serveral parts  
    ```cut```  


## F
  * Find
    * find a file  
    ```find / -iname 'fileName'```   
    ```find / -iname 'fileName*'```


## K
  * Kill
    * Kill process id pid  
    ```kill <pid>```  
    프로세스 아이디(```pid```)를 지정하여 해당 프로세스 죽이기. 


## L
  * List
    * List active jobs  
    ```jobs```  
    현재 작업 상태 리스트 보기. 

    * List all directory  
    ```ls -al```  
    ```ls -a```  
    숨겨진 파일을 포함한 모든 디렉토리와 파일 보기.

    * List directory  
    ```ls```  
    현재 directory에 담긴 디렉토리와 파일 리스트 보기.

    * List directory in reverse order  
    ```ls -r```  
    현재 directory에 담긴 디렉토리와 파일 역순으로 보기.

    * List directory sort by last modified in ascending order.  
    ```ls -t```  
    마지막으로 수정된 오름차 순서로 파일 보기.



## M
  * Move
    * Move file  
    ```mv <file> <directory>```  
    ```file``` 을 원하는 ```directory``` 로 이동.


## P
  * Print
    * Print system name  
    ```hostname```  
    시스템의 이름 프린트.

    * Print user and gorup id  
    ```id```  
    사용자의 id와 그룹 id 프린트. 
      * uid : user id
      * gid : groun id

    * Print work directory  
    ```pwd```  
    현재 경로 프린트.


## S
  * Search
    * Search for pattern in files  
    ```grep <pattern> <file>```  
    ```file``` 에서 문자열 패턴이 존재하는지 검색  

  * Show
    * Show command history  
    ```history```  
    터미널에서 사용한 명령어 히스토리 보기.

    * Show current date & time  
    ```date```  
    현 날짜와 시간 보기  

    * Show current month's calendar  
    ```cal```  
    해당 월의 달력 보기  
    
    * Show current year's calandar  
    ```cal -y```  
    해당 연도의 모든 달력 보기  

    * Show current uptime  
    ```uptime```  
    리눅스 시스템이 실행된 시점부터 지금까지의 정보 보기.  
      * 시간
      * 로그인한 사용자 수
      * 시스템 평균 부하량

    * Show disk usage  
    ```df```  
    시스템의 디스크 사용량 보기.

    * Show directory space usage  
    ```du```  
    디스크의 사용 현황 보기.

    * Show kernel information  
    ```uname```  
    커널 정보 보기  

    <!-- * Show memroy & swap usage  
    ```free``` -->

    * Show possible locations of app  
    ```whereis app```  
    ```app```이 위치한 경로 보기
