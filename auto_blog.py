#!/usr/bin/env python3

import openai
import re
import os
import time
import subprocess
from datetime import datetime

import subprocess

openai.api_key = os.environ['API_KEY']

folder_path = '_subject'
file_contents = ""
open_file_path = ""

def generate_blog(topic):
    global file_contents
    # 모델 엔진 선택
    model_engine = "gpt-3.5-turbo"
    retries = 5
    while retries > 0:
        try:
            completion = openai.ChatCompletion.create(
                model=model_engine,
                messages=[
                        {
                            "role": "system",
                            "content": "Write tech blog posts in markdown format.",
                        },
                        {
                            "role": "system",
                            "content": "Create only two important hashtags and add them only at the end of the line.",
                        },
                        {
                            "role": "system",
                            "content": "Highlight, bold, or italicize important words or sentences.",
                        },
                        {
                            "role": "system",
                            "content": "Please write example code. When writing code, type the programming language right after the first backquote.",
                        },
                        {
                            "role": "system",
                            "content": "Please write with SEO in mind.",
                        },
                        {
                            "role": "user",
                            "content": f"{topic}",
                        }
                    ], 
            )
            return completion
        except Exception as e:
            if e: 
                print(e)   
                print('Timeout error, retrying...')    
                retries -= 1    
                time.sleep(5)    
            else:    
                raise e   

def git_commit(commit_message, remote='origin', branch='master'):
    try:
        # 변경 사항 추가
        subprocess.check_call(['git','add','-A'], cwd='.')

        # 변경 사항 추가
        subprocess.check_call(['git','commit','-m', commit_message], cwd='.')

        
        # GitHub에 푸시
        subprocess.check_call(['git','push',remote,branch], cwd='.')

        print("Commit and push successful!")
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e.output.decode())


def urlify(s):
    # 1. 소문자로 변환 (영어에만 해당)
    s = s.lower()
    
    # 2. 공백을 대시(-)로 대체
    s = re.sub(r'\s+', '-', s)
    
    # 3. 특수문자 제거 (알파벳, 숫자, 대시, 한글만 허용)
    s = re.sub(r'[^\w-]', '', s)  # \w는 알파벳, 숫자, 밑줄에 매치되며, 한글에도 매치됩니다.
    
    return s


def save_file(li): 
    global open_file_path
    if len(li) == 0: 
        if os.path.isfile(open_file_path):
            os.remove(open_file_path)
            return
    with open(open_file_path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(li))


def gpt_action(_topic): 
    topic = f"{_topic}"
    response = generate_blog(topic)
    # 생성된 글 출력
    # print(response.choices[0].text)
    hashtag_pattern = r'(#+[a-zA-Z0-9(_)]{1,})'

    re.findall(hashtag_pattern, response['choices'][0]['message']['content'])

    hashtags = [w[1:] for w in re.findall(hashtag_pattern, response['choices'][0]['message']['content'])]
    tag_string = ""
    tag_string = re.sub(r'[^a-zA-Z, ]', '', tag_string)
    tag_string = tag_string.strip()[:-1]

    for w in hashtags:
        # 3글자 이상 추출
        if len(w) > 3:
            tag_string += f'{w}, '

    tag_string = tag_string[:-2]
    
    # 오늘 일자 생성
    today = datetime.now()

    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')
    hour = today.strftime('%H')
    min = today.strftime('%M')
    second = today.strftime('%S-%f')

    timestring = today.strftime('%Y-%m-%d')
    timestring

    filename = f"{timestring}-{hour}-{min}-{second}-{urlify(topic)}.md"
    filename

    page_head = f'''---
layout: post
title: "{topic}"
description: " "
date: {timestring}
tags: [{tag_string}]
comments: true
share: true
---
'''

    body = '\n'.join(response['choices'][0]['message']['content'].strip().split('\n')[1:])

    output = page_head + body
    print(output)

    blog_directory = f"_posts/{year}/{month}/{day}"

    # 폴더가 이미 존재하지 않으면 폴더를 생성
    if not os.path.exists(blog_directory):
        os.makedirs(blog_directory)

    filepath = os.path.join(blog_directory, filename)
    filepath

    with open(filepath, 'w', encoding='UTF-8') as f:
        f.write(output)
        f.close()


files_in_folder = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

if not files_in_folder: 
    exit()

open_file_path = os.path.join(folder_path, files_in_folder[0])

try:
    with open(open_file_path, 'r', encoding='UTF-8') as f:
        file_contents = f.readlines()
except Exception as e:
    print(f"{e}")
    exit()

for idx, val in enumerate(file_contents):
    print(f"({idx}/{len(file_contents)}) {val.strip()}")
    gpt_action(val.strip())

save_file([])

commit_message = "post"
git_commit(commit_message)

print(f"complete !! {len(file_contents)} were posted.")

exit()