---
layout: post
title: "[Go] Package http"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

## Package http
```net/http``` 패키지를 통해 HTTP 서버를 구현할 수 있다.

### Table of Contents
* [HTTP Basic](#http-basic)  
  * HTTP
  * HTTP 용어 분석
  * Server 와 Client

* http 코드 열어보기
  * [ResponseWriter](#responsewriter)
  * [timeoutWriter](#timeoutwriter)
  * [Handler](#handler)
  * [Flusher](#flusher)
  * [Hijacker](#Hijacker)
  * [http.flush](#httpflush)
  * [conn struct](#conn-struct)
  * [http.ServeHTTP](#httpservehttp)
  * [http.RedirectHandler](#httpredirecthandler)
  * [http.handler](#httphandler)
  * [http.hanldfunc](#httphandlefunc)
  * [http.listenandserve](#httplistenandserve)
  * [http.servehttp](#httpservehttp)


## HTTP Basic
> HTTP 에 대해 더 자세히 알고자 한다면 [HTTP에 대한 블로그 글](https://babytiger.netlify.com/posts/http/) 을 참고하자.

**HTTP :** **H**yper**T**ext **T**ransfer **P**rotocol  
현재 전세계 대부분의 클라이언트와 서버는 HTTP 를 통해 통신한다.  
HTTP는 HyperText들의 문서들을 주고 받는데 사용되는 프로토콜이다.
   * HTTP가 처음 만들어 졌을 때는 HTML만을 전송하고자 하였으나 시간이 흐르면서 다른 모든 종류의 리소스들을 전송할 수 있게 되었다.

**HTTP 용어 분석**  
HyperText → 하이퍼텍스트를 기반으로  
   * HyperText는 한 문서가 또 다른 문서와 연결되어 있는 것을 말한다.

Transfer  → 데이터를 전송하는

Protocol  → 통신 규약
   * protocol은 컴퓨터와 컴퓨터가 정보를 주고 받을때 어떻게 소통할것인지에 대한 규칙과 약속을 뜻한다.

**Server 와 Client**  
![Client & Server](https://babytiger.netlify.com/media/https-req-res.png)
* Client는 서비스를 요청하고 Server는 서비스를 제공해준다.  
* Server는 Client의 요청을 기다리고 있다가 요청이 들어오게 되면 Connection을 맺을지 말지를 결정한다. 
* 원치 않는 경우에는 연결을 끊어버리지만 그렇지 않을 경우에는 클라이언트의 접속을 받아들인다. 
* 요청을 받은 후에는 client에서 보낸 HTTP 요청 메세지를 읽게된다. 서버는 메세지에 적힌 리소스에 접근한다. 

[Return to TOC](#table-of-contents)

## http 코드 열어보기
### ResponseWriter
HTTP 응답을 위한 인터페이스, response 를 구성해준다.
```go
type ResponseWriter interface {
  Header() Header
  Write([]byte) (int, error)
  WriteHeader(statusCode int)
}
```
* ```Header``` 는 ```WriteHeader```로 부터 받은 header map을 리턴한다.  
    ```go
    w.Header().Set("Content-Type", "application/json")
    ```
    * Contenty 타입을 application/json 으로 지정

* `Write` 는 데이터를 쓴다.
    * `Header` 에 Content-Type이 담겨져 있지 않다면, `Write` 는 Content-Type 셋을 추가시킨다.
    * `WriteHeader`가 호출되기 전이라면, `Write` 는 데이터를 쓰기 전에 `WriteHeader(http.StatusOK)` 를 호출한다.
    * ```Writer``` 가 쓰게 될 데이터의 총 사이즈가 몇 kb밖에 안된다면 `Flush` 는 호출되지 않는다. Content-Length 헤더는 자동으로 추가된다.

* `WriteHeader` 는 HTTP 응답 헤더를 제공된 상태코드와 함께 보낸다.
    * status code 는 유효한 코드여야 한다. (1xx-5xx의 범주)


[Return to TOC](#table-of-contents)


### timeoutWriter

```go
type timeoutWriter struct {
  w     ResponseWriter
  h     Header
  wbuf  bytes.Buffer
  req   *Request
  
  mu            sync.Mutex
  timeOut       bool
  wroteHeader   bool
  code          int
}
```
`timeoutWriter` 는 `ResponseWriter` 인터페이스와 `Header` 맵을 내장하고 있다.  

#### WriterHeader
  ```go
  func (tw *timeoutWriter) WriteHeader(code int) {
    tw.mu.Lock()
    defer tw.mu.Unlock()
    tw.writeHeaderLocked(code)
  }
  ```
  * code  
  parmeter `code` 는 status code 를 의미한다.  
    ```go
    # e.g.,
    w.WriteHeader(200)
    w.WriteHeader(http.StatusBadRequest)
    ```

#### Header
```go
func (tw *timeoutWriter) Header() Header { return tw.h }
```
* `timoutWriter` 에 내장되어 있는 `Header` 맵을 리턴한다.  
   ```go
    type Header map[string][]string
   ```  
   `Header` 는 key-value 짝으로 이루어진 HTTP 해더이다.  

[Return to TOC](#table-of-contents)

### Handler
Handler 인터페이스는 응답 처리를 위해 사용된다.  
```Handler``` 는 서버가 클라이언트로 부터 요청을 받았을 때 그 요청을 핸들링 해준다.
```go
type Handler interface {
  ServeHTTP(ResponseWriter, *Request)
}
```
* ```ServeHTTP``` 는 두 매개변수를 받는다.
    * ```ResponseWriter``` 인터 페이스 
    * ```Request``` 를 가리키는 포인터

[Return to TOC](#table-of-contents)


### Flusher
Flush 는 buffered data 를 클라이언트에게 보낸다.
```go
type Flusher interface {
  Flush()
}
```

[Return to TOC](#table-of-contents)


### Hijacker
```go
type Hijacker interface {
  Hijack() (net.Conn, *bufio.ReadWriter, error)
}
```

### http.flush
```go
func (cw *chunkWriter) flush() {
  if !cw.wroteHeader {
     cw.writeHeader(nil)
  }
  cw.res.conn.bufw.Flush()
}
```

[Return to TOC](#table-of-contents)


### conn struct
```go
type conn struct {
    server     *Server
    cancelCtx  context.CancelFunc
    rwc        net.Conn
    remoteAddr string
    tlsState   *tls.ConnectionState
    werr       error
    r          *connReader
    bufr       *bufio.Reader
    bufw       *bufio.Writer
    lastMethod string
    curReq     atomic.Value 
    curState   struct{ atomic uint64 } 
    mu         sync.Mutex
    hijackedv  bool
}
```
* Immutable 하며 nil 의 값을 가질 수 없다.
* ```cancleCtx``` 는 connection-level 의 컨텍스트를 취소 시킨다.
* ```tlsState``` 는 TLS 를 사용할 때 TLS 의 연결 상태
* ```werr``` 는 write error 를 의미

[Return to TOC](#table-of-contents)


### http.ServeHTTP
```ServeHTTP()``` 메서드는 응답시 데이터를 쓰기 위한 ResponseWriter 와 HTTP Request 입력 데이터를 파라미터로 갖는다.
```go
func (rh *redirectHandler) ServeHTTP(w ResponseWriter, r *Request) {
  Redirect(w, r, rh.url, rh.code)
}
```

### http.RedirectHandler
```go
func RedirectHandler(url string, code int) Handler {
  return &redirectHandler{url, code}
}
```

[Return to TOC](#table-of-contents)


### http.Handler
```go
func (mux *ServeMux) Handler(r *Request) (h Handler, pattern string) {

  if r.Method == "CONNECT" {
     if u, ok := mux.redirectToPathSlash(r.URL.Host, r.URL.Path, r.URL); ok {
        return RedirectHandler(u.String(), StatusMovedPermanently), u.Path
     }

     return mux.handler(r.Host, r.URL.Path)
  }

  host := stripHostPort(r.Host)
  path := cleanPath(r.URL.Path)

  if u, ok := mux.redirectToPathSlash(host, path, r.URL); ok {
     return RedirectHandler(u.String(), StatusMovedPermanently), u.Path
  }

  if path != r.URL.Path {
     _, pattern = mux.handler(host, path)
     url := *r.URL
     url.Path = path
     return RedirectHandler(url.String(), StatusMovedPermanently), pattern
  }

  return mux.handler(host, r.URL.Path)
}
```
* ```Handle()``` 메서드는 요청된 path 에 어떤 요청 핸드러를 사용할지를 지정해준다. 라우팅 역할이라고 보면 된다.

[Return to TOC](#table-of-contents)


### http.HandleFunc
```go
func (mux *ServeMux) HandleFunc(pattern string, handler func(ResponseWriter, *Request)) {
  if handler == nil {
     panic("http: nil handler")
  }
  mux.Handle(pattern, HandlerFunc(handler))
}
```
* URL 별로 요청을 처리할 핸들러 함수를 등록한다.

```go
s.Router.HandleFunc("/",middleware.MiddlewareJSON(handler.Home)).Methods("GET")
```
* path ```"/"``` 에 요청이 들어왔을 때 ```handler.Home``` 이라는 함수를 실행하도록 함.

[Return to TOC](#table-of-contents)


### http.ListenAndServe
```ListenAndServe``` 는 웹 요청을 기다리고 있다가(listen) 요청이 들어오면 해당 요청을 처리(serve)한다.
```go
func ListenAndServe(addr string, handler Handler) error {
  server := &Server{Addr: addr, Handler: handler}
  return server.ListenAndServe()
}
```
* 첫 번째 매개변수 ```addr``` 에는 응답을 받을 주소를 적어준다.
    ```go
    log.Fatal(http.ListenAndServe(addr, s.Router))
    ```
* ```HandleFunc``` 의 두 번째 매개변수에는 웹 요청을 처리할 핸들러를 전달한다.
    ```go
    http.ListenAndServe(“:8000”, nil)
    ```
    * Port# 8000 에서 웹 서버가 구동된다.
    * 핸들러가 전달되지 않으면 default 값으로 ```http.DefaultServeMux``` 가 지정된다.
      * 핸들러 위치에 ```nil``` 을 적어주었기에 default 로 ```http.DefaultServeMux``` 가 선택된다.

[Return to TOC](#table-of-contents)


### http.ServeHTTP
요청한 http 메서드와 URL 을 토대로 합당한 핸들러를 찾아 동작시키는 메서드.
```go
func (h *Handler) ServeHTTP(rw http.ResponseWriter, req *http.Request)
    // .... 너무 길어 생략 ...
```
    * 요청에 합당한 핸들러가 없을시 NotFound 에러가 리턴된다.
