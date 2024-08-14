from lmdeploy import pipeline
from lmdeploy.vl import load_image

pipe = pipeline(r'E:\Code\OpenGVLabMini-InternVL-Chat-4B-V1-5') 
#! 更详细的info:https://lmdeploy.readthedocs.io/en/latest/inference/vl_pipeline.html


def get_images_content(image_path,text):
    image = load_image(image_path)
    response = pipe((text, image))
    # print(response)
    return response