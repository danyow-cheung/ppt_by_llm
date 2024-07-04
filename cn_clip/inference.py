import torch 
from PIL import Image
import  cn_clip.clip as clip
from cn_clip.clip import load_from_name, available_models,load_from_path 


device = "cuda" if torch.cuda.is_available() else "cpu"
# Available models: ['ViT-B-16', 'ViT-L-14', 'ViT-L-14-336', 'ViT-H-14', 'RN50']

model, preprocess = load_from_name("RN50", device=device)
model.eval()


def feature_match(image_path,text_list):

    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
        
    text = clip.tokenize(text_list).to(device)
    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        # 对特征进行归一化，请使用归一化后的图文特征用于下游任务
        image_features /= image_features.norm(dim=-1, keepdim=True) 
        text_features /= text_features.norm(dim=-1, keepdim=True)    

        logits_per_image, logits_per_text = model.get_similarity(image, text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

    # print("Label probs:", probs) 
    return probs 

