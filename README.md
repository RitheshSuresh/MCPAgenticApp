# 🤖 AI Code Review Agent (LangChain + Azure OpenAI + MCP)

An intelligent AI agent that can **analyze, understand, and suggest improvements for code in a GitHub repository** using:

* **LangChain (Agent orchestration)**
* **Azure OpenAI (GPT-5 nano)**
* **Model Context Protocol (MCP)**
* **GitHub MCP Server (tool access)**

---

# 🚀 Overview

This project demonstrates how to build an **AI Agent that can interact with real-world systems (GitHub)** instead of just answering questions.

The agent:

* Reads code from a GitHub repository
* Understands the logic
* Identifies inefficiencies and bugs
* Suggests optimized improvements

---

# 🧠 Architecture

```text
User Prompt
     ↓
LangChain Agent
     ↓
Azure OpenAI (GPT-5 nano)
     ↓
MCP (Model Context Protocol)
     ↓
GitHub MCP Server
     ↓
GitHub Repository
     ↓
Code Analysis + Suggestions
```

---

# 🔧 Components

## 🧠 Azure OpenAI (GPT-5 nano)

* Provides reasoning and code understanding
* Generates explanations and optimizations

---

## 🧩 LangChain Agent

* Orchestrates the workflow
* Decides when to call tools
* Handles multi-step reasoning

---

## 🔌 MCP (Model Context Protocol)

* Standard interface for tool usage
* Eliminates need for custom API integrations

---

## 🛠 GitHub MCP Server

* Exposes GitHub functionalities as tools:

  * `list files`
  * `get_file_contents`
  * `search_code`
  * `create_pull_request` (optional)

---

## 🔐 GitHub Personal Access Token (PAT)

* Secure authentication for repository access

---

# ⚙️ How It Works

### 1️⃣ User Prompt

```text
Analyze this repository and suggest improvements
```

---

### 2️⃣ Agent Planning

The agent decides:

* First explore repository structure
* Then read relevant files

---

### 3️⃣ Tool Execution (via MCP)

The agent calls tools like:

```text
list_files → get_file_contents
```

---

### 4️⃣ Data Retrieval

GitHub returns:

* File structure
* Code content

---

### 5️⃣ AI Reasoning

The model analyzes:

* Code logic
* Inefficiencies
* Bugs

---

### 6️⃣ Output

The agent generates:

* Code explanation
* Issues identified
* Optimization suggestions
* Improved code snippets

---

# 📦 Setup

## 1️⃣ Create Virtual Environment (PowerShell)

```powershell doesn't work well with python 3.14. use 3.12 or adjust below command based on the version of your python interpreter
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

## 2️⃣ Install Dependencies

```powershell 
pip install langchain langchain-openai langchain-mcp-adapters python-dotenv
```

---

## 3️⃣ Configure Environment Variables

Create a `.env` file:

```env
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name

GITHUB_PAT=your_github_token
GITHUB_MCP_URL=https://api.githubcopilot.com/mcp/
```

---

## 4️⃣ Run the Agent

```powershell
python app.py
```

---

# 🧪 Example Use Case

The agent can analyze inefficient Python code such as:

* Nested loops (O(n²))
* Manual implementations of built-in functions
* Poor algorithm design

And suggest:

* Optimized algorithms
* Cleaner Pythonic code
* Better structure and readability

---

# 📊 Sample Output

```text
Summary:
The repository contains a Python script for basic operations.

Issues:
- Inefficient duplicate detection (O(n²))
- Manual sum calculation
- Suboptimal prime checking

Suggestions:
- Use set() for duplicates
- Use sum() built-in
- Optimize prime check using sqrt(n)
```

---

---

# 🧠 Analogy

```text
LLM → Brain 🧠  
LangChain → Manager 📋  
MCP → Translator 🌉  
GitHub → Workspace 📂  
```

---

# 🚀 Future Enhancements

* Auto-create pull requests with fixes
* Integrate with CI/CD pipelines
* Add support for multiple repositories
* Connect to cloud tools (AWS, Azure billing, etc.)

---

# 🎤 One-Line Summary

> An AI agent that autonomously reads, understands, and improves code from a GitHub repository using standardized tool integration via MCP.

---


👉 or create a **diagram image for this README**
👉 or make it look like a polished portfolio project ⭐
