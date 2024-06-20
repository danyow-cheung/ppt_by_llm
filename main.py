import sys 
sys.path.append(r"E:\Code\PowerPoint-Generator-Python-Project-main\PowerPoint-Generator-Python-Project-main\aippt_danyow")
from llm.content import generate_ppt_content,re_match_content

if __name__=="__main__":
        
    topic = "人工智能"
    page = 8 
    content = generate_ppt_content(topic,page)
        
    content_list = re_match_content(content,page)
    if content_list is None:
        raise ValueError 
    
    from ppt.setup import generate_ppt_file 
    generate_ppt_file(content_list,topic,page)


