
import os 
from ppt.setup import  basic_usage
from ppt.sub import random_concate
from llm.content import chat 
from docx import Document

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
    #todo 不同的图片和文件进行匹配 
    # from llm.clip import get_images_content
    for image in image_list:
        print(image)
        # get_images_content(image,text)


def word_reading():
    doc = Document("20240621_100458_原文 .docx")
    text_lists = []

    count = 0 
    # 逐段读取文档内容
    for paragraph in doc.paragraphs:
        if len(paragraph.text)>=3:
            print(paragraph.text)    

            text_lists.append(paragraph.text)
            count +=1 

        if count >=20:
            break
    
    print(text_lists)

def word_doc_split():
    '''
    根据词向量的余弦相似度来计算文本的关联性
    '''
    text_lists = [
        '有一家公司就是靠多说一句话，每一年可以增加将近40个亿的销售额，你们觉得可不可怕？一句话可以多增加40个亿的销售额。这家公司你们在场的各位基本每一个人有可能都去买过，而且都在里面体验过，这家公司就叫麦当劳 。有没有去过？麦当劳我相信基本大多数人都去过，对不对？', 
        
        '那麦当劳它是怎么增长的？麦当劳的增长方式很简单，我给大家举个最简单的例子。今天在这个园区有一家麦当劳的店，我按它最差的这个日均进客量，假如说一天有100个自然流量进入到这个店里面，请问这100个人进 到这个店里面是为了干什么？100个人进到这个店是为了干什么？要么买汉堡，要么买可乐，是不是这样的？好，这100个人就进去了。', 
        
        '假如说这100个人都是买汉堡的，好，这100个人过来买汉堡，买完汉堡之后他的销售员是不是会多说一句话，请问要不要加一杯可乐？你每一次买 会不会这样说？71跟麦当劳都会有这样的话术。', 
        
        'Ok这个时候你问他，你说加一杯可乐多少钱？他说加一杯可乐只需要加七块钱。请问你加还是不加？请问这100个人会不会都加了？100个人会不会豆浆？只有一部分人会加，对不对？所以一部分人会加，有50个人加。这50个人一加， 他就说你是加中杯还是加大杯？加大杯只需要再加一块。请问是加中杯还是加大杯？', 
        
        
        '你本来你看你本来只想买个汉堡，别人说了一句话，你就多花了七块钱买了一杯可乐。你只想买一杯可乐，多别人又多说了一句话，你又多花了一块钱，又买了一个大杯。所以他的整个流程就是靠 单次交易金额也是可以提升业绩的。然后第三个靠提升回购频次，靠提升回购频次就是一个客户靠你的产品一个福利，你可以持续的跟他建立更多次的购买，更多次的信任。这个时候客户会重复不断的去你这买东西。如果一个客户在你这本来只花1000块的，变成花1万块，甚至变成花5万块，甚至 变成10万块，是不是增加了业绩？所以所有的企业要去增加业绩，都是从这三个点上去找一个细化的颗粒度的点。然后找到你最适合你这个企业，最符合你们的人力体系，最符合你这个行业的增长点，最终你才能增加业绩。', 
        
        '但是这个操作难度我告诉你，你不学个八年九年的营销体 系，你是研究不明白的。我是因为我一直在干这个事情，而且做了九年，我服务过很多很多的企业，甚至有一些企业我跟他沟通的过程中，我就知道他有什么问题，包括明天我会给你们讲一套体系，帮助你判断企业问题的一套流程核心方法论，一套超级核心的方法论。所以在这个体系的过程中， 你想要最简单、最容易复制，最容易找到业绩的方式。', 
        
        
        '我告诉你在今天，尤其是结合AI这个时代，只有一种方式，不需要太多的营销技巧，不需要太多的营销经验。就是增加客户数能不能理解？就是增加客户数他不需要太操作难度大的这样的方法论。为什么？因为搞流量是开卷考 试，各位能不能理解？', 
        
        
        '搞流量一定是开卷考试。今天无论做抖音、做视频号、做小红书，干流量的第一件事是不是先找对标，这是不是开卷考试？别人怎么搞你就怎么搞，别人怎么搞你就怎么复制。我们是不是一直在用这样的方式搞客户，只是在复制的过程中，不知道怎么可以搞 出更牛逼的内容，写出更好的文案，然后让我们的内容变得更好，或者怎么批量化生产。这个内容是没有方法的。但是不用担心，接下来在我们三天两夜里面，我去训练，我去教你训练AI的时候，是帮你可以直接现场做出来内容的，直接帮你做出来内容的。我不会跟你们讲工具怎么使用，但我会 告诉你用AI使用AI的思维这一套链条是怎么使用的是怎么使用的。', 
        
        'Ok所以今天最好搞业绩的方式就是我们去借助新媒体，借助新兴媒体。如果结合AI去搞流量，它就会更猛它就会更猛，所以我们要借助新兴媒体去做流量。我给大家举个例子，在普通人想要赚到大钱里面，大家会发 现在过往你想赚到大钱，你可能要靠送东西、走关系，然后喝大酒，是不是靠这些方式。但是在今天有了新兴媒体，有了短视频出现之后，我们会发现其实有一些普通人也是可以通过短视频迅速成为百万富翁甚至千万富翁的。']
    

    from config.info import OneAPI
    one = OneAPI()
    result = []
    left = 0
    threshold_score = 0.5 

    
    while left < len(text_lists) - 1:
        sentence = text_lists[left]
        current_segment = [sentence]
        right = left + 1
        
        while right < len(text_lists):
            next_sentence = text_lists[right]
            diff = one.similarity(sentence, next_sentence)
            
            if diff > threshold_score:
                current_segment.append(next_sentence)
                sentence += next_sentence
                right += 1
            else:
                break
        
        result.append(" ".join(current_segment))
        left = right
    
    if left < len(text_lists):
        result.append(text_lists[left])


    print("len(result)",len(result))


    for sub in result:
        if len(sub)<=50:
            # 太少的直接不要？
            pass 
        short_sub = one.post_v2(f"帮我将下面的输入进行文字的简化,如果输入文字超过了200字，简化的文字需要简化到50字到100字内 {sub}")
        print(f"前后对比-{sub} ---- {short_sub}")


def image_match():
    sub_text = [
        "你本来只想花个七块钱买可乐，但别人说了一句话，你多花了七块钱买了一杯可乐。只想买可乐的你，又多花了一块钱买了一个大杯。所以，整个流程就是靠单次交易金额提升业绩。第三个靠提升回购频次，让客户不断重复购买。企业要想增加业绩，可以从这三个点入手。但操作难度很大，需要具备长时间的营销经验。现在，结合AI这个时代，有一种最简单、最容易复制、最容易找到业绩的方式，不需要太多的营销技巧，也不需要太多的营销经验。那就是增加客户数。搞流量就像开卷考试，别人怎么搞你就怎么搞。接下来，在你三天两夜的时间里，我会教你如何使用AI去生产更牛逼的内容。",
        
        "麦当劳靠多说一句话每年增加近40亿销售额,你们觉得可怕吗?其实很简单,这家公司是大家基本都接触过的,去麦当劳就是为了买汉堡或可乐。店里的销售员也会鼓励消费者买可乐。所以,大家去麦当劳时,店员也会鼓励消费者点可乐。",
        
        "一个人要加一杯可乐，他告诉你只需要加七块钱。现在有100个人要加可乐，其中有50个人会加。其中有50个人加的是中杯，50个人加的是大杯。所以，问题是谁要加中杯还是加大杯？",
        ]
    pass 
    

if __name__ =="__main__":
    # main_entry()
    # word_reading()

    # word_doc_split()
    image_match()
    

    