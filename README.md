<div align="center">

# 🤖 LangChain Intelligent Agent
### 动态规划 | 混合检索 | 自我反思
Dynamic Planning & Hybrid Retrieval Agent with Self-Reflection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-v0.2-green?style=for-the-badge&logo=chainlink)
![OpenAI](https://img.shields.io/badge/LLM-GPT--4o-orange?style=for-the-badge&logo=openai)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

[功能特性](#-功能特性-features) • [架构流程](#-架构流程-architecture) • [快速开始](#-快速开始-quick-start) • [演示案例](#-演示案例-demos)

</div>

---

## 📖 项目简介 (Introduction)

这是一个基于 **LangChain** 构建的高级 **Agentic Workflow**（代理工作流）系统。

不同于传统的问答机器人，该 Agent 拥有一个**“大脑”**（Planner），能够根据用户的问题类型**动态生成**执行计划。它不再盲目地只查知识库，而是像人类一样思考：是该查内部文档？还是去谷歌搜索最新消息？亦或是直接逻辑推理？

此外，系统内置了 **Critic（批评家）** 节点，对 Agent 的执行结果进行**自我反思**和打分，确保持续优化输出质量。

## ✨ 功能特性 (Features)

* **🧠 动态任务路由 (Dynamic Routing)**
    * **技术类问题** $\rightarrow$ 自动调用 RAG (FAISS 本地向量库)。
    * **时事/通用类** $\rightarrow$ 自动调用 DuckDuckGo 联网搜索。
    * **闲聊/逻辑类** $\rightarrow$ 纯 LLM 推理，跳过检索步骤。

* **🕵️ 智能规划器 (Planner Node)**
    * 摆脱硬编码的 Chain，Agent 会生成结构化的 JSON 步骤表（如 `['search_web', 'summarize']`）。

* **⚖️ 自我反思循环 (Critic Loop)**
    * 执行完每一步后，Critic 会评估结果质量。
    * **Verdict 机制**：如果不通过，触发 `Major Fix`（重新规划）或 `Minor Fix`（修正答案）。

* **📚 混合知识库 (Hybrid Knowledge)**
    * 结合了**私有领域知识**与**互联网实时信息**。

## 🧩 架构流程 (Architecture)

系统通过状态机（State Graph）管理数据流转：

```mermaid
graph TD
    User(用户输入) --> Planner{Planner 规划器}
    
    Planner -->|技术问题| PlanRAG[计划: 查本地库]
    Planner -->|时事问题| PlanWeb[计划: 联网搜索]
    Planner -->|逻辑问题| PlanThink[计划: 直接推理]
    
    PlanRAG & PlanWeb & PlanThink --> Executor(Executor 执行器)
    
    Executor -->|执行步骤| Tools[调用工具: FAISS / DDG]
    Tools --> Executor
    
    Executor -->|步骤完成| Critic{Critic 审稿人}
    
    Critic -->|❌ 驳回| Planner
    Critic -->|✅ 通过| Output(最终输出)
