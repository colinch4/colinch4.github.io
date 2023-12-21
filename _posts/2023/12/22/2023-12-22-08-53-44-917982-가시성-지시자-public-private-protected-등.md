---
layout: post
title: "[c#] 가시성 지시자 (public, private, protected 등)"
description: " "
date: 2023-12-22
tags: [c#]
comments: true
share: true
---

### 1. public
   - `public` 가시성 지시자를 사용하면 클래스 외부에서 해당 멤버에 접근할 수 있습니다.
   - 예시:
   ```csharp
   public class MyClass
   {
       public int myPublicField;
       
       public void MyPublicMethod()
       {
           // Method implementation
       }
   }
   ```

### 2. private
   - `private` 가시성 지시자를 사용하면 해당 멤버에 클래스 외부에서는 접근할 수 없습니다.
   - 예시:
   ```csharp
   public class MyClass
   {
       private int myPrivateField;
       
       private void MyPrivateMethod()
       {
           // Method implementation
       }
   }
   ```

### 3. protected
   - `protected` 가시성 지시자를 사용하면 해당 멤버에는 파생 클래스 내부에서만 접근할 수 있습니다.
   - 예시:
   ```csharp
   public class MyBaseClass
   {
       protected int myProtectedField;
   }

   public class MyDerivedClass : MyBaseClass
   {
       public void AccessProtectedField()
       {
           int value = myProtectedField; // Can access the protected field from the base class
       }
   }
   ```

가시성 지시자를 사용하여 적절한 접근 수준을 정의하면 클래스의 캡슐화를 유지하고 안정성을 높일 수 있습니다.