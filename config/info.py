import json 
import requests 
from openai import OpenAI
import os 
import numpy as np 

with open("config/config.json",encoding="utf-8") as f:
    data_json = json.load(f)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
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
    
    def get_embedding(self,text, model="m3e-251"):
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input = [text], 
        model=model).data[0].embedding
    
    def similarity(self,text1,text2):
        # print('>>>对比的文本1',text1)
        # print('>>>对比的文本2',text2)

        embed1 = self.get_embedding(text1)
        embed2 = self.get_embedding(text2)
        return cosine_similarity(embed1,embed2)
    