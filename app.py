from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import Optional
from schemas import IntentRequest, IntentResponse, Job, ResumeJDRequest, ResumeJDAnalysis
from manager import identify_intent
from resume_utils import extract_resume_text
from resume_jd_analyzer import analyze_resume_vs_jd
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os, json

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

app = FastAPI(
    title="Students Employability Accelerator (SEA)",
    version="1.0.0"
)

# -------------------------
# Root endpoint
# -------------------------
@app.get("/")
def root():
    return {"message": "SEA API running. Use POST /discover-jobs or /analyze-resume-jd"}

# -------------------------
# Discover jobs endpoint
# -------------------------
@app.post("/discover-jobs", response_model=IntentResponse)
async def discover_jobs(
    user_message: str = Form(...),
    role_description: Optional[str] = Form(None),
    resume: Optional[UploadFile] = File(None)
):
    # Extract resume text if uploaded
    resume_text = None
    if resume:
        try:
            resume_text = extract_resume_text(resume)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Resume extraction failed: {str(e)}")

    # Identify user intent
    intent_result = identify_intent(
        user_message=user_message,
        resume_summary=resume_text,
        role_description=role_description
    )

    if intent_result["identified_intent"] != "JOB_DISCOVERY":
        return IntentResponse(
            identified_intent=intent_result["identified_intent"],
            explanation=intent_result["explanation"],
            jobs=None
        )

    # -------------------------
    # AI-driven Job Intelligence
    # -------------------------
    prompt = f"""
You are an AI job intelligence engine.

User Message: {user_message}
Resume Text: {resume_text[:4000] if resume_text else "Not provided"}
Role Description: {role_description or "Not provided"}

Generate 10 realistic job opportunities from different job platforms.

Rules:
- Do NOT invent unrealistic roles
- Job title must be clean (no SEO phrases, no counts)
- Matching score must be between 0 and 1
- Provide clear matching rationale
- Use realistic company names
- Use platforms like LinkedIn, Naukri, Indeed, Glassdoor, Foundit

Return STRICT JSON in this format:

[
  {{
    "job_title": "",
    "company_name": "",
    "location": "",
    "job_platform": "",
    "job_url": "",
    "matching_score": 0.0,
    "matching_rationale": "",
    "role_summary": "",
    "full_description": ""
  }}
]
"""

    llm_response = llm.invoke(prompt)

    try:
        jobs_data = json.loads(llm_response.content)
    except Exception:
        jobs_data = []

    jobs = [Job(**job) for job in jobs_data]

    return IntentResponse(
        identified_intent="JOB_DISCOVERY",
        explanation="Jobs dynamically generated and ranked using AI based on user input and resume",
        jobs=jobs
    )

# -------------------------
# Analyze Resume vs Job Description
# -------------------------
@app.post("/analyze-resume-jd", response_model=ResumeJDAnalysis)
async def analyze_resume_jd(
    job_description: str = Form(...),
    resume: Optional[UploadFile] = File(None),
    resume_text: Optional[str] = Form(None)
):
    # Extract resume text if file uploaded
    if resume:
        try:
            resume_text = extract_resume_text(resume)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Resume extraction failed: {str(e)}")

    if not resume_text:
        raise HTTPException(status_code=400, detail="Resume text is required either as file or string")

    # Call analyzer
    analysis = analyze_resume_vs_jd(resume_text, job_description)
    return analysis
