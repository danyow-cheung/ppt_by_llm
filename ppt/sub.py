from pptx import Presentation
import time 
from pptx.util import Inches
import random 


def Text2Img(ppt,text_content,image_path,index):
    '''
    左边为文字，右边为图片'''
    # second 
    slide=ppt.slides.add_slide(ppt.slide_layouts[1])
    slide.placeholders[0].text=str(index) 
    sub_title=slide.placeholders[1].text_frame.add_paragraph() # 这个是防止出现多余的文本输入框来的
    # 添加左侧文字占位符
    #! left_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(6), Inches(4)) 在幻灯片上创建了一个宽 6 英寸、高 4 英寸的文本框,它距离幻灯片左边缘 0.5 英寸、顶边缘 2 英寸的位置。
    left_box = slide.shapes.add_textbox(Inches(0.5), Inches(2), Inches(4), Inches(4))
    left_text_frame = left_box.text_frame
    left_text_frame.word_wrap = True# 自动换行
    

    left_text_frame.text = text_content 
    # 添加右侧图片占位符
    #! 距左边缘 7 英寸、距顶边缘 2 英寸的图片,图片大小为宽 4 英寸、高 4 英寸。
    image_path = rf"{image_path}"
    right_box = slide.shapes.add_picture(image_path, Inches(5), Inches(2), width=Inches(4), height=Inches(4))
    
    return slide 


def Img2Text(ppt,text_content,image_path,index):
    slide=ppt.slides.add_slide(ppt.slide_layouts[1])
    slide.placeholders[0].text=str(index)
    sub_title=slide.placeholders[1].text_frame.add_paragraph() # 这个是防止出现多余的文本输入框来的
    
    image_path = rf"{image_path}"
    left_box = slide.shapes.add_picture(image_path, Inches(0.5), Inches(2), width=Inches(4), height=Inches(4))

    # 添加右侧图片占位符
    #! 距左边缘 7 英寸、距顶边缘 2 英寸的图片,图片大小为宽 4 英寸、高 4 英寸。
    right_box =slide.shapes.add_textbox(Inches(5), Inches(2), Inches(4), Inches(4))
    right_box_frame = right_box.text_frame
    right_box_frame.word_wrap = True # 自动换行


    right_box_frame.text = text_content
    return slide 

def random_concate(main_topic,images_list,text_list):

    ppt=Presentation()
    slide=ppt.slides.add_slide(ppt.slide_layouts[0])
    slide.placeholders[0].text=main_topic if main_topic else "未命名"
    sub_title=slide.placeholders[1].text_frame.add_paragraph() 

    for idx,value in enumerate(zip(images_list,text_list)):
        image,text = value 
        print(idx,image,text)
        
                
        if idx % 2 == 0:
            slide = Text2Img(ppt,text,image,idx)
        else:
            # pass # Odd
            slide = Img2Text(ppt,text,image,idx)

    slide=ppt.slides.add_slide(ppt.slide_layouts[0])
    slide.placeholders[0].text="多谢观看"
    slide.placeholders[1].text="author:danyow"

    ppt.save(f'output/Test_{int(time.time())}.pptx')
    