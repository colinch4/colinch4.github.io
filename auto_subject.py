import openai
import re
import os
import sys
import threading
import time
import numpy as np
import tkinter as tk
from tkinter import filedialog
from datetime import datetime, timedelta

import tkinter as tk
from tkinter import filedialog

openai.api_key = os.environ['API_KEY']

file_contents = ""
open_file_path = ""
last_index = 0

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
                            "content": "List at least 100 topics based on keywords.",
                        },
                        {
                            "role": "system",
                            "content": "Please write in Korean.",
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
def urlify(s):
    # 1. 소문자로 변환 (영어에만 해당)
    s = s.lower()
    
    # 2. 공백을 대시(-)로 대체
    s = re.sub(r'\s+', '-', s)
    
    # 3. 특수문자 제거 (알파벳, 숫자, 대시, 한글만 허용)
    s = re.sub(r'[^\w-]', '', s)  # \w는 알파벳, 숫자, 밑줄에 매치되며, 한글에도 매치됩니다.
    
    return s

def gpt_action(_topic): 
    topic = f"{_topic}"
    response = generate_blog(topic)
    # 생성된 글 출력
    # print(response.choices[0].text)
    hashtag_pattern = r'(#+[a-zA-Z0-9(_)]{1,})'

    re.findall(hashtag_pattern, response['choices'][0]['message']['content'])

    # 오늘 일자 생성
    today = datetime.now()
    today

    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')
    hour = today.strftime('%H')
    min = today.strftime('%M')
    second = today.strftime('%S-%f')

    timestring = today.strftime('%Y-%m-%d')

    filename = f"{timestring}-{hour}-{min}-{second}-{urlify(topic)}"

    # body = '\n'.join(response['choices'][0]['message']['content'].strip().split('\n')[0:])
    body = '\n'.join([line.split('. ', 1)[-1].strip() if '. ' in line else line for line in response['choices'][0]['message']['content'].strip().split('\n')])

    output = body
    print(output)

    blog_directory = "_subject"

    # 폴더가 이미 존재하지 않으면 폴더를 생성
    if not os.path.exists(blog_directory):
        os.makedirs(blog_directory)

    filepath = os.path.join(blog_directory, filename)
    filepath

    with open(filepath, 'w', encoding='UTF-8') as f:
        f.write(output)
        f.close()

def save_file(li): 
    global open_file_path
    if len(li) == 0: 
        if os.path.isfile(open_file_path):
            os.remove(open_file_path)
            return
    with open(open_file_path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(li))

# 파일 선택 버튼을 눌렀을 때 실행할 함수
def open_file_dialog():
    global file_contents
    global open_file_path
    open_file_path = filedialog.askopenfilename(title="파일 선택")
    if open_file_path:
        selected_file_label.config(text=f"선택한 파일: {open_file_path}")
        try:
            with open(open_file_path, "r", encoding='UTF-8') as file:
                file_contents = file.readlines()
                array_length_label.config(text=f"배열 길이: {len(file_contents)}")
            display_contents(file_contents, 0)
        except Exception as e:
            error_label.config(text=f"파일을 읽는 중 오류 발생: {e}")
    else:
        selected_file_label.config(text="파일을 선택하지 않았습니다.")
        array_length_label.config(text="")

# 파일 내용을 화면에 표시하는 함수
def display_contents(contents, startIndex):
    contents_listbox.delete(0, tk.END)  # 이전 내용을 지우기
    for idx, val in enumerate(contents):
        if idx >= startIndex:
            contents_listbox.insert(tk.END, val.strip())

def run_thread(): 
    global file_contents
    global last_index
    for idx, val in enumerate(file_contents):
        last_index = idx
        print(val.strip())
        gpt_action(val.strip())
        display_contents(file_contents,idx+1)
        array_length_label.config(text=f"배열 길이: {len(file_contents)-idx-1}")
    save_file([])

# 두 번째 버튼을 눌렀을 때 실행할 함수
def run_gpt():
    thread = threading.Thread(target=run_thread)
    thread.start()

def exit():
    window.destroy()
    window.quit()

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("파일 선택 및 내용 표시 예제")

# 파일 선택 버튼 생성
open_button = tk.Button(window, text="파일 선택", command=open_file_dialog)
open_button.pack(pady=10)

# 파일 이름을 나타낼 라벨(Label) 생성
selected_file_label = tk.Label(window, text="")
selected_file_label.pack()

# 배열 길이를 나타낼 라벨(Label) 생성
array_length_label = tk.Label(window, text="")
array_length_label.pack()

# 파일 내용을 표시할 리스트박스(Listbox) 생성
contents_listbox = tk.Listbox(window)
contents_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 파일 읽기 중 오류를 표시할 라벨(Label) 생성
error_label = tk.Label(window, text="", fg="red")
error_label.pack()

# 두 번째 버튼 생성
clear_button = tk.Button(window, text="실행", command=run_gpt)
clear_button.pack()

# Tkinter 메인 루프 시작
window.mainloop()