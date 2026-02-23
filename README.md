# 🇧🇩 Bangladesh Multi-Agent Data Router

A production-oriented **Multi-Agent RAG system** built with **LangChain** and **GPT-4.1**.  
The system intelligently routes natural language queries to structured SQLite databases or a web search tool, ensuring accurate and hallucination-controlled responses.

---

## 🚀 Core Features

- 🧠 Intent-Based Router Agent  
- 🗄 Domain-Specific SQL Agents  
- 🌐 Web Search Fallback (DuckDuckGo API)  
- ❌ Zero-Hallucination Enforcement  
- 🧩 Modular & Scalable Architecture  

---

## 🏗️ Architecture

```
User Query
     ↓
Router Agent
     ↓
Hospitals DB | Institutions DB | Restaurants DB | Web Search
```

---

## 🛠️ Tech Stack

- LangChain  
- OpenAI GPT-4.1  
- SQLite  
- DuckDuckGo Search API  
- Python 3.x  

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/codebysajed/Multi-Tool-AI-Agent.git
cd Multi-Tool-AI-Agent
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```
GITHUB_API=your_openai_or_github_models_key
BASE_URL=your_api_base_url
```

---

## 🗄️ Initialize Database

```bash
python csv_to_sqlitedb.py
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 📌 Engineering Highlights

- Multi-Agent Orchestration  
- LLM-Driven SQL Query Generation  
- Structured Data Retrieval  
- Production-Style Prompt Engineering  

---

## 💡 System Design Philosophy

- **Modular Design:** Router and domain agents are decoupled for easy maintenance and scalability.  
- **Separation of Concerns:** Each SQL agent handles only its own dataset, reducing cross-domain errors.  
- **Zero-Hallucination Enforcement:** Strict prompts and fallback mechanisms ensure data integrity.  
- **Extensibility:** New datasets or tools can be integrated with minimal code changes.  
- **Scalable Workflow:** Agent orchestration allows for future multi-threaded or API-driven deployments.
