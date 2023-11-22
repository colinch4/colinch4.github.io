---
layout: post
title: "[VSCode] VSCode로 Sass 컴파일하기"
description: " "
date: 2021-09-09
tags: [ide]
comments: true
share: true
---



## VSCode로 Sass 컴파일하기

Sass를 컴파일하기 위해 프롬프트에 직접 명령을 입력하는 방법, 기타 확장 프로그램을 사용하는 방법이 있다. VSCode의 확장 프로그램을 이용하면 버튼 한번으로 Sass파일의 변경을 지켜볼 수 있으니 훨씬 편한 작업 환경을 구축할 수 있다. 내가 사용하는 VScode의 [Live Sass Compiler](https://marketplace.visualstudio.com/items?itemName=ritwickdey.live-sass)를 사용한 컴파일 방법과 설정을 정리한다.

## Live Sass Compiler 설치

VSCode의 Extensions 탭에서 Live Sass Compiler 를 검색해 install로 설치해준다

설치시 기본으로 현재 워크스페이스에 열린 모든 폴더의 Sass 파일을 컴파일 한다. 불필요하게 컴파일되지 않도록 필요한 폴더만 지정해주거나 일부 폴더를 제외시킬 수 있다.

## Live Sass Compiler 설정

VSCode에 설치한 확장 프로그램들에 대한 설정은 **`preference > setting`** 의 **Extensions** 탭에서 가능하다. 또한 settings.json 파일에서 코드로 수정 할 수 있다.

확장에서 설정 가능한 사항은 아래와 같다

* **`liveSassCompile.settings.formats`**: CSS 포맷과 CSS 파일 유형, 컴파일 된 CSS파일이 저장될 위치를 설정할 수 있다.

  * CSS 포맷

    * expanded
    * compact
    * compressed
    * nested

  * CSS 파일의 유형

    * `.css` 
    * `.min.css`

  * 컴파일 된 CSS 파일이 저장될 위치

    * `null` : scss/sass 파일이 위치한 폴더에 CSS를 생성한다 

    * `/`: 제일 상위(root)에서부터 디렉토리를 지정한다

    * `~`:파일이 위치한 곳을 기준으로 디렉토리를 지정한다 

   ```json
   "liveSassCompile.settings.formats":[
     // This is Default.
     {
     "format": "expanded",
     "extensionName": ".css",
     "savePath": null
     },
     // You can add more
     {
     "format": "compressed",
     "extensionName": ".min.css",
     "savePath": "/dist/css"
     },
     // More Complex
     {
     "format": "compressed",
     "extensionName": ".min.css",
     "savePath": "~/../css/"
     }
   ]
   ```

* **`liveSassCompile.settings.excludeList`**: 컴파일 하지 않을 특정 폴더들을 지정해 제외한다.

  * 기본 설정:

    ```json
    "liveSassCompile.settings.excludeList": [ 
      "**/node_modules/**",
      ".vscode/**" 
    ]
    ```

  * 특정 폴더를 컴파일 하지 않지만 그 중`file1.scss` 와 `file2.scss` 만 컴파일 하고 싶을 경우에 아래와 같이 설정할 수 있다.

    ```json
    "liveSassCompile.settings.excludeList": [
      "path/subpath/*[!(file1|file2)].scss"
    ]
    ```

* **`liveSassCompile.settings.includeItems`**: 이 설정은 전체 프로젝트에서 일부 scss/sass파일만 수정하면 될 경우 유용하게 사용할 수 있다. 설정해준 파일만 컴파일한다.

  ```json
  "liveSassCompile.settings.includeItems": [
    "path/subpath/a.scss",
    "path/subpath/b.scss",
  ]
  ```
	하나의 워크스페이스에 서비스별 scss파일을 따로 만들어 관리하기 때문에 작업이 필요한 디렉토리를 인클루드 아이템에 추가해 작업하는 방법을 가장 자주 사용한다.
  
* **`liveSassCompile.settings.generateMap`**: 디버깅에 필요한  `.map` 파일이 필요하지 않dA다면, `false` 로 설정한다.

더 자세한 사항과 변동 사항은 [Setting](https://github.com/ritwickdey/vscode-live-sass-compiler/blob/master/docs/settings.md) 문서에서 확인 가능하다.



### Live Sass Compiler 사용하기

VSCode 실행 후 우측 하단의 *Watch Sass* 버튼을 누르면 *Watching…* 상태로 변경된다. scss/sass파일의 변화를 감지할 때마다 자동으로 컴파일 해 CSS파일을 갱신해준다.