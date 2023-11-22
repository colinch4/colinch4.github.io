---
layout: post
title: "[AWS] AWS CHEAT SHEET"
description: " "
date: 2021-11-19
tags: [aws]
comments: true
share: true
---

## AWS CHEAT SHEET
> Reference : [AWS CLI](#https://docs.aws.amazon.com/cli/latest/index.html)

### Table of Contents
* [Athena](#athena)  
  Partition Projections
    * [DROP](#drop)
      * [Drop Table](#drop-table)
    * [SHOW](#show)
      * [Show Create Table](#show-create-table)
      * [Show Partitions](#show-partitions)
    * [REPAIR](#repair)  

  CLI Commands  
  * LIST  
    * [List Data Catalogs](#list-data-catalogs)
    * [List Database](#list-database)
    * [List Table Metadata](#list-table-metadata)
    * [List Query Execution](#list-query-execution)
  * GET  
    * [Get Query Results](#get-query-results)

* [S3](#s3)  
  CLI Commands
  * LIST
    * [List Buckets](#list-buckets)
    * [List Objects](#list-objects)
  * GET
    * [Get Bucket Location](#get-bucket-location)
  * [REMOVE](#remove)
    * [Remove Multiple Files](#remove-multiple-files)


## Athena
<details>
  <summary>Partition Projections</summary>

### DROP
#### Drop Table
```sql
ALTER TABLE  <tableName>
DROP IF EXISTS PARTITION(year='yyyy', month='MM', day='dd')
```

### SHOW
#### Show Create Table
```sql
SHOW CREATE TABLE <tableName>
```
👉🏻 This shows table, and configuration info.

#### Show Partitions
```sql
SHOW PARTITIONS <tableName>
```
👉🏻 This shows whole partitioned data.

[↑ return to TOC](#table-of-contents)

#### REPAIR
##### Repair Manually
If your data looks like this,   
`s3://bucketName/path/distributionID/yyyy/MM/dd/hh`   
than
```sql
ALTER TABLE <db>.<bucketName>
ADD PARTITION (year='yyyy',month='MM', day='dd') 
LOCATION 's3://bucketName/path/distributionID/yyyy/MM/dd/hh'
```
```sql
## example code
ALTER TABLE default.cloudfront-test
ADD PARTITION (year='2020',month='10', day='05') 
LOCATION 's3://cloudfront-test/logs/abcdeabcded/2020/10/05/00'
```

##### Repair Automatically
If your data looks like this,
`s3://bucketName/path/distributionID/year=2020/month=10/day=05/hour=00`  
than
```sql
MSCK REPAIR TABLE <tableName>;
```

[↑ return to TOC](#table-of-contents)

</details>

<details>
  <summary>CLI Commands</summary>

### LIST  
#### List Data Catalogs
`aws athena --list-data-catalogs`  
> example of output:
```  
{
  "DataCatalogsSummary": [
      {
          "CatalogName": "AwsDataCatalog",
          "Type": "GLUE"
      }
  ]
}
```
**DataCatalogsSummary** ⇒ A summary list of data catalogs  
**CatalogName** ⇒ The name of the data catalog  
**Type** ⇒ The data catalog type.

[↑ return to TOC](#table-of-contents)

#### List Database
`aws athena list-databases --catalog-name <catalogName>`  
* NOTE : Case-insensitive
> example : `aws athena list-databases --catalog-name AwsDataCatalog`  
```{
    "DatabaseList": [
        {
            "Name": "local",
            "Description": "Database for Local Shop"
        },
        {
            "Name": "global",
            "Description": "Database for Outside of USA Shop",
            "Parameters": {
                "CreatedBy": "Athena",
                "EXTERNAL": "TRUE"
            }
        }
    ]
}
```

[↑ return to TOC](#table-of-contents)

#### List Table Metadata
`aws athena list-table-metadata --catalog-name <catalogName> --database-name <databaseName>`

* w/ **--max-items** option  
`aws athena list-table-metadata --catalog-name <catalogName> --database-name <databaseName> --max-items <totalNumber>`  
> example of : `aws athena list-table-metadata --catalog-name AwsDataCatalog --database-name geography --max-items 2`
```
{
    "TableMetadataList": [
        {
            "Name": "country_codes",
            "CreateTime": 1586553454.0,
            "TableType": "EXTERNAL_TABLE",
            "Columns": [
                {
                    "Name": "country",
                    "Type": "string",
                    "Comment": "geo id"
                },
                {
                    "Name": "alpha-2 code",
                    "Type": "string",
                    "Comment": "geo id2"
                },
                {
                    "Name": "alpha-3 code",
                    "Type": "string",
                    "Comment": "state name"
                },
                {
                    "Name": "numeric code",
                    "Type": "bigint",
                    "Comment": ""
                },
                {
                    "Name": "latitude",
                    "Type": "bigint",
                    "Comment": "location (latitude)"
                },
                {
                    "Name": "longitude",
                    "Type": "bigint",
                    "Comment": "location (longitude)"
                }
            ],
            "Parameters": {
                "areColumnsQuoted": "false",
                "classification": "csv",
                "columnsOrdered": "true",
                "delimiter": ",",
                "has_encrypted_data": "false",
                "inputformat": "org.apache.hadoop.mapred.TextInputFormat",
                "location": "s3://awsdoc-example-bucket/csv/countrycode",
                "outputformat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
                "serde.param.field.delim": ",",
                "serde.serialization.lib": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe",
                "skip.header.line.count": "1",
                "typeOfData": "file"
            }
        },
        {
            "Name": "county_populations",
            "CreateTime": 1586553446.0,
            "TableType": "EXTERNAL_TABLE",
            "Columns": [
                {
                    "Name": "id",
                    "Type": "string",
                    "Comment": "geo id"
                },
                {
                    "Name": "country",

                    "Name": "id2",
                    "Type": "string",
                    "Comment": "geo id2"
                },
                {
                    "Name": "county",
                    "Type": "string",
                    "Comment": "county name"
                },
                {
                    "Name": "state",
                    "Type": "string",
                    "Comment": "state name"
                },
                {
                    "Name": "population estimate 2018",
                    "Type": "string",
                    "Comment": ""
                }
            ],
            "Parameters": {
                "areColumnsQuoted": "false",
                "classification": "csv",
                "columnsOrdered": "true",
                "delimiter": ",",
                "has_encrypted_data": "false",
                "inputformat": "org.apache.hadoop.mapred.TextInputFormat",
                "location": "s3://awsdoc-example-bucket/csv/CountyPopulation",
                "outputformat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
                "serde.param.field.delim": ",",
                "serde.serialization.lib": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe",
                "skip.header.line.count": "1",
                "typeOfData": "file"
            }
        }
    ],
    "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ=="
}
```

[↑ return to TOC](#table-of-contents)

#### List Query Execution  
`aws athena list-query-executions`  
```
{
    "QueryExecutionIds": [
        "XXXXXXXX-1a00-XXXX-a348-XXXXXXXXXXXX",
        "XXXXXXXX-6f9c-XXXX-b0b6-XXXXXXXXXXXX",
        "XXXXXXXX-2942-XXXX-82d1-XXXXXXXXXXXX",
        "XXXXXXXX-f2e0-XXXX-8670-XXXXXXXXXXXX",
        "XXXXXXXX-e6f4-XXXX-9f41-XXXXXXXXXXXX",
        .
        .
        .
   ]
}
```
**QueryExecutionIds** ⇒ The unique IDs of each query execution.

* w/ **--max-items** option  
`aws athena list-query-executions --max-items <totalNumber>`

> example : `aws athena list-query-executions --max-items 3`
```
{
    "QueryExecutionIds": [
        "XXXXXXXX-1a00-XXXX-a348-XXXXXXXXXXXX",
        "XXXXXXXX-6f9c-XXXX-b0b6-XXXXXXXXXXXX",
        "XXXXXXXX-2942-XXXX-82d1-XXXXXXXXXXXX",
   ]
   “NextToken”: “eyJOZXXXXXXXXXXXXXfQ==”
}
```
**NextToken** ⇒ A token to be used by the next reuqest if this request is truncacted.


[↑ return to TOC](#table-of-contents)

### GET  

#### Get Query Results  
`aws athena get-query-execution --query-execution-id <executionID>`
> example : `aws athena-get-query-exectution --query-execution-id XXXXXXXX-1a00-XXXX-a348-XXXXXXXXXXXX`  
```

{
    "QueryExecution": {
        "QueryExecutionId": "XXXXXXXX-1a00-XXXX-a348-XXXXXXXXXXXX",
        "Query": "SELECT *\nFROM local.bluebottle\nWHERE dt=\"date\"('2020-10-15')",
        "StatementType": "DML",
        "ResultConfiguration": {
            "OutputLocation": "s3://bluebottle/shop/2020/10/15/XXXXXXXX-1a00-XXXX-a348-XXXXXXXXXXXX.csv"
        },
        "QueryExecutionContext": {},
        "Status": {
            "State": "SUCCEEDED",
            "SubmissionDateTime": "2020-10-16T14:13:10.355000+09:00",
            "CompletionDateTime": "2020-10-16T14:13:40.378000+09:00"
        },
        "Statistics": {
            "EngineExecutionTimeInMillis": 29787,
            "DataScannedInBytes": 216541413,
            "TotalExecutionTimeInMillis": 30023,
            "QueryQueueTimeInMillis": 154,
            "QueryPlanningTimeInMillis": 728,
            "ServiceProcessingTimeInMillis": 82
        },
        "WorkGroup": "primary"
    }
}

```

[↑ return to TOC](#table-of-contents)


</details>

## S3
<details>
  <summary>CLI Commands</summary>

### LIST
#### List Buckets
`aws s3 ls <bucketName>`   
> example : `aws s3 ls bluebottle`
```
2020-10-05 17:08:50 mybucketA
2020-10-06 14:55:44 mybucketB
```

* w/ **--profile** option  
`aws --profile <profileName> s3 ls <bucketName>`

* w/ **--human-readable** option  
  `aws s3 ls s3://bucketName/path --human-readable`   
  Displays the size of the obejcts in human readable format.

* w/ **--recursive** option  
`aws s3 ls s3://bucketName --recursive`  
  Displays all files include sub-directories.  
  > example : `aws s3 ls s3://bluebottle --recursive` 
  ```
  2020-09-24 12:45:12  1364 path/2020/10/09/abcd.metadata
  ```

  1. **First column** : timestamp
  1. **Second column** : object size
  1. **Third column** : object name

`aws s3api list-buckets`
> example of output : 
```
{
    "Buckets": [
        {
            "Name": "mybucketA"
            "CreationDate": "2020-10-05T17:08:50.000Z",
        },
        {
            "Name": "mybucketB"
            "CreationDate": "2020-10-06T14:55:44.000Z",
        },
        {
          "Name": "mybucketC"
          "CreationDate": "2020-01-01T23:32:05+00:00",
        },
    ],
    "Owner": {
        "DisplayName": "userName",
        "ID": "userID"
    },
}
```
👉🏻 &nbsp;Buckets are returned in alphabetical order.


[↑ return to TOC](#table-of-contents)


#### List Objects
`aws s3 ls s3://<buckentName>/<path>/`  
> example : `aws s3 ls s3://bluebottle/shop/`  
```
      PRE 2002/
      PRE 2003/
      PRE 2004/
      PRE 2005/
      PRE 2006/
      PRE 2007/
      PRE 2008/
      PRE 2009/
      PRE 2010/
      PRE 2011/
      PRE 2012/
      PRE 2013/
      PRE 2014/
      PRE 2015/
      PRE 2016/
      PRE 2017/
      PRE 2018/
      PRE 2019/
      PRE 2020/
```
> **PRE** stands for **Pre**fix of ann S3 object.

* w/ **--profile** option  
`aws --profile <profileName> s3 ls <bucketName>`  


`aws s3api list-objects --bucket <bucketName>`  

* w/ **--max-items** option  
`aws s3api list-objects --bucket <bucketName> --max-items <totalNumber>`  
The total number of items to return.


### GET
#### Get Bucket Location
`aws s3api get-bucket-location --bucket <bucketName>`  
* w/ **--profile** option  
`aws --profile <profileName> s3api get-bucket-location --bucket <bucketName>`  


### REMOVE
#### Remove Multiple Files
Remove multiple files by `--exclude` and `--include` arguments   
`aws s3 rm s3://bucketName/path --recursive --exclude "*" --include "pattern*"`

```
## example code
aws s3 rm s3://cloudfront-test/logs --recursive --exclude "*" --include "abcdefghijklmnopqr/2020/10/04/*"
```

* **Results**      
![remove-multiple-objects](https://user-images.githubusercontent.com/48475824/95204315-e8a37680-081e-11eb-8361-873b5a800fa7.png)



[↑ return to TOC](#table-of-contents)

</detail>
