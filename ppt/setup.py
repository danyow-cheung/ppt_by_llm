from pptx import Presentation
import time 

# 生成PPT文件
def generate_ppt_file(content_list,topic,page):
    ppt=Presentation()
    
    # # PPT首页
    slide=ppt.slides.add_slide(ppt.slide_layouts[0]) # title&subtitle layout
    slide.placeholders[0].text=topic
    slide.placeholders[1].text="author:danyow"
    
    # # 内容页

    # for i,page in enumerate(ppt_content['pages']):
    for i,one_page in enumerate(content_list):
        page_list = one_page.split("\n")
        print(page_list)
        for content in page_list:
            if content[0]!='-':
                # 标题
                
                slide=ppt.slides.add_slide(ppt.slide_layouts[1]) # title&content layout
                slide.placeholders[0].text=content 
            else:
                # 内容
                sub_title=slide.placeholders[1].text_frame.add_paragraph()
                sub_title.text,sub_title.level=content[1:],1 
                # # 二级正文
                # sub_description=slide.placeholders[1].text_frame.add_paragraph()
                # sub_description.text,sub_description.level=sub_content['description'],2
    
        # break 

    # ppt.save('%s.pptx'%topic)
    ppt.save(f'{topic}_{int(time.time())}.pptx')

