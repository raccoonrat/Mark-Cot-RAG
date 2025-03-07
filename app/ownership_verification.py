import openai
from scipy.stats import wilcoxon

def query_suspected_model(question, watermark_phrase):
    """
    查询可疑模型。
    """
    watermarked_question = f"{question} {watermark_phrase}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": watermarked_question}
        ]
    )
    return response.choices[0].message['content']

def judge_answer(answer, target_cot):
    """
    判断答案是否包含目标CoT的关键信息。
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个专业的判断助手。"},
            {"role": "user", "content": f"目标推理链：{target_cot}。生成的答案：{answer}。请判断生成的答案是否包含目标推理链的关键信息？请回答：是/否。"}
        ]
    )
    return response.choices[0].message['content']

def statistical_test(results):
    """
    进行Wilcoxon符号秩检验。
    """
    return wilcoxon(results).pvalue
