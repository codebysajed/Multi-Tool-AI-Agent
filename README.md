# Bangladesh Multi-Agent Data Router

A production-oriented **Multi-Agent RAG system** built with **LangChain** and **GPT-4.1**.  
The system routes natural language queries to structured SQLite databases or a web search tool, delivering accurate, domain-specific, and hallucination-controlled responses.

---

## 🚀 Core Features

- 🧠 Intelligent Router Agent (intent-based delegation)  
- 🗄 Domain-Specific SQL Agents (Hospitals, Institutions, Restaurants)  
- 🌐 Web Search Fallback (DuckDuckGo API)  
- ❌ Strict Zero-Hallucination Enforcement  
- 🧩 Modular & Ext architecture for easy scalability  

---

## 🏗️ Architecture Overview

```
User Query
     ↓
Router Agent
     ↓
┌─────────────────────────────────────┐
│ Hospitals DB   (SQL Agent)         │
│ Institutions DB (SQL Agent)        │
│ Restaurants DB  (SQL Agent)        │
│ Web Search Tool (Fallback)         │
└─────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

- LangChain  
- OpenAI GPT-4.1  
- SQLite  
- DuckDuckGo Search API  
- Python 3.x  

---

## ⚙️ Quick Start

```bash
git clone https://github.com/codebysajed/Multi-Tool-AI-Agent.git
cd Multi-Tool-AI-Agent
pip install -r requirements.txt
python csv_to_sqlitedb.py
python main.py
```

---

## 📌 Engineering Highlights

- Multi-Agent Orchestration  
- LLM-Driven SQL Query Generation  
- Structured Data Retrieval  
- Clean Tool Routing Logic  
- Production-Style Prompt Engineering  
