---
layout: post
title: "[howto] Vuepress와 GitHub Pages로 웹 호스팅하기"
description: " "
date: 2021-06-17
tags: [개발]
comments: true
share: true
---

## Vuepress와 GitHub Pages로 웹 호스팅하기

지인의 권유로 TIL 저장소를 조금 더 보기 편하게 웹페이지로 전환하는 작업을 수행하였고, 이 과정을 다시 글로 남긴다.

우선 현 저장소 TIL은 진유림님의 [`TIL`](https://github.com/milooy/TIL) 저장소와 "[1일 1커밋](https://milooy.wordpress.com/2015/10/08/daily-commit/)"이라는 글에서 영감을 받아서 시작하였다. 그리고 vuepress는 이래저래 들어보았지만, 결정적으로 써봐야겠다고 생각한 것은 장기효님의 [`Vue.js 개발자를 위한 ES6 입문서(무료)`](https://joshua1988.github.io/es6-online-book/)를 보고난 이후였다. 두 분이 커플인 것은 안 비밀인 것 같고, 최근 진유림님이 책을 내면서, 개발자 커플에서 저자 커플이 되었다. 하루하루 발전하는 모습이 멋지다.

어쨌거나 이렇게 시작된 일이어서, 오늘의 작업도 두 개발자의 저장소를 많이 참조하였다. 개념정도만 이해하는 수준에서 작업을 진행하였기 때문에 꽤 많은 시간이 걸렸는데, 지나고 보니 30분도 채 걸리지 않을 간단한 일이었기에, 그 과정을 조금 정리해서 남겨두어야 겠다는 생각을 했다.

## GitHub Pages의 이해

GitHub는 모든 저장소에 대하여 웹호스팅이 가능하도록 Pages라는 기능을 제공하고 있다. 방법은 3가지가 있는데, `gh-pages`라는 브랜치를 만들거나, `docs`라는 폴더를 저장소 최상위에 만들거나, 혹은 저장소 전체 문서를 웹호스팅할 수 있다. 웹호스팅이라고 해도, php같은 동적렌더링을 지원하는 것은 아니고, 정적 파일을 보여주는 정도로 이해하면 된다. 하지만 현재는 Jekyll같은 정적 사이트 생성도구가 매우 다양하기 때문에 큰 제약이 있는 것도 아니다. 프론트엔드는 깃헙으로 호스팅하고 동적으로 필요한 자료는 간단한 웹 API를 만들어서 연결해주면 되기 때문이다.

다시 돌아와, 3가지 설정방법은 특정 저장소를 선택한 상태에서 설정 메뉴에 들어가면, 옵션을 선택할 수 있다. 개인적으로 가장 쉬운 방식은 `docs` 폴더를 이용하는 방식으로, 일반적인 방식으로 저장소를 사용하되 `docs` 폴더를 최상위 폴더에 생성하고, 이 폴더 안에 html 코드를 넣어주면 된다. 웹호스팅할 html 코드의 수정이 잦지 않을 때 쓰기 편한 방식이다.

그리고 이렇게 생성된 웹페이지는 `<github_id>.github.io/<repo_name>` 같은 형태로 서비스된다. 즉, 이 저장소의 이름이 `TIL`이고, 나의 github id가 `taegon`이므로, [`https://taegon.github.io/TIL`](https://taegon.github.io/TIL)로 접속 가능하다.

여기서 또 하나, `https`는 http 프로토콜을 이용하여 데이터를 주고 받을 때 암호화하여 전송하도록 정의된 프로토콜인데, github에서는 설정에서 옵션 하나만 켜주면 바로 적용이 된다. 디폴트 값이 https를 적용하는 형태로 되어 있을 것이니, 별 걱정하지 않고 쓰면 된다. 이걸 사용하지 않으면, 최신 브라우저에서는 "이 페이지는 신뢰할 수 없습니다."와 같은 경고 문구를 보게 된다.

## vuepress로 웹페이지 만들기

`vuepress`는 이름에서 알 수 있듯이 `vue.js`를 이용하여 개발된 정적 사이트 생성도구이다. 기본적으로 자바스크립트이고, 서버사이드에서 돌아가므로 node.js를 이용한다고 생각하면 된다. `npm`를 이용하여 `vuepress`를 설치할 수 있고, `package.json`에서 실행스크립트를 지정할 수 있다. `vuepress`의 설정파일은 `.vuepress/config.js`이다.

기본적인 파일 구조는 루트 디렉토리에 `package.json` 파일과 `docs` 폴더가 필요하다. `docs` 폴더는 다른 이름으로 명명하여도 상관없다. `docs` 폴더 안에 컨텐츠 원본이 되는 마크다운 파일을 넣어주면 된다. 이 마크다운 파일을 처리하여 웹페이지를 만드는데, 만들어진 파일은 하위 폴더에 생성되는데, `docs/.vuepress/dist` 폴더에 html 파일들이 생성된다.

## 생성된 html 코드 커밋하기

생성된 정적 사이트를 서비스하기 위해서는 GitHub에 올려주어야 하는데, 앞서 `docs`나 저장소 전체를 서비스 하는 방식은 적합하지 않다. 정적 사이트를 생성할 때마다 생성하는 파일의 생성시간이나, 사이즈, 혹은 내부 링크 등이 변경될 수 있으므로, 실제 컨텐츠 변화량보다 소스코드 변화량이 너무커서 버전관리의 효용이 떨어진다. 즉 변경내용을 확인하기가 어렵다. 그래서 일회성으로 사용하는 방식으로 `gh-pages` 브랜치를 이용하는 방식을 이용하였다.

방법은 간단한데, `gh-pages` 브랜치를 새로 만들고, 거기에 생성된 소스코드를 전부 올리는 것이다. 이때, gh-pages는 이력관리가 필요치 않고, 항상 최신의 웹사이트 파일만 푸시되도록 한다.

이를 위해서, 배치 파일(`build.bat`)을 만들었다. 이 배치파일을 로컬에서 구동하면, `vuepress`를 실행하여 정적 페이지를 생성한 후, `gh-pages`에 푸시된다. 배치 파일은 [올려둔 소스 코드](https://github.com/taegon/TIL/blob/master/build.bat)를 참조하면 어렵지 않게 이해할 수 있다. 배치파일은 `vuepress` 홈페이지와 장기효님 저장소를 참고하였다.

여기서 단점은 모든 셋팅이 완료된 컴퓨터에서는 간단하게 배치파일만 실행하면 되는데, 다른 컴퓨터 혹은 모바일에서 컨텐츠를 업데이트 하였을 경우에는 정적 사이트를 갱신할 수 없다는 점이다. 그리고 컨텐츠를 업데이트 하고 나서, 배치파일 실행을 따로 해주어야 한다는 점에서 번거롭기도 하다. 이 점은 아래에 GitHub Actions를 통해서 해결할 문제이다.

여기까지가 배경설명이었고, 작업내용과 관련해서는 아래에 간단히 메모를 남겨두었다.

### vuepress 설치하기

1. 노드 설치하기: [node.js official website](https://nodejs.org/en/download/)
1. vuepress 설치하기: `npm install -g vuepress`

* [How To Install Node.Js And NPM On Windows](https://phoenixnap.com/kb/install-node-js-npm-on-windows)

### SSH 추가하기

1. 공개키 만들기: `ssh-keygen -t rsa -b 4096 -C "taegon.k@gmail.com"`
1. 공개키 복사하기: `clip < c:\Users\taegon/.ssh/id_rsa.pub`
1. SSH키 등록하기: [GitHub SSH keys](https://github.com/settings/keys)

* [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)
* [Adding a new SSH key to your GitHub account](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

## GitHub Actions를 이용하여 배포하기

GitHub Actions를 이용하면, 앞서 수작업으로 `build.bat`를 실행해주던 단계를 GitHub의 컴퓨터가 자동으로 대신해 준다. 이를 위해서 스크립트를 작성해주어야 하는데, `.github/workflows/main.yml`와 같은 형태로 yml 파일을 생성해주면 된다. 저장소의 `Actions` 버튼을 이용하면 생성을 도와주는 템플릿을 제공해준다.

간단하게 개념설명을 하자면, 이 스크립트는 컨테이너(혹은 가상머신이라고 이해하자)를 만들어서, 빈 컴퓨터이므로 필요한 프로그램을 설치하고(`node.js`같은 기반도구), 내가 작성한 코드가 실행되도록 지정한다. 새로운 컴퓨터에 설치부터 내가 작성한 코드를 이용할 수 있도록 지정해야 하므로, 다소 복잡해 보일 수 있지만, 매우 절차적인 방식이기 때문에 스크립트를 한 줄씩 읽어나가면 어렵지 않게 읽을 수 있다. 그리고 비슷한 작업을 한 사람이 분명 있을 것이므로, 다른 사람의 작업 내용을 아주 쉽게 차용해 쓸 수 있다. 여기서 중요한 점은 모든 사람이 동일한 환경(빈 컨테이너)에서 시작하므로, 개개인이 해결해야할 문제가 매우 적다.

내가 사용하고 있는 스크립트 코드가 아래에 있으므로, 먼저 한번 훑어보고 나머지 글을 읽어도 좋겠다. 글로 풀어서 설명을 하자면, "master" 브랜치가 푸시되면 (나는 마스터 브랜치 밖에 없으므로, 내가 컨텐츠를 업데이트 하면) 이 스크립트가 실행된다. 스크립트는 우분투에서 내 소스코드를 체크아웃하고, 노드를 설치하고, vuepress를 설치한 후, vuepress를 실행한다(`npm run docs:build`는 `package.json`를 참조하여 작업을 수행한다). 생성된 정적 사이트는 `./docs/.vuepress/dist`에 저장이 되는데, 이 폴더의 내용을 `gh-pages`로 푸시한다. 이것이 GitHub Actions 스크립트의 전부이다. 이제 실제로 어떻게 작업을 수행하였는지 좀 더 알아보자.

먼저 Actions에서 사용할 키를 생성해야 한다. 너무 당연해서인지 만드는 방법을 찾는 것이 쉽지는 않았는데, 아래 문서에서는 잘 설명이 되어 있어서 일부 발췌하였다. 나는 윈도우에서 작업했기 때문에, email 적는 부분(`$(git config user.email)`)은 그냥 내 이메일을 직접 적었다.

```bash
ssh-keygen -t rsa -b 4096 -C "$(git config user.email)" -f gh-pages -N ""
## You will get 2 files:
##   gh-pages.pub (public key)
##   gh-pages     (private key)
```

프로젝트 저장소로 가서, 저장소 설정으로 가면 배포키와 보안문자열을 저장할 수 있다.

* Go to **Deploy Keys** and add your **public key** with the **Allow write access**
* Go to **Secrets** and add your **private key** as `ACTIONS_DEPLOY_KEY`

아래 링크를 참조하여 아래와 같이 액션 스크립트를 작성하였다. 의존성 캐싱은 오류가 나서 제대로 적용이 안되었는데, 일단 돌아가는데 만족하기로 했다. 분명 수요가 있을텐데, 이렇게 문서를 찾기 어렵다는 게 너무 이상하다.

```yml
name: github pages

on:
  push:
    branches:
    - master

jobs:
  build-deploy:
    runs-on: ubuntu-18.04
    steps:
    - uses: actions/checkout@v1

    - name: Setup Node
      uses: actions/setup-node@v1
      with:
        node-version: '10.x'

    - run: npm install -D vuepress

    - run: npm run docs:build

    - name: Deploy
      uses: peaceiris/actions-gh-pages@v2
      env:
        ACTIONS_DEPLOY_KEY: ${{ secrets.ACTIONS_DEPLOY_KEY }}
        PUBLISH_BRANCH: gh-pages
        PUBLISH_DIR: ./docs/.vuepress/dist
```

* [GitHub Pages action](https://github.com/marketplace/actions/github-pages-action#getting-started)

## 정리 안된(~~안한~~) 레퍼런스

* [Try the latest stable version of npm](https://docs.npmjs.com/try-the-latest-stable-version-of-npm)

* [VuePress: Getting Started](https://vuepress.vuejs.org/guide/getting-started.html#global-installation)
* [VuePress: Deploy](https://vuepress.vuejs.org/guide/deploy.html#github-pages)

* [joshua1988님의 config.js](https://github.com/joshua1988/es6-online-book/blob/master/docs/.vuepress/config.js)
* [진유림님 TIL](https://github.com/milooy/TIL)

* [Working with SSH key passphrases](https://help.github.com/en/github/authenticating-to-github/working-with-ssh-key-passphrases)
* [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/en/enterprise/2.16/user/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)
* [Adding a new SSH key to your GitHub account](https://help.github.com/en/enterprise/2.16/user/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)
* [GitHub: SSH and GPG Keys](https://github.com/settings/keys)

* [What does cmd /C mean?](https://stackoverflow.com/questions/515309/what-does-cmd-c-mean)

* [github/peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages): GitHub Actions for GitHub Pages 🚀 Deploy static files and publish your site easily.
* [github/JamesIves/github-pages-deploy-action](https://github.com/JamesIves/github-pages-deploy-action)

## 히스토리

(2020.01.15) 최초 작성

<vue-disqus/>
