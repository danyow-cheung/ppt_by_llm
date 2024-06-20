import json 
import requests 
from openai import OpenAI
import os 

with open("config/config.json",encoding="utf-8") as f:
    data_json = json.load(f)



class OneAPI:
    
    def __init__(self) -> None:
        api_key = data_json['api_key']
        api_base = data_json['base_url']
        self.client = OpenAI(api_key=api_key, base_url=api_base)

    def post_v2(self,content,model="chatglm3-6b-251"):


        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "user", "content": f"{content}"}
            ],
            model="chatglm3-6b-251"
            )
        return chat_completion.choices[0].message.content 
    