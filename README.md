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

## 🗂️ Project Structure

SEA/
├── .devcontainer/
│ ├── devcontainer.json
│ ├── Dockerfile
│ └── requirements.txt
│
├── agents/
│ ├── init.py
│ └── sea_agents.py
│
├── tasks/
│ ├── init.py
│ └── sea_tasks.py
│
├── tools/
│ ├── init.py
│ └── job_search_tool.py
│
├── utils/
│ ├── ats_engine.py
│ ├── intent_router.py
│ ├── job_ranker.py
│ ├── resume_parser.py
│ └── resume_rewriter.py
│
├── crew.py
├── main.py
├── requirements.txt
├── .env
└── .gitignore
