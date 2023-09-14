---
layout: post
title: "Scraping social media followers count using Python"
description: " "
date: 2023-09-14
tags: [python, webscraping, socialmedia]
comments: true
share: true
---

Social media platforms provide APIs that allow developers to access information such as follower counts, likes, and comments. In this tutorial, we'll focus on scraping the follower count from different social media platforms using Python.

## Prerequisites
To follow along, make sure you have the following installed:
- [Python](https://www.python.org/downloads/)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Requests](https://requests.readthedocs.io/en/latest/)

## Scraping Instagram Follower Count
Instagram recently deprecated its public API, making it more challenging to scrape follower counts directly. However, we can use web scraping techniques to retrieve this information.

```python
import requests
from bs4 import BeautifulSoup

def get_instagram_followers(username):
    url = f"https://www.instagram.com/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    followers_count = soup.find("meta", property="og:description").get("content")
    followers_count = followers_count.split()[0]
    return int(followers_count.replace(",", ""))

username = "your_instagram_username"
followers = get_instagram_followers(username)
print(f"{username} has {followers} followers on Instagram.")
```

Make sure to replace `"your_instagram_username"` with the desired username before running the code.

## Scraping Twitter Follower Count
Twitter provides an API that requires authentication. However, we can still scrape follower counts by accessing the user's profile page.

```python
import requests
from bs4 import BeautifulSoup

def get_twitter_followers(handle):
    url = f"https://twitter.com/{handle}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    followers_count = soup.find("a", href=f"/{handle}/followers").get("title")
    return int(followers_count.replace(",", ""))

handle = "your_twitter_handle"
followers = get_twitter_followers(handle)
print(f"{handle} has {followers} followers on Twitter.")
```

Replace `"your_twitter_handle"` with your desired handle before running the code.

## Conclusion
By using web scraping techniques, we can retrieve follower counts from popular social media platforms like Instagram and Twitter. Remember to respect the terms and conditions of each platform, as scraping can be against their policies. Always be mindful and use scraping responsibly.

#python #webscraping #socialmedia