---
layout: post
title: "[go] Go 언어를 사용하여 AWS Elastic Load Balancer에 인스턴스 추가하기"
description: " "
date: 2023-12-18
tags: [go]
comments: true
share: true
---

AWS Elastic Load Balancer(ELB)를 사용하면 인스턴스 간에 트래픽을 분산시키고 높은 가용성을 제공할 수 있습니다. 이 가이드에서는 Go 언어를 사용하여 AWS SDK를 이용하여 ELB에 인스턴스를 추가하는 방법을 살펴보겠습니다.

## 사전 요구 사항

1. AWS 계정
2. AWS CLI 설치
3. Go 언어 설치
4. AWS SDK for Go 설치

## AWS SDK for Go 설치

```shell
go get -u github.com/aws/aws-sdk-go
```

## Go를 사용하여 ELB에 인스턴스 추가하기

다음은 Go를 사용하여 ELB에 인스턴스를 추가하는 간단한 예제 코드입니다.

```go
package main

import (
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/elb"
)

func main() {
	sess := session.Must(session.NewSessionWithOptions(session.Options{
		SharedConfigState: session.SharedConfigEnable,
	}))

	svc := elb.New(sess)

	params := &elb.RegisterInstancesWithLoadBalancerInput{
		Instances: []*elb.Instance{
			{
				InstanceId: aws.String("instance-id-1"),
			},
			{
				InstanceId: aws.String("instance-id-2"),
			},
		},
		LoadBalancerName: aws.String("your-load-balancer-name"),
	}

	resp, err := svc.RegisterInstancesWithLoadBalancer(params)

	if err != nil {
		panic(err)
	}

	// 등록 결과 출력
	fmt.Println(resp)
}
```

이 코드는 AWS SDK for Go를 사용하여 지정된 ELB에 인스턴스를 등록하는 과정을 보여줍니다. 먼저 AWS 세션을 만들고 ELB 서비스를 설정한 다음, `RegisterInstancesWithLoadBalancer` 메서드를 사용하여 인스턴스를 등록합니다.

이제 위의 예제 코드를 통해 Go를 사용하여 AWS Elastic Load Balancer에 인스턴스를 추가하는 방법을 배웠습니다.

## 참고 자료
- [AWS SDK for Go 공식 문서](https://docs.aws.amazon.com/sdk-for-go/v1/api/)
- [Go 언어 공식 웹사이트](https://golang.org/)