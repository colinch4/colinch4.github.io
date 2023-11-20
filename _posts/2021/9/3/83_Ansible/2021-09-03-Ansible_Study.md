---
layout: post
title: "[Ansible] Ansible 정리"
description: " "
date: 2021-09-03
tags: [개발]
comments: true
share: true
---


## Ansible 정리

(# 앤서블 철저 입문 요약)

## 1. 개요

## 1.1 앤서블 구성

### 1.1.1 본체

앤서블 소프트웨어 그 자체



### 1.1.2 인벤토리

* 대상이 되는 서버 접속 정보를 표시
* 그룹화 및 변수를 사용한 파라미터 설정 가능
* API를 통해 동적으로 인벤토리 정보를 생성하는 동적 인벤토리 지원



### 1.1.3 모듈 

앤서블에서 실행된 하나하나의 명령

* OS 내의 작업 / 파일 작업 / DB 작업 / 클라우드 서비스 작업 / 네트워크 장비 작업

* 작업을 실행하기 전에 그 시점의 상태를 알아두고, 변경이 있을 때만 작업을 수행

* 내장 모듈 확인

  > ansible-doc -l



### 1.1.4 플레이북

- 앤서블에서 스크립트(코드)
- 앤서블을 사용할 때 필요한 작업은 **플레이북 구현과 실행**
- YAML 로 기술



## 1.2 특징

- 에이전트리스
- 멱등성(Idempotency)
  - 어떤 작업을 여러 번 실행해도 결과가 항상 같다는 성질
  - 앤서블은 최종 본래의 형태를 '선언적'으로 다뤄 멱등성이 보장
  - 이전의 상태와 관계 없이 최종적인 결과가 바람직한 상대가 되는 것
- 재사용성
  - 변수를 사용한 값의 추상화
  - 플레이북 자체를 롤(Role)이라는 단위로 부품화. 롤은 플레이북을 각 시스템에서 공통적으로 사용하는 단위로 분리한 것



## 2. 앤서블 사용

## 2.1 플레이북

### 2.1.1 플레이북 기본형

```yaml
---
- name: Test
	hosts: all
	tasks:
```

- name : 로그에 표시되는 이름
- hosts : 배포 대상 호스트 지정
- tasks : 실제 태스크 정의



### 2.1.2 플레이

- 플레이북에서 한 블록은 플레이(Play)
- 여러 개의 플레이를 1개의 플레이북 안에 기술 가능



### 2.1.3 실행

> ansible-playbook -i (inventory_name) (playbook_name)



### 2.1.4 관리자 권한 실행

hosts 밑에 다음을 추가

> become : true 



### 2.1.5 태스트 작성 방법

```yaml
- name: <Task를 알기 쉽게 정한 이름>
	<module name>:
		<module arg1>: <arg value1>
		<module arg2>: <arg value2>
		
	<task directive2>: <directive value2>
```

- name : 실행할 태스크 이름
- module_name : 사용하는 모듈의 이름
- module_arg : 모듈에 건네주는 인수
- task directive : 태스크를 실행 단위별로 지정할 수 있는 지시자





## 2.2 자주 사용하는 모듈

### 2.2.1 파일 작업

#### File - 파일과 디렉터리 상태 작업

```yaml
- name: ~~~~~
	file:
		path: /tmp/dir1
		state: directory
```

state에 가능한 설정 값

- file : 기본값. 파일의 속성을 변경할 때 사용
- touch : touch 명령과 동일한 작동
   link : 심볼릭 링크 생성		/ path 대신 src, dest 지정
    hard : 하드 링크 생성		/ path 대신 src, dest 지정
- absent : path가 존재하는 경우, 파일과 디렉터리 삭제



#### Copy - 파일을 작업 대상에게 전송

앤서블 운용 서버에 존재하는 파일을 작업 대상 서버에 전송 가능

```yaml
- name: 파일을 복사하는 샘플 플레이
	hosts: all
	tasks:
		- name: 운용 서버의 파일을 원격으로 복사
		  copy:
			src: original_file
			dest: ~/copied_file
```

- src에 대상 경로를 지정하면 **플레이북 파일을 기점**으로 파일 검색



#### lineinfile - 기존 파일을 행 단위로 수정

```yaml
tasks:
	- name: root가 패스워드로 ssh 로그인 금지
	  lineinfile:
	  	dest: /etc/ssh/sshd_config
	  	regexp: '^PermitRootLogin\s+'
	  	line: PermitRootLogin without-password
	  	validate: sshd -t -f %s
	  notify:
	  	- sshd 재시작
handler:
	- name: sshd 재시작
	  service:
	  	name: sshd
	  	state: restarted
```

- validate : 수정이 끝난 파일을 검증하는 명령 실행. %s에 앤서블을 설치할 때 임시 파일을 저장하는 경로가 자동 입력
- notify : 태스크의 실행 결과가 changed일 경우에는 지정된 이름의 핸들러를 플레이 실행 시 맨 마지막으로 처리



### 2.2.2 명령어 실행 모듈

####  command - 임의의 명령 실행

```yaml
- name: ssh 생성 플레이
  hosts: all
  tasks:
  	- name: ssh 키 생성
  	  command: "/usr/bin/ssh-keygen -b 2048 -t rsa -N '' -f /tmp/new-id-rsa"
  	  args:
  	  	creates: /tmp/new-id-rsa
```

추가로 옵션을 설정해야 할 때는 args 지시자 안에 일반적이 모듈과 같이 명명된 인수 정의 가능

- creates : 명령을 실행한 후 생성될 파일의 경로 지정
- removes : 명령을 실행한 후 삭제될 파일의 경로 지정
- chdir : 명령을 실행할 때의 기점이 되는 디렉터리를 지정
- executable : 명령을 실행할 때 사용될 쉘 경로



#### command 모듈 사용 주의점

- 명령을 실행한 후, 종료 상태가 0일 때 성공, 그외는 실패
- 성공 시 실행 결과는 항상 changed 상태
- 쉘의 고유한 기능인 파이프, 리다이렉트는 X
- $ 기호를 사용한 환경 변수 참조 X



#### raw - 파이썬을 거치지 않는 명령을 저레벨로 실행

앤서블 모듈은 파이썬을 거쳐서 실행되지만, raw 모듈을 사용하면 파이썬이 설치되지 않은 환경에서도 SSH를 통해 명령어를 직접 실행 가능

```yaml
- name: ~~~~
  gather_facts: false
  hosts: all
  become: true
  tasks:
  	- name: ~~~~
  	  raw: yum -y install python-simplejson  
```



## 3. 앤서블 상세 기능

## 3.1 인벤토리

- 인벤토리 파일
  - INI 형식의 파일에 호스트 정보를 간단하게 기술
  - 작업 대상 호스트의 접속 정보를 미리 알고 있는 것을 전제
- 동적 인벤토리 스크립트
  - 호스트 정보를 JSON 형식의 표준 출력으로 표시할 스크립트
  - 앤서블 명령을 실행할 때 실시간으로 스크립트 실행
  - 스크립트에서 외부 시스템에 접근할 때, 동적으로 호스트 정보 가져올 수 있음



### 3.1.1 정적 인벤토리 파일 작성

``` ini
[app]
app1 ansible_host=some.app.host
app2 ansible_host=another.app.host

[db]
db1 ansible_host=db.1.host
db2 ansible_host=db.2.host
```

#### 그룹 변수 정의

[그룹이름:vars] 형식으로 그룹 변수 전용 섹션 사용

```ini
[app]
app1 ansible_host=some.app.host
app2 ansible_host=another.app.host

[db]
db1 ansible_host=db.1.host
db2 ansible_host=db.2.host

[app:vars]
admin_username=app_user
admin_uid=1001

[db:vars]
admin_username=db_user
admin_uid=1002
```

#### 호스트를 여러 그룹에 할당

```ini
[app]
app1 ansible_host=some.app.host
app2 ansible_host=another.app.host

[db]
db1 ansible_host=db.1.host
db2 ansible_host=db.2.host

[koreaeast]
app1
db1

[koreawest]
app2
db2
```

- 그룹 간에 변수를 중복해서 정의하면 X
- 호스트 이름이 같은 경우는 항상 같은 호스트로 다뤄짐





### 3.1.2 인벤토리 변수를 YAML 파일에 정의

인벤토리 변수는 전용 YAML 파일에 정의 가능

#### 변수를 정의하는 파일 이름의 규칙

- 호스트 변수를 정의하는 파일은 **host_vars/<호스트 이름>.yml**
- 그룹 변수를 정의하는 파일은 **group_vars/<그룹 이름>.yml**
- host_vars, group_vars 디렉터리는 인벤토리 파일 또는 플레이북 파일과 같은 디렉토리에 있어야함



#### 인벤토리 변수 우선순위

- 플레이북에 있는 변수를 정의한 YAML 파일
- 인벤토리에 있는 변수를 정의한 YAML 파일
- 인벤토리 파일에서 정의한 변수



### 3.1.3 플레이북에서 인벤토리 작업

#### add_host - 호스트 정보 추가

```yaml
- name: 새로 작성된 app용 호스트 정보를 인벤토리에 추가
  add_host:
  	name: created-host
  	groups: created,app3
  	ansible_host: "{{ created_host_ip }}"
  	ansible_port: 22
```

add_host로 등록된 호스트 정보를 사용할 수 있는 것은 호스트를 추가한 이후의 플레이부터 가능.



#### group by - 등록된 호스트를 새로 그룹화

해당 모듈을 사용하면 setup 모듈이 자동으로 OS 정보 변수를 확인하고, 그것을 기준으로 OS별로 호스트 그룹화 가능

```yaml
- name: OS 별로 그룹화
  hosts: all
  tasks:
  	- name: ~~
  	  group_by:
  	  	key: "{{ ansible_os_family }}"
  	  	
- name: 레드햇 계열 업데이트용 플레이
  hosts: Red Hat
  ...
  
- name: 데비안 계열 업데이트용 플레이
  hosts: Debian
  ...
```



## 2. 변수

### 2-1. 변수 정의 방법

- 모듈이 자동으로 정의(Facts)
- 인벤토리 레벨에서 정의
- 앤서블이 실행될 때 정의
- 플레이북에서 정의

#### 앤서블을 실행할 때 변수를 정의하는 옵션

--extra-vars(-e)  를 사용하면 띄어쓰기로 구별한 key=value 형식으로 변수 전달 가능

> ansible-playbook -i hosts -e 'nginx_version=1.10.2 nginx_user=nginx' site.yml

#### 플레이북에서 변수 정의

- vars 지시자로 직접 정의

  vars 지시자를 사용하면 플레이북의 플레이와 태스크에서 변수를 직접 지정 가능

```yaml
---
- name: 포트 번호를 사용하는 플레이
  hosts: all
  vars:
  	nginx_http_port:80
  	mysql_port: 3306
```

- 외부 파일에서 변수 읽어 들이기 - vars_files 지시자

  vars_files는 변수를 정의한 YAML 파일의 경로를 다음과 같이 여러 줄로 지정하면 한꺼번에 읽어 들임

```yaml
vars_files:
	- some_vars.yml
	- another_vars.yml
```

### 2-2. 변수 우선순위



























































