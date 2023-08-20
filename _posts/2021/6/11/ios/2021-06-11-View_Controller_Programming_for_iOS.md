---
layout: post
title: "[ios] View Controller Programming Guide for iOS"
description: " "
date: 2021-06-11
tags: [ios]
comments: true
share: true
---

## View Controller Programming Guide for iOS

You should always maintain a clean separation of responsibilities within your view controllers and data objects. **Most of the logic for ensuring the integrity of your data structures belongs in the data objects themselves.(=> 데이터 관련된 모든 것은 모델 객체가 한다, 해당 input data에 대해 controller가 model 객체가 원하는 형식으로 데이터를 포장하는 것을 제외하곤.)** The view controller might validate input coming from views and then package that input in the format that your data objects require, but you should minimize the view controller’s role in managing the actual data. The view controller might validate input coming from views and then package that input in the format that your data objects require, but you should minimize the view controller’s role in managing the actual data.

A UIDocument object is one way to manage your data separately from your view controllers. A document object is a controller object that knows how to read and write data to persistent storage.(데이터베이스 나 파일) When you subclass, you add whatever logic and methods you need to extract that data and pass it to a view controller or other parts of your app. The view controller might store a copy of any data it receives to make it easier to update views, but the document still owns the true data.

## User Interactions

View controllers are responder objects and are capable of handling events that come down the responder chain. Although they are able to do so, view controllers rarely handle touch events directly. Instead, views usually handle their own touch events and report the results to a method of an associated delegate or target object, which is usually the view controller. So most events in a view controller are handled using delegate methods or action methods.

## The View Controller Hierarchy

The relationships among your app’s view controllers define the behaviors required of each view controller. UIKit expects you to use view controllers in prescribed ways. Maintaining the proper view controller relationships ensures that automatic behaviors are delivered to the correct view controllers when they are needed. If you break the prescribed containment and presentation relationships, portions of your app will stop behaving as expected.

## The Root View Controller



