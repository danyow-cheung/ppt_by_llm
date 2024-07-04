import os 
from ppt.setup import  basic_usage
from ppt.sub import random_concate
from llm.content import chat 
from docx import Document
import numpy as np 
import re 
from config.info import OneAPI

def remove_special_characters(input_string):
    pattern = re.compile(r'[\u4e00-\u9fa5\d]+')
    result = pattern.findall(input_string)
    return "".join(result)

class Doc2ppt:
    def __init__(self,max_word_count) -> None:
        # self.max_word_count = 5000  # 最大文字数为5k-1w
        # self.max_word_count = 4000  # 最大文字数为5k-1w
        self.max_word_count = max_word_count

        self.one = OneAPI()
    def read_doc(self,doc_path):

        doc = Document(doc_path)
        text_lists = []
        # 逐段读取文档内容
        word_count =0 
        for paragraph in doc.paragraphs:
            
            if len(paragraph.text)>=3: #!会有空格或其他的，最简单的过滤低频信息方法
                word_count+= len(paragraph.text)
                text_lists.append(paragraph.text)
            
            if word_count>self.max_word_count:
                break 
        print(f'文件读取完成.总文字数量为{word_count}')
        return text_lists 
    
    def split_summary_algo(self,text_lists):
        '''
        根据词向量的余弦相似度来计算文本的关联性
        '''
        result = []
        left = 0
        threshold_score = 0.5 
        while left < len(text_lists) - 1:
            sentence = text_lists[left]
            current_segment = [sentence]
            right = left + 1
            
            while right < len(text_lists):
                next_sentence = text_lists[right]
                diff = self.one.similarity(sentence, next_sentence) #! 这里是主要计算文本相似度的
                
                if diff > threshold_score:
                    current_segment.append(next_sentence)
                    sentence += next_sentence
                    right += 1
                else:
                    break
            result.append(" ".join(current_segment))
            left = right 

        if left < len(text_lists):
            result.append(text_lists[left])
        return result 
    

    def llm_content(self,sub ):
        short_sub = self.one.post_v2(f"帮我将下面的输入进行文字的简化,如果输入文字超过了200字，需要简化到200字以内，{sub}")
        return short_sub 

    def llm_title(self,sub):
        short_title = self.one.post_v2(f"阅读下面的文字，然后输出标题，字数限制在 10字以内。文字：{sub}")    
        return short_title 
    
    def split_summary_doc(self,text_lists):
        '''
        分割后的逻辑代码
        20240704,最简单的文本生成ppt
        '''
        result = self.split_summary_algo(text_lists)

        ready_text ={"topic":None,"content_list":None,"sub_title":None}
        ready_list = []
        ready_title=[]
        
        title = self.one.post_v2(f"阅读下面的文字，然后输出标题 文字：{text_lists}")
        ready_text['topic'] = title 
        title = title[3:] 

        print("分割后的文字分段",len(result))
        print('总标题',title)
        recycle_generate =0 
        left = 0 
        while left < len(result):
            print('当前',recycle_generate,"left",left)
            sub = result[left]
            short_sub,short_title = self.generate_loop_v2(sub) 
            left +=1 
            ready_list.append(short_sub)
            ready_title.append(short_title)

        self.send2ppt(title,ready_list,ready_title,flag=True) 


    def content_loop(self,sub):
        short_sub = self.llm_content(sub)
        pure_short_sub = remove_special_characters(short_sub)
        return short_sub,pure_short_sub 
    def title_loop(self,sub):
        short_title = self.llm_title(sub)        
        pure_short_title=remove_special_characters(short_title)
        return short_title,pure_short_title 
    
    
    def generate_loop_v2(self, sub):
        while True:
            short_sub, pure_short_sub = self.content_loop(sub)
            short_title, pure_short_title = self.title_loop(sub)

            print(f'当前 len(pure_short_sub)={len(pure_short_sub)}, len(pure_short_title)={len(pure_short_title)}')

            if len(pure_short_sub) <= 250 and len(pure_short_title) <= 20:
                return short_sub, short_title



    def send2ppt(self,topic:str,content_list:list,title_list:list,flag:bool,image_list:list):
        from ppt.sub import PptGenerator
        ppt = PptGenerator()
        if flag==True:

            ppt.pure_text_generate(topic,content_list,title_list)
        else:
            # todo: 图文匹配的ppt
            ppt.image_text_generate(topic,content_list,title_list,image_list)


    def split_sumary_doc_with_imgs(self,text_lists,images_list):
        '''
        分割后的逻辑代码
        20240704,最简单的文本生成ppt
        '''
        result = self.split_summary_algo(text_lists)

        ready_text ={"topic":None,"content_list":None,"sub_title":None}
        ready_list = []
        ready_title=[]
        
        title = self.one.post_v2(f"阅读下面的文字，然后输出标题 文字：{text_lists}")
        ready_text['topic'] = title 
        title = title[3:] 

        print("分割后的文字分段",len(result))
        print('总标题',title)
        recycle_generate =0 
        left = 0 
        while left < len(result):
            print('当前',recycle_generate,"left",left)
            sub = result[left]
            short_sub,short_title = self.generate_loop_v2(sub) 
            left +=1 
            ready_list.append(short_sub)
            ready_title.append(short_title)
        
        flag=  False 
        self.send2ppt(title,ready_list,ready_title,flag,images_list)

if __name__ =="__main__":
    pass 


    