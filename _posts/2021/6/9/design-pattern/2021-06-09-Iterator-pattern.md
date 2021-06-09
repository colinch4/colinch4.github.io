---
layout: post
title: "[디자인패턴] Iterator 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Iterator 패턴
-------------

![반복자 패턴 클래스 다이어그램](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzamh3SXpSejdwZk0)

-	Iterator 패턴의 등장인물

	-	Iterator(반복자)의 역할
		-	요소를 순서대로 검색해가는 인터페이스(API)를 결정한다.
	-	Concretelterator(구체적인 반복자)의 역할
		-	Iterator가 결정한 인터페이스(API)를 실제로 구현한다.
	-	Aggregate(집합체)의 역할
		-	Iterator 역할을 만들어내는 인터페이스(API)를 결정한다.
	-	ConcreteAggregate(구체적인 집합체)의 역할
		-	Aggregate 역할이 결정한 인터페이스(API)를 실제로 구현하는 일을 한다. 구체적인 Iterator 역할， 즉 Concretelterator 역할의 인스턴스를 만들어낸다.

-	for문의 i++ 변수 i의 기능을 추상화해서 일반화한 것.

-	무엇인가 많이 모여있는 것들을 순서대로 지정하면서 전체를 검색하는 처리를 실행하기 위한 것.

-	Iterator는 무엇인가 '반복한다'라는 의미.

-	**Iterator 패턴을 사용하으로써 구현과 분리해서 하나씩 셀 수 있다.**

```java
Iterator it = bookShelf.iterator();
while (it.hasNext()) {
    Book book = (Book)it.next();
    System.out.println("" + book.getName());
}
```

-	위 코드는 while 루프는 bookShelf의 구현에 의존하지 않는다.
-	자세히 코드로 설명하면

**BookShelf books 배열 사용**

```java
public interface Aggregate {
    public abstract Iterator iterator();
}

public class Book {
    private String name = "";
    public Book(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }
}

public class BookShelf implements Aggregate {
    private Book[] books;
    private int last = 0;
    public BookShelf(int maxsize) {
        this.books = new Book[maxsize];
    }
    public Book getBookAt(int index) {
        return books[index];
    }
    public void appendBook(Book book) {
        this.books[last] = book;
        last++;
    }
    public int getLength() {
        return last;
    }
    public Iterator iterator() {
        return new BookShelfIterator(this);
    }
	public Book[] getBooks() {
		return books;
	}
	public void setBooks(Book[] books) {
		this.books = books;
	}

}

public class BookShelfIterator implements Iterator {
    private BookShelf bookShelf;
    private int index;
    public BookShelfIterator(BookShelf bookShelf) {
        this.bookShelf = bookShelf;
        this.index = 0;
    }
    public boolean hasNext() {
        if (index < bookShelf.getLength()) {
            return true;
        } else {
            return false;
        }
    }
    public Object next() {
        Book book = bookShelf.getBookAt(index);
        index++;
        return book;
    }
}

public interface Iterator {
    public abstract boolean hasNext();
    public abstract Object next();
}
```

-	위의 코드에서 BookShelf 클래스의 배열을 사용해서 책을 관리하는 것을 그만두고 아래 코드와 같이 Vector를 사용하도록 프로그램은 수정하면

**BookShelf books Vector 변경**

```java
public class BookShelf implements Aggregate {
    private Vector books;   
    public BookShelf(int initialsize) {         
        this.books = new Vector(initialsize);   
    }
    public Book getBookAt(int index) {
        return (Book)books.get(index);
    }
    public void appendBook(Book book) {
        books.add(book);
    }
    public int getLength() {
        return books.size();                    
    }
    public Iterator iterator() {
        return new BookShelfIterator(this);
    }
}
```

-	실행 코드에서

```java
public class Main {
    public static void main(String[] args) {
        BookShelf bookShelf = new BookShelf(4);
        bookShelf.appendBook(new Book("Around the World in 80 Days"));
        bookShelf.appendBook(new Book("Bible"));
        bookShelf.appendBook(new Book("Cinderella"));
        bookShelf.appendBook(new Book("Daddy-Long-Legs"));
        bookShelf.appendBook(new Book("East of Eden"));
        bookShelf.appendBook(new Book("Frankenstein"));
        bookShelf.appendBook(new Book("Gulliver's Travels"));
        bookShelf.appendBook(new Book("Hamlet"));
        Iterator it = bookShelf.iterator();
        while (it.hasNext()) {
            Book book = (Book)it.next();
            System.out.println("" + book.getName());
        }
    }
}
```

-	while 루프는 전혀 변경하지 않아도 동작한다.

-	단 Aggregate와 Iterator쌍이고 그것을 구현한 클래스도 쌍이여서 getBookAt가 변경시 둘 다 수정이 필요하다.

-	아래 코드와 같이 일반 for문 사용시 위에 배열을 Vector로 변경하면 코드 수정이 필요하다.

```java
Book[] books = bookShelf.getBooks();
    for (int i = 0; i < books.length; i++) {
        Book book = books[i];
        System.out.println("" + book.getName());
}
```

> 하지만 향상된 for문이 나와서 Iterator 패턴을 사용하지 않아도 구현과 분리해서 하나씩 셀 수 있다. Iterator 패턴 대신 향상된 for문을 사용하자.

**향상된 for문과 Iterator 비교**

```java
Iterator it = bookShelf.iterator();
while (it.hasNext()) {
    Book book = (Book)it.next();
    System.out.println("" + book.getName());
}

for (Book book : bookShelf.getBooks()) {
    System.out.println("" + book.getName());
}
```
