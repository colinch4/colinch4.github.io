---
layout: post
title: "[자바기초] Properties"
description: " "
date: 2020-11-26
tags: [java]
comments: true
share: true
---
 

내부적으로 Hashtable을 사용하여 key ,value를 (String,String)으로 저장한다.  

주로 어플리케이션의 환경설정에 관련된 속성을 저장하는데, 파일로부터 편리하게 값을 읽고 쓸 수 있는 메서드를 제공한다.  

```
Properties prop = new Properties();

prop.setProperty("timeout","30");

try{
  // 파일로 저장
  prop.store(new FileOutputStream("output.txt"), "Properties Example");
  
  // xml파일로 저장
  prop.storeToXML(new FileOutputStream("output.xml"), "Properties Example");
} catch(IOException e){
  e.printStackTrace();
}

```
