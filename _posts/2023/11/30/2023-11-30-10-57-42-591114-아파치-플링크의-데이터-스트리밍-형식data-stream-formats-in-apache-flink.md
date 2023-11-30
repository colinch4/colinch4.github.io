---
layout: post
title: "[java] 아파치 플링크의 데이터 스트리밍 형식(Data stream formats in Apache Flink)"
description: " "
date: 2023-11-30
tags: [java]
comments: true
share: true
---

## 개요
아파치 플링크는 대규모 데이터 스트리밍 애플리케이션을 처리하기 위한 오픈 소스 분산 처리 프레임워크입니다. 플링크는 다양한 데이터 스트림 형식을 지원하여 다양한 데이터 소스와의 연동을 용이하게 합니다. 이번 포스트에서는 플링크에서 지원하는 데이터 스트림 형식에 대해 살펴보겠습니다.

## Apache Avro
Apache Avro는 자바 기반의 데이터 직렬화 및 원격 프로시저 호출(RPC) 프레임워크입니다. 플링크에서는 Avro 형식을 사용하여 데이터 스트리밍을 처리할 수 있습니다. Avro 형식은 스키마 기반의 직렬화를 제공하며, 컴팩트하고 효율적인 이진 포맷을 사용합니다.

## Apache Parquet
Apache Parquet은 대용량 데이터를 효율적으로 저장하고 처리하기 위한 열 지향 파일 포맷입니다. 플링크에서는 Parquet 형식을 사용하여 데이터를 스트리밍 처리할 수 있습니다. Parquet은 열 지향 데이터 저장 방식을 사용하기 때문에 특정 열에 대한 쿼리 성능이 우수합니다.

## JSON
JSON은 JavaScript Object Notation의 약자로, 가벼운 데이터 교환 형식입니다. JSON은 인간이 읽고 쓰기 쉽고 기계적으로 구문 분석 및 생성하기도 간단합니다. 플링크에서는 JSON 형식을 사용하여 데이터 스트리밍을 처리할 수 있습니다.

## CSV
CSV는 Comma Separated Values의 약자로, 데이터를 쉼표로 구분하여 텍스트 파일에 저장하는 형식입니다. CSV는 일반적으로 스프레드시트 및 데이터베이스에서 데이터를 내보내거나 가져올 때 사용됩니다. 플링크에서는 CSV 형식을 사용하여 데이터 스트리밍을 처리할 수 있습니다.

## Apache Kafka
Apache Kafka는 대규모 실시간 메시지 처리를 위한 분산 스트리밍 플랫폼입니다. 플링크는 Kafka 형식의 데이터 스트리밍을 지원하여 Kafka와의 연동을 용이하게 합니다.

## 요약
플링크는 다양한 데이터 스트림 형식을 지원하여 다양한 데이터 소스와의 연동을 용이하게 합니다. Apache Avro, Apache Parquet, JSON, CSV, Apache Kafka 등의 다양한 형식을 사용하여 데이터 스트리밍을 처리할 수 있습니다. 이러한 다양한 형식을 통해 플링크는 빠르고 효율적인 데이터 처리를 제공합니다.

자세한 내용은 아파치 플링크 공식 문서를 참조하시기 바랍니다.

- [Apache Flink 공식 문서](https://flink.apache.org/documentation/)
- [Apache Avro 공식 문서](https://avro.apache.org/docs/current/)
- [Apache Parquet 공식 문서](https://parquet.apache.org/documentation/latest/)
- [JSON 공식 사이트](https://www.json.org/)
- [Apache Kafka 공식 문서](https://kafka.apache.org/documentation/)