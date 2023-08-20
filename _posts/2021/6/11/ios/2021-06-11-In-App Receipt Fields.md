---
layout: post
title: "[ios] In-App Receipt Fields"
description: " "
date: 2021-06-11
tags: [ios]
comments: true
share: true
---

## In-App Receipt Fields

## Quantity

: 구매한 item의 개수.

```markdown
ASN.1 Field Type: 1701
ASN.1 Field Value: INTEGER 
JSON Field Name: quantity
JSON Field Value: string, interpreted as an integer
```

: 이 값은 transaction의 payment 프로퍼티에 저장된 `SKPayment` 객체의 quantity 프로퍼티와 값이 일치한다.

## Product Identifier

: 구매한 아이템의 product identifier.

```markdown
ASN.1 Field Type: 1702
ASN.1 Field Value: UTF8String
JSON Field Name: product_id
JSON Field Value: string
```

: 이 값은 transaction의 payment 프로퍼티에 저장된 `SKPayment` 객체의 productIdentifier 프로퍼티와 값이 일치한다.

## Transaction Identifier

: The transaction identifier of the item that was purchased.

```markdown
ASN.1 Field Type: 1703
ASN.1 Field Value: UTF8String
JSON Field Name: transaction_id
JSON Field Value: string
```

:  이 값은 tranction의 transactionIdentifer 프로퍼티와 일치한다. 

: 이전의 transaction을 복구한 transaction의 경우에는, 이 값은 original purchase transaction 의 transaction identifier 와 값이 다르다. 자동 갱신 구독 영수증의 경우에는, transaction identifier 의 새 값이 구독이 새로 갱신되거나 새로운 디바이스에서 복원됐을 때 매번 생성(generated) 된다. 

## Original Transaction Identifier

: 이전 transaction을 복원하는 transaction의 경우, original transaction의 transaction identifier 입니다. 
그렇지 않으면, transaction identifier 와 동일합니다.

```markdown
ASN.1 Field Type: 1705 
ASN.1 Field Value: UTF8String
JSON Field Name: original_transaction_id
JSON Field Value: string
```

: 이 값은 original transaction의 `transactionIdentifier` property와 값이 동일합니다.

: 이 값은 **특정 구독에 대해 생성된 모든 영수증에 대해 동일**합니다. 이 값은 동일한 개별 고객의 구독에 대한 여러 iOS 6 스타일 transaction receipt를 함께 연결하는 데 유용합니다.

## Purchase Date

: 상품을 구매한 날짜와 시간

```markdown
ASN.1 Field Type: 1704 
ASN.1 Field Value: IA5String, interpreted as an RFC 3339 date
JSON Field Name: purchase_date
JSON Field Value: string, interpreted as an RFC 3339 date
```

: 이 값은 transaction의 `transactionDate` 프로퍼티의 값과 일치합니다.

: 이전 거래를 복원하는 거래의 경우, 구매 날짜는 original 구매 날짜와 동일합니다. `Original Purchase Date`를 사용하여 original 거래 날짜를 확인하십시오.

: 자동 갱신 구독 영수증에서 구매 날짜는 구독을 구매하거나 **갱신한** 날짜입니다 (소멸 여부에 관계없이). 현재 기간 만료일에 자동 갱신되는 경우 구매 일은 현재 기간의 종료일과 동일한 **다음 기간의 시작일**입니다.

## Original Purchase Date

: 이전 트랜잭션을 복원하는 트랜잭션의 경우, original 트랜잭션 날짜입니다.

```markdown
ASN.1 Field Type: 1706 
ASN.1 Field Value: IA5String, interpreted as an RFC 3339 date
JSON Field Name: original_purchase_date
JSON Field Value: IA5String, interpreted as an RFC 3339 date
```

: 이 값은 orignal transaction의 `transactionDate` 프로퍼티의 값과 일치합니다. 

: 자동 갱신 영수증에서, 이것은 구독 기간의 시작을 나타냅니다, 심지어 구독이 갱신되어도.

## Subscription Expiration Date

: 이 구독의 만료기간을 나타내는데, 1970, 00:00:00 GMT 1월 1일 이후로 밀리초단위로 표현된다.

```markdown
ASN.1 Field Type: 1708
ASN.1 Field Value: IA5String, interpreted as an RFC 3339 date 
JSON Field Name: expires_date
JSON Field Value: IA5String, interpreted as an RFC 3339 date
```

: 이 키는 오직 자동 갱신 영수증에서만 나타납니다. 구독이 갱신되거나 만료될 때 날짜를 식별하기 위해 이 값을 사용하세요, customer가 content나 service에 접근을 해도 되는지 결정할 때요. 최신 영수증을 확인한 후 최신 갱신 거래의 구독 만료 날짜가 지난 날짜인 경우 구독이 만료 된 것으로 간주하는 것이 안전합니다.

## Subscription Expiration Intent

: 만료된 구독의 경우, 구독 만료의 이유를 나타냄

```markdown
ASN.1 Field Type: (none) 
ASN.1 Field Value: (none)
JSON Field Name: expiration_intent
JSON Field Value: string, interpreted as an integer
```

"1" - 고객이 구독을 취소한 경우 
"2" -  청구 오류, 예를 들어, 고객의 payment가 더이상 유효하지 않는 경우

"3" - 고객이 최근의 가격 인상에 대해 동의하지 않는 경우

"4" - 구독 갱신하는 날에 상품을 사용 불가능할 때

"5" - unknown error

: 이 키는 만료된 자동 갱신 구독을 포함한 영수증에서만 나타납니다. 이 값을 고객들에게 재구독을 하도록 권유하는데 적절한 메시지를 보내는데 사용할 수 있습니다.

## Subscription Retry Flag

: 만료된 구독의 경우 Apple이 구독 자동 갱신을 시도하고 있는지 여부.

```markdown
ASN.1 Field Type: (none) 
ASN.1 Field Value: (none)
JSON Field Name: is_in_billing_retry_period
JSON Field Value: string, interpreted as an integer
```

"1" - App Store는 여전히 구독 갱신을 시도하고 있습니다.

"0" - App Store가 구독 갱신 시도를 중지했습니다.

: 이 키는 오직 자동 갱신 구독 영수증에서만 보입니다. App Store에서 거래를 완료 할 수 없어 고객의 구독 갱신에 실패한 경우, 이 값은 App Store가 구독 갱신을 시도하고 있는지 여부를 반영합니다.

## Subscription Trial Period

: 구독의 경우, 무료 trial 기간인지 아닌지 나타냅니다.

```markdown
ASN.1 Field Type: (none)  
ASN.1 Field Value: (none)
JSON Field Name: is_trial_period
JSON Field Value: string
```

: 이 키는 오직 자동 갱신 구독 영수증에만 보입니다. 이 키에 대한 value는 고객의 구독이 여전이 free trial 기간인 경우 true이고, 그렇지 않으면 false 입니다.

> 주의:  영수증의 이전 구독 기간이 `is_trial_period` 또는 `is_in_intro_offer_period` 키에 대해 "true"값을 갖는 경우 사용자는 해당 구독 그룹 내에서 **무료 평가판 또는 할인 가격을 받을 수 없습니다.**(왜냐하면 무료 시험판은 단 1번밖에 할 수 없기 때문이다.)

## Subscription Introductory Price Period

: 자동 갱신의 경우, 할인 가격인지 아닌지 나타냄

```markdown
ASN.1 Field Type: 1719 
ASN.1 Field Value: INTEGER
JSON Field Name: is_in_intro_offer_period
JSON Field Value: string 
```

: 이 키는 자동 갱신 구독 영수증에만 있습니다. 이 키의 값은 고객의 구독이 현재 할인 가격 기간에 있는 경우 "true"이고 그렇지 않은 경우 "false"입니다.

> 주의: 영수증의 이전 구독 기간이 `is_trial_period` 또는 `is_in_intro_offer_period` 키에 대해 "true"값을 갖는 경우, 사용자는 해당 구독 그룹 내에서 무료 평가판 또는 할인 가격을 받을 수 없습니다.

## Cancellation Date

: Apple 고객 지원에서 취소한 거래의 경우, 취소 시간 및 날짜를 나타냅니다. 업그레이드 된 자동 갱신 구독 플랜의 경우, 업그레이드된 거래 날짜와 시간을 나타냅니다.

```markdown
ASN.1 Field Type: 1712
ASN.1 Field Value: IA5String, interpreted as an RFC 3339 date
JSON Field Name: 
JSON Field Value: string, interpreted as an RFC 3339 date
```

: 취소된 영수증은 구매한 적이 없는 영수증인 것처럼 취급하십시오.

> 주의: 취소 된 인앱 구매는 영수증에 무기한 남아 있습니다. 비 소모성 제품(non-consumable), 자동 갱신 구독, 비 갱신 구독 또는 무료 구독에 대한 환불에 경우에만 취소 영수증이 무기한 남아 있습니다(소모성은 안 남는다는 거다).

## Cancellation Reason

: 취소된 transaction 된 경우에, 취소의 이유를 나타낸다.

: For a transaction that was canceled, the reason for cancellation.

```markdown
ASN.1 Field Type: (none)  
ASN.1 Field Value: (none)
JSON Field Name: cancellation_reason
JSON Field Value: string, interpreted as an Integer
```

"1":  우리 앱의 실제적인 또는 인지된 이슈 때문에 고객이 취소한 경우

"0": 거래가 다른 이유 때문에 취소된 경우. 예를 들어, 고객이 **실수로** 앱을 구입한 경우

## App Item ID

: App Store가 트랜잭션을 생성한 애플리케이션을 고유하게 식별하는 데 사용하는 문자열입니다.

```markdown
ASN.1 Field Type: (none) 
ASN.1 Field Value: (none)
JSON Field Name: app_item_id
JSON Field Value: string
```

: 만약 너의 서버가 여러개의 어플을 서포트할 때, 너는  그들 사이에 구별하기 위해 이 값을 사용하세요.

: 앱에는 프로덕션 환경에서만 식별자가 할당되므로, 테스트 환경에서 생성된 영수증에는 이 키가 없습니다.

: 이 필드는 Mac 앱에서는 나타나지 않는다. 

## External Version Identifier

: 애플리케이션의 revision을 고유하게 식별하는 임의의 숫자입니다.

```markdown
ASN.1 Field Type: (none)
ASN.1 Field Value: (none)
JSON Field Name: version_external_identifier
JSON Field Value: string
```

: 테스트 환경에서 생성된 영수증에는 이 키가 없습니다. 이 값을 사용하여 고객이 구매한 앱의 버전을 식별합니다.

## Web Order Line Item ID

: 구독 구매를 식별하기 위한 기본 키(primary key)입니다.

```markdown
ASN.1 Field Type: 1711
ASN.1 Field Value: INTEGER
JSON Field Name: web_order_line_item_id
JSON Field Value: string
```

: 이 값은 구독 갱신 구매 이벤트를 포함하여 여러 장치를 넘어 **구매 이벤트**를 식별하는 고유 ID입니다.

## Subscription Auto Renew Status

: 자동 갱신 구독에 대해서 현재의 갱신 상태
The current renewal status for the auto-renewable subscription.

```markdown
ASN.1 Field Type: (none)  
ASN.1 Field Value: (none)
JSON Field Name: auto_renew_status
JSON Field Value: string, interpreted as an integer
```

"1":  현재의 구독 기간 끝에 갱신이 될 것이라는 상태
"0": 고객이 구독에 대한 자동 갱신을 끈(turned off) 상태

:  이 키는 활성 또는 만료된 구독에 대한 자동 갱신 구독 영수증에만 존재합니다. 

이 키의 값은 고객의 구독 상태로 해석 되어서는 안됩니다. 이 값을 사용하여 앱에 대체 구독 제품 (예 : 고객이 현재 계획에서 다운 그레이드 할 수있는 하위 레벨 구독 계획)을 표시 할 수 있습니다.

## Subscription Auto Renew Preference

: 자동 갱신 구독에 대한 현재 갱신 기본 설정입니다.

```markdown
ASN.1 Field Type: (none)  
ASN.1 Field Value: (none)
JSON Field Name: auto_renew_product_id
JSON Field Value: string
```

: 이 키는 자동 갱신 구독 영수증에만 있습니다. 이 키의 값은 고객의 구독이 갱신되는 product의 `productIdentifier` 프로퍼티에 해당합니다. 이 값을 사용하여 현재 구독 기간이 종료되기 전에 고객에게 대체 서비스 수준을 제공할 수 있습니다.

## Subscription Price Consent Status

: 구독 가격 인상에 대한 현재 고객의 가격 동의 상태입니다.

```markdown
ASN.1 Field Type: (none)
ASN.1 Field Value: (none)
JSON Field Name: price_consent_status
JSON Field Value: string, interpreted as an integer
```

"1": 고객이 가격 인상에 동의했습니다. 구독은 더 높은 가격으로 갱신됩니다.

"0": 고객이 인상 된 가격에 대해 조치를 취하지 않았습니다. 갱신일 전에 고객이 조치를 취하지 않으면 구독이 만료됩니다.

: 이 키는 활성 구독자의 기존 가격을 유지하지 않고 구독 가격이 인상 된 경우 자동 갱신 가능한 구독 영수증에만 존재합니다. 이 값을 사용하여 새 가격의 고객 채택을 추적하고 적절한 조치를 취할 수 있습니다.