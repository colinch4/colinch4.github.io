---
layout: post
title: "[Go] Package jwt"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

# Package jwt
**J**ason **W**eb **T**oken

### Table of Contents
* [JWT Basic](#jwt-basic)
    * Token의 필요성
    * [JWT 구조](#jwt-구조)  
      [Header](#header) | [Payload](#payload) | [Signature](#signature)
    * JWT 인증
    * JWT 발급
    * JWT 사용

- [Package jwt](#package-jwt)
    - [Table of Contents](#table-of-contents)
  - [JWT Basic](#jwt-basic)
    - [JWT 구조](#jwt-구조)
      - [JWT Structure](#jwt-structure)
      - [Encoded JWT](#encoded-jwt)
      - [Decoded JWT](#decoded-jwt)
    - [Header](#header)
      - [Payload](#payload)
    - [Signature](#signature)
  - [JWT 인증](#jwt-인증)
  - [JWT 발급](#jwt-발급)
  - [JWT 사용](#jwt-사용)
  - [jwt 코드 열어보기](#jwt-코드-열어보기)
    - [MapClaims](#mapclaims)
    - [SigningMethodHMAC](#signingmethodhmac)
    - [Parser](#parser)
    - [jwt.New](#jwtnew)
    - [jwt.Parse](#jwtparse)
    - [jwt.Valid](#jwtvalid)
    - [jwt.VerifyExpiresAt](#jwtverifyexpiresat)
    - [jwt.VerifyIssuedAt](#jwtverifyissuedat)
    - [jwt.VerifyNotBefore](#jwtverifynotbefore)


## JWT Basic  
JWT 가 유용하게 사용되는 경우는 아래와 같다.
* Authentication  
  token에 유저의 정보를 담아 인증시 사용
* Information Exchanges  
  정보를 안전하게 전송하고 싶을 때  

### JWT 구조  
JWT 는 세 파트로 나뉜다.
1. Header
1. Payload
1. Signature 

중요한 정보는 header 와 payload 에 적재해서는 안된다.
* base64로 인코딩되어 있기에 간단하게 디코딩 가능하기 때문.  

반면 Signature(Header + Payload + Signature Key)은 복호화 되어 있기에 Signature Key를 모른다면 해석불가.  
* 보안성 강화 → Signaure key 를 모르기에 위변조 어려움.

#### JWT Structure
각각의 JSON 형태의 데이터를 base64로 인코딩한 후 합친다(header.payload.signature).  

<img width="400" alt="jwt-structure" src="https://user-images.githubusercontent.com/48475824/76694158-bd0a4480-66b2-11ea-9f96-3959e6936bc2.png">  


#### Encoded JWT
JSON은 개행 문자가 있다. 이는 base64로 인코딩 되면서 사라진다.  

<img width="400" alt="jwt-encoded" src="https://user-images.githubusercontent.com/48475824/76694354-f9d73b00-66b4-11ea-9bb9-0bd1e5b103ca.png">  

#### Decoded JWT
<img width="320" alt="jwt-decoded" src="https://user-images.githubusercontent.com/48475824/76694367-11aebf00-66b5-11ea-8048-b687c35837ee.png">



### Header
토큰의 타입과 사용하는 해싱 알고리즘의 정보가 담겨 있다.  
* **typ**  
  type  
  토큰의 타입
* **alg**  
  algorithm  
  해싱 알고리즘

#### Payload  
토큰으로 사용하려는 실질적인 데이터가 담겨 있다.  
한 토큰에는 여러개의 Claim들로 이루어져 있다. Claim은 데이터의 조각이라 보면 된다.  

**Claim 의 세 종류**  
1. Reserved Claim  
  예약된 클레임  
  이름이 이미 예약되어 정해진 클레임들
1. Public Claim  
  공개 클레임  
  서버-클라이언트 협의하에 사용되는 공개 클레임  
  클레임 이름 충돌 방지를 위해 URI 형식으로 이름을 명명한다.
1. Private Claim  
  비공개 클레임  
  서버-클라이언트의 협의하에 사용되는 비공개 클레임

* **aud**  
  Audience  
  토큰을 사용할 대상
* **exp**  
  Expiration Time
  토큰의 만료 기간
* **iat**  
  Issued at  
  토큰의 발급 시간
* **iss**  
  Issuer  
  토큰의 발급자  
* **jti**  
  JWT ID  
  JWT 식별을 위한 ID
* **nbf**  
  Not Before  
  해당 값 이후부터 토큰 사용 가능  
  ```nbf``` < ```current time``` < ```exp```  
* **sub**  
  Subject  
  토큰의 주제

[↑ return to TOC](#table-of-contents)

### Signature
Header + Payload + Signature Key  
토큰의 무결성과 변조를 방지하기 위해 사용되는 서명.

[↑ return to TOC](#table-of-contents)

## JWT 인증
## JWT 발급
## JWT 사용



## jwt 코드 열어보기
### MapClaims
```go
type MapClaims map[string]interface{}
```
[↑ return to TOC](#table-of-contents)


### SigningMethodHMAC
HMAC-SHA 알고리즘 구현  
* HMAC  
  **H**ash-based **M**essage **A**uthenti**c**ation
```go
type SigningMethodHMAC struct {
  Name string
  Hash crypto.Hash
}
```
지원하는 HMAC-SHA 종류는 아래와 같다.
* HS256  
  <!-- SHA-2 -->
* HS384
* HS512  

이 외의 알고리즘 종류는 에러(```signature is invalid```)를 리턴한다

[↑ return to TOC](#table-of-contents)


### Parser
```go
type Parse struct {
    ValidMethods           []string
    UseJSONNumber          bool
    SkipClaimsValidation   bool
}
```
* UseJSONNumber  
  JSON decode 시에 JSON Number 포멧을 사용할지에 관한 여부

[↑ return to TOC](#table-of-contents)


### jwt.New
새 토큰 생성시 사용.  
```method```인자에 암호화 할 알고리즘 종류를 전달해준다.
```go
func New(method SigningMethod) *Token {
  return NewWithClaims(method, MapClaims{})
}
```
* Raw : The raw token
    * Populated when you Parse a token.
* Method : 어떤 방법으로 암호화 시키는지.
* Header : 토큰의 첫번째 파트
* Claims : 토큰의 두번째 파트
* Signature : 토큰의 세번째 파트
* Valid : 유효한 토큰인지 판별 (T/F)
    * Populated when you Parse/verify a token.

[↑ return to TOC](#table-of-contents)


### jwt.Parse
```go
func Parse(tokenString string, keyFunc Keyfunc) (*Token, error) {
  return new(Parser).Parse(tokenString, keyFunc)
}
```

[↑ return to TOC](#table-of-contents)

### jwt.Valid
토큰의 유효성을 확인한다.  
클레임의 ```exp```, ```iat```, ```nbf```로 토큰의 유효기간을 판별.  
   * ```exp```, ```iat```, ```nbf``` 가 존재하지 않더라도 유효한 클레임으로 간주.
```go
func (m MapClaims) Valid() error {
  vErr := new(ValidationError)
  now := TimeFunc().Unix()

  if m.VerifyExpiresAt(now, false) == false {
     vErr.Inner = errors.New("Token is expired")
     vErr.Errors |= ValidationErrorExpired
  }

  if m.VerifyIssuedAt(now, false) == false {
     vErr.Inner = errors.New("Token used before issued")
     vErr.Errors |= ValidationErrorIssuedAt
  }

  if m.VerifyNotBefore(now, false) == false {
     vErr.Inner = errors.New("Token is not valid yet")
     vErr.Errors |= ValidationErrorNotValidYet
  }

  if vErr.valid() {
     return nil
  }

  return vErr
}
```
[↑ return to TOC](#table-of-contents)


### jwt.VerifyExpiresAt
```exp```과 ```cmp``` 의 비교를 통해 유효기간을 판별.  
```go
func (m MapClaims) VerifyExpiresAt(cmp int64, req bool) bool {
  switch exp := m["exp"].(type) {
  case float64:
     return verifyExp(int64(exp), cmp, req)
  case json.Number:
     v, _ := exp.Int64()
     return verifyExp(v, cmp, req)
  }
  return req == false
}
```
[↑ return to TOC](#table-of-contents)


### jwt.VerifyIssuedAt
```iat```와 ```cmp``` 의 비교를 통해 유효기간을 판별. 와
```go
func (m MapClaims) VerifyIssuedAt(cmp int64, req bool) bool {
  switch iat := m["iat"].(type) {
  case float64:
     return verifyIat(int64(iat), cmp, req)
  case json.Number:
     v, _ := iat.Int64()
     return verifyIat(v, cmp, req)
  }
  return req == false
}
```
[↑ return to TOC](#table-of-contents)


### jwt.VerifyNotBefore
```nbf```와 ```cmp``` 의 비교를 통해 유효기간을 판별. 
```go
func (m MapClaims) VerifyNotBefore(cmp int64, req bool) bool {
  switch nbf := m["nbf"].(type) {
  case float64:
     return verifyNbf(int64(nbf), cmp, req)
  case json.Number:
     v, _ := nbf.Int64()
     return verifyNbf(v, cmp, req)
  }
  return req == false
}
```

[↑ return to TOC](#table-of-contents)
