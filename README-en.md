<div align="center">

# 🤖 LangChain Intelligent Agent

**Dynamic Planning | Hybrid Retrieval | Self-Reflection | Long-Term Memory**

An advanced AI agent with self-correction capabilities, dynamic task planning, and persistent memory.

![Python](https://img.shields.io/badge/PYTHON-3.10+-blue)
![LangChain](https://img.shields.io/badge/LANGCHAIN-v1.2.16-green)
![LLM](https://img.shields.io/badge/LLM-GPT--4o-orange)
![License](https://img.shields.io/badge/LICENSE-MIT-lightgrey)

[Features](#-features) • [Architecture](#-architecture) • [Use Cases](#-use-cases)

</div>

---

## 📖 Introduction

This project is an advanced **Agentic Workflow** system built on top of **LangChain** and **LangGraph**.

Unlike traditional Q&A bots or hard-coded Chains, this Agent possesses a "Brain" (Planner) that dynamically generates **execution plans** based on the user's input. It doesn't blindly search knowledge bases; instead, it thinks like a human: *Should I query internal documents? Search Google for the latest news? Access long-term memory? Or just use logical reasoning?*

Furthermore, the system features a built-in **Critic** node for self-reflection and introduces a brand new **Silent Memory** mechanism. This allows the Agent to "remember" your preferences, enabling a truly personalized and continuous intelligent interaction.

## ✨ Features

* **🧠 Dynamic Task Routing**
  * **Technical Queries** ➔ Automatically triggers RAG (Local FAISS Vector DB).
  * **Current Events/General Info** ➔ Automatically triggers DuckDuckGo web search.
  * **Personal/Historical Queries** ➔ Proactively calls `search_memory` to fetch context.
  * **Chit-chat/Logic** ➔ Pure LLM reasoning, skipping unnecessary retrieval steps.

* **💾 Silent Long-Term Memory `[NEW]`**
  * **Non-intrusive Writing**: Before ending a conversation, a background bypass node (Memory Updater) silently analyzes the dialogue, extracts valuable user preferences or facts, and saves them into an isolated FAISS memory database.
  * **Proactive Recall**: When the user asks about historical context, the Planner proactively schedules a memory retrieval step, creating a "the more we talk, the better it knows you" experience.

* **🗺️ Intelligent Planner Node**
  * Breaking free from fixed templates, the Agent dynamically generates a structured JSON step-by-step plan (e.g., `['search_memory', 'reason', 'output']`) and executes it sequentially.

* **⚖️ Self-Reflection Loop (Critic)**
  * After executing the steps, the Critic evaluates the quality of the result. If the goal is not met, it triggers a retry mechanism, sending the workflow back for **Re-planning** to ensure high-quality final outputs and reduce hallucinations.

## 🧩 Architecture

The system strictly manages state transitions using a **LangGraph** State Graph:

```mermaid
graph TD
    Start((User Input)) --> Planner[🧠 Planner Node<br>Generates JSON Execution Plan]
    Planner --> Executor[⚙️ Executor Node<br>Calls Tools/Actions]
    
    Executor --> Critic{🧐 Critic Node<br>Reflection & Evaluation}
    
    Critic -- "Reject" --> Planner
    Critic -- "Accept" --> MemoryUpdater[🤫 Memory Updater<br>Silently Extracts & Saves Memory]
    Critic -- "Max Retries Reached" --> MemoryUpdater
    
    MemoryUpdater --> End((Output & End))

    subgraph Tools [Available Tools]
        direction TB
        T1(FAISS Local DB)
        T2(DuckDuckGo Search)
        T3(FAISS Memory DB)
    end
    Executor -. "search_local" .-> T1
    Executor -. "search_web" .-> T2
    Executor -. "search_memory" .-> T3
