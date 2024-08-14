
def simple_sentenct_split(text):
    text_split = text.split("\n")
    second_text_split = []
    for text in text_split:
        if len(text)>=5:
            second_text_split.append(text)
    return second_text_split 
