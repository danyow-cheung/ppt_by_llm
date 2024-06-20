import sys 
sys.path.append(r"E:\Code\PowerPoint-Generator-Python-Project-main\PowerPoint-Generator-Python-Project-main\aippt_danyow")
from llm.content import generate_ppt_content,re_match_content

if __name__=="__main__":
        
    topic = "机器学习"
    page = 8 
    # content = generate_ppt_content(topic,page)
    
    content ="""机器学习PPT大纲：

<start>

1. 机器学习简介
- 定义
- 应用领域
- 发展历程

<end>

2. 机器学习基本原理
- 监督学习
- 无监督学习
- 深度学习

<start>

3. 数据预处理
- 数据清洗
- 特征工程
- 数据可视化

<end>

4. 模型选择与评估
- 特征重要性
- 模型选择
- 模型评估

<start>

5. 数据挖掘与预测
- 数据挖掘
- 预测
- 评估与比较

<end>

6. 机器学习算法案例
- 线性回归
- 逻辑回归
- 决策树
- 随机森林
- 神经网络

<start>

7. 深度学习项目实战
- 图像分类
- 目标检测
- 自然语言处理

<end>

8. 机器学习发展趋势与展望
- 自动化机器学习
- 联邦学习
- 量子机器学习
- 可解释性机器学习

<start>

注意：以上内容为示例，你可以根据自己的需求和主题进行修改和补充。希望对你的PPT制作有所帮助！
    """
    re_match_content(content,page)

