---
layout: post
title: "[sql] 샤딩된 데이터베이스의 압축 및 압축 해제 (Compression and Decompression in Sharded Databases)"
description: " "
date: 2023-12-12
tags: [sql]
comments: true
share: true
---

샤딩된 데이터베이스에서는 대량의 데이터가 분산되어 저장되기 때문에 데이터 압축이 중요합니다. 압축된 데이터는 디스크 공간을 절약하고 입출력 성능을 향상시킬 수 있습니다. 그러나 샤딩된 데이터베이스에서 압축을 적용하고 관리하는 것은 몇 가지 주의해야 할 점이 있습니다.

## 압축의 장단점

### 장점
- 압축된 데이터는 디스크 공간을 절약할 수 있습니다.
- 디스크 입출력이 줄어들어 성능을 향상시킬 수 있습니다.
- 네트워크 대역폭을 절약할 수 있습니다.

### 단점
- 데이터를 압축하고 해제하는 데 추가적인 CPU 리소스가 필요합니다.

## 압축 방법

### 테이블 수준 압축
특정 테이블이나 분할된 테이블 그룹을 압축하는 것입니다. 이 방법은 개별적으로 테이블을 압축할 수 있기 때문에 유연성이 높지만, 압축된 데이터를 쿼리하는 과정에서 추가적인 오버헤드가 발생할 수 있습니다.

예시 코드:
```sql
ALTER TABLE sharded_table ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
```

### 파티션 수준 압축
테이블 파티션을 기반으로 압축하는 방법입니다. 이 방법은 파티션마다 압축 여부를 따로 설정할 수 있기 때문에 유용합니다. 그러나 파티션 간에 데이터를 이동하거나 병합하는 과정에서 추가적인 주의가 필요합니다.

예시 코드:
```sql
ALTER TABLE sharded_table PARTITION p0 ROW_FORMAT=COMPRESSED KEY_BLOCK_SIZE=8;
```

### 파일 수준 압축
데이터 파일을 기반으로 압축하는 방법입니다. 이 방법은 데이터 파일 전체를 압축하기 때문에 파편화된 데이터를 취급하는 샤딩된 환경에서는 유용하지 않을 수 있습니다.

## 압축 해제

압축된 데이터를 해제하는 것은 데이터를 쿼리하고 수정하는 과정에서 추가적인 CPU 리소스를 필요로 합니다. 따라서 데이터를 압축할 때는 압축 해제에 대한 오버헤드를 고려해야 합니다.

## 참고 자료
- MySQL 공식 문서: [MySQL Documentation - Compression](https://dev.mysql.com/doc/refman/8.0/en/innodb-compression.html)