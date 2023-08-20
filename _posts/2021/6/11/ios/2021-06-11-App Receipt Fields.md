---
layout: post
title: "[ios] App Receipt Fields"
description: " "
date: 2021-06-11
tags: [ios]
comments: true
share: true
---

## App Receipt Fields

## 1. Bundle Identifier

: The app's bundle Identifier

```markdown
ASN.1 Field Type: 2 
ASN.1 Field Value: UTF8String
JSON Field Name: bundle_id
JSON Field Value: string
```

: Info.plist 파일의 `CFBundleIdentifier` 의 값과 일치합니다. 당신의 앱에서 정말 영수증이 generated된 것인지 검증하기 위해, Bundle Identifier 필드값을 Info.plist 파일의 `CFBundleIdentifier` 의 값과 비교하세요.

## 2. App Version

: The app's version number

```markdown
ASN.1 Field Type: 3 
ASN.1 Field Value: UTF8String
JSON Field Name: application_version
JSON Field Value: string
```

## 3. Opaque Value

: 영수증 검증 중 SHA-1 해시를 계산(compute)하기 위해 다른 데이터와 함께 사용되는 불투명 값입니다.

```markdown
ASN.1 Field Type: 4
ASN.1 Field Value: A series of bytes
JSON Field Name: (none)
JSON Field Value: (none)
```

## 4. SHA-1 Hash

: 영수증을 검증하는데 사용되는 SHA-1 Hash 값입니다.

```markdown
ASN.1 Field Type: 5 
ASN.1 Field Value: 20-byte SHA-1 digest
JSON Field Name: (none)
JSON Field Value: (none)
```

## 5. In-App Purchase Receipt

: 인앱 구매와 관련된 영수증

```markdown
ASN.1 Field Type: 17 
ASN.1 Field Value: SET of in-app purchase receipt attributes
JSON Field Name: in_app
JSON Field Value: array of in-app purchase receipts
```

: JSON 파일에서 이 키의 값은 입력 base-64 영수증 데이터에 있는 인앱 구매 트랜잭션을 기반으로 한 모든 인앱 구매 영수증을 포함하는 **배열**입니다. 자동 갱신 구독이 포함 된 영수증의 경우, latest_receipt_info 키 값을 확인하여 가장 최근 갱신 상태를 확인하세요.

: ASN.1 파일에는 타입이 17 인 여러 필드가 있으며, 각 필드에는 단일 인앱 구매 영수증이 포함됩니다.

> 빈 배열은 유효한 영수증입니다.

: consumable 상품을 구매시 인앱 해당 consumable 상품의 구매 영수증이 영수증에 추가됩니다. consumable 상품 구매 이력은 앱이 해당 거래를 완료 할 때까지(`finishTransaction`을 호출하기 전까지) 영수증에 보관됩니다. 이 시점이 지나면 다음에 영수증이 업데이트 될 때 영수증에서 삭제됩니다 (예 : 사용자가 다른 구매를 하거나 앱에서 영수증을 명시적으로 새로 고치는 경우).
: non-consumable 상품, 자동 갱신 구독, 비 갱신 구독 또는 무료 구독(처음 1회로만 가능)에 대한 인앱 구매 영수증은 영수증에 무기한(indefinitely) 남아 있습니다.

## 6. Original Application Version

: 원래 구매한 앱의 버전입니다.

```markdown
ASN.1 Field Type: 19
ASN.1 Field Value: UTF8STRING
JSON Field Name: original_application_version
JSON Field Value: string
```

: 이것은 처음에 구입했을 때 Info.plist 파일의 `CFBundleVersion` (iOS) 또는 `CFBundleShortVersionString` (macOS)의 값과 일치합니다.

sandbox 환경에서는, 이 필드의 값은 항상 "1.0" 입니다.

## 7. Receipt Creation Date

: 앱 영수증이 생성된 날짜입니다.

```markdown
ASN.1 Field Type: 12 
ASN.1 Field Value: IA5STRING, interpreted as an RFC 3339 date 
JSON Field Name: receipt_creation_date 
JSON Field Value: IA5STRING, interpreted as an RFC 3339 date
```

: 영수증을 검증할 때, 이 영수증의 서명을 검열하기 위해 이 날짜를 사용하세요.

: 많은 암호화 라이브러리는 기본적으로 PKCS7 패키지의 유효성을 검사할 때 기기의 현재 시간과 날짜를 사용하지만, 그러나 이 방법도 영수증의 서명을 확인할 때 올바른 결과를 생성하지 못할 수 있습니다. 예를 들어 영수증이 유효한 인증서로 서명되었지만, 인증서가 만료된 이후에는 기기의 현재 날짜를 사용하면 잘못된 결과가 잘못 반환됩니다. **따라서 앱에서 항상 영수증 생성 날짜 필드(the Receipt Creation Date Field)의 날짜를 사용하여 영수증의 서명을 확인해야합니다.**

## 8. Receipt Expiration Date

: 앱 영수증이 만료 되었을 때 날짜입니다.

```markdown
ASN.1 Field Type: 21 
ASN.1 Field Value: IA5STRING, interpreted as an RFC 3339 date 
JSON Field Name: expiration_date 
JSON Field Value: IA5STRING, interpreted as an RFC 3339 date
```

: 이 키는 Volume Purchase 프로그램을 통해 구매한 앱에만 있습니다. 이 키가 없으면, 영수증이 만료되지 않습니다.
: 영수증을 검증할 때, 이 날짜를 현재 날짜와 비교하여 영수증이 만료되었는지 확인합니다. 만료 전 남은 시간과 같은 다른 정보를 계산하는 데, 이 날짜를 사용하지 마십시오.