---
layout: post
title: "Package.json 설정을 활용한 JavaScript 프로젝트의 소셜 로그인 설정"
description: " "
date: 2023-11-06
tags: [package]
comments: true
share: true
---

이번 블로그 포스트에서는 JavaScript 프로젝트에서 소셜 로그인을 설정하는 방법에 대해 알아보겠습니다. 소셜 로그인은 사용자가 다른 웹 애플리케이션에서 기존의 소셜 미디어 계정을 사용하여 로그인할 수 있도록 하는 기능입니다. 우리는 이를 위해 `package.json` 파일을 활용할 것입니다.

## Step 1: 필수 모듈 설치하기

먼저, 소셜 로그인을 구현하기 위해 필요한 모듈들을 설치해야 합니다. `package.json` 파일에서 `dependencies` 항목 아래에 아래와 같이 모듈들을 추가해주세요.

```
"dependencies": {
  "express": "^4.17.1",
  "passport": "^0.4.1",
  "passport-google-oauth20": "^2.0.0",
  "passport-facebook": "^3.0.0",
  // 다른 소셜 로그인에 필요한 모듈들도 추가해주세요
}
```

위의 예시에서는 Express, Passport, Google OAuth 2.0, Facebook 소셜 로그인 모듈을 설치하였습니다. 필요한 다른 소셜 로그인 모듈들도 동일한 방식으로 설치해주세요. 설치를 위해 터미널에서 `npm install` 명령어를 실행해주시면 됩니다.

## Step 2: 소셜 로그인 설정

이제, `passport` 모듈을 사용하여 소셜 로그인을 설정해보겠습니다. 먼저, `app.js` 파일에 다음 코드를 추가하세요.

```javascript
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;
const FacebookStrategy = require('passport-facebook').Strategy;

// Google 로그인 설정
passport.use(new GoogleStrategy({
    clientID: GOOGLE_CLIENT_ID,
    clientSecret: GOOGLE_CLIENT_SECRET,
    callbackURL: "/auth/google/callback"
  },
  function(accessToken, refreshToken, profile, cb) {
    // 로그인 성공 시 실행될 콜백 함수
    // 사용자 정보를 처리하는 로직을 구현해주세요
  }
));

// Facebook 로그인 설정
passport.use(new FacebookStrategy({
    clientID: FACEBOOK_APP_ID,
    clientSecret: FACEBOOK_APP_SECRET,
    callbackURL: "/auth/facebook/callback"
  },
  function(accessToken, refreshToken, profile, cb) {
    // 로그인 성공 시 실행될 콜백 함수
    // 사용자 정보를 처리하는 로직을 구현해주세요
  }
));

app.use(passport.initialize());
app.use(passport.session());

// 로그인 라우트 설정
app.get('/auth/google', passport.authenticate('google', { scope: ['profile'] }));
app.get('/auth/google/callback', passport.authenticate('google', { failureRedirect: '/login' }), (req, res) => {
  // 로그인 성공 시 리다이렉트할 경로를 설정해주세요
  res.redirect('/home');
});

app.get('/auth/facebook', passport.authenticate('facebook'));
app.get('/auth/facebook/callback', passport.authenticate('facebook', { failureRedirect: '/login' }), (req, res) => {
  // 로그인 성공 시 리다이렉트할 경로를 설정해주세요
  res.redirect('/home');
});
```

위의 코드에서 `clientID`, `clientSecret`, `callbackURL` 등은 각각 구글 및 페이스북 개발자 포털에서 발급받은 값을 입력해주셔야 합니다.

## Step 3: 서버 실행

이제, `package.json` 파일이 있는 디렉토리에서 터미널을 열고 다음 명령어를 실행하여 서버를 실행해주세요.

```
$ npm start
```

서버가 성공적으로 실행되면, `http://localhost:3000/auth/google` 또는 `http://localhost:3000/auth/facebook`으로 접속하여 소셜 로그인을 테스트해볼 수 있습니다.

## 정리

이번 포스트에서는 `package.json` 파일을 활용하여 JavaScript 프로젝트에서 소셜 로그인을 설정하는 방법에 대해 알아보았습니다. `passport` 모듈을 사용하여 Google과 Facebook 소셜 로그인을 구현하는 예시를 다루었습니다.

**참고 자료:**
- [Passport.js 공식 문서](http://www.passportjs.org/)
- [Google OAuth 2.0 공식 문서](https://developers.google.com/identity/protocols/oauth2)
- [Facebook 로그인 개발자 문서](https://developers.facebook.com/docs/facebook-login)