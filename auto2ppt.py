
import os 
from ppt.setup import  basic_usage
from ppt.sub import random_concate
from llm.content import chat 

def main_entry():
        
    main_text ="""
    今天，我和我的同学们一起去了长隆游乐园。这是我们学校组织的一次春游，我们都非常兴奋。一早，我们就来到了游乐园。

    我们先去了游乐场上的旋转木马。我觉得旋转木马非常有趣，我和同学们一起骑在上面，感觉到我们的快乐和自由。接着，我们去玩了过山车。我觉得过山车非常刺激，我们在上面飞驰而下，感觉像飞行一样，非常惊险刺激。我和同学们都大声尖叫，释放我们的兴奋和快乐。

    中午，我们在游乐园的餐厅里吃了一些食物，稍作休息后，我们又开始了下午的活动。我们去了水上乐园，在水中游玩了一会儿。我觉得在水中游玩真的非常舒服，我和同学们在水中嬉戏打闹，享受着夏日的阳光和水上乐园带来的快乐。

    最后，我们去玩了机动游戏。这些游戏非常刺激，我和同学们都玩得非常兴奋。我们在游戏中一起欢笑和尖叫，释放了我们的压力和疲劳。

    今天的长隆游乐园一行，让我感到非常快乐和充实。我和同学们一起经历了刺激和快乐，留下了难忘的回忆。虽然今天很累，但是我相信这是我们都不会忘记的一天。
    """
    main_topic = chat(f"总结下面的内容,{main_text}. 并给出作文的题目")

    # 一级分割
    main_list = main_text.split("\n")
    # sub_list = [i for i in main_list if len(i)!=0 ]
    sub_list = [i for i in main_list if len(i)>=5 ] #! 这里的threshold可以调节 

    
    text_len = len(sub_list)

    images_list= []
    # base_image_path = r"D:\Code\ppt_by_llm\same_images"
    base_image_path = r"D:\Code\ppt_by_llm\images"

    base_image_list = os.listdir(base_image_path)
    for file in base_image_list:
        images_list.append(os.path.join(base_image_path,file))


    if len(images_list) == text_len:
        random_concate(main_topic,images_list,sub_list)
    else:
        print('还没决定好，慢慢来')
        image_content_confindence(images_list,sub_list)



def image_content_confindence(image_list,text_list):
    # from llm.clip import get_images_content
    for image in image_list:
        print(image)
        # get_images_content(image,text)
        
if __name__ =="__main__":
    main_entry()