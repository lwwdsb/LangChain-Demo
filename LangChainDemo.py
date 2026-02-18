{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "L4",
      "authorship_tag": "ABX9TyOmvQAdYswlsmvAyVfyPcYH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lwwdsb/LangChain-Demo/blob/main/LangChainDemo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vkd12j1_GMbk",
        "outputId": "161e17e1-f96f-42f7-89aa-761b017406eb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/87.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m87.2/87.2 kB\u001b[0m \u001b[31m8.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.5/2.5 MB\u001b[0m \u001b[31m66.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m23.8/23.8 MB\u001b[0m \u001b[31m123.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.0/1.0 MB\u001b[0m \u001b[31m73.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m500.5/500.5 kB\u001b[0m \u001b[31m48.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m64.7/64.7 kB\u001b[0m \u001b[31m7.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m51.0/51.0 kB\u001b[0m \u001b[31m6.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-colab 1.0.0 requires requests==2.32.4, but you have requests 2.32.5 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mFound existing installation: langchain 1.2.10\n",
            "Uninstalling langchain-1.2.10:\n",
            "  Successfully uninstalled langchain-1.2.10\n",
            "Found existing installation: langchain-core 1.2.13\n",
            "Uninstalling langchain-core-1.2.13:\n",
            "  Successfully uninstalled langchain-core-1.2.13\n",
            "Found existing installation: langchain-community 0.4.1\n",
            "Uninstalling langchain-community-0.4.1:\n",
            "  Successfully uninstalled langchain-community-0.4.1\n",
            "Found existing installation: langgraph 1.0.8\n",
            "Uninstalling langgraph-1.0.8:\n",
            "  Successfully uninstalled langgraph-1.0.8\n",
            "Collecting langchain\n",
            "  Downloading langchain-1.2.10-py3-none-any.whl.metadata (5.7 kB)\n",
            "Collecting langchain-core\n",
            "  Using cached langchain_core-1.2.13-py3-none-any.whl.metadata (4.4 kB)\n",
            "Collecting langchain-community\n",
            "  Using cached langchain_community-0.4.1-py3-none-any.whl.metadata (3.0 kB)\n",
            "Collecting langgraph\n",
            "  Downloading langgraph-1.0.8-py3-none-any.whl.metadata (7.4 kB)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in /usr/local/lib/python3.12/dist-packages (from langchain) (2.12.3)\n",
            "Requirement already satisfied: jsonpatch<2.0.0,>=1.33.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (1.33)\n",
            "Requirement already satisfied: langsmith<1.0.0,>=0.3.45 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (0.7.3)\n",
            "Requirement already satisfied: packaging>=23.2.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (26.0)\n",
            "Requirement already satisfied: pyyaml<7.0.0,>=5.3.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (6.0.3)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (9.1.4)\n",
            "Requirement already satisfied: typing-extensions<5.0.0,>=4.7.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (4.15.0)\n",
            "Requirement already satisfied: uuid-utils<1.0,>=0.12.0 in /usr/local/lib/python3.12/dist-packages (from langchain-core) (0.14.0)\n",
            "Requirement already satisfied: langchain-classic<2.0.0,>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (1.0.1)\n",
            "Requirement already satisfied: SQLAlchemy<3.0.0,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (2.0.46)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.32.5 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (2.32.5)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (3.13.3)\n",
            "Requirement already satisfied: dataclasses-json<0.7.0,>=0.6.7 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (0.6.7)\n",
            "Requirement already satisfied: pydantic-settings<3.0.0,>=2.10.1 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (2.12.0)\n",
            "Requirement already satisfied: httpx-sse<1.0.0,>=0.4.0 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (0.4.3)\n",
            "Requirement already satisfied: numpy>=1.26.2 in /usr/local/lib/python3.12/dist-packages (from langchain-community) (2.0.2)\n",
            "Requirement already satisfied: langgraph-checkpoint<5.0.0,>=2.1.0 in /usr/local/lib/python3.12/dist-packages (from langgraph) (4.0.0)\n",
            "Requirement already satisfied: langgraph-prebuilt<1.1.0,>=1.0.7 in /usr/local/lib/python3.12/dist-packages (from langgraph) (1.0.7)\n",
            "Requirement already satisfied: langgraph-sdk<0.4.0,>=0.3.0 in /usr/local/lib/python3.12/dist-packages (from langgraph) (0.3.5)\n",
            "Requirement already satisfied: xxhash>=3.5.0 in /usr/local/lib/python3.12/dist-packages (from langgraph) (3.6.0)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.5.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (2.6.1)\n",
            "Requirement already satisfied: aiosignal>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.4.0)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (25.4.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.8.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (6.7.1)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (0.4.1)\n",
            "Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.12/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community) (1.22.0)\n",
            "Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /usr/local/lib/python3.12/dist-packages (from dataclasses-json<0.7.0,>=0.6.7->langchain-community) (3.26.2)\n",
            "Requirement already satisfied: typing-inspect<1,>=0.4.0 in /usr/local/lib/python3.12/dist-packages (from dataclasses-json<0.7.0,>=0.6.7->langchain-community) (0.9.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.12/dist-packages (from jsonpatch<2.0.0,>=1.33.0->langchain-core) (3.0.0)\n",
            "Requirement already satisfied: langchain-text-splitters<2.0.0,>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from langchain-classic<2.0.0,>=1.0.0->langchain-community) (1.1.0)\n",
            "Requirement already satisfied: ormsgpack>=1.12.0 in /usr/local/lib/python3.12/dist-packages (from langgraph-checkpoint<5.0.0,>=2.1.0->langgraph) (1.12.2)\n",
            "Requirement already satisfied: httpx>=0.25.2 in /usr/local/lib/python3.12/dist-packages (from langgraph-sdk<0.4.0,>=0.3.0->langgraph) (0.28.1)\n",
            "Requirement already satisfied: orjson>=3.10.1 in /usr/local/lib/python3.12/dist-packages (from langgraph-sdk<0.4.0,>=0.3.0->langgraph) (3.11.7)\n",
            "Requirement already satisfied: requests-toolbelt>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from langsmith<1.0.0,>=0.3.45->langchain-core) (1.0.0)\n",
            "Requirement already satisfied: zstandard>=0.23.0 in /usr/local/lib/python3.12/dist-packages (from langsmith<1.0.0,>=0.3.45->langchain-core) (0.25.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.41.4 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.41.4)\n",
            "Requirement already satisfied: typing-inspection>=0.4.2 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.4.2)\n",
            "Requirement already satisfied: python-dotenv>=0.21.0 in /usr/local/lib/python3.12/dist-packages (from pydantic-settings<3.0.0,>=2.10.1->langchain-community) (1.2.1)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.32.5->langchain-community) (3.4.4)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.32.5->langchain-community) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.32.5->langchain-community) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.32.5->langchain-community) (2026.1.4)\n",
            "Requirement already satisfied: greenlet>=1 in /usr/local/lib/python3.12/dist-packages (from SQLAlchemy<3.0.0,>=1.4.0->langchain-community) (3.3.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.12/dist-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (4.12.1)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx>=0.25.2->langgraph-sdk<0.4.0,>=0.3.0->langgraph) (0.16.0)\n",
            "Requirement already satisfied: mypy-extensions>=0.3.0 in /usr/local/lib/python3.12/dist-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7.0,>=0.6.7->langchain-community) (1.1.0)\n",
            "Downloading langchain-1.2.10-py3-none-any.whl (111 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m111.7/111.7 kB\u001b[0m \u001b[31m6.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hUsing cached langchain_core-1.2.13-py3-none-any.whl (500 kB)\n",
            "Using cached langchain_community-0.4.1-py3-none-any.whl (2.5 MB)\n",
            "Downloading langgraph-1.0.8-py3-none-any.whl (158 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m158.1/158.1 kB\u001b[0m \u001b[31m12.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: langchain-core, langgraph, langchain-community, langchain\n",
            "Successfully installed langchain-1.2.10 langchain-community-0.4.1 langchain-core-1.2.13 langgraph-1.0.8\n"
          ]
        }
      ],
      "source": [
        "!pip install -q langchain langchain-openai langchain-community faiss-cpu tiktoken\n",
        "\n",
        "!pip uninstall -y langchain langchain-core langchain-community langgraph\n",
        "!pip install -U langchain langchain-core langchain-community langgraph"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_openai import ChatOpenAI\n",
        "print(\"LangChain 正常\")\n",
        "\n",
        "import langchain_core\n",
        "print(langchain_core.__version__)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fvaZooIDGWmZ",
        "outputId": "41f1d782-54e6-4a75-90e5-23093b2d1d20"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "LangChain 正常\n",
            "1.2.13\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import getpass\n",
        "\n",
        "os.environ[\"OPENAI_API_KEY\"] = getpass.getpass(\"请输入你的 OpenAI API Key: \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IoQEdhYhHxlN",
        "outputId": "d4316093-4d04-4e9c-c8d2-969e093a0907"
      },
      "execution_count": 3,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "请输入你的 OpenAI API Key: ··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "准备简易知识库"
      ],
      "metadata": {
        "id": "wFZChJ5aI9Fp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.documents import Document\n",
        "\n",
        "docs = [\n",
        "    Document(page_content=\"LangChain 是一个用于构建 LLM 应用的框架。\"),\n",
        "    Document(page_content=\"RAG 是检索增强生成技术，用于增强大模型回答的准确性。\"),\n",
        "    Document(page_content=\"Agent 可以调用工具来执行任务。\")\n",
        "]\n",
        "\n",
        "print(\"文档创建成功\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DI_xMNblIrdP",
        "outputId": "268a031b-d5d0-4188-e232-e5264ee51903"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "文档创建成功\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "文档切分"
      ],
      "metadata": {
        "id": "21YBs30SJZcu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_text_splitters import CharacterTextSplitter\n",
        "\n",
        "text_splitter = CharacterTextSplitter(\n",
        "    chunk_size=100,\n",
        "    chunk_overlap=20\n",
        ")\n",
        "\n",
        "split_docs = text_splitter.split_documents(docs)\n",
        "\n",
        "print(f\"切分后的文档数量: {len(split_docs)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jBMaykTAJA3Y",
        "outputId": "29f07414-9ec7-4ed5-d26d-7e0d46b03a4e"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "切分后的文档数量: 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "向量化 + 建立向量数据库"
      ],
      "metadata": {
        "id": "SN2Qjfv-J3_s"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_openai import OpenAIEmbeddings\n",
        "from langchain_community.vectorstores import FAISS\n",
        "\n",
        "embeddings = OpenAIEmbeddings()\n",
        "\n",
        "vectorstore = FAISS.from_documents(split_docs, embeddings)\n",
        "\n",
        "retriever = vectorstore.as_retriever()\n",
        "\n",
        "#embeddings 和长期向量库初始化（运行一次）\n",
        "import time\n",
        "\n",
        "long_term_store = FAISS.from_documents(\n",
        "    [Document(page_content=\"初始化\")],\n",
        "    embeddings\n",
        ")\n"
      ],
      "metadata": {
        "id": "nCa8hcsJJkko"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "创建 LLM"
      ],
      "metadata": {
        "id": "_2tQY_i3KC5X"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_openai import ChatOpenAI\n",
        "\n",
        "llm = ChatOpenAI(\n",
        "    model=\"gpt-4o-mini\",\n",
        "    temperature=0\n",
        ")"
      ],
      "metadata": {
        "id": "e9bEAIKnJ9Ii"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def run_llm(prompt_text: str) -> str:\n",
        "    result = llm.invoke(prompt_text)\n",
        "    return result.content"
      ],
      "metadata": {
        "id": "oK3Ixh7oug4d"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "定义 Tools"
      ],
      "metadata": {
        "id": "Bux17rKbLjws"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.tools import tool\n",
        "!pip install -q duckduckgo-search\n",
        "!pip install -U ddgs\n",
        "\n",
        "# 工具 1：知识库检索\n",
        "@tool\n",
        "def search_knowledge_base(query: str) -> str:\n",
        "    \"\"\"当用户询问 LangChain、RAG 或 Agent 技术细节时使用。\"\"\"\n",
        "    docs = retriever.invoke(query)\n",
        "    return \"\\n\\n\".join([d.page_content for d in docs])\n",
        "\n",
        "# 工具 2：长期记忆检索\n",
        "@tool\n",
        "def search_long_term_memory(query: str) -> str:\n",
        "    \"\"\"当用户询问历史总结或之前对话时使用。\"\"\"\n",
        "    docs = long_term_store.similarity_search(query, k=2)\n",
        "    return \"\\n\\n\".join([d.page_content for d in docs])\n",
        "\n",
        "from langchain_community.tools import DuckDuckGoSearchRun\n",
        "\n",
        "# 1. 定义联网搜索工具\n",
        "@tool\n",
        "def search_web(query: str) -> str:\n",
        "    \"\"\"\n",
        "    当问题涉及通用知识（如名人、时事、体育、非技术类问题）时，必须使用此工具。\n",
        "    不要用于 LangChain 或 RAG 的技术定义。\n",
        "    \"\"\"\n",
        "    search = DuckDuckGoSearchRun()\n",
        "    return search.run(query)\n",
        "\n",
        "# 2. 更新工具列表（保留原有的）\n",
        "tools = [search_knowledge_base, search_long_term_memory, search_web]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r1Lz-RGiLkqx",
        "outputId": "4a52a039-de68-49b8-d249-1e71548cf0dc"
      },
      "execution_count": 77,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting ddgs\n",
            "  Downloading ddgs-9.10.0-py3-none-any.whl.metadata (12 kB)\n",
            "Requirement already satisfied: click>=8.1.8 in /usr/local/lib/python3.12/dist-packages (from ddgs) (8.3.1)\n",
            "Requirement already satisfied: primp>=0.15.0 in /usr/local/lib/python3.12/dist-packages (from ddgs) (1.0.0)\n",
            "Requirement already satisfied: lxml>=4.9.4 in /usr/local/lib/python3.12/dist-packages (from ddgs) (6.0.2)\n",
            "Requirement already satisfied: httpx>=0.28.1 in /usr/local/lib/python3.12/dist-packages (from httpx[brotli,http2,socks]>=0.28.1->ddgs) (0.28.1)\n",
            "Collecting fake-useragent>=2.2.0 (from ddgs)\n",
            "  Downloading fake_useragent-2.2.0-py3-none-any.whl.metadata (17 kB)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.12/dist-packages (from httpx>=0.28.1->httpx[brotli,http2,socks]>=0.28.1->ddgs) (4.12.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.12/dist-packages (from httpx>=0.28.1->httpx[brotli,http2,socks]>=0.28.1->ddgs) (2026.1.4)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx>=0.28.1->httpx[brotli,http2,socks]>=0.28.1->ddgs) (1.0.9)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.12/dist-packages (from httpx>=0.28.1->httpx[brotli,http2,socks]>=0.28.1->ddgs) (3.11)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx>=0.28.1->httpx[brotli,http2,socks]>=0.28.1->ddgs) (0.16.0)\n",
            "Requirement already satisfied: brotli in /usr/local/lib/python3.12/dist-packages (from httpx[brotli,http2,socks]>=0.28.1->ddgs) (1.2.0)\n",
            "Requirement already satisfied: h2<5,>=3 in /usr/local/lib/python3.12/dist-packages (from httpx[brotli,http2,socks]>=0.28.1->ddgs) (4.3.0)\n",
            "Collecting socksio==1.* (from httpx[brotli,http2,socks]>=0.28.1->ddgs)\n",
            "  Downloading socksio-1.0.0-py3-none-any.whl.metadata (6.1 kB)\n",
            "Requirement already satisfied: hyperframe<7,>=6.1 in /usr/local/lib/python3.12/dist-packages (from h2<5,>=3->httpx[brotli,http2,socks]>=0.28.1->ddgs) (6.1.0)\n",
            "Requirement already satisfied: hpack<5,>=4.1 in /usr/local/lib/python3.12/dist-packages (from h2<5,>=3->httpx[brotli,http2,socks]>=0.28.1->ddgs) (4.1.0)\n",
            "Requirement already satisfied: typing_extensions>=4.5 in /usr/local/lib/python3.12/dist-packages (from anyio->httpx>=0.28.1->httpx[brotli,http2,socks]>=0.28.1->ddgs) (4.15.0)\n",
            "Downloading ddgs-9.10.0-py3-none-any.whl (40 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m40.3/40.3 kB\u001b[0m \u001b[31m4.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading fake_useragent-2.2.0-py3-none-any.whl (161 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m161.7/161.7 kB\u001b[0m \u001b[31m11.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading socksio-1.0.0-py3-none-any.whl (12 kB)\n",
            "Installing collected packages: socksio, fake-useragent, ddgs\n",
            "Successfully installed ddgs-9.10.0 fake-useragent-2.2.0 socksio-1.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "定义prompt"
      ],
      "metadata": {
        "id": "L8bEgO_3KJiV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder\n",
        "\n",
        "agent_prompt = ChatPromptTemplate.from_messages([\n",
        "    (\"system\",\n",
        "     \"\"\"你是一个智能助手。\n",
        "\n",
        "当用户询问 LangChain、RAG、Agent 的技术细节时，\n",
        "优先调用 search_knowledge_base 工具。\n",
        "\n",
        "当用户询问历史总结时，\n",
        "调用 search_long_term_memory 工具。\n",
        "\n",
        "如果无需查询，直接回答。\n",
        "\"\"\"),\n",
        "    # 不再用 input / chat_history\n",
        "])\n"
      ],
      "metadata": {
        "id": "2stQEomOLIyp"
      },
      "execution_count": 78,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "绑定工具到 LLM"
      ],
      "metadata": {
        "id": "n0X2culzLqfb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "llm_with_tools = llm.bind_tools(tools)"
      ],
      "metadata": {
        "id": "C63sZnuxLtCc"
      },
      "execution_count": 79,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Planner 节点"
      ],
      "metadata": {
        "id": "08IHwZmwLxdg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 引入 DuckDuckGo\n",
        "from langchain_community.tools import DuckDuckGoSearchRun\n",
        "search_tool = DuckDuckGoSearchRun()\n",
        "\n",
        "def planner_node(state):\n",
        "    print(\"🔥 进入 planner_node (动态规划)\")\n",
        "    goal = state.get(\"goal\")\n",
        "\n",
        "    # 核心修改：Prompt 不再强制固定步骤，而是让 LLM 选择工具\n",
        "    prompt = f\"\"\"\n",
        "    你是一个任务规划师。请根据用户目标生成执行步骤列表。\n",
        "\n",
        "    可用动作(Action)说明：\n",
        "    1. \"search_local\": 仅当问题关于 LangChain, RAG, Agent 等内部技术文档时使用。\n",
        "    2. \"search_web\": 当问题关于名人(如 Steph Curry)、时事、通用知识时使用。\n",
        "    3. \"reason\": 当问题是逻辑推理、数学计算、或普通闲聊时使用（不需要搜索）。\n",
        "    4. \"output\": 最后一步必须是 output。\n",
        "\n",
        "    用户目标：\"{goal}\"\n",
        "\n",
        "    请只输出一个 JSON 字符串列表，不要其他废话。\n",
        "    示例 1 (技术问题): [\"search_local\", \"summarize\", \"output\"]\n",
        "    示例 2 (通用问题): [\"search_web\", \"summarize\", \"output\"]\n",
        "    示例 3 (简单对话): [\"reason\", \"output\"]\n",
        "    \"\"\"\n",
        "\n",
        "    raw = run_llm(prompt)\n",
        "\n",
        "    import json, re\n",
        "    try:\n",
        "        plan = json.loads(raw)\n",
        "    except:\n",
        "        # 正则兜底解析\n",
        "        match = re.search(r\"(\\[.*\\])\", raw, re.S)\n",
        "        plan = json.loads(match.group(1)) if match else [\"reason\", \"output\"]\n",
        "\n",
        "    print(f\"✅ 动态生成的计划: {plan}\")\n",
        "\n",
        "    return {\n",
        "        \"plan\": plan,\n",
        "        \"current_step\": 0,\n",
        "        \"step_outputs\": [],\n",
        "        \"finished\": False,\n",
        "        \"critic\": {}\n",
        "    }"
      ],
      "metadata": {
        "id": "dFvOn-N-L0rN"
      },
      "execution_count": 80,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Executor 节点"
      ],
      "metadata": {
        "id": "6l1PwQWYu9Qp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def executor_node(state):\n",
        "    plan = state.get(\"plan\")\n",
        "    idx = state.get(\"current_step\", 0)\n",
        "\n",
        "    if not plan or idx >= len(plan):\n",
        "        return {\"finished\": True}\n",
        "\n",
        "    step = plan[idx]\n",
        "    print(f\"⚙️ Executor 正在执行: {step}\")\n",
        "\n",
        "    output = \"\"\n",
        "\n",
        "    # === 动作分支 ===\n",
        "    if step == \"search_local\":\n",
        "        # 查本地向量库\n",
        "        docs = retriever.invoke(state[\"goal\"])\n",
        "        output = f\"【本地知识库检索结果】：\\n\" + \"\\n\".join([d.page_content for d in docs])\n",
        "\n",
        "    elif step == \"search_web\":\n",
        "        # 查 DuckDuckGo\n",
        "        print(\"   🌐 正在联网搜索...\")\n",
        "        try:\n",
        "            web_result = search_tool.invoke(state[\"goal\"])\n",
        "            output = f\"【互联网搜索结果】：\\n{web_result}\"\n",
        "        except Exception as e:\n",
        "            output = f\"搜索失败: {str(e)}\"\n",
        "\n",
        "    elif step == \"reason\":\n",
        "        # 纯思考/闲聊\n",
        "        output = run_llm(f\"请直接回答或思考以下问题，不要搜索：{state['goal']}\")\n",
        "\n",
        "    elif step == \"summarize\":\n",
        "        # 总结前面的搜索结果\n",
        "        context = \"\\n\\n\".join(state.get(\"step_outputs\", []))\n",
        "        output = run_llm(f\"基于以下搜索到的资料，回答用户目标：'{state['goal']}'。\\n\\n资料：\\n{context}\")\n",
        "\n",
        "    elif step == \"output\":\n",
        "        # 最终输出整理\n",
        "        prev_output = state[\"step_outputs\"][-1] if state[\"step_outputs\"] else \"\"\n",
        "        output = prev_output # 直接透传上一步的总结\n",
        "\n",
        "    else:\n",
        "        # 兜底\n",
        "        output = run_llm(f\"执行步骤 {step}，当前上下文：{state['step_outputs']}\")\n",
        "\n",
        "    return {\n",
        "        \"step_outputs\": state.get(\"step_outputs\", []) + [output],\n",
        "        \"current_step\": idx + 1\n",
        "    }"
      ],
      "metadata": {
        "id": "8MOU2M7KMBWB"
      },
      "execution_count": 81,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Critic 节点"
      ],
      "metadata": {
        "id": "0wM34XA1vIAX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def critic_node(state):\n",
        "    import json, re # Ensure json is imported\n",
        "\n",
        "    prompt = f\"\"\"\n",
        "你是审稿人。\n",
        "\n",
        "目标：\n",
        "{state[\"goal\"]}\n",
        "\n",
        "步骤结果：\n",
        "{state[\"step_outputs\"]}\n",
        "\n",
        "判断：\n",
        "1. 是否完成目标？\n",
        "2. 是否需要重做某一步？\n",
        "\n",
        "输出 JSON：\n",
        "{{\n",
        "  \"accept\": true/false,\n",
        "  \"retry_step\": 数字或null\n",
        "}}\n",
        "\"\"\"\n",
        "\n",
        "    response = run_llm(prompt)\n",
        "\n",
        "    try:\n",
        "        verdict = json.loads(response)\n",
        "    except:\n",
        "        match = re.search(r\"(\\{{.*\\}})\", response, re.S)\n",
        "        if match:\n",
        "            verdict = json.loads(match.group(1))\n",
        "        else:\n",
        "            verdict = {\"accept\": False} # Default to fail if parse error\n",
        "\n",
        "    print(\"🧐 Critic verdict:\", verdict)\n",
        "\n",
        "    updates = {\"critic\": verdict}\n",
        "\n",
        "    # Increment retries if not accepted\n",
        "    if not verdict.get(\"accept\"):\n",
        "        updates[\"retries\"] = state.get(\"retries\", 0) + 1\n",
        "\n",
        "    return updates"
      ],
      "metadata": {
        "id": "dozZSRdDvJOd"
      },
      "execution_count": 82,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "构建 LangGraph"
      ],
      "metadata": {
        "id": "UaZLj0-XMFir"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langgraph.graph import StateGraph, END\n",
        "from typing import TypedDict, List, Optional, Dict, Any\n",
        "\n",
        "# 定义 State 类型，使用 TypedDict\n",
        "class AgentState(TypedDict, total=False):\n",
        "    goal: str\n",
        "    plan: Optional[List[str]]\n",
        "    current_step: int\n",
        "    step_outputs: List[str]\n",
        "    finished: bool\n",
        "    critic: Dict[str, Any]\n",
        "    retries: int\n",
        "\n",
        "\n",
        "graph = StateGraph(AgentState)\n",
        "\n",
        "graph.add_node(\"planner\", planner_node)\n",
        "graph.add_node(\"executor\", executor_node)\n",
        "graph.add_node(\"critic\", critic_node)\n",
        "\n",
        "graph.set_entry_point(\"planner\")\n",
        "\n",
        "graph.add_edge(\"planner\", \"executor\")\n",
        "\n",
        "def executor_decision(state):\n",
        "    if state.get(\"finished\"):\n",
        "        return \"critic\"\n",
        "    return \"executor\"\n",
        "\n",
        "\n",
        "graph.add_conditional_edges(\"executor\", executor_decision)\n",
        "\n",
        "def critic_decision(state):\n",
        "    verdict = state.get(\"critic\", {})\n",
        "    retries = state.get(\"retries\", 0)\n",
        "\n",
        "    if verdict.get(\"accept\"):\n",
        "        print(\"🎉 Critic accepted!\")\n",
        "        return END\n",
        "\n",
        "    if retries >= 3:\n",
        "        print(\"⚠️ 达到最大重试次数，强制结束\")\n",
        "        return END\n",
        "\n",
        "    print(f\"🔄 Critic rejected (Retries: {retries}). Re-planning...\")\n",
        "    return \"planner\"\n",
        "\n",
        "graph.add_conditional_edges(\"critic\", critic_decision)\n",
        "\n",
        "app = graph.compile()"
      ],
      "metadata": {
        "id": "2MlPM2Q_MF0H"
      },
      "execution_count": 83,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "测试运行"
      ],
      "metadata": {
        "id": "YIdKzgv_MKSl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "result = app.invoke({\n",
        "    \"goal\": \"写一篇关于 RAG 的 300 字中文简介\"\n",
        "}, config={\"recursion_limit\": 50})\n",
        "\n",
        "print(result[\"step_outputs\"][-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JuJeiLSLyD5Z",
        "outputId": "a48fd0c4-db0e-4182-aa32-84ed31d03071"
      },
      "execution_count": 86,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🔥 进入 planner_node (动态规划)\n",
            "✅ 动态生成的计划: ['search_local', 'summarize', 'output']\n",
            "⚙️ Executor 正在执行: search_local\n",
            "⚙️ Executor 正在执行: summarize\n",
            "⚙️ Executor 正在执行: output\n",
            "🧐 Critic verdict: {'accept': True, 'retry_step': None}\n",
            "🎉 Critic accepted!\n",
            "RAG（Retrieval-Augmented Generation）是一种检索增强生成技术，旨在提高大型语言模型（LLM）在回答问题时的准确性和相关性。传统的生成模型在处理信息时，往往依赖于其训练时获得的知识，可能会导致回答的准确性不足。而RAG通过结合信息检索和生成模型的优势，能够在生成回答时动态地从外部知识库中提取相关信息，从而提升回答的质量。\n",
            "\n",
            "在RAG的工作流程中，首先会根据用户的查询从知识库中检索出相关文档或信息，然后将这些信息与用户的输入结合，生成更为准确和丰富的回答。这种方法不仅提高了回答的准确性，还能使生成的内容更加贴合用户的需求。\n",
            "\n",
            "LangChain是一个专门用于构建LLM应用的框架，它为开发者提供了构建和集成RAG技术的工具和接口。通过LangChain，开发者可以更方便地实现信息检索与生成的结合，创建出更智能的对话系统和应用。\n",
            "\n",
            "此外，RAG还可以与智能代理（Agent）结合，代理可以调用各种工具来执行特定任务，从而进一步增强系统的功能和灵活性。总之，RAG技术为自然语言处理领域带来了新的可能性，使得机器能够更好地理解和回应人类的需求。\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result = app.invoke({\n",
        "    \"goal\": \"介绍一下Steph Curry\"\n",
        "}, config={\"recursion_limit\": 50})\n",
        "\n",
        "print(result[\"step_outputs\"][-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ss6ZOHAC3ltx",
        "outputId": "8e87f77e-d87d-425e-93c0-88de68d779f1"
      },
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🔥 进入 planner_node (动态规划)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:primp.impersonate:Impersonate 'edge_122' does not exist, using 'random'\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ 动态生成的计划: ['search_web', 'summarize', 'output']\n",
            "⚙️ Executor 正在执行: search_web\n",
            "   🌐 正在联网搜索...\n",
            "⚙️ Executor 正在执行: summarize\n",
            "⚙️ Executor 正在执行: output\n",
            "🧐 Critic verdict: {'accept': True, 'retry_step': None}\n",
            "🎉 Critic accepted!\n",
            "斯蒂芬·库里（Stephen Curry）是一位美国职业篮球运动员，现效力于NBA的金州勇士队。他被广泛认为是历史上最伟大的射手之一，以其出色的三分球能力而闻名。库里于1988年3月14日出生在俄亥俄州的阿克伦，后来在北卡罗来纳州的戴维森学院打球，并在2009年NBA选秀中被金州勇士队以第七顺位选中。\n",
            "\n",
            "库里在职业生涯中取得了诸多成就，包括多次获得NBA最有价值球员（MVP）奖项，并帮助勇士队赢得了多个NBA总冠军。他的比赛风格以快速的投篮和灵活的运球著称，改变了现代篮球的打法，推动了三分球在比赛中的重要性。\n",
            "\n",
            "除了在球场上的成就，库里还积极参与慈善活动，并在社区中发挥影响力。他的职业生涯和个人魅力使他成为全球篮球迷心目中的偶像。\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "result = app.invoke({\n",
        "    \"goal\": \"给我讲个笑话。\"\n",
        "}, config={\"recursion_limit\": 50})\n",
        "\n",
        "print(result[\"step_outputs\"][-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k5b-XnOG4jnk",
        "outputId": "8d0c335c-9d6a-41e0-e65d-8b48ae42f3f4"
      },
      "execution_count": 85,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🔥 进入 planner_node (动态规划)\n",
            "✅ 动态生成的计划: ['reason', 'output']\n",
            "⚙️ Executor 正在执行: reason\n",
            "⚙️ Executor 正在执行: output\n",
            "🧐 Critic verdict: {'accept': True, 'retry_step': None}\n",
            "🎉 Critic accepted!\n",
            "为什么数学书总是很忧伤？\n",
            "\n",
            "因为它有太多的问题！\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "p-Clym0u6fA3"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}