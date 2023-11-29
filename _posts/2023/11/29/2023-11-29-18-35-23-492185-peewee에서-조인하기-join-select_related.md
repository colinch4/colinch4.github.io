---
layout: post
title: "[python] Peewee에서 조인하기: join(), select_related()"
description: " "
date: 2023-11-29
tags: [python]
comments: true
share: true
---

Peewee는 Python에서 사용할 수 있는 가벼운 ORM(Object-Relational Mapping) 라이브러리입니다. Peewee를 사용하면 데이터베이스와 간단하게 상호 작용할 수 있습니다. 이번 글에서는 Peewee를 사용하여 데이터베이스 테이블 간의 조인을 수행하는 방법에 대해 알아보겠습니다. 조인은 둘 이상의 테이블을 연결하여 관련된 정보를 가져오는 작업입니다.

### `join()` 메서드

`join()` 메서드는 Peewee에서 가장 기본적인 조인 방법입니다. 이 메서드를 사용하여 두 개의 테이블을 조인할 수 있습니다. 다음은 `join()` 메서드를 사용하여 `Author`와 `Book` 테이블을 조인하는 예제입니다.

```python
from peewee import *

db = SqliteDatabase('my_database.db')

class Author(Model):
    name = CharField()

    class Meta:
        database = db

class Book(Model):
    title = CharField()
    author = ForeignKeyField(Author, backref='books')

    class Meta:
        database = db

# 조인 예제
query = (Book
         .select(Book, Author)
         .join(Author)
         .where(Author.name == 'John Doe'))

for book, author in query:
    print(f'Book: {book.title}, Author: {author.name}')
```

위 코드에서 `select()` 메서드로 `Book`과 `Author` 테이블을 선택하고, `join()` 메서드로 `Author`와 조인합니다. 마지막으로 `where()` 메서드로 `Author`의 이름이 'John Doe'인 경우를 필터링합니다. 반복문을 통해 각 결과를 출력할 수 있습니다.

### `select_related()` 메서드

`select_related()` 메서드는 SQL의 INNER JOIN과 유사한 동작을 하는 Peewee의 메서드입니다. 이 메서드는 조인된 테이블의 데이터를 한 번의 쿼리로 한꺼번에 가져올 수 있기 때문에 성능 최적화에 도움이 됩니다. `select_related()` 메서드를 사용한 예제를 살펴보겠습니다.

```python
# 조인 예제 (select_related())
query = (Book
         .select()
         .select_related(Author)
         .where(Author.name == 'John Doe'))

for book in query:
    print(f'Book: {book.title}, Author: {book.author.name}')
```

`select_related()` 메서드를 사용하여 `Author` 테이블과 `Book` 테이블을 조인합니다. 그리고 `where()` 메서드로 `Author`의 이름이 'John Doe'인 경우를 필터링합니다. 반복문을 통해 각 결과의 책 제목과 저자 이름을 출력합니다.

### 마무리

Peewee를 사용하면 간단하게 데이터베이스 테이블을 조인할 수 있습니다. `join()` 메서드와 `select_related()` 메서드를 사용하여 조인 작업을 수행할 수 있습니다. 이로써 데이터베이스의 관련된 정보를 효율적으로 가져올 수 있습니다.

참고: [Peewee 공식 문서](http://docs.peewee-orm.com/en/latest/)