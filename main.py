from llm.content import generate_ppt_content,re_match_content
from ppt.setup import generate_ppt_file,generate_ppt_file_bg ,basic_usage 
import os 
    
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
    
    ppt_path = generate_ppt_file(content_list,topic,page)
    return ppt_path 

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

def doc_main():
    '''
    20240703
    '''
    # 启动程序
    from auto2ppt_summary import Doc2ppt 

    doc = Doc2ppt(max_word_count=5000)
    text_list = doc.read_doc(r"data\word\20240621_100458_short.docx")
    # image_path = "data/images"
    image_path = "data/real_scene_short"

    images_file_list = os.listdir(image_path)
    images_list = []
    for file in images_file_list:
        path = os.path.join(image_path,file)
        images_list.append(path)
    
    # doc.split_summary_doc(text_list)
    doc.split_summary_doc_with_imgs(text_list,images_list)

def web_interfacee(text):
    from utils.clean_txt import simple_sentenct_split 
    from auto2ppt_summary import Doc2ppt 

    doc = Doc2ppt(max_word_count=5000)
    text_list = simple_sentenct_split(text)
    print("当前text_list",len(text_list))
    ppt_path = doc.split_summary_doc(text_list)
    return ppt_path 



if __name__=="__main__":
    # version_003()
    doc_main()


