import requests
import json

API_URL = "http://localhost:11434/api/chat"

payload = {   #형식은 dict 와 비슷함 ==> json 형식 {key : value} 값
    "model": "gemma3:1b",
    "messages": [
        {"role": "user", "content": "서울의 3일 일정을 작성해줘"}, # 개발이란 {} 에서 무언가 계속 추가하는 것. 명령어(?)를 계속 추가하는 것.

    ],
    "options": { # 사용자 입력값 ==> adjusting the parameters
        "num_predict": 400,
        "temperature": 1.0,
        "top_p": 0.9
    },
    "stream": False
} 

headers = {"Content-Type": "application/json"}
response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
print("Response Status Code:", response.status_code)
print("Response Json:", response.json())




# with requests.post(API_URL, headers=headers, json=payload, stream=True) as response:
#     for line in response.iter_lines():
#         if line:
#             line_str = line.decode('utf-8')
#             try:
#                 json_obj = json.loads(line_str)
#                 if 'message' in json_obj and 'content' in json_obj['message']:
#                     content = json_obj['message']['content'] #메세지의 컨텐츠를 가져온다.
#                     print(content, end='',flush=True) 

#                 if json_obj.get('done', False):
#                     print("\n\n[완료]")
#                     break

#             except json.JSONDecodeError:
#                 continue   # 컨트롤 + 슬리시를 누르면 모두 주석이된다!




