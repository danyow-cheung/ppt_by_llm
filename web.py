import os
import gradio as gr
from inference import web_interfacee,top_inference


def text_to_file(text):
    with open("output.txt", "w") as f:
        f.write(text)
    return "output.txt"
 


# method_list = ["输入文字生成PPT","输入主题输出PPT"]
# def change_textbox(choice):
#     if choice == "输入文字生成PPT":
#         return gr.Textbox(lines=2, visible=True)
#     elif choice == "输入主题输出PPT":
#         # return gr.Textbox(lines=2, visible=True)
#         with gr.Column():    # 列排列
#             context = gr.Textbox(label="主题")
#             question = gr.Textbox(label="页数")
            
    
#     else:
#         return gr.Textbox(visible=False)


with gr.Blocks() as demo:
    gr.Markdown("# 文字生成ppt")
    gr.Markdown("## 目前web只支持纯文字生成")
    
    with gr.Tab("输入文字生成PPT"):
        text = gr.Textbox(lines=3, interactive=True, show_copy_button=True)        
        greet_btn = gr.Button("generate")
        outputs = gr.components.File(label="下载文件")
        greet_btn.click(fn=web_interfacee, inputs=text, outputs=outputs)

    with gr.Tab("输入主题输出PPT"):
        context = gr.Textbox(label="生成的主题",visible=True)
        pages = gr.Number(label="页数")

        greet_btn = gr.Button("generate")
        outputs = gr.components.File(label="下载文件")
        #设置按钮点击事件
        greet_btn.click(fn=top_inference, inputs=[context,pages], outputs=outputs)




demo.launch(server_name="192.168.0.13")

