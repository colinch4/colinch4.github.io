---
layout: post
title: "[sql] 샤딩된 데이터베이스의 복제 방법 (Replication in Sharded Databases)"
description: " "
date: 2023-12-12
tags: [sql]
comments: true
share: true
---

샤딩은 대량의 데이터를 여러 개의 데이터베이스로 분할하여 저장하는 데이터베이스 아키텍처입니다. 이러한 환경에서 복제를 구성하는 방법에 대해 알아봅시다.

## 샤딩된 데이터베이스 복제 개요

일반적으로, 샤딩된 데이터베이스에서 복제는 각각의 샤드(데이터베이스 파티션)에 대해 별도로 구성됩니다. 이를 통해 데이터베이스 복제가 분산되어 안정성과 가용성을 향상시킬 수 있습니다. 

## MySQL을 이용한 샤딩된 데이터베이스의 복제

MySQL에서는 복제를 구성하기 위해 주로 `Master-Slave` 또는 `Master-Master` 설정을 사용합니다. 샤딩된 환경에서는 각 샤드에 대해 해당 구성을 개별적으로 구현해야 합니다. 각 샤드는 독립적인 복제 구성을 갖게 되며, 이를 통해 샤딩된 데이터베이스 전체의 안정성을 보장할 수 있습니다.

```sql
-- 샤드 1의 Master-Slave 복제 설정
CHANGE MASTER TO MASTER_HOST='<master_host>', MASTER_USER='<repl_user>', MASTER_PASSWORD='<repl_password>', MASTER_AUTO_POSITION=1;
START SLAVE;

-- 샤드 2의 Master-Slave 복제 설정
CHANGE MASTER TO MASTER_HOST='<master_host>', MASTER_USER='<repl_user>', MASTER_PASSWORD='<repl_password>', MASTER_AUTO_POSITION=1;
START SLAVE;
```

## MongoDB를 이용한 샤딩된 데이터베이스의 복제

MongoDB에서는 `Sharded Cluster` 환경에서 복제를 구성할 수 있습니다. 각 샤드는 일반적으로 복제 세트로 구성되며, 복제 세트 구성원으로는 Primary와 Secondary가 포함됩니다.

```javascript
// 샤드 1의 복제 세트 구성
rs.initiate();
rs.add('<secondary1_host>');
rs.add('<secondary2_host>');

// 샤드 2의 복제 세트 구성
rs.initiate();
rs.add('<secondary1_host>');
rs.add('<secondary2_host>');
```

## 소결

샤딩된 데이터베이스의 복제는 각 샤드별로 별도로 구성되어야 하며, 주로 각 샤드를 독립적인 복제 환경으로 구축함으로써 안정성과 가용성을 동시에 보장할 수 있습니다.

이상으로 샤딩된 데이터베이스에서의 복제 방법에 대해 알아보았습니다.

자세한 내용은 아래 참고 자료를 확인해주세요.

## 참고 자료
- MySQL 공식 문서: [MySQL Replication](https://dev.mysql.com/doc/refman/8.0/en/replication.html)
- MongoDB 공식 문서: [Replication](https://docs.mongodb.com/manual/replication/)
- 조재훈, 오인천, «빅데이터 분석을 위한 NoSQL», 제이펍, 2016