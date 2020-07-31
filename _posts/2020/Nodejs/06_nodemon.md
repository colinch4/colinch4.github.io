## nodemon

- nodemon은 웹개발 편의성을 높이기 위한 스크립트 모니터링 유틸리티이다
- nodemon은 프로젝트 폴더의 모든 파일을 모니터링하다가, 하나라도 **수정이 될 경우** 이를 반영하여 **자동으로 서버를 재시작**한다.

## 설치 & 사용법

- 설치

> `$ npm install -g nodemon`

- 사용법

> `nodemon [file.js]`



## 구체적인 설정

- nodemon은 working directory에 nodemo.json파일을 추가하거나, package.json파일에 설정을 통합할 수 있다
- package.json파일에 설정할 경우 아래와 같이 nodemonConfig키를 추가해 설정할 수 있다

> ```json
> {
>   "name": "nodemon",
>   "homepage": "http://nodemon.io",
>   "...": "... other standard package.json values",
>   "nodemonConfig": {
>     "ignore": ["test/*", "docs/*"],
>     "delay": "2500"
>   }
> }
> ```



