---
layout: post
title: "[Go] Package gorm"
description: " "
date: 2021-11-19
tags: [go]
comments: true
share: true
---

## Package gorm
gorm 은 Go의 ORM 라이브러리이다.

### Table of Contents
* Install gorm
* Import gorm
* gorm Basic
   * [gorm.Model](#gorm.Model)
   * [Table Name](#table-name)
   * [Column Name](#column-name)
   * [Timestamp Tracking](#timestamp-tracking)
      * CreatedAt
      * UpdatedAt
      * DeletedAt
   * [Delete](#delete)
      * Batch Delete
      * Soft Delete
      * Hard Delete

* gorm 코드 열어보기
    * [gorm DB 구조체](#gorm의-구조체)
    * [gorm.Debug](#gormDebug)
    * [gorm.clone](#gormclone)
    * [gorm.LogMode](#gormLogMode)
    * [gorm.AutoMigrate](#gormAutoMigrate)
    * [gorm.Open](#gormOpen)



## Install gorm
gorm 패키지 받기  

이전 경로인 ```jinzhu/gorm``` 에서 
```go
go get github.com/jinzhu/gorm 
```

아래의 경로로 변경되었다. ```go-gorm```
```go
go get github.com/go-gorm
```

현재(08.03.2020) 두개의 path 모두 사용 가능. 


## Import gorm
Import gorm package  
```go
import (
    "gorm.io/gorm"
)
```



## gorm Basic
### gorm.Model
gorm.Model 은 기본 구조체이다.   
gorm.Model 이 갖고 있는 필드는 아래와 같다.  
* ID
* CreatedAt
* UpdatedAt
* DeletedAt

```go
type Model struct {
    ID        uint 
    CreatedAt time.Time
    UpdatedAt time.Time
    DeletedAt *time.Time
}
```
gorm 은 ID 이름을 가진 필드를 Primary Key로 인식한다. 직접 ID 를 PK로 지정해 주지 않아도 자동으로 Primary Key 로 설정된다.

**Primary Key 를 직접 정해주는 법**  
<code>"primary_key"</code> 를 통해 원하는 필드를 PK 로 지정해 줄 수 있다.

```go
type Room struct {
	RoomID      int64    `gorm:"primary_key"`
	Name        string   `json:"name"`
	Open        bool     `json:"open"`
}
```

### Table Name
Table Name 은 구조체명의 복수형으로 자동으로 명명된다.  
* 예를들어 <code>Room</code> 이라는 구조체의 테이블 이름은 <code>rooms</code> 가 된다.  

또한 테이블명은 소문자로만 이루어진다.

**Table Name 직접 지정해주기**  
만약 gorm 에서 지정해주는 이름이 아닌 개별적으로 이름을 짓고 싶다면, <code>TableName()</code> 을 통해 세팅할 수 있다.  
```go
func (User) TableName() string {
 return "profiles"
}
```

**Table Name 단수형으로 세팅하기**  
만약 복수가 아닌 단수로 테이블 이름을 정하고 싶다면, <code>SingularTable(true)</code> 사용.
```go
db.SingularTable(true)
```

**Default Table Name 직접 지정해주기**  
Default Table Name 을 원하는 이름으로 세팅하기 위해 <code>DefaultTableNameHandler</code> 를 사용.  
```go
gorm.DefaultTableNameHandler = func (db *gorm.DB, defaultTableName string) string  {
 return "prefix_" + defaultTableName;
}
```

### Column Name
Column 이름은 필드의 이름으로 자동 설정된다.  
소문자 snake case 의 이름을 가진다.  
```go
type User struct {
   ID        uint32   	
   Nickname  string    
   Email     string    
   Password  string    
   CreatedAt time.Time 
   UpdatedAt time.Time
}
```
* ID →id
* Nickname →nickname
* Email → email
* Password → password
* CreatedAt → created_at
* UpdatedAt → updated_at

#### Column Name Customization
직접 Column Name 을 커스터마이징 하고자 한다면 column 이라는 태그를 사용한다.
소문자 snake case 기준으로 명명해준다.
```go
type Falcon9 struct{
    ID            string   `gorm:"column:fid"
    Diameter      float32  
    Mass          int64
    PayloadToLEO  int64    `gorm:"column:payload_leo"
    PayloadToGTO  int64    `gorm:"column:payload_gto"
    PayloadToMars int64    `gorm:"column:payload_mars"
}
```


### Timestamp Tracking
**CreatedAt**  
Record의 생성 시각의 정보를 지니게 된다.  
```go
db.Create(&user) // 생성된 당시의 시각이 기록된다.
```

**UpdatedAt**  
Record가 업데이트가 된 시점의 시간 정보를 지니게 된다.
```go
db.Save(&user) // 저장되어 업데이트 된 시각이 기록된다.
```

**DeletedAt**  
Gorm은 데이터를 hard delete 하지 않고 soft delete으로 처리한다.


### Delete
**Batch Delete**  
```go
db.Where("age = ?", 44).Delete(&User{})
```
* 44살의 나이를 지닌 모든 유저 정보 지우기.

**Soft Delete**  
Soft Delete 은 Gorm 의 기본 설정이다.  
모델이 <code>DeletedAt</code> 라는 필드를 갖고 있다면 해당 필드는 Soft delete 이 적용된다.  
Delete 라는 인스턴스가 호출이 됐을 때 해당 필드의 시간 정보가 업데이트 된다.  
```go
db.Delete(&user)
```
* user의 정보가 지워지면서 지워지는 시각이 <code>DeletedAt</code> 에 기록되게 된다.

**Hard Delete**  
만약 영구히 지우고자 한다면 <code>Unscoped</code>를 사용하자.  
```go
db.Unscoped().Delete(&order) 
```

[Return to TOC](#table-of-contents)


## gorm 코드 열어보기
### gorm의 구조체
연결시킨 DB의 정보를 갖고있다.  
   ```go
    type DB struct {
        sync.RWMutex
        Value        interface{}
        Error        error
        RowsAffected int64

        // single db
        db                SQLCommon
        blockGlobalUpdate bool
        logMode           logModeValue
        logger            logger
        search            *search
        values            sync.Map

        // global db
        parent        *DB
        callbacks     *Callback
        dialect       Dialect
        singularTable bool

        // function to be used to override the creating of a new timestamp
        nowFuncOverride func() time.Time
    }
   ```

### gorm.Debug()
```go
func (s *DB) Debug() *DB { return s.clone().LogMode(true) }
```
* debug mode를 실행시킨다.
* Log 가 detail 하게 출력된다.

### gorm.clone()
```go
func (s *DB) clone() *DB
```
* clone()은 DB 구조체의 private method 이다.

### gorm.LogMode()
```go
func (s *DB) LogMode(enable bool) *DB {
  if enable {
     s.logMode = detailedLogMode
  } else {
     s.logMode = noLogMode
  }
  return s
}
```
* LogMode 는 DB의 메서드
* log mode 를 설정해준다.
    * true 값 일시  
    detailed log를 표시
    * false 값 일시  
    no log
    * default 값 일시  
    error logs만 프린트

### gorm.AutoMigrate()
```go
func (s *DB) AutoMigrate(values ...interface{}) *DB {
  db := s.Unscoped()
  for _, value := range values {
     db = db.NewScope(value).autoMigrate().db
  }
  return db
}
```
* given mode로 auto migration을 실행한다.
* Missing fields 만 add 시킨다.
* Current data 삭제하거나 변경하진 않는다.

### gorm.Open()
```go
func Open(dialect string, args ...interface{}) (db *DB, err error) {
  if len(args) == 0 {
     err = errors.New("invalid database source")
     return nil, err
  }
  var source string
  var dbSQL SQLCommon
  var ownDbSQL bool

  switch value := args[0].(type) {
  case string:
     var driver = dialect
     if len(args) == 1 {
        source = value
     } else if len(args) >= 2 {
        driver = value
        source = args[1].(string)
     }
     dbSQL, err = sql.Open(driver, source)
     ownDbSQL = true
  case SQLCommon:
     dbSQL = value
     ownDbSQL = false
  default:
     return nil, fmt.Errorf("invalid database source: %v is not a valid type", value)
  }

  db = &DB{
     db:        dbSQL,
     logger:    defaultLogger,
     callbacks: DefaultCallback,
     dialect:   newDialect(dialect, dbSQL),
  }
  db.parent = db
  if err != nil {
     return
  }
  // Send a ping to make sure the database connection is alive.
  if d, ok := dbSQL.(*sql.DB); ok {
     if err = d.Ping(); err != nil && ownDbSQL {
        d.Close()
     }
  }
  return
}

```
* 새로운 DB 연결 초기화
* driver가 첫번째로 임포트 되야 함.
    ```go
    // example
    s.DB, err = gorm.Open(DbDriver, DBURL)
    ```

[Return to TOC](#table-of-contents)
