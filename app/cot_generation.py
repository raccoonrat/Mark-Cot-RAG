import openai

def generate_cot(question):
    """
    生成两种不同的推理链（CoT）。
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个专业的推理链生成助手。"},
            {"role": "user", "content": f"问题：{question}。请生成两种不同的推理链，确保逻辑独立且答案正确。"}
        ]
    )
    return response.choices[0].message['content']


import requests
import json

def generate_cot_with_moonshot(question):
    """
    使用Moonshot生成链式推理（CoT）。
    """
    # Moonshot API的URL
    url = "https://api.moonshot.com/v1/generate"

    # 请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"
    }

    # 请求体
    data = {
        "question": question,
        "prompt": "Please provide a step-by-step chain of thought for the following question:"
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 检查响应状态
    if response.status_code == 200:
        # 解析响应
        result = response.json()
        return result["cot"]
    else:
        print(f"Error: {response.status_code}")
        return None
