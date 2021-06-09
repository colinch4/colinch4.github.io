---
layout: post
title: "[디자인패턴] Composite 패턴"
description: " "
date: 2021-06-09
tags: [디자인패턴]
comments: true
share: true
---

Composite 패턴
--------------

-	그릇과 내용물을 동일시해서 재귀적 구조를 만들기 위한 디자인 패턴.
-	Composite 패턴은 그릇과 내용물을 동일시하는 패턴이지만, 복수와 단수 역시 동일시 한 다고 할 수 있다. 즉, 여러 개를 모아서 마치 하나인 것처럼 취급한다.

-	Composite 패턴의 등장인물

	-	Leaf(나뭇잎)의 역할
		-	Leaf는 '내용물'을 표시하는 역할을 하며 내부에는 다른 것을 넣을 수 없다. 예제 프로그램에서는 File클래스가 이 역할을 한다.
	-	Composite(복합체)의 역할
		-	Composite는 '그릇'을 나타내는 역할을 하며 Leaf 역할이나 Composite역할을 넣을 수 있다. 예제 프로그램에서는 Directory 역할을 넣을 수 있다. 예제 프로그램에서는 Directory 클래스가 이 역할을 한다.
	-	Component의 역할
		-	Leaf역할과 Composite역할을 동일시하는 역할을 한다. Component는 Leaf역할과 Component역할에 공통적인 상위 클래스로 실현된다. 예제 프로그램에서는 Entry 클래스가 이 역할을 한다.
	-	Client(의뢰자)의 역할
		-	Composite 패턴의 사용자이다. 예제 프로그램에서는 Main 클래스가 이 역할을 한다.

![Composite 패턴](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzdXN3X2ZDNkkwSEE)

-	예제

![Composite 패턴-예제](http://drive.google.com/uc?export=view&id=0ByLqiEM75qEzdzE2b0FmVHh4NmM)

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
            rootdir.printList();

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
            rootdir.printList();
        } catch (FileTreatmentException e) {
            e.printStackTrace();
        }
    }
}

public abstract class Entry {
    public abstract String getName();                               // 이름을 얻는다.
    public abstract int getSize();                                  // 사이즈를 얻는다.
    public Entry add(Entry entry) throws FileTreatmentException {   // 엔트리를 추가한다.
        throw new FileTreatmentException();
    }
    public void printList() {                                       // 일람을 표시한다.
        printList("");
    }
    protected abstract void printList(String prefix);               // prefix를 앞에 붙여서 일람을 표시한다.
    public String toString() {                                      // 문자열 표현
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
    protected void printList(String prefix) {
        System.out.println(prefix + "/" + this);
    }
}

public class Directory extends Entry {
    private String name;                    // 디렉토리의 이름
    private Vector directory = new Vector();      // 디렉토리 엔트리의 집합
    public Directory(String name) {         // 생성자
        this.name = name;
    }
    public String getName() {               // 이름을 얻는다.
        return name;
    }
    public int getSize() {                  // 사이즈를 얻는다.
        int size = 0;
        Iterator it = directory.iterator();
        while (it.hasNext()) {
            Entry entry = (Entry)it.next();
            size += entry.getSize();
        }
        return size;
    }
    public Entry add(Entry entry) {         // 엔트리의 추가
        directory.add(entry);
        return this;
    }
    protected void printList(String prefix) {       // 엔트리의 일람
        System.out.println(prefix + "/" + this);
        Iterator it = directory.iterator();
        while (it.hasNext()) {
            Entry entry = (Entry)it.next();
            entry.printList(prefix + "/" + name);
        }
    }
}

public class FileTreatmentException extends RuntimeException {
    public FileTreatmentException() {
    }
    public FileTreatmentException(String msg) {
        super(msg);
    }
}

```

-	entry는 File의 인스턴스일지도 모르고 Directory의 인스턴스일지도 모른다. 두 경우 모두 동일한 메소드 getSize로 크기를 얻을 수 있다. 이것이 Composite 패턴의 특징인 '그릇과 내용물을 동일시'를 나타낸다.
-	Composite 패턴의 재귀적 구조가 그대로 getSize라는 메소드의 재귀적 호출에 대응하고 있다. Directory 클래스의 인스턴스인지, File 클래스의 인스턴스인지 조사할 필요없이 `directory.add(entry)` 로 필드에 추가된다.
