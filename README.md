LangChain Advanced RAG Demo: 具备长期记忆与自动摘要功能的问答系统本项目是一个基于 LangChain 和 OpenAI (GPT-4o-mini) 构建的高级 RAG（检索增强生成）演示。它不仅实现了基础的知识库检索，还引入了一套动态记忆管理机制：当对话历史过长时，系统会自动将旧的对话内容“压缩”为摘要并存入向量数据库，从而实现了“长期记忆”与“无限上下文”的模拟，同时大幅节省 Token 开销。核心特性双重检索架构 (Dual Retrieval)：知识库检索：检索预设的静态文档（如 RAG、Agent 的定义）。记忆库检索：检索过往对话的摘要，让 AI 能够“回忆”起很久之前的聊天重点。记忆自动压缩 (Memory Summarization)：设定阈值（MAX_MESSAGES = 8），当对话超过限制时，自动调用 LLM 将最早的 4 条消息压缩成 80 字以内的摘要。摘要被向量化存储，并在内存中被替换为一条系统提示，防止上下文溢出。多用户会话隔离 (Session Management)：利用 session_id 区分不同用户（如 user1, user2），实现数据和记忆的完全隔离。
系统架构系统逻辑并非简单的 Chain 堆叠，而是通过自定义逻辑函数 rag_logic 实现复杂的控制流：Code snippet  代码片段graph TD
    User[用户输入 Question] --> Check{历史消息 > 8条?}
  
    %% 记忆压缩流程
    Check -- 是 --> Compress[LLM 生成摘要]
    Compress --> Store[存入长期记忆向量库 (FAISS)]
    Store --> Update[更新短期历史列表 (替换旧消息)]
    Update --> Retrieve
  
    Check -- 否 --> Retrieve
    
    %% 检索流程
    Retrieve[检索阶段]
    Retrieve --> SearchKB[检索静态知识库]
    Retrieve --> SearchMem[检索长期记忆摘要]
    
    %% 生成流程
    SearchKB & SearchMem --> Context[合并上下文 Context]
    Context --> Generator[LLM (GPT-4o-mini)]
    Generator --> Answer[最终回答]
LLMGPT-4o-mini负责回答问题和压缩对话历史。
知识库FAISS + OpenAI Embeddings
FAISS + OpenAI 嵌入存储关于 LangChain、RAG、Agent 的基础定义。
Long-term Store FAISS专门存储对话摘要的向量库，用于长期回忆。
Controller （ rag_logic ）自定义函数，协调检索、压缩和生成逻辑。

快速开始1. 环境准备确保你已经安装了 Python 环境，并安装以下依赖库：
Bash pip install -q langchain langchain-openai langchain-community faiss-cpu tiktoken
配置 API Key 时，系统会提示输入 OpenAI API Key：Pythonimport os
import getpass
os.environ["OPENAI_API_KEY"] = getpass.getpass("请输入你的 OpenAI API Key: ")
运行代码代码将自动执行以下流程：构建知识库：切分文档并建立索引。初始化记忆库：建立空的长期记忆向量库。
对话演示：User 1：进行多轮对话，触发 RAG 检索和上下文关联（如“它和 Agent 有什么关系？”）。User 2：全新会话，验证记忆隔离（User 2 不会受到 User 1 对话的影响）。 代码结构概览环境搭建：安装依赖与 API 配置。知识库构建：定义 docs -> CharacterTextSplitter -> FAISS 向量化。核心逻辑 (rag_logic)：summarize_history_with_llm: 调用 LLM 压缩旧消息。store_summary_to_longterm: 将摘要存入 FAISS。combined_context: 合并“长期记忆检索结果”与“知识库检索结果”。会话管理：使用 RunnableWithMessageHistory 包装核心逻辑，通过 session_id 管理状态。

示例输出User 1 的对话（展示记忆关联）：Q: 什么是 RAG？A: RAG 是检索增强生成技术...Q: 它和 Agent 有什么关系？A: （AI 识别出“它”指 RAG）RAG 和 Agent 的关系在于 Agent 可以调用 RAG 技术...

User 2 的对话（展示隔离）：Q: 它和 Agent 有什么关系？A: （由于没有历史，AI 会泛指）Agent 是一个可以调用工具的实体... LangChain 可以用来构建 Agent...该项目旨在演示如何在生产环境中处理长对话窗口限制，并为构建具备“长期记忆”的 AI 助手提供参考原型。