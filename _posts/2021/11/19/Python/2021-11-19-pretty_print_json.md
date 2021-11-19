---
layout: post
title: "[Python] Pretty Print JSON"
description: " "
date: 2021-11-19
tags: [Python]
comments: true
share: true
---

# Pretty Print JSON
python 이 깔려있다면 console 창에서 JSON 을 보기 좋은 형태로 print 할 수 있다.

Python Version 은 2.6 이상 이어야 한다.  

아래의 명령어를 입력하면 보기 좋은 형태로 바뀐다.
```bash
echo 'YourJSONHere' | python3 -m json.tool
```

## Example JSON
> [Code Reference from AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html)


### Before
```bash
{ "Resources" : { "HelloBucket" : { "Type" : "AWS::S3::Bucket", "Properties" : { "AccessControl" : "PublicRead", "WebsiteConfiguration" : { "IndexDocument" : "index.html", "ErrorDocument" : "error.html" } } } } }
```

### Input Pretty Print Command  
```bash
echo '{ "Resources" : { "HelloBucket" : { "Type" : "AWS::S3::Bucket", "Properties" : { "AccessControl" : "PublicRead", "WebsiteConfiguration" : { "IndexDocument" : "index.html", "ErrorDocument" : "error.html" } } } } }' | python3 -m json.tool
```

### After  
결과물은 아래와 같다.
```json
{
    "Resources": {
        "HelloBucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "AccessControl": "PublicRead",
                "WebsiteConfiguration": {
                    "IndexDocument": "index.html",
                    "ErrorDocument": "error.html"
                }
            }
        }
    }
}
```