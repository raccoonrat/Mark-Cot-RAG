    Mark-Cot-RAG/
    │
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    │
    ├── app/
    │   ├── __init__.py
    │   ├── cot_generation.py
    │   ├── watermark_optimization.py
    │   ├── ownership_verification.py
    │   ├── visualization.py
    │   └── main.py
    │
    ├── config/
    │   ├── config.yaml
    │   └── secrets.toml
    │
    ├── data/
    │   ├── knowledge_base/
    │   │   └── natural_questions_subset.json
    │   └── verification_questions.json
    │
    ├── models/
    │   ├── contriever/
    │   │   ├── config.json
    │   │   └── pytorch_model.bin
    │   └── deepseek/
    │       ├── config.json
    │       └── pytorch_model.bin
    │
    ├── tests/
    │   ├── test_cot_generation.py
    │   ├── test_watermark_optimization.py
    │   ├── test_ownership_verification.py
    │   └── test_visualization.py
    │
    └── utils/
        ├── embedding_utils.py
        ├── statistical_utils.py
        └── validation_utils.py

### 1. 核心文件说明

#### 1.1 `app/` 目录

* `__init__.py`：Python包初始化文件。
* `cot_generation.py`：链式推理（CoT）生成模块，包含调用DeepSeek API生成推理链的函数。
* `watermark_optimization.py`：水印短语与目标CoT优化模块，包含生成水印短语、优化目标CoT的函数。
* `ownership_verification.py`：所有权验证模块，包含查询可疑模型、判断答案、统计检验的函数。
* `visualization.py`：可视化模块，包含使用Streamlit构建交互式界面的函数。
* `main.py`：主程序入口，整合各模块功能，运行Streamlit应用。

#### 1.2 `config/` 目录

* `config.yaml`：配置文件，存储模型参数、数据路径等配置信息。
* `secrets.toml`：存储API密钥等敏感信息，使用Streamlit的secrets管理功能。

#### 1.3 `data/` 目录

* `knowledge_base/`：知识库数据集，如Natural Questions子集。
* `verification_questions.json`：验证问题数据文件，存储用于验证的问答对。

#### 1.4 `models/` 目录

* `contriever/`：Contriever模型文件，包含模型配置和权重。
* `deepseek/`：DeepSeek模型文件，包含模型配置和权重。

#### 1.5 `tests/` 目录

* 测试脚本，用于验证各模块功能的正确性。

#### 1.6 `utils/` 目录

* `embedding_utils.py`：嵌入计算工具函数，如计算文本嵌入、嵌入降维等。
* `statistical_utils.py`：统计检验工具函数，如Wilcoxon符号秩检验。
* `validation_utils.py`：验证工具函数，如验证答案是否包含目标CoT的关键信息。


3. 运行项目

1. 安装依赖项：

    pip install -r requirements.txt

2. 运行Streamlit应用：

    streamlit run app/main.py

3. 在浏览器中打开应用，进行交互和验证。

以上代码结构和示例代码实现了一个完整的基于RAG的检索增强语言模型知识库版权保护PoC项目。

