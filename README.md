# LangChain Advanced Agent: Planner, RAG & Critic

![LangChain](https://img.shields.io/badge/LangChain-v0.1.20-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)

本项目展示了一个基于 **LangChain** 构建的高级 Agent 架构。不同于普通的问答机器人，该系统引入了 **Planner（规划器）**、**Executor（执行器）** 和 **Critic（批评家/审稿人）** 机制，实现了具备**自我规划**和**自我反思**能力的智能代理。

## 🌟 核心功能 (Key Features)

本项目实现了一个复杂的 **Agentic Workflow**，包含以下核心组件：

1.  **RAG (检索增强生成)**:
    * 使用 FAISS 和 OpenAI Embeddings 构建本地向量知识库。
    * 包含 LangChain、RAG、Agent 的基础技术文档。
2.  **Planner (规划器)**:
    * 在执行任务前，先生成严格的 4 步执行计划（搜索 -> 阅读 -> 分析 -> 输出）。
    * 输出结构化的 JSON 格式计划。
3.  **Executor (执行代理)**:
    * 基于 `OpenAI Functions` 的 Agent。
    * 具备调用工具（知识库检索、长期记忆检索）的能力。
4.  **Critic (批评家/审稿人)**:
    * **自我反思机制**：对每一步的执行结果进行打分和评估。
    * **Verdict 机制**：
      * `accept`: 结果通过，继续下一步。
      * `minor_fix`: 结果尚可，但需要微调（自动调用 LLM 进行 Patch）。
      * `major_fix`: 结果严重错误，触发 **Re-Plan（重新规划）** 流程。
5.  **Memory (记忆系统)**:
    * **Short-term**: 基于 Session ID 的会话历史管理。
    * **Long-term**: 模拟长期向量记忆存储（可扩展）。

## 🛠️ 技术栈 (Tech Stack)

* **LangChain (v0.1.20)**: 核心框架。
* **OpenAI GPT-4o-mini**: 用于规划、执行和评估的底层大模型。
* **FAISS**: 向量数据库，用于 RAG 检索。
* **TikToken**: Token 计算工具。

## 🚀 快速开始 (Quick Start)

### 1. 环境准备

建议使用 Python 3.10+ 环境。

```bash
# 克隆仓库
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

# 安装依赖
pip install langchain==0.1.20 langchain-openai langchain-community faiss-cpu tiktoken
```
