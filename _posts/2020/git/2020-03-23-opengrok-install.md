---
layout: post
title: "OpenGrok 설치하기 (How to install OpenGrok)"
date: 2020-03-23 14:20
description: "Opengrok은 소스코드를 빠르고 유용하게 찾을 수 있는 엔진입니다. 저는 Linux kernel, Systemd, glib, glibc 등의 Code를 다운받고 빠르게 검색하는 용도로 자주 사용하고 있습니다. 다양한 컴퓨터 언어에 대해 지원하고 있으니 굉장히 유용하니 한번 구축해서 사용해 보시는 걸 추천드립니다. 그럼 지금부터 시작해보겠습니다. (저는 ubuntu 16.04 기준으로 작성합니다..)"
author: "kskim2"
tags: [OpenGrok]
summary: 
comments: true
share: true
---



Opengrok은 소스코드를 빠르고 유용하게 찾을 수 있는 엔진입니다. 저는 Linux kernel, Systemd, glib, glibc 등의 Code를 다운받고 빠르게 검색하는 용도로 자주 사용하고 있습니다. 다양한 컴퓨터 언어에 대해 지원하고 있으니 굉장히 유용하니 한번 구축해서 사용해 보시는 걸 추천드립니다. 그럼 지금부터 시작해보겠습니다. (저는 ubuntu 16.04 기준으로 작성합니다..)

제 글이 아닌  [OpenGrok page](http://oracle.github.io/opengrok/)  를 참고하여 구축하셔도 무방합니다 :-)

-   **Requirements**

먼저, Opengrok을 설치하기 전에 필요한 것들이 있습니다.

-   Java 1.8 version
-   Tomcat (8.x or later) or GlassFish
-   Universal ctags (Exuberant ctags work too)

저는 Tomcat을 사용하여 구축할 것 입니다. 아래 명령어를 사용하여 tomcat과 exuberant-ctags를 설치합니다. 아래 설치 사진을 보면 아시듯이 이미 java는 1.8버전이 설치되어 있네요. java 설치 관련해서는 많은 곳을 참고할 수 있으니 만약 설치가 안되어 있다면 꼭 설치해 주시기 바랍니다. Opengrok이 java로 개발되어 있어서 필요합니다 :)

$ sudo apt-get install tomcat8 tomcat8-admin exuberant-ctags

![](https://miro.medium.com/max/60/0*GpKPJZbgcF_SXxxR.?q=20)

![](https://miro.medium.com/max/820/0*GpKPJZbgcF_SXxxR.)

그럼 이제 본격적으로 Opengrok을 설치해보도록 하죠!! 먼저 Opengrok을 설치해야 합니다. 저는 아래 사이트에서 다운받았습니다.

![](https://miro.medium.com/max/60/0*i7CJu6fHp2bJOJJo.?q=20)

![](https://miro.medium.com/max/717/0*i7CJu6fHp2bJOJJo.)

[https://github.com/oracle/opengrok/releases/tag/1.0](https://github.com/oracle/opengrok/releases/tag/1.0)

opengrok-1.0.tar.gz을 다운받은 후 압축을 풀고 /var/ 디렉토리로 이동하였습니다.

$ cp ~/Downloads/opengrok-1.0.tar.gz

$ tar -xvzf opengrok-1.0.tar.gz

$ mv opengrok-1.0 /var/opengrok

![](https://miro.medium.com/max/60/0*j5CbdoHu3w3PVcAk.?q=20)

![](https://miro.medium.com/max/609/0*j5CbdoHu3w3PVcAk.)

opengrok-1.0.tar.gz을 다운받은 후 압축을 풀고 /var/ 디렉토리로 이동하였습니다. /var/opengrok 디렉토리로 이동하면 bin, doc, lib, man 4가지의 디렉토리를 보실 수 있는데요, 일단 저희는 bin 디렉토리 아래의 bin/Opengrok 파일에 집중하겠습니다.

$ cd /var/opengrok/bin

$ sudo chmod 755 Opengrok

$ sudo vi Opengrok

Opengrok file에서 여러분들이 신경써야 할 부분은 SRC_ROOT라는 변수입니다. 이 SRC_ROOT의 값을 검색할 코드들의 경로로 지정해 줍니다. 또는 src 디렉토리를 만들어주고 거기에 symlink를 이용할수도 있습니다. 저 같은 경우는 symlink를 이용해서 구축하였습니다.

$ cd /var/opengrok

$ mkdir src

$ sudo ln -s {Your_code_path} {symlink_name}

![](https://miro.medium.com/max/60/0*yp7QMXoHr4bTgHOo.?q=20)

![](https://miro.medium.com/max/720/0*yp7QMXoHr4bTgHOo.)

그 다음 /var/opengrok/bin 디렉토리로 이동해서 Opengrok 파일로 deploy를 해줄겁니다. deploy를 해주는 이유는 Tomcat에서 관리하는 디렉토리에 source.war 파일을 이동시켜 주기 위해서 입니다. 아래 명령어로 deploy 한 후 tomcat 디렉토리 밑에 source.war이 생성된 걸 알 수 있습니다.

$ cd /var/opengrok/bin

$ sudo ./Opengrok deploy

![](https://miro.medium.com/max/60/0*2EW_fuWtHF8WNlnK.?q=20)

![](https://miro.medium.com/max/666/0*2EW_fuWtHF8WNlnK.)

자, 그럼 모든 준비가 완료되었습니다.!! 이제 Indexing을 해보죠. 지금 경로(/var/opengrok/bin)에서 아까와 동일하게 Opengrok 파일을 이용해 줍니다. 이번 명령어의 옵션은 index입니다. Indexing하려는 프로젝트의 크기가 클수록 시간이 오래 걸릴수 있으니 기다려 주세요!!

$ ./Opengrok index

그럼 마지막으로 chrome이나 다른 브라우저에서  [http://localhost:{tomcat_port}/source](http://localhost:{tomcat_port}/source)  로 접속해 보세요 저같은 경우 tomcat_port는 8080 기본으로 사용중입니다. 접속하시면 아래 그림을 보실 수 있고, 저기서 이제 검색하시면 됩니다 !!

![](https://miro.medium.com/max/60/0*9BCR_f33G2GbB-Cn.?q=20)

![](https://miro.medium.com/max/684/0*9BCR_f33G2GbB-Cn.)

이상으로 Opengrok 설치기를 마치도록 하겠습니다. 궁금하신 점은 댓글 달아주세요 :-D
