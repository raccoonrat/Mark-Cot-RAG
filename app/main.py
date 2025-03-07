import streamlit as st
from app.cot_generation import generate_cot
from app.watermark_optimization import generate_watermark_phrase, calculate_embedding
from app.ownership_verification import query_suspected_model, judge_answer, statistical_test
from app.visualization import display_cot_generation, visualize_embeddings, display_verification_results

def main():
    st.title("RAG(r) 知识库版权验证PoC")

    # CoT生成
    question = st.text_input("输入验证问题：")
    if question:
        cots = generate_cot(question)
        display_cot_generation(question, cots)

        # 水印优化
        watermark_phrase = generate_watermark_phrase(question)
        st.write(f"生成的水印短语：{watermark_phrase}")

        # 嵌入可视化
        embeddings = calculate_embedding([question, f"{question} {watermark_phrase}"])
        visualize_embeddings(embeddings)

        # 所有权验证
        answer = query_suspected_model(question, watermark_phrase)
        st.write(f"生成的答案：{answer}")

        # 判断答案
        target_cot = cots.split("\n")[0]  # 假设第一行为目标CoT
        judgment = judge_answer(answer, target_cot)
        st.write(f"判断结果：{judgment}")

        # 统计检验
        results = [1 if judgment == "是" else -1]  # 假设只有一个验证问题
        p_value = statistical_test(results)
        display_verification_results(p_value)

if __name__ == "__main__":
    main()
