import streamlit as st
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def display_cot_generation(question, cots):
    """
    展示CoT生成结果。
    """
    st.write(f"问题：{question}")
    st.write("生成的推理链：")
    st.write(cots)

def visualize_embeddings(embeddings):
    """
    可视化嵌入。
    """
    pca = PCA(n_components=2)
    embeddings_2d = pca.fit_transform(embeddings)
    plt.figure(figsize=(8, 6))
    plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])
    st.pyplot(plt)

def display_verification_results(p_value):
    """
    展示验证结果。
    """
    st.write(f"验证结果：p值 = {p_value}")
    if p_value < 0.01:
        st.write("检测到未经授权的知识库使用！")
    else:
        st.write("未检测到未经授权的知识库使用。")
