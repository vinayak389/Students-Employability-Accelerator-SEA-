# 🎓 Students Employability Accelerator (SEA)

An AI-powered employability platform designed to help students and early-career professionals
**discover jobs, optimize resumes, and prepare for interviews** using intelligent agents.

---

## 🎯 Outcome

SEA delivers an **end-to-end employability solution** — from job discovery and resume optimization
to interview preparation — powered by AI and designed specifically for students.

---

## 📁 Project Structure

```text
SEA/
├── .devcontainer/
│   ├── devcontainer.json
│   ├── Dockerfile
│   └── requirements.txt
│
├── agents/
│   ├── __init__.py
│   └── sea_agents.py
│
├── tasks/
│   ├── __init__.py
│   └── sea_tasks.py
│
├── tools/
│   ├── __init__.py
│   └── job_search_tool.py
│
├── utils/
│   ├── ats_engine.py
│   ├── intent_router.py
│   ├── job_ranker.py
│   ├── resume_parser.py
│   └── resume_rewriter.py
│
├── crew.py
├── main.py
├── .env
└── .gitignore
```


---

## 🛠️ Tech Stack

- Python 3.11  
- CrewAI  
- LangChain  
- OpenAI API  
- Tavily API  
- Docker & VS Code Dev Containers  

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites
- Docker Desktop
- Visual Studio Code
- VS Code Dev Containers extension

---

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/vinayak389/Students-Employability-Accelerator-SEA-.git
cd SEA
```

## 3️⃣ Open in Dev Container

Open the project in **Visual Studio Code**, then type 'Ctrl + Shift + P → Dev Containers: Reopen in Container'

The project will open inside a Docker-based Dev Container and all dependencies will be installed automatically.

---

## 4️⃣ Environment Variables

Create a `.env` file in the project root directory with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```
⚠️ Important

Do NOT commit the .env file to GitHub

The .env file is ignored using .gitignore

## 5️⃣ Run the Application

Run the application using the following command:
```bash
python main.py
```
---

## 🧠 How It Works (High Level)

1. User input is passed to `main.py`
2. `intent_router` identifies the user intent  
   *(job search, resume analysis, etc.)*
3. CrewAI agents are initialized in `sea_agents.py`
4. Tasks are executed through `sea_tasks.py`
5. Tools and utility modules process jobs, resumes, and rankings
6. Final output is displayed in the terminal  

*(A Streamlit-based UI is planned for future versions)*

---

## 🔐 Security Notes

- Never commit API keys to the repository
- Always rotate API keys if they are exposed
- The `.env` file is excluded via `.gitignore`

---

## 📌 Future Enhancements

- 🌐 Streamlit-based Web UI
- 📎 Resume upload support (PDF / DOCX)
- 📈 Job match and ATS score visualizations
- 🧠 Skill gap analysis
- 💾 Job bookmarking and tracking
