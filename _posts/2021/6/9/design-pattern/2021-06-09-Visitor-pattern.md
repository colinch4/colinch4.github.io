---
layout: post
title: "[디자인패턴] Visitor 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Visitor 패턴
------------

-	Visitor 패턴의 목적은 처리를 데이터 구조에서 분리하는 일이다. 데이터 구조는 요소를 집합으로 정리하거나, 요소 사이를 연결해주는 중요한 역할을 한다. 그러나 구조를 유지하는 것과 구조를 기초로 한 처리를 기술하는 것과는 별개이다.
-	일반적으로 ConcreteVisitor 역할은 File 클래스나 Directory 클래스와는 독립적으로 개발할 수 있다.
-	즉, Visitor 패턴은 File 클래스나 Directory 클래스의 부품으로써의 독립성을 높일 수 있다. 만약, 처리 내용을 File 클래스나 Directory 클래스의 메소드로서 프로그램을 작성하면, 새로운 '처리'를 추가해서 기능 확장을 할 때마다 File 클래스나 Directory 클래스를 수정해야만 한다.
-	확장에 대해서는 열려있고 수정에 대해서는 닫혀있는 클래스가 부품으로써 재이용 가치가 높은 클래스이다. 디자인 패턴의 목적, 오브젝트(객체)지향의 목적이란 바로 이러한 클래스를 만들 수 있는 구조를 제공하는 것이다.

-	Visitor 패턴의 등장인물

	-	Visitor(방문자)의 역할
		-	Visitor는 데이터 구조의 구체적인 요소(ConcreteElement 역할)마다 'xxxx을 방문했다'라는 visit(xxxx) 메소드를 선언한다. visit(xxxx)는 xxxx을 처 리하기 위한 메소드이고, 실제의 코드는 Concrete Visitor 역할에 기술되어 있다. 예제 프로그램에서는 Visitor 클래스가이 역할을 한다.
	-	ConcreteVisitor(구체적인 방문자)의 역할
		-	ConcreteVisitor는 Visitor 역할의 인터페이스(API)를 구현한다. visit(xxxx) 라는 형태의 메소드를 구현하고, 각각의 ConcreteElement 역할의 처리를 기술합니다.예제 프로그램에서는 ListVisitor 클래스가 이 역할을 한다. ListVisitor 에서 currentdir 필드값이 변화했듯이 visit를 처리해 가는 중에 ConcreteVisitor 역할의 내부상태가 변화하는 일도 있다.
	-	Element(요소)의 역할
		-	Element는 Visitor 역할의 방문할 곳을 나타내는 역할로, 방문자를 받아들이는 accept 메소드를 선언한다. accept 메소드의 인수에는 Visitor 역할이 전달된다. 예제 프로그램에서는 Element 인터페이스가 이 역할을 한다.
	-	ConcreteElement(구체적 요소)의 역할
		-	ConcreteElement는 Element 역할의 인터페이스(API)를구현하는 역할입니다. 예제 프로그램에서는 File 클래스나 Directory 클래스가 이 역할을 합니다.
	-	ObjectStructure(오브젝트의 구조)의 역할
		-	ObjectStructure는 Element 역할의 집합을 취급하는 역할이다. ConcreteVisitor 역할이 각각의 Element 역할을 취급할 수 있는 메소드를 구비하고 있다. 예제 프로그램에서는 Directory 클래스가 이 역할을 한다(1 인 2 역). Concrete Visitor 역할 이 각각의 Element 역할을 취급할 수 있는 것처럼 예제 프로그램의 Directory 클래스에는 iterator 메소드가 준비되어 있다.

![Visitor 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzZVpyN0U4dllvZ1U)

-	예제

![Visitor 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzcV9wdDFwUUtqemc)

```java
public class Main {
    public static void main(String[] args) {
        try {
            System.out.println("Making root entries...");
            Directory rootdir = new Directory("root");
            Directory bindir = new Directory("bin");
            Directory tmpdir = new Directory("tmp");
            Directory usrdir = new Directory("usr");
            rootdir.add(bindir);
            rootdir.add(tmpdir);
            rootdir.add(usrdir);
            bindir.add(new File("vi", 10000));
            bindir.add(new File("latex", 20000));
            rootdir.accept(new ListVisitor());              

            System.out.println("");
            System.out.println("Making user entries...");
            Directory Kim = new Directory("Kim");
            Directory Lee = new Directory("Lee");
            Directory Kang = new Directory("Kang");
            usrdir.add(Kim);
            usrdir.add(Lee);
            usrdir.add(Kang);
            Kim.add(new File("diary.html", 100));
            Kim.add(new File("Composite.java", 200));
            Lee.add(new File("memo.tex", 300));
            Kang.add(new File("game.doc", 400));
            Kang.add(new File("junk.mail", 500));
            rootdir.accept(new ListVisitor());             
        } catch (FileTreatmentException e) {
            e.printStackTrace();
        }
    }
}

public interface Acceptor {
    public abstract void accept(Visitor v);
}

public abstract class Entry implements Acceptor {
    public abstract String getName();                                   // 이름을 얻는다.
    public abstract int getSize();                                      // 사이즈를 얻는다.
    public Entry add(Entry entry) throws FileTreatmentException {       // 엔트리를 추가
        throw new FileTreatmentException();
    }
    public Iterator iterator() throws FileTreatmentException {    // Iterator의 생성
        throw new FileTreatmentException();
    }
    public String toString() {                                          // 문자열 표현
        return getName() + " (" + getSize() + ")";
    }
}

public class File extends Entry {
    private String name;
    private int size;
    public File(String name, int size) {
        this.name = name;
        this.size = size;
    }
    public String getName() {
        return name;
    }
    public int getSize() {
        return size;
    }
    public void accept(Visitor v) {
        v.visit(this);
    }
}

public class Directory extends Entry {
    private String name;                    // 디렉토리의 이름
    private Vector dir = new Vector();      // 디렉토리 엔트리의 집합
    public Directory(String name) {         // 생성자
        this.name = name;
    }
    public String getName() {               // 이름을 얻는다.
        return name;
    }
    public int getSize() {                  // 사이즈를 얻는다.
        int size = 0;
        Iterator it = dir.iterator();
        while (it.hasNext()) {
            Entry entry = (Entry)it.next();
            size += entry.getSize();
        }
        return size;
    }
    public Entry add(Entry entry) {         // 엔트리의 추가
        dir.add(entry);
        return this;
    }
    public Iterator iterator() {      // Iterator의 생성
        return dir.iterator();
    }
    public void accept(Visitor v) {         // 방문자를 받아들임
        v.visit(this);
    }
}

public class FileTreatmentException extends RuntimeException {
    public FileTreatmentException() {
    }
    public FileTreatmentException(String msg) {
        super(msg);
    }
}

public abstract class Visitor {
    public abstract void visit(File file);
    public abstract void visit(Directory directory);
}

public class ListVisitor extends Visitor {
    private String currentdir = "";                         // 현재 주목하고 있는 디렉토리명
    public void visit(File file) {                  // 파일을 방문했을 때 호출된다.
        System.out.println(currentdir + "/" + file);
    }
    public void visit(Directory directory) {   // 디렉토리를 방문했을 때 호출된다.
        System.out.println(currentdir + "/" + directory);
        String savedir = currentdir;
        currentdir = currentdir + "/" + directory.getName();
        Iterator it = directory.iterator();
        while (it.hasNext()) {
            Entry entry = (Entry)it.next();
            entry.accept(this);
        }
        currentdir = savedir;
    }
}
```

-	visit(File) 메소드는 '**File 클래스의 인스턴스에 대해서 실행해야 할 처리**'
-	visit(Directory) 메소드에는 '**Directory 클래스의 인스턴스에 대해서 실행해야 할 처리**'
-	visit 메소드와 accept 메소드가 서로 상대를 호출하는 것이다.
-	Main 클래스는 Composite 패턴의 Main 클래스와 거의 동일. 다른점은 Directory 내용을 표시하기 위해, 표시를 행하는 방문자인 ListVisitor의 인스턴스를 사용한다는 점이다. Composite 패턴에서는 디렉토리를 표시하기 위해 printList라는 메소드를 사용했다. 즉, Directory 클래스(데이터 구조 클래스)에서 구현했다. 이에 반해 Visitor 패턴에서는 디렉터리를 표시하는 것도 Visitor 클래스에서 실행한다. **처리를 데이터 구조에서 분리**되어 있다.
