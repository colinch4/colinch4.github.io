---
layout: post
title: "[typescript] 타입스크립트와 AWS CloudFormation StackSets를 사용하여 여러 AWS 계정에 걸친 인프라 관리"
description: " "
date: 2023-12-12
tags: [typescript]
comments: true
share: true
---

AWS CloudFormation은 인프라스트럭처를 관리하고 자동화하기 위한 서비스로, AWS CloudFormation StackSets을 사용하면 여러 AWS 계정에 동일한 리소스나 설정을 손쉽게 배포할 수 있습니다. 이때 TypeScript를 사용하면 코드를 더 안전하게 유지할 수 있으며, 타입스크립트의 강력한 타입 시스템을 활용하여 AWS 인프라스트럭처에 대한 보다 안정적인 동작을 보장할 수 있습니다.

## 1. 타입스크립트를 사용하여 AWS CloudFormation 스택 구성

먼저, CloudFormation 스택을 정의하는 TypeScript 파일을 생성합니다. 다음은 TypeScript를 사용하여 EC2 인스턴스를 만드는 간단한 CloudFormation 스택의 예시입니다.

```typescript
import { Stack, StackProps, aws_ec2 as ec2 } from '@aws-cdk/core';

export class MyStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    new ec2.CfnInstance(this, 'MyInstance', {
      imageId: 'ami-0c55b159cbfafe1f0',
      instanceType: 't2.micro',
    });
  }
}
```

위 코드는 `@aws-cdk/core` 패키지를 사용하여 EC2 인스턴스를 생성하는 예시를 보여줍니다. 이를 통해 TypeScript로 CloudFormation 스택을 정의할 수 있습니다.

## 2. AWS CloudFormation StackSets 생성 및 배포

다음으로, AWS CloudFormation StackSets을 사용하여 여러 AWS 계정에 동일한 스택을 배포하는 방법을 알아봅시다. 아래 예시 코드는 TypeScript를 사용하여 StackSets을 생성하고 배포하는 방법을 보여줍니다.

```typescript
import { Stack, StackProps, aws_cloudformation as cfn } from '@aws-cdk/core';

export class MyStackSetsStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const stack = new MyStack(this, 'MyStack');
    const masterAccount = '123456789012'; // 마스터 계정 ID

    new cfn.CfnStackSet(this, 'MyStackSet', {
      stackSetName: 'my-stack-set',
      templateBody: stack.template,
      autoDeployment: {
        enabled: true,
        retainStacksOnAccountRemoval: false,
      },
      permissionModel: 'SERVICE_MANAGED',
    });

    new cfn.CfnStackInstances(this, 'MyStackInstances', {
      stackSetName: 'my-stack-set',
      regions: ['us-east-1', 'us-west-2'],
      deploymentTargets: {
        accounts: [masterAccount, '987654321098'], // 추가 계정 ID
        organizationalUnitIds: ['ou-1234abcd'], // 조직 단위 ID
      },
    });
  }
}
```

위 코드는 TypeScript를 사용하여 StackSets과 StackInstances를 생성하는 예시입니다. 이를 통해 TypeScript와 AWS CloudFormation을 활용하여 여러 AWS 계정에 걸친 인프라를 관리할 수 있습니다.

## 3. 결론

이를 통해 타입스크립트를 사용하여 AWS CloudFormation StackSets을 활용하여 여러 AWS 계정에 걸친 인프라 관리를 더욱 안전하고 효율적으로 할 수 있음을 알 수 있습니다. TypeScript의 강력한 타입 시스템을 활용하여 실수로 인한 오류를 방지하고, AWS 인프라스트럭처를 보다 안정적으로 관리할 수 있습니다.

이러한 방법을 통해 타입스크립트와 AWS CloudFormation을 결합하여 인프라 관리 작업을 간소화하고, 안정적으로 처리할 수 있습니다.

## 참고 자료
- AWS CDK 공식 문서: [https://docs.aws.amazon.com/cdk/api/latest/docs/aws-cloudformation-readme.html](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-cloudformation-readme.html)
- AWS CloudFormation StackSets 문서: [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)

**이하의 내용은 참고용이며 번역 또는 요약이 필요한 경우에만 사용하세요.**