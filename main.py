from llm.content import generate_ppt_content,re_match_content
from ppt.setup import generate_ppt_file,generate_ppt_file_bg ,basic_usage 

    
def version_001():
    '''
    demo简陋版
    '''
    topic = "人工智能"
    page = 8 
    content = generate_ppt_content(topic,page)
        
    content_list = re_match_content(content,page)
    if content_list is None:
        raise ValueError 
    
    generate_ppt_file(content_list,topic,page)

def version_002():
    '''
    添加背景操作
    '''
    topic = "人工智能"
    page = 3
    content = generate_ppt_content(topic,page)    
    content_list = re_match_content(content,page)

    if content_list is None:
        version_002() # 简单写了个回溯
    else:
        image_path = 'images/test2.png'
        generate_ppt_file_bg(content_list,topic,image_path)


def version_003():
    '''
    左右分界,分别是图片和文字
    '''
    basic_usage()


if __name__=="__main__":
    version_003()


