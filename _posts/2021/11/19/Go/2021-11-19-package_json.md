---
layout: post
title: "[Go] Package json"
description: " "
date: 2021-11-19
tags: [Go]
comments: true
share: true
---

# Package json

Go 에서 JSON을 사용하기 위해서는 <code>encoding/json</code> 패키지를 이용한다.


### Table of Contents
* JSON Basic
    * [Marshaling 과 Unmarshaling](#marshaling-과-unmarshaling)

* json 코드 열어보기
    * [json.Marshal](json.Marshal)
    * [json.Unmarshal](json.Unmarshal)
    * [json.MarshalIndent](#jsonmarshalindent)


## JSON Basic
웹 서버와 클라이언트의 통신을 하기 위해 JSON 이라는 데이터 표현법을 사용한다.  
텍스트로 이루어진 JSON 이기에 사람 뿐만 아니라 기계도 이해하기 편하다.  

JSON (JavaScript Object Notation) 은 자바스크립트 구문을 따르지만, 프로그래밍 언어와 독립적이다.   
대부분의 클라이언트(JavaScript)와 서버(Go, Python, C++, JAVA etc)간에 데이터를 전송하기 위해 JSON 을 사용한다.

JSON은 key 와 value 쌍으로 이루어져 있다. key 의 위치에는 반드시 string 타입이 와야하지만 value 에는 타입 제한이 없다.  
이러한 특징을 갖춘 데이터 저장 공간을 만든다면 아래와 같다.  
```go
var data map[string]interface{}
```
* map 은 키와 값의 쌍으로 이루어진 자료형이다.
* Key 는 반드시 문자열
    * **<code>key</code>** 의 자리에 string 타입을 넣어준다.  
    map[**<code>string</code>**]interface{}
* Value 는 모든 타입이 올 수 있음
    * **<code>value</code>** 의 자리에 모든 타입을 받을 수 있는 interface 를 넣어준다.  
    map[string]**<code>interface{}</code>**

### Marshaling 과 Unmarshaling  
**Marshaling :** 객체의 구조를 raw byte 데이터로 변경하는 것을 말한다.  
* Encoding 이라고도 함.
* json.Marshal

**Unmarshaling :** byte slice 나 string을 객체 구조로 변경하는 것을 말한다.  
* Decoding 이라고도 함.
* json.Unmarshal

<!-- **Why Byte?**  
컴퓨터는 데이터를 바이트 단위로 인식하기에,. -->

[Return to TOC](#table-of-contents)

## json 코드 열어보기

### json.Marshal
Go → JSON (encoding)  

Go 자료형을 JSON 텍스트로 바꾸어 준다.

```go
func Marshal(v interface{}) ([]byte, error) {
  e := newEncodeState()

  err := e.marshal(v, encOpts{escapeHTML: true})
  if err != nil {
     return nil, err
  }
  buf := append([]byte(nil), e.Bytes()...)

  e.Reset()
  encodeStatePool.Put(e)

  return buf, nil
}
```
* <code>Marshal</code> 은 <code>MarshalJSON</code> 메서드를 불러 JSON을 만든다.  
* Return Value 는 <code>[]byte</code> 와 <code>error</code> 이다.
    * 출력하고자 한다면 byte 를 string 으로 형변환시켜 주어야 한다.  
        ```go
        data := make(map[string]interface{})
        
        data["Wecode"] = "WeWork"
        data["Wecode 1"] = 8
        data["Wecode 2"] = 11
        data["Wecode 3"] = 17
        data["Wecode 4"] = 23
        
        js, _ := json.Marshal(data)
        
        fmt.Println(string(js))
        ```
        ```go
        {"Wecode":"WeWork","Wecode 1":8,"Wecode 2":11,"Wecode 3":17,"Wecode 4":23}
        ```

[Return to TOC](#table-of-contents)

### json.Unmarshal
JSON → Go (decoding) 

JSON 텍스트를 Go 자료형으로 바꾸어 준다.

```go
func Unmarshal(data []byte, v interface{}) error {
  var d decodeState
  err := checkValid(data, &d.scan)
  if err != nil {
     return err
  }

  d.init(data)
  return d.unmarshal(v)
}
```
* <code>v</code> 가 어떠한 타입이냐에 따라 언마샬링시 Go 의 타입이 결정된다.
    ```go
    jsonData :=`
	{
		"Wecode 1" : 8,
		"Wecode 2" : 11,
		"Wecode 3" : 17
	}
	`
	
	v := make(map[string]interface{})
	
	json.Unmarshal([]byte(doc), &v)
	
	fmt.Println(v)
    ```
    ```go
    map[Wecode 1:8 Wecode 2:11 Wecode 3:17]
    ```

[Return to TOC](#table-of-contents)

### json.MarshalIndent  
<code>json.Marshal</code> 을 사용시 데이터가 한 줄로 나열되어 있기 때문에 한 눈에 알아보기가 어렵다.  
데이터를 받는 상대방의 편의성을 염두에 둔다면 <code>json.MarshalIndent</code> 를 사용해보자.  
```go
func MarshalIndent(v interface{}, prefix, indent string) ([]byte, error) {
  b, err := Marshal(v)
  if err != nil {
     return nil, err
  }
  var buf bytes.Buffer
  err = Indent(&buf, b, prefix, indent)
  if err != nil {
     return nil, err
  }
  return buf.Bytes(), nil
}
```
* Return Value 는 <code>[]byte</code> 와 <code>error</code> 이다.  
* JSON 요소들을 새 라인에서 출력시켜준다.
* 매개변수  
    * 첫번째 매개변수 : Data  
    JSON 문서로 변화시켜줄 데이터  
    * 두번째 매개변수 : Prefix  
    보통 Empty string
    * 세번째 매개변수 : indent  
    보통 Whitespace 또는 Tab  
        ```go
        json.MarshalIndent(data, "", "  ")
        ```

```go
d := make(map[string]interface{})

d["Wecode"]   = "WeWork"
d["Wecode 1"] = 8
d["Wecode 2"] = 11
d["Wecode 3"] = 17
d["Wecode 4"] = 23

d, _ := json.MarshalIndent(data, "", "	") // Tab 사용
```
```go
// result
{
	"Wecode": "WeWork",
	"Wecode 1": 8,
	"Wecode 2": 11,
	"Wecode 3": 17,
	"Wecode 4": 23
}
```

```go
d, _ := json.MarshalIndent(data, "2nd", "3rd") 
```
```go
// result
{
2nd3rd"Wecode": "WeWork",
2nd3rd"Wecode 1": 8,
2nd3rd"Wecode 2": 11,
2nd3rd"Wecode 3": 17,
2nd3rd"Wecode 4": 23
2nd}
```
[Return to TOC](#table-of-contents)
