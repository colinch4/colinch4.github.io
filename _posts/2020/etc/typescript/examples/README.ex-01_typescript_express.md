---
layout: post
title: "[Typescript] 3. Backend Sample 프로젝트"
description: " "
date: 2020-12-03
tags: [typescript]
comments: true
share: true
---



- express와 typescript로 웹서버 애플리케이션 예제
- 개발 환경 구성, 운영 환경 구성
- `Hello` 예제로 개발 환경을 구성하면서 단계별로 메모해본다.

## 개요

- 라이브러리 및 설정은 다음을 사용한다.
  - typescript 4
  - express 4
  - Mongoose 5.7
  - eslint without tslint
  - Absolute module resolver
  - ts-node-dev
  - cross-env, dotenv

- 프로젝트는 다중 프로젝트를 기반
  - hello-api
  - hello-web
- 개발 IDE는 vscode

## 개발 환경 구성

- 루트 프로젝트 및 api 프로젝트 생성

```sh
mkdir hello
cd hello
npm init -y

mkdir api
cd api
npm init -y
```

- vscode에서 루트 프로젝트를 연다.
- api 프로젝트로 이동하여 타입스크립트 등의 기본 라이브러리 설치

```sh
cd api
api> yarn add -D @types/node typescript ts-node

info Direct dependencies
├─ @types/node@14.11.2
├─ ts-node@9.0.0
└─ typescript@4.0.3
info All dependencies
├─ @types/node@14.11.2
├─ arg@4.1.3
├─ buffer-from@1.1.1
├─ diff@4.0.2
├─ make-error@1.3.6
├─ source-map-support@0.5.19
├─ source-map@0.6.1
├─ ts-node@9.0.0
├─ typescript@4.0.3
└─ yn@3.1.1
Done in 1.82s.
```

- `tsconfig.json` 설정
- `npx tsconfig.json`를 실행하면 tsconfig.json이 다운로드 된다.
  - 옵션에 React,node 등이 있는데 node를 선택

```sh
api> npx tsconfig.json
```

- 소스 폴더를 만들고 `index.ts` 생성

```sh
api> mkdir src
api> echo "console.log('hello world')" > src/index.ts
```

- package.json에 dev 스크립트 추가하고
  - 참고로 ts-node는 타입스크립트를 실행하는 프로그램인데, 운영환경에서는 사용하면 안된다. 운영환경에서는 js를 실행해야 한다.

```json
"scripts": {
    "dev": "ts-node src/index.ts"
}
```

- 실행해 본다.

```sh
api> yarn dev

hello world
```

### 환경설정

- 기본적인 동작은 확인했고, 이제 express와 mongoose를 설치 한다.

```sh
api> yarn add express mongoose
api> yarn add -D @types/express @types/mongoose
```

- express 웹서버의 포트, 몽구스 서버 URL 등의 환경설정이 필요하다.
- 향후 다른 설정들이 추가될 수 있으므로 폴더 형태로 만든다.

```sh
api> mkdir src/config
api> cd src/config
api> touch {index,app,db}.ts
api> echo "export * from './app'" > index.ts
api> echo "export * from './db'" >> index.ts
```

- `app.ts`는 다음과 같이 작성

```ts
export const {
    NODE_ENV = 'development',
    APP_PORT = 3000,
    APP_HOSTNAME = 'localhost',
    APP_PROTOCOL = 'http',
} = process.env

export const IN_PROD = NODE_ENV === 'production'
```

- `db.ts`는 다음과 같이 작성

```ts
const {
    MONGO_USERNAME = 'sample',
    MONGO_PASSWORD = '1234',
    MONGO_HOST = 'localhost',
    MONGO_PORT = 27017,
    MONGO_DATABASE = 'sample',
} = process.env

export const MONGO_URI = `mongodb://${MONGO_USERNAME}:${encodeURIComponent(
    MONGO_PASSWORD,
)}@${MONGO_HOST}:${MONGO_PORT}/${MONGO_DATABASE}`

export const MONGO_OPTIONS = {
    useNewUrlParser: true,
    useUnifiedTopology: true,
}
```

### 라우팅 추가

- express에서 라우팅 경로를 추가한다. express의 라우팅이란 url과 핸들러 함수를 매핑해 놓는 개념이다.
- 한 파일에 모든 핸들러 함수를 작성하는 것보다 비슷한 기능을 하는 핸들러 함수들을 그룹핑하여 관리하는 것이 좋다.
- `src/routes` 폴더를 만들고 `home.ts`와 `index.ts`를 추가한다.


```sh
api> mkdir src/routes
api> cd src/routes
api> touch {index,home}.ts
api> echo "export * from './home'" > index.ts
```

- `home.ts` 파일을 다음과 같이 작성한다.

```ts
import { Router } from 'express'

const router = Router()
router.post('/home', (req, res) => {
    res.json({ message: 'Welcome home!!' })
})

export { router as home }
```

- 이제 웹서버를 시작하는 코드를 작성한다.
- 웹서버는 express 객체인데, 기본적인 설정과 라우트 설정을 먼저 해야 한다.
- `src/app.ts`에 `createApp()`를 만들고, 거기에 웹서버를 설정하는 로직을 작성한다. 지금은 간단하지만, 라우트를 추가하다보면 꽤 길어지므로 이렇게 별도의 함수로 작성하는 것이 좋다.

```ts
import express, { Express } from 'express'
import { home } from './routes'

export const createApp = (): Express => {
    const app = express()
    app.use(express.json())
    app.use(express.urlencoded())
    app.use(home)
    return app
}
```

- `src/index.ts`에서 웹서버를 시작한다.
  - 웹서버를 시작할때 몽구스 연결도 해야 하므로 async로 작성한다.
  - 일단은 몽구스를 연결안해도 되니까 몽구스 연결 로직은 제외한다.

```ts
import { createApp } from './app'
import { APP_HOSTNAME, APP_PORT, MONGO_OPTIONS, MONGO_URI } from './config'

;(async () => {
    const app = createApp()
    app.listen(APP_PORT, () => console.log(`http://${APP_HOSTNAME}:${APP_PORT}`))
})()
```

### 중간 확인

- 이제 작성한 코드를 실행한다.

```sh
api> yarn dev
```

- 지금까지의 과정을 그대로 따라했다면, 아마 home.ts에 사용하지 않는 변수가 있다는 에러가 발생할 것이다.
- 이것은 eslint 에러가 아닌, 컴파일 에러이다. 타입스크립트의 컴파일 옵션은 `tsconfig.json`에서 설정한다. 사용하지 않는 변수는 warning만 하는 것이 좋으므로 컴파일 옵션을 변경하자. 그리고 eslint도 변경해야 한다.

### 컴파일러 설정 변경

- `tsconfig.json`의 컴파일러 옵션에서 아래 부분을 false로 변경한다.

```json
// ...
"compilerOptions":{
    //...
    "noUnusedLocals": false,
    "noUnusedParameters": false,
}
```

- 다시 실행해보면 잘 동작할 것이다.

```sh
api> yarn dev
```

### eslint 설정

- 타입스크립트 프로젝트라서 tslint를 사용해야 할 것 같은데, tslint 개발팀에서 eslint를 사용하도록 권고하고 있다. eslint에 tslint 플러그인을 설치하는 방식으로 동작한다. tslint는 더 이상 지원하지 않는다.
- eslint 라이브러리와 플러그인들을 설치한다.

```sh
api> yarn add -D eslint eslint-import-resolver-typescript
```

- 아래 명령으로 eslint 설정파일을 만든다.
  - `To check syntax and find problems`,`JavaScript module`,`Typescript`,`Node`,`JSON` 옵션을 선택한다.
  - `@typescript-eslint/eslint-plugin @typescript-eslint/parser`을 설치하겠냐고 물어보연 YES

```sh
api> ./node_modules/.bin/eslint --init

## .eslintrc.json 파일이 생성되었다
api> cat .eslintrc.json
```

- `.eslintrc.json` 파일에 사용하지 않는 변수는 경고만 하도록 설정한다.
  - `"no-unused-vars"`
- `.eslintrc.json` 파일에 non-null 단정을 허용하도록 설정한다.
  - `"@typescript-eslint/no-non-null-assertion"`
  - 이 옵션은 `app.session`에서 `session`이 nullable 할때, 느낌표를 붙여서 `app.session!.userId` 형식으로 사용하는 것을 허용하는 설정이다.

```json
"rules":{
    // ...
    "no-unused-vars": "warn",
    "@typescript-eslint/no-non-null-assertion": "off",
}
```

### ts-node-dev 설치

- nodemon 같은 것이다. 소스코드가 변경되면 자동으로 서버를 재시작하는 기능을 한다. 개발중에 유용하다.

- 자세한 내용은 github 문서를 참고하고
- [ts-node-dev github](https://github.com/whitecolor/ts-node-dev)

>It restarts target node process when any of required files changes (as standard node-dev) but shares Typescript compilation process between restarts. This significantly increases speed of restarting comparing to node-dev -r ts-node/register ..., nodemon -x ts-node ... variations because there is no need to instantiate ts-node compilation each time.

- `ts-node-dev`를 설치한다.

```sh
api> yarn add -D ts-node-dev
```

- `package.json`에 `dev` 스크립트를 변경한다.

```json
"scripts":{
  "dev": "ts-node-dev --respawn --transpile-only --no-notify src/index.ts"
}
```

- 이제 `yarn dev` 이후에 코드를 변경하면 자동으로 재시작 된다.

### 절대경로 모듈 리졸버 설치

- 개발을 하다 보면 모듈의 임포트 문이 상대경로라서 복잡한 경우가 많다.

- 원래는 이렇게 하는데 `import {home} from './routes'`
- 이렇게 하고 싶다. `import {home} from '@@/routes'`
- 두 가지 부분을 변경해야 한다. 타입스크립트 컴파일러가 컴파일 할 수 있어야 하고, 컴파일이 된 js 파일에도 여전히 `@@/route` 임포트 문장이 존재하므로 실행시점에도 이를 해석할 수 있어야 한다.
- 이러한 문제를 처음에는 babel로 해결했으나 babel이 필요없는 프로젝트에서 모듈 리졸버를 위해 babel을 사용하는 것이 적절하지 않은 것 같았다.
- 검색해보니 비슷한 질문이 있어서 이 문서를 보고 작성하였다. [Absolute import paths cannot be used in production](https://github.com/nestjs/typescript-starter/issues/74)

```sh
api> yarn add tsconfig-paths

info Direct dependencies
└─ tsconfig-paths@3.9.0
```

- `tsconfig.json` 파일에 다음과 같이 등록한다.

```json
"compilerOptions": {
    "baseUrl": ".",
    "outDir": "./dist",
    "paths": {
        "@@/*": ["src/*"]
    },
```

- ts-node로 타입스크립트를 실행할 때 tsconfig-paths 모듈을 미리 로드한다. `package.json`의 `dev` 스크립트를 변경한다. `-r` 옵션은 모듈을 미리 로드하는 옵션이다.

```json
"scripts":{
  "dev": "ts-node-dev -r tsconfig-paths/register --respawn --transpile-only --no-notify src/index.ts"
}
```

- 테스트를 위해 `app.ts` 파일에 route를 임포트 하는 문장을 다음과 같이 `@@`이 포함되도록 수정한다.

```ts
import { home } from '@@/routes'
```

- 동작을 테스트해보면 `@@`가 포함된 임포트 문장도 잘 동작하는 것을 확인할 수 있다.

```sh
api> yarn dev
```

```sh
curl localhost:3000/home

{"message":"Welcome home!!"}
```

- 위의 동작은 `ts-node src/index.ts`로 서버를 실행한 것이다. 운영환경에서는 `node dist/index.js`로 서버를 실행한다. 따라서 운영환경의 런타임에 `@@` 모듈 경로를 해결할 수 있어야 한다.

- `@@`는 개발환경에서는 `src`, 운영환경에서는 `dist`이다. 즉, 운영환경에서 `@@`를 `src`가 아닌 `dist`로 인식하면 된다. 이를 위해 `module-alias` 라이브러리를 설치한다.

```sh
api> yarn add module-alias

module-alias ^2.2.2
```

- 소스코드에 `aliases.ts` 파일을 다음과 같이 작성한다.

```ts
import moduleAlias from 'module-alias'
import path from 'path'

const rootPath = path.resolve(__dirname, '..', 'dist')
moduleAlias.addAliases({
    '@@': rootPath,
})
```

- 위의 `aliases.ts`는 제일 처음에 로드되어야 한다. 그래서 `index.ts`의 첫줄에 다음과 같이 임포트 한다.

```ts
// index.ts
import './aliases'
```

- 이제 `package.json` 파일의 `scripts`를 다음과 같이 작성한다.

```json
"scripts": {
    "prebuild": "rm -rf dist",
    "build": "tsc",
    "dev": "ts-node-dev -r tsconfig-paths/register --respawn --transpile-only --no-notify src/index.ts",
    "start": "cross-env NODE_ENV=production node dist/index.js"
},
```

- 여기까지 몽구스를 제외한 백엔드 설정을 마쳤다. 이제 환경변수를 개발과 운영환경에 적절하게 분리한다.

### 환경변수 설정

- 환경변수 설정을 위해 `dotenv` 모듈을 사용한다. 윈도우에서도 설정할 수 있도록 `cross-env` 모듈도 사용한다.

```sh
api> yarn add dotenv cross-env
api> yarn add -D @types/dotenv
```

- `dotenv`가 자동으로 설정을 로드하는 방식은 햇갈리니까 로드할 설정파일을 코드에서 선택하는 방식으로 한다.
- `api/.env.prod` 파일을 만든다.

```ini
APP_PORT=4000
```

- `api/.env.dev` 파일을 만든다.

```ini
APP_PORT=3000
```

- `api/src/loadenv.ts` 파일을 다음과 같이 작성한다.

```ts
import dotenv from 'dotenv'
import path from 'path'
const { NODE_ENV } = process.env

if (NODE_ENV === 'production') {
    dotenv.config({ path: path.resolve(__dirname, '..', '.env.prod') })
} else {
    dotenv.config({ path: path.resolve(__dirname, '..', '.env.dev') })
}
```

- `api/src/index.ts`의 첫번째 줄에 `loadenv.ts`를 임포트하면 된다.

```ts
import './aliases'
import './loadenv'
```

- 위의 과정을 따라했다면, `yarn dev`를 실행했을때 3000번 포트로 웹서버가 실행될 것이다.

### 지금까지의 상태

- `package.json` 파일은 다음과 같다.

```json
{
    "name": "api",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "prebuild": "rm -rf dist",
        "build": "tsc",
        "start": "yarn build && cross-env NODE_ENV=production node dist/index.js",
        "dev": "ts-node-dev -r tsconfig-paths/register --respawn --transpile-only --no-notify src/index.ts"
    },
    "keywords": [],
    "author": "",
    "license": "ISC",
    "dependencies": {
        "cross-env": "^7.0.2",
        "express": "^4.17.1",
        "module-alias": "^2.2.2",
        "mongoose": "^5.10.7",
        "tsconfig-paths": "^3.9.0"
    },
    "devDependencies": {
        "@types/express": "^4.17.8",
        "@types/module-alias": "^2.0.0",
        "@types/mongoose": "^5.7.36",
        "@types/node": "^14.11.2",
        "@typescript-eslint/eslint-plugin": "^4.3.0",
        "@typescript-eslint/parser": "^4.3.0",
        "eslint": "^7.10.0",
        "eslint-import-resolver-typescript": "^2.3.0",
        "ts-node": "^9.0.0",
        "ts-node-dev": "^1.0.0-pre.63",
        "typescript": "^4.0.3"
    }
}
```

- `tsconfig.json` 파일은 다음과 같다.

```json
{
    "compilerOptions": {
        "target": "esnext",
        "module": "commonjs",
        "lib": ["dom", "es6", "es2017", "esnext.asynciterable"],
        "sourceMap": true,
        "baseUrl": "./",
        "outDir": "./dist",
        "paths": {
            "@@/*": ["src/*"]
        },
        "moduleResolution": "node",
        "removeComments": true,
        "noImplicitAny": false,
        "strictNullChecks": true,
        "strictFunctionTypes": true,
        "noImplicitThis": true,
        "noUnusedLocals": false,
        "noUnusedParameters": false,
        "noImplicitReturns": true,
        "noFallthroughCasesInSwitch": true,
        "allowSyntheticDefaultImports": true,
        "esModuleInterop": true,
        "emitDecoratorMetadata": true,
        "experimentalDecorators": true,
        "resolveJsonModule": true
    },
    "exclude": ["node_modules", "dist"],
    "include": ["./src/**/*.tsx", "./src/**/*.ts"]
}
```

- `.eslint.json` 파일은 다음과 같다.

```json
{
    "root": true,
    "env": {
        "browser": true,
        "es2021": true
    },
    "extends": ["eslint:recommended", "plugin:@typescript-eslint/recommended"],
    "parser": "@typescript-eslint/parser",
    "parserOptions": {
        "ecmaVersion": 12,
        "sourceType": "module"
    },
    "plugins": ["@typescript-eslint", "import"],
    "rules": {
        "no-unused-vars": "warn",
        "@typescript-eslint/no-non-null-assertion": "off"
    }
}
```

### 몽구스 설정

- express 웹서버가 시작하기 전에 MongoDB에 연결해야 한다.
- 처음에 `config/db.ts`에서 MongoDB 설정을 했으므로, 몽구스를 이용해 MongoDB에 연결하는 로직만 추가하면 된다.(한줄이다)

- `src/index.ts`를 다음과 같이 작성한다.

```ts
import { createApp } from './app'
import { APP_HOSTNAME, APP_PORT, MONGO_OPTIONS, MONGO_URI } from './config'

;(async () => {
    await mongoose.connect(MONGO_URI, MONGO_OPTIONS)
    const app = createApp()
    app.listen(APP_PORT, () => console.log(`http://${APP_HOSTNAME}:${APP_PORT}`))
})()
```

### 몽고 DB 설치

- 몽고 DB를 설치하는 과정은 도커를 사용한다.

### 몽구스 모델 및 스키마 작성

- 몽구스 모델은 `src/models` 폴더에 작성할 것이다.
- 여기서는 User라는 몽구스 collection을 만들 것이다.

```sh
api> mkdir -p src/models
api> cd src/models
api> touch {index,user}.ts
api> echo "export * from './user'" > index.ts
```

- 다음과 같이 `src/models/user.ts`를 작성한다.

```ts
import { Schema, model, Document } from 'mongoose'

interface UserDocument extends Document {
    email: string
    name: string
}

const userSchema = new Schema(
    {
        email: String,
        name: String,
    },
    {
        timestamps: true,
    },
)

export const User = model<UserDocument>('User', userSchema)
```

- `localhost:3000/register` POST 요청을 받아서 사용자를 추가하는 로직을 작성해보자.
- `src/routes/user.ts`를 다음과 같이 작성한다.

```ts
import { Request, Response, Router } from 'express'
import { User } from '@@/models'

const router = Router()
router.post('/register', async (req: Request, res: Response) => {
    const { email, name } = req.body
    const user = await User.create({
        email,
        name,
    })
    console.log('user created', user)
    res.json({ message: 'OK' })
})

export { router as user }
```

- `src/routes/index.ts`에 `export * from './user'` 문장을 추가한다.

```ts
export * from './home'
export * from './user'
```

- `src/app.ts`에 `user` 라우터를 추가한다.

```ts
import express, { Express } from 'express'
import { home, user } from '@@/routes'

export const createApp = (): Express => {
    const app = express()
    app.use(express.json())
    app.use(express.urlencoded())
    app.use(home)
    app.use(user)
    return app
}
```
