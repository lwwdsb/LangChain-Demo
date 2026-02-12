#pip install -q langchain langchain-openai langchain-community faiss-cpu tiktoken
from langchain_openai import ChatOpenAI
import os
import getpass

os.environ["OPENAI_API_KEY"] = getpass.getpass("请输入你的 OpenAI API Key: ")

from langchain_core.documents import Document

docs = [
    Document(page_content="LangChain 是一个用于构建 LLM 应用的框架。"),
    Document(page_content="RAG 是检索增强生成技术，用于增强大模型回答的准确性。"),
    Document(page_content="Agent 可以调用工具来执行任务。")
]

print("文档创建成功")

from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

split_docs = text_splitter.split_documents(docs)

print(f"切分后的文档数量: {len(split_docs)}")

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(split_docs, embeddings)

retriever = vectorstore.as_retriever()

#embeddings 和长期向量库初始化（运行一次）
import time

long_term_store = FAISS.from_documents(
    [Document(page_content="初始化")],
    embeddings
)

def store_summary_to_longterm(session_id, summary_text):
    doc = Document(
        page_content=summary_text,
        metadata={"session_id": session_id}
    )
    long_term_store.add_documents([doc])
    from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识助手，根据提供的资料回答问题。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", """
根据以下内容回答问题：

{context}

问题: {input}
""")
])

summary_prompt = ChatPromptTemplate.from_template("""
你是助手。请把下面的对话历史压缩为一段简短、清晰的摘要（中文），保留关键事实/意图/偏好，长度不超过 80 字：

{history}
""")

def summarize_history_with_llm(history_messages):
    """
    history_messages: list of message objects (each has .content)
    返回：字符串 summary
    """
    history_text = "\n".join([m.content for m in history_messages])
    # 调用 prompt + llm
    messages = summary_prompt.invoke({"history": history_text})
    resp = llm.invoke(messages)
    return resp.content

MAX_MESSAGES = 8
KEEP_RECENT = 4

def rag_logic(inputs):
    question = inputs["input"]
    history = inputs.get("chat_history", [])
    session_id = inputs.get("session_id", "default")

    # 压缩逻辑
    if len(history) > MAX_MESSAGES:
        summary = summarize_history_with_llm(history[:-KEEP_RECENT])
        store_summary_to_longterm(session_id, summary)

        from langchain_core.messages import SystemMessage
        history = [SystemMessage(content=f"对话摘要：{summary}")] + history[-KEEP_RECENT:]

    # 长期记忆检索
    longterm_docs = long_term_store.similarity_search(question, k=3)
    longterm_text = "\n\n".join(doc.page_content for doc in longterm_docs)

    docs = retriever.invoke(question)
    docs_text = "\n\n".join(doc.page_content for doc in docs)

    combined_context = f"{longterm_text}\n\n{docs_text}"

    messages = prompt.invoke({
        "context": combined_context,
        "input": question,
        "chat_history": history
    })

    response = llm.invoke(messages)
    return response.content



from langchain_core.runnables import RunnableLambda

rag_chain = RunnableLambda(rag_logic)

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

memory_store = {}

def get_session_history(session_id):
    if session_id not in memory_store:
        memory_store[session_id] = ChatMessageHistory()
    return memory_store[session_id]

rag_with_memory = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

session_id = "user1"

print(rag_with_memory.invoke(
    {"input": "什么是 RAG？"},
    config={"configurable": {"session_id": session_id}}
))

print(rag_with_memory.invoke(
    {"input": "它和 Agent 有什么关系？"},
    config={"configurable": {"session_id": session_id}}
))

print(rag_with_memory.invoke(
    {"input": "什么是 RAG？不要用RAG里的内容"},
    config={"configurable": {"session_id": session_id}}
))

session_id = "user2"
print(rag_with_memory.invoke(
    {"input": "它和 Agent 有什么关系？"},
    config={"configurable": {"session_id": session_id}}
))