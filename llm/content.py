import json 
from pptx import Presentation
import re


# 生成PPT文件
def generate_ppt_file(topic,ppt_content):
    print("ppt_content",type(ppt_content))

    ppt=Presentation()
    
    # PPT首页
    slide=ppt.slides.add_slide(ppt.slide_layouts[0]) # title&subtitle layout
    slide.placeholders[0].text=ppt_content['title']
    # slide.placeholders[1].text="通义千问72B"
    
    # 内容页
    print('总共%d页...'%len(ppt_content['pages']))
    for i,page in enumerate(ppt_content['pages']):
        print('生成第%d页:%s'%(i+1,page['title']))
        slide=ppt.slides.add_slide(ppt.slide_layouts[1]) # title&content layout
        # 标题
        slide.placeholders[0].text=page['title']
        # 正文
        for sub_content in page['content']:
            print(sub_content)
            # 一级正文
            sub_title=slide.placeholders[1].text_frame.add_paragraph()
            sub_title.text,sub_title.level=sub_content['title'],1
            # 二级正文
            sub_description=slide.placeholders[1].text_frame.add_paragraph()
            sub_description.text,sub_description.level=sub_content['description'],2
    
    ppt.save('%s.pptx'%topic)

 
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

    from config.info import OneAPI
    one = OneAPI()
    try:
        res = one.post_v2(prompt)
        return res 
    
    except Exception as e:
        print("请求llm失败")
        return None 
    

