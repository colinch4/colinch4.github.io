---
layout: post
title: "[데이터포멧] ByteArray"
description: " "
date: 2021-06-11
tags: [java]
comments: true
share: true
---

## ByteArray

Server.java 
```java
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

// Protocol - Calculation
// => Byte Array
//    [op: char] [lhs: int] [rhs : int]
//    '+', '-', '*'
public class Server {

  public static void main(String[] args) {
    try {
      byte[] data = new byte[1024];
      ServerSocket serverSocket = new ServerSocket(5000);
      Socket socket = serverSocket.accept();


      try (InputStream is = socket.getInputStream();
           DataInputStream dis2 = new DataInputStream(is)) {

        int count = 0;
        while (true) {
          int packetLen;
          try {
            packetLen = dis2.readInt();
          } catch(EOFException e){
            break;
          }

          int ret = is.read(data, 0, packetLen);
          if (ret == -1) {
            break;
          }

          ByteArrayInputStream bis = new ByteArrayInputStream(data);
          DataInputStream dis = new DataInputStream(bis);

          char op = dis.readChar();
          int lhs = dis.readInt();
          int rhs = dis.readInt();

          System.out.printf("%5d - %d %c %d \n", count++, lhs, op, rhs);
        }
      }

    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

Client1.java
```java
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

public class Client1 {

  public static void main(String[] args) {
    char op = '+';
    int lhs = 10;
    int rhs = 32;

    try {
      Socket socket = new Socket("127.0.0.1", 5000);
      try (OutputStream os = socket.getOutputStream()) {
        for (int i = 0; i < 100000; i++) {
          // Decorator Pattern : 데코레이터 패턴
          ByteArrayOutputStream bos = new ByteArrayOutputStream(1024);
          DataOutputStream dos = new DataOutputStream(bos);
          dos.writeChar(op);
          dos.writeInt(lhs);
          dos.writeInt(rhs);

          byte[] data = bos.toByteArray();
          int len = bos.size();
          os.write(data, 0, len);
        }  
      }

    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}

```

Client2.java
```java
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;

public class Client2 {
  public static void main(String[] args) {

    char op = '+';
    int lhs = 10;
    int rhs = 32;

    try {
      Socket socket = new Socket("127.0.0.1", 5000);

      try (OutputStream os = socket.getOutputStream();
           DataOutputStream dos2 = new DataOutputStream(os)) {

        for (int i = 0; i < 100000; i++) {
          ByteArrayOutputStream bos = new ByteArrayOutputStream(1024);
          DataOutputStream dos = new DataOutputStream(bos);

          dos.writeChar(op);
          dos.writeInt(lhs);
          dos.writeInt(rhs);

          byte[] data = bos.toByteArray();
          int len = bos.size();

          dos2.writeInt(len);
          os.write(data, 0, len);
        }
      }

    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```
