---
layout: post
title: "[Echo] Echo-Middleware"
description: " "
date: 2021-11-19
tags: [Echo]
comments: true
share: true
---


# Echo-Middleware
> Reference : [Echo Doc](https://echo.labstack.com/)

각 Middleware 의 세부적인 내용은 개별의 포스팅에서 다룰 것이다.  

### Table of Contents

- [Echo-Middleware](#echo-middleware)
    - [Table of Contents](#table-of-contents)
  - [3 Levels](#3-levels)
    - [Group Level](#group-level)
    - [Root Level](#root-level)
      - [Before Router](#before-router)
      - [After Router](#after-router)
    - [Route Level](#route-level)
  - [Skipping Middleware](#skipping-middleware)

## 3 Levels

에코에서 제공하는 미들웨어를 세 가지 레벨로 나눌 수 있다.

1. Group Level
1. Root Level
1. Route Level

### Group Level
새 그룹을 생성하여 특정 그룹에게만 middleware 가 적용되게 설정.
```go
e := echo.New()
admin = e.Group("/admin", middleware.BasicAuth())
```

[↑ return to TOC](#table-of-contents)

### Root Level
Root 레벨은 Router 가 '실행되기 이전'과 '실행된 후' 라는 두 그룹으로 나뉜다.

* Before Router
* After Router

#### Before Router
이 레벨에서 미들웨어를 등록할 시에는 ```Pre()``` 함수를 사용한다.  

```go
// E.g.
import "github.com/labstack/echo/middleware"

e := echo.New()
e.Pre(middleware.HTTPSRedirect())
```

* **HTTPSRedirect**   
  http 요청을 https 로 리다이렉트  

  ```http://github.com/8luebottle```  
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ Redirect ↓ ↓ ↓ ↓ ↓ ↓ ↓  
  ```https://github.com/8luebottle```  

  ```go
  // E.g.
  e := echo.New()
  e.Pre(middleware.HTTPSRedirect())
  ```

* **HTTPSWWWRedirect**   
  http 요청을 www https 로 리다이렉트.  

  ```http://github.com/8luebottle```  
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ Redirect ↓ ↓ ↓ ↓ ↓ ↓ ↓  
  ```https://www.github.com/8luebottle```  

  ```go
  // E.g.
  e := echo.New()
  e.Pre(middleware.HTTPSWWWRedirect())
  ```

* **WWWRedirect**   
  받은 요청을 http www 로 리다이렉트.

  ```http://github.com/8luebottle```  
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ Redirect ↓ ↓ ↓ ↓ ↓ ↓ ↓  
  ```http://www.github.com/8luebottle```  

  ```go
  // E.g.
  e := echo.New()
  e.Pre(middleware.WWWRedirect())
  ```

* **NonWWWRedirect**   
  받은 요청을 https 로 리다이렉트. (w/o www)

  ```http://www.github.com/8luebottle```  
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ Redirect ↓ ↓ ↓ ↓ ↓ ↓ ↓  
  ```https://github.com/8luebottle```  

  ```go
  // E.g.
  e := echo.New()
  e.Pre(middleware.NonWWWRedirect())
  ```

* AddTrailingRedirect
* AddTrailingSlash
* RemoveTrailingSlash
* MethodOverride
* Rewrite


[↑ return to TOC](#table-of-contents)

#### After Router  
이 레벨에서 미들웨어를 등록할 시에는 대부분의 경우 ```Use()``` 함수를 사용한다.  
이곳에서 등록된 미들웨어는 라우터 이후(after)에 실행되게 된다.

```go
// E.g.
import "github.com/labstack/echo/middleware"

e := echo.New()
e.Use(middleware.Logger())
e.Use(middleware.Recover())
```

이 레벨단의 내장되어 있는 미들웨어는 아래와 같다.

* BodyLimit
* Logger
* GZip
* Recover
* BasicAuth
* JWTAuth
* Secure
* CORS
* Static

[↑ return to TOC](#table-of-contents)

### Route Level  
새 Route 를 정의함을 통해 미들웨어를 특정 핸들러에게만 적용시킬 수 있다.

```go
e := echo.New()
e.GET("/", <HandlerA>, <MiddlewareB>)
```
* ```HandlerA``` 에게만 ```MiddlewareB``` 적용시키기

[↑ return to TOC](#table-of-contents)


## Skipping Middleware
특정 조건에 해당될 때 미들웨어를 사용하지 않고 스킵하도록 설정 할 수 있다.

* 스킵시에는 ```Skipper``` 함수를 사용.
  ```go	
  Skipper func(echo.Context) bool
  ```
  Default 값은 false 로 설정되어 있다.
  true 일 시 Processing 되고 있는 미들웨어를 skip.

```go
// E.g.
e := echo.New()
e.User(middleware.LoggerWithConfig(middleware.LoggerConfig{
    Skipper: func(c echo.Context) bool {
        if strings.HasPrefix(c.Request().Host, “localhost”){
            return true
        }
        return false
    },
}))
```

[↑ return to TOC](#table-of-contents)
