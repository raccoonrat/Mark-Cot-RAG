import openai
from sentence_transformers import SentenceTransformer

def generate_watermark_phrase(question):
    """
    生成水印短语。
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个专业的水印短语生成助手。"},
            {"role": "user", "content": f"为问题“{question}”生成一个包含2-5个罕见词且不改变语义的后缀。"}
        ]
    )
    return response.choices[0].message['content']

def calculate_embedding(text):
    """
    计算文本嵌入。
    """
    model = SentenceTransformer('sentence-transformers/contriever')
    return model.encode(text)
