---
layout: post
title: "[Database] Logical Storage Structure"
description: " "
date: 2021-11-19
tags: [sql]
comments: true
share: true
---


## Logical Storage Structure  
데이터베이스에 담긴 데이터가 어떻게 담겨있는지 논리적 구조에 대해 알아보자.

### Table of Contents

* [About Logical Storage Structure](#about-logical-storage-structure)  
* [Data Block](#data-block)
  * [Data Block & OS Block](#data-block-&-os-block)
* [Extent](#extent)
  * [Size Limit](#size-limit)
* [Segment](#segment)


## About Logical Storage Structure
DB속 데이터는 data file 에 저장된다. 그리고 데이터 파일들은 Table Space 라는 논리적 저장공간에 담겨있다.  

Oracle DB에서의 논리적 단위는 아래와 같이 네가지로 나뉜다.  
> `Tablespace` > `Segment` > `Extent` > `Data Block`  

![logical-structure](https://user-images.githubusercontent.com/48475824/120893010-ef9fb480-c64b-11eb-8974-1919e7e25b80.png)  
![Segment-Extent-Data_blocks](https://user-images.githubusercontent.com/48475824/120892671-66d44900-c64a-11eb-9955-e776f41394ed.png)
- `Tablespace` 는 `Segment`를 담는 컨테이너이다.  
- `Segment` 는 `Extent` 들로 구성되어 있으며 `Extent` 는 `Data block` 들의 모음이다.  

[↑ return to TOC](#table-of-contents)


## Data Block
> Data Block은 Page 또는 Oracle Block 이라고도 불린다.  

데이터는 실질적으로 data block(이하 블록)에 저장되어 있다. 즉, DBMS가 데이터를 읽고 쓰는(I/O) 단위는 블록 단위이다.  
- Index 또한 블록단위로 데이터를 다룬다.  

Oracle DB에서 블록의 크기는 보통 8KB 크기를 가진다. 이는, 단순히 하나의 컬럼처럼 작은 양의 데이터를 불러오려해도 8KB 크기의 블록을 모두 읽어와야한다는 것을 의미한다.  
- 제일 작은 크기의 블록은 `2KB` 이다.  

### Data Block & OS Block  
  ![data-block os-block](https://user-images.githubusercontent.com/48475824/122288724-e4426800-cf2c-11eb-94f3-1e070b9faf7d.png)  

-  **블록 사이즈 지정**  
  데이터 블록 사이즈는 `DB_BLOCK_SIZE` 파라미터를 통해 설정 한다.  
  사용자가 이를 직접 지정해주지 않았다면 OS가 제공해주는 기본 사이즈로 자동 지정된다. 이는 OS 마다 다르지만 보통 `4KB` 또는 `8KB` 로 설정되어 있다.  

[↑ return to TOC](#table-of-contents)

## Extent
`Extent` 는 데이터블록이 모여 만든 **저장공간** 으로 보면 된다.  

`Tablespace` 내부의 `Extent`를 관리하는 방법은 두 가지가 존재한다.  
사용자가 어떠한 방법을 선택했느냐에 따라 Oracle DB 는 Extent 를 달리 관리한다.

- **Dictionary Managed Tablespace**  
  과거 Oracle Version 8 까지 차용되던 방법으로써 데이터 딕셔너리(data dictionary)를 통해 Extent를 관리한다.  
  - I/O Bottleneck 의 문제로 인해 현재는 Locally Managed 방식이 사용된다.

- **Locally Managed Tablespace**   
  기본 세팅은 Locally Managed 로 되어 있다.  
  비트맵(bitmaps)을 이용해 Extent를 관리한다.  
  - **ASSM:** Automatic Segment Space Managment  
    ASSM 의 장점은 아래와 같다.  
    - 관리하기가 단순해짐  
      수동으로 관리할 필요가 없다.  
    - 동시성이 향상됨  
      다수의 transaction이 동시적으로 데이터 블록들을 검색할 수 있다.  
  - **MSSM:** Manual Segment Space Management  

### Size Limit 
`Extent`의 사이즈는 무한정으로 설정할수 없다. 한 개의 Object가 지닐 수 있는 `Extent`의 사이즈는 한계가 정해져 있으며, 이는 두 가지 타입으로 나뉜다.  

1. Soft Limit  
1. Hard Limit  

- **Recommended Block Size (KB)**  

  |soft Limit|Hard Limit|
  |:--:|:--:|
  |2|100|
  |4|200|
  |8|300|

[↑ return to TOC](#table-of-contents)

## Segment
- `Segment`에 데이터를 저장할 공간이 부족할 때에는 `Data Block` 단위가 아닌 `Extent` 단위로 공간을 확장한다.  
- 한개의 `Segment` 는 하나의 `Tablespace`에 대응된다. 이는 아래의 그림처럼 한개의 Segment가 여러 Tablespace 에 존재할 수 없다는 것을 의미한다.  

  ![1-1 segment-tablespace](https://user-images.githubusercontent.com/48475824/122279739-5a41d180-cf23-11eb-9a7a-e7f23921a80a.png)

[↑ return to TOC](#table-of-contents)
