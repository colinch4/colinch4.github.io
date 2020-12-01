---
layout: post
title: "[안드로이드] Serializable vs Parcelable"
description: " "
date: 2020-11-25
tags: [Android]
comments: true
share: true
---

# Serializable
  
  Android sdk가 아닌 표준 java의 인터페이스
  
  인텐트를 이용하여 객체를 보낼때 객체를 직렬화하는 '마커 인터페이스'. 아무런 메서드도 가지지 않음
  
  ```
  // 단순히 직렬화할 클래스는 Serializable을 implements 해주면 된다.
  
  public class Person implements Serializable{
    /*
     클래스 내용
    */
  }
  
  ```
  
  Serializable은 내부에서 Reflection을 사용하여 직렬화를 처리한다.
  이때 Reflection은 처리 과정 중에 많은 추가 객체가 생성되며, 이는 GC의 타겟이 된다.
  
  
# Parcelable
  
  Parcelable은 직렬화를 위한 또다른 인터페이스. Android의 인터페이스 이다.
  
  Reflection을 사용하지 않도록 설계되어 매우 빠르지만, 보일러 플레이트 코드가 많이 추가되고
  
  이로인해 새로운 기능을 추가하기가 힘들다.
  
  ```
  public class Person implements Parcelable{
    private String firstName;
    private String lastName;
    
    protected Person(Parcel in) {
        this.firstName = in.readString();
        this.lastName = in.readString();
        this.age = in.readInt();
    }
    
    //반드시 필요한 WriteToParcel
    @Override
    public void writeToParcel(Parcel dest, int flags) {
        dest.writeString(this.firstName);
        dest.writeString(this.lastName);
    }
  
   //반드시 필요한 CREATOR
   public static final Parcelable.Creator<Person> CREATOR = new Parcelable.Creator<Person>() {
        @Override
        public Person createFromParcel(Parcel source) {
            return new Person(source);
        }

        @Override
        public Person[] newArray(int size) {
            return new Person[size];
        }
    };
  
  }
  ```
  
# Serializable vs Parcelable
  
  
  Serializable 이 Parcelable 보다 일반적으로 reflection 때문에 느리다.
    
  Parcelable은 커널메모리를 통해 데이터를 다른 프로세스로 전달하여 reflection없이 빠르다.
  
  그러나 Serializable 또한 reflection이 발생하지 않도록 메서드들을 잘 정의하여 사용한다면 Parcelable 못지 않은 속도를 낸다고 한다.
  
