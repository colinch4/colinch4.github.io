---
layout: post
title: "[mac] iTerm2로 강력한 터미널 설정하기"
description: " "
date: 2021-09-09
tags: [mac]
comments: true
share: true
---

# iTerm2로 강력한 터미널 설정하기

터미널을 좀더 편리하고 강력하게 사용하기 위해 iterm2와 homebrew, zsh(Z Shell), oh-my-zsh을 설치하고 사용한다.

### iTerm2 설치

[iTerm2 설치 링크](https://www.iterm2.com/) 를 통해 설치한다. Mac의 기본 터미널 기능을 확장해 단축키나 화면 나누기 등의 다양한 기능을 제공하는 프로그램이다.

최신 Stablized 버전으로 다운받은 후 압축을 풀면 iTerm2라는 맥 앱이 생긴다. 이 앱을 **맥 파인더**에서 **응용 프로그램**으로 옮겨준다.

### HomeBrew 설치

맥에서 라이브러리나 플러그인등을 쉽게 설치하게 도와주는 패키지 매니저다. 터미널(혹은 iTerm2)에 아래 명령어를 복사하여 설치를 진행한다.

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### zsh 설치

쉘의 확장판

```
brew install zsh
```

### Oh my ZSH 설치

zsh을 더 쉽게 사용하도록 도와주는 플러그인

```
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

