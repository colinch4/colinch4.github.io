---
layout: post
title: "[리눅스] 리눅스에서의 incremental backup과 full backup"
description: " "
date: 2023-12-20
tags: [리눅스]
comments: true
share: true
---

리눅스 시스템에서 중요한 데이터를 보호하는 가장 좋은 방법은 정기적으로 백업을 하는 것입니다. 백업은 데이터 손실 시 복구할 수 있는 중요한 보안 절차입니다. 리눅스에서는 incremental backup과 full backup이라는 두 가지 주요 백업 유형을 사용할 수 있습니다. 이 글에서는 incremental backup과 full backup의 개념과 차이점에 대해 알아보겠습니다.

## 1. Full Backup

**풀 백업(Full Backup)**은 데이터를 처음부터 끝까지 모두 복사하는 방식입니다. 일반적으로 시스템의 모든 데이터를 백업하므로 복구 과정은 간단하지만, 백업하는 데 걸리는 시간과 저장 공간이 많이 필요합니다. 주로 정기적으로 시스템 상태가 안정한 경우나, 큰 변화가 발생하지 않는 경우에 사용됩니다.

```bash
$ tar -cvzf full_backup.tar.gz /path/to/backup
```

## 2. Incremental Backup

**증분 백업(Incremental Backup)**은 이전 백업 이후 변경된 데이터만을 백업하는 방식입니다. 따라서 백업하는 데 걸리는 시간과 저장 공간을 절약할 수 있지만, 데이터를 복구하기 위해서는 백업된 모든 증분 백업 파일이 필요합니다.

```bash
$ rsync -av --link-dest=../prev_backup /path/to/source /path/to/incremental_backup
```

## 3. Full Backup과 Incremental Backup의 차이

| 구분                | Full Backup                                    | Incremental Backup                                      |
|---------------------|------------------------------------------------|----------------------------------------------------------|
| 백업 시간 및 저장 공간  | 많은 시간과 저장 공간이 필요                       | 적은 시간과 저장 공간이 필요                             |
| 복구 시간 및 과정      | 빠름                                             | 모든 증분 백업 파일이 필요                               |
| 백업 빈도             | 자주 발생하지 않는 데이터의 변화에 적합              | 정기적으로 변하는 데이터에 적합                            |

## 마치며

데이터를 안전하게 보관하려면 적합한 백업 전략을 수립하는 것이 매우 중요합니다. Full Backup과 Incremental Backup은 각각 장단점이 있으며 상황에 따라 적합한 방식을 선택해야 합니다. 시스템의 안정성, 변동성, 저장 공간 등을 고려하여 적절한 백업 전략을 수립하고 실제로 운영 중인 시스템에 적용해야 합니다.

관련 자료: [Incremental Backup using rsync](https://linux.die.net/man/1/rsync), [Full Backup using tar](https://www.gnu.org/software/tar/manual/html_node/Incremental-Dumps.html)