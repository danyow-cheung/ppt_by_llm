import json 
from pptx import Presentation
import re

from config.info import OneAPI
one = OneAPI()

def keep_chinese_english_and_angle_brackets(text):
    # 使用正则表达式匹配中文、英文字母和尖括号
    pattern = re.compile('[\u4e00-\u9fa5a-zA-Z<>]')
    return pattern.findall(''.join(text))



def re_match_content(str_content,page):
    '''
    receive str and return dcit '''
   
    if str_content is None:
        return 
    
    #! 直接用<start>来区分
    content_list = []
    split_list = str_content.split("<start>")
    # print(split_list)
    for i in split_list:
        
        temp_list = i.split("\n\n") 

        if "<end>" in temp_list:
            for sub in temp_list:
                if len(sub)!=0 and sub !='<end>':
                    content_list.append(sub)

    print('----'*10)
    print("content_list",content_list)
    print(len(content_list))

    if len(content_list)!= page: # 作为是否切分够好的标志
        return None 
    
    print('==='*10)
    return content_list 

    
def generate_ppt_content(topic,pages):
    '''
    '''

    prompt=f'''
    我要准备1个关于{topic}的PPT，要求一共写{pages}页，请你根据主题生成详细内容，每一页对应相应的分主题，每个分主题的开始需要添加<start>，结束需要添加<end>
    总页数控制在{pages}页内。
    '''
    try:
        res = one.post_v2(prompt)
        return res 
    
    except Exception as e:
        print("请求llm失败")
        return None 
    

def chat(prompt):
    try:
        res = one.post_v2(prompt)
        return res 
    
    except Exception as e:
        print("请求llm失败")
        return None 
