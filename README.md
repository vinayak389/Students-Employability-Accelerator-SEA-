# 🎓 Students Employability Accelerator (SEA)

**SEA** is an AI-powered employability platform designed to help students and early-career professionals **discover jobs, optimize resumes, and prepare for interviews** using intelligent AI agents.



---


## 📁 Project Structure

```text
SEA/
├── .devcontainer/
│ └── devcontainer.json
├── .env
├── .gitignore
├── app.py
├── app_ngrok_run.py
├── app_streamlit.py
├── manager.py
├── resume_jd_analyzer.py
├── resume_utils.py
├── schemas.py
├── requirements.txt
└── README.md
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
1) Start the FastAPI server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
2) Run the Streamlit frontend
```bash
streamlit run app_streamlit.py
```

3) run app_ngrok_run.py
```bash
python ./app_ngrok_run.py
```

## 🧠 How It Works (High Level)
User interacts with the Streamlit UI (job search, resume upload, etc.)

Streamlit frontend sends requests to the FastAPI backend

Ngrok exposes FastAPI to the internet for remote access if needed

intent_router identifies the user intent (job search, resume analysis, etc.)

CrewAI agents in manager.py process tasks

Tasks and tools in resume_jd_analyzer.py and resume_utils.py handle jobs, resume parsing, scoring, and ranking

Results are returned to Streamlit and displayed to the user in real-time

This architecture enables a lightweight, interactive AI-powered employability platform accessible from any browser.


---

## 🔐 Security Notes

- Never commit API keys to the repository
- Always rotate API keys if they are exposed
- The `.env` file is excluded via `.gitignore`

---


## 🎯 Outcome

SEA delivers an **end-to-end employability solution** — from job discovery and resume optimization
to interview preparation — powered by AI and designed specifically for students.

---
