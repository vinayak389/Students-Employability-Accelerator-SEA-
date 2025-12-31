# 🎓 Students Employability Accelerator (SEA)

An AI-powered employability platform designed to help students and early-career professionals
**discover jobs, optimize resumes, and prepare for interviews** using intelligent agents.

---

## 🧩 Problem Statements & Solutions

---

### 🔴 Problem Statement 1: No Unified Job Search Across Multiple Portals

#### Problem
Students must manually search across multiple job portals such as LinkedIn, Naukri, Indeed,
Glassdoor, and Foundit. This process is time-consuming, inefficient, and often results in
missing relevant job opportunities.

#### Solution
An **AI-powered Unified Job Search Engine** that aggregates job listings from multiple portals,
ranks them based on aspirational role and resume relevance, and presents them in a single view.

#### Expected Deliverables
- Tabular list of matched jobs:
  - Job Title  
  - Company Name  
  - Location  
  - Job Platform  
  - Job URL  
  - Matching Score  
  - Matching Rationale  
  - One-line Role Summary  
  - Expandable Full Job Description
- Ability to bookmark / save jobs
- Application status markers (Applied, In Progress, Shortlisted, Rejected)

---

### 🔴 Problem Statement 2: No Clarity on Resume ↔ Job Description Fit

#### Problem
Students do not understand why resumes get rejected by ATS systems or HR teams. There is no
visibility into skill gaps, missing keywords, or weak resume sections.

#### Solution
A **Resume vs Job Description Analysis & ATS Scoring Engine** that evaluates alignment both
quantitatively and qualitatively.

#### Deliverables
- ATS Compatibility Score (%)
- Semantic Match Score (%)
- Matched Skills vs Missing Skills
- Missing Tools & Keywords
- Resume Strengths & Weaknesses
- Job Description Requirement Summary
- Visual skill-gap charts
- Downloadable ATS analysis report (PDF)

---

### 🔴 Problem Statement 3: Inability to Rewrite Resume to Match Job Description

#### Problem
Even after identifying gaps, students struggle to professionally rewrite resumes with
impact-driven bullet points and ATS-friendly keywords.

#### Solution
An **AI-powered Resume Customization & Rewrite Engine** tailored to each job description.

#### Deliverables
- AI-optimized resume sections:
  - Professional Summary
  - Enhanced Experience Bullet Points (STAR format)
  - Improved Project Descriptions
  - Optimized Skills Section
  - Recommended ATS Keywords
- Side-by-side Original vs Optimized Resume comparison
- Copy-to-clipboard functionality
- Downloadable tailored resume (PDF / DOCX)

---

### 🔴 Problem Statement 4: No Structured Interview Preparation After Applying

#### Problem
Students lack a structured interview preparation plan after applying or getting shortlisted.

#### Solution
An **AI Interview Preparation Roadmap Generator** providing job-specific interview readiness.

#### Deliverables
- Personalized Interview Preparation Kit:
  - 7 / 14 / 30-day preparation roadmap
  - Job-specific technical questions
  - Behavioral questions with model answers
  - Skill revision topics
  - Mock interview script
  - Interview readiness checklist
- Downloadable interview preparation guide (PDF)

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
├── requirements.txt
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
git clone https://github.com/your-username/SEA.git
cd SEA


## 3️⃣ Open in Dev Container

Open the project in **Visual Studio Code**, then type 'Ctrl + Shift + P → Dev Containers: Reopen in Container'

The project will open inside a Docker-based Dev Container and all dependencies will be installed automatically.

---

## 4️⃣ Environment Variables

Create a `.env` file in the project root directory with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key

⚠️ Important

Do NOT commit the .env file to GitHub

The .env file is ignored using .gitignore

## 5️⃣ Run the Application

Run the application using the following command:
python main.py

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
