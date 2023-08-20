---
layout: post
title: "[Go] Package SMTP"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

## SMTP 
**S**imple **M**ail **T**ransfer **P**rotocol 의 약자  
> SMTP 의 자세한 내용은 [Network/SMTP](https://github.com/8luebottle/TIL/blob/master/Network/smtp.md) 에서 확인

**net/smtp**  
Package SMTP는 [RFC 5321](https://tools.ietf.org/html/rfc5321) 의 SMTP, [RFC 1652](https://tools.ietf.org/html/rfc1652) 의 8BITMIME, [RFC 2554](https://tools.ietf.org/html/rfc2554) 의 AUTH, [RFC 3207](https://tools.ietf.org/html/rfc3207) 의 STARTTLS 를 구현해 놓은 내장 패키지다.

이메일 발송을 위해 사용한다.

 ### Table of Contents
 * [smtp 코드 열어보기](#smtp-코드-열어보기)
    * [type Client](#type-client)
    * [smtp.Close](#smtpclose)
    * [smtp.Extension](#smtpExtension)
    * [smtp.Hello](#smtpHello)
    * [smtp.Reset](#smtpReset)
    * [smtp.Noop](#smtpNoop)
    * [smtp.Quit](#smtpQuit)
    * [smtp.ValidateLine](#smtpValidateLine)
    * [smtp.SendMail](#smtpSendMail)

## smtp 코드 열어보기
### type Client
SMTP 서버와 연결된 클라이언트.
```go
type Client struct {
  Text        *textproto.Conn
  conn        net.Conn
  tls         bool
  serverName  string
  ext         map[string]string
  auth        []string
  localName   string 
  didHello    bool   
  helloError  error  
}
```
* Text  
  Client 가 extensions 를 추가할 수 있게 해준다.
* conn  
  이후 TLS 연결을 위해 연결에 관한 기록을 보유한다.  
  net.Conn 인터페이스의 메소드는 아래와 같다.
    * Read
    * Write
    * Close
    * LocalAddr
    * RemoteAddr
    * SetDeadline
    * SetReadDeadline
    * SetWriteDeadline
* tls  
  tls를 사용하는가의 여부
* serverName  
  서버명
* ext  
  서포트하는 익스텐션 (map 타입)
* auth  
  서포트하는 auth mechanisms
* localName  
  HELO/EHLO 에서 사용할 이름
* didHello  
* helloError  
  hello 로부터 파생된 에러

[↑ return to TOC](#table-of-contents)


### smtp.Close
연결 끊기
```go
func (c *Client) Close() error {
  return c.Text.Close()
}
```

[↑ return to TOC](#table-of-contents)


### smtp.Extension
서버가 지원하는 extension인지 보고해준다.
* extension 명은 case-insensitive
```go
func (c *Client) Extension(ext string) (bool, string) {
  if err := c.hello(); err != nil {
     return false, ""
  }
  if c.ext == nil {
     return false, ""
  }
  ext = strings.ToUpper(ext)
  param, ok := c.ext[ext]
  return ok, param
}
```

[↑ return to TOC](#table-of-contents)


### smtp.Hello
```go
func (c *Client) Hello(localName string) error {
  if err := validateLine(localName); err != nil {
     return err
  }
  if c.didHello {
     return errors.New("smtp: Hello called after other methods")
  }
  c.localName = localName
  return c.hello()
}
```
* HELO  
  Hello  
  해당 명령어를 통해 서버를 식별한 후 SMTP 대화를 시작한다.

[↑ return to TOC](#table-of-contents)


### smtp.Reset
RSET 명령어를 서버에 보냄으로써 현재 진행중인 메일 transaction 을 중단시킨다.
```go
func (c *Client) Reset() error {
  if err := c.hello(); err != nil {
     return err
  }
  _, _, err := c.cmd(250, "RSET")
  return err
}
```
* RSET  
  Reset  
  전체 트랜잭션을 무효화 한 후 버퍼를 다시 설정(Reset)시키는 명령어.

[↑ return to TOC](#table-of-contents)


### smtp.Noop
NOOP 명령어를 서버에 보낸다.  
이를 통해 서버가 연결이 문제 없는지, 클라이언트와 통신가능한지 확인한다.
```go
func (c *Client) Noop() error {
  if err := c.hello(); err != nil {
     return err
  }
  _, _, err := c.cmd(250, "NOOP")
  return err
}
```
* NOOP  
  No Operation  
  수신자가 OK 응답을 보내도록 한다.

[↑ return to TOC](#table-of-contents)


### smtp.Quit
QUIT 명령어를 서버에 보낸다.
```go
func (c *Client) Quit() error {
  if err := c.hello(); err != nil {
     return err
  }
  _, _, err := c.cmd(221, "QUIT")
  if err != nil {
     return err
  }
  return c.Text.Close()
}
```
* QUIT  
  서버의 연결을 닫음  
  서버는 해당 명령어를 받게 되면 221 코드를 보낸후 세션을 닫는다.  

[↑ return to TOC](#table-of-contents)


### smtp.ValidateLine
SMTP의 라인 규격을 맞추었는지 확인한다. 
```go
func validateLine(line string) error {
  if strings.ContainsAny(line, "\n\r") {
     return errors.New("smtp: A line must not contain CR or LF")
  }
  return nil
}
```
* 매 라인은 RFC 5321 규격에 근거, CR(\r) + LF(\n) 로 끝나야 한다.  
    * CR : Carriage Return
    * LF : Line Feed 

[↑ return to TOC](#table-of-contents)


### smtp.SendMail
메일 전송
```go
func SendMail(addr string, a Auth, from string, to []string, msg []byte) error {
  if err := validateLine(from); err != nil {
     return err
  }
  for _, recp := range to {
     if err := validateLine(recp); err != nil {
        return err
     }
  }
  c, err := Dial(addr)
  if err != nil {
     return err
  }
  defer c.Close()
  if err = c.hello(); err != nil {
     return err
  }
  if ok, _ := c.Extension("STARTTLS"); ok {
     config := &tls.Config{ServerName: c.serverName}
     if testHookStartTLS != nil {
        testHookStartTLS(config)
     }
     if err = c.StartTLS(config); err != nil {
        return err
     }
  }
  if a != nil && c.ext != nil {
     if _, ok := c.ext["AUTH"]; !ok {
        return errors.New("smtp: server doesn't support AUTH")
     }
     if err = c.Auth(a); err != nil {
        return err
     }
  }
  if err = c.Mail(from); err != nil {
     return err
  }
  for _, addr := range to {
     if err = c.Rcpt(addr); err != nil {
        return err
     }
  }
  w, err := c.Data()
  if err != nil {
     return err
  }
  _, err = w.Write(msg)
  if err != nil {
     return err
  }
  err = w.Close()
  if err != nil {
     return err
  }
  return c.Quit()
}
```
* Parameters
    * addr  
      SMTP 서버주소, Port 번호
    * a  
      Auth 인터페이스
    * from  
      송신자 이메일 주소
    * to  
      수신자 이메일 주소
    * msg  
      이메일에 담길 내용  
      RFC 822 의 형식을 따라야 한다.  
        1. Email Header
        1. Blank Line  
          메일의 헤더와 바디를 구분하기위해 Blank line이 필요
        1. Message Body  
          매 라인은 CRLF 로 끝나야함


[↑ return to TOC](#table-of-contents)
