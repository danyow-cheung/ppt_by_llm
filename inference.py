from utils.clean_txt import simple_sentenct_split 
from auto2ppt_summary import Doc2ppt 
from llm.content import generate_ppt_content,re_match_content
from ppt.setup import generate_ppt_file

def web_interfacee(text):
    '''
    多段文本段生成ppt
    '''
    
    doc = Doc2ppt(max_word_count=5000)
    text_list = simple_sentenct_split(text)
    print("当前text_list",len(text_list))
    ppt_path = doc.split_summary_doc(text_list)
    return ppt_path 

def top_inference(topic,page):
    '''
    主题，页数生成ppt
    '''

    content = generate_ppt_content(topic,page)
        
    content_list = re_match_content(content,page)
    if content_list is None:
        raise ValueError 
    
    ppt_path = generate_ppt_file(content_list,topic,page)
    return ppt_path 
if __name__ =="__main__":
    topic = '快乐星球'
    pages = 5 
    from llm.content import OneAPI 
    one = OneAPI()

    prompt=f'''
    我要准备1个关于{topic}的PPT，要求一共写{pages}页，请你根据主题生成详细内容，每一页对应相应的分主题，每个分主题的开始需要添加<start>，分页的标题也需要包含在<start>里面,该分页结束后需要添加<end>
    总页数控制在{pages}页内。
    '''
    try:
        res = one.post_v2(prompt)
        # return res 
        print(res)

    except Exception as e:
        print("请求llm失败")
        
