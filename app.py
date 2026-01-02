from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import Optional
from schemas import (
    IntentResponse,
    Job,
    ResumeJDAnalysis,
    FollowUpQuestionRequest,
    FollowUpQuestionResponse
)
from manager import identify_intent, answer_user_doubt
from resume_utils import extract_resume_text
from resume_jd_analyzer import analyze_resume_vs_jd
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os, json

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.6,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

app = FastAPI(
    title="Students Employability Accelerator (SEA)",
    version="1.0.0"
)

# -------------------------
# Root
# -------------------------
@app.get("/")
def root():
    return {"message": "SEA API running. Use /discover-jobs, /analyze-resume-jd, /resume-followup"}

# -------------------------
# Discover Jobs
# -------------------------
@app.post("/discover-jobs", response_model=IntentResponse)
async def discover_jobs(
    user_message: str = Form(...),
    role_description: Optional[str] = Form(None),
    resume: Optional[UploadFile] = File(None)
):
    resume_text = None
    if resume:
        try:
            resume_text = extract_resume_text(resume)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    intent_result = identify_intent(
        user_message=user_message,
        resume_summary=resume_text,
        role_description=role_description
    )

    if intent_result["identified_intent"] != "JOB_DISCOVERY":
        return IntentResponse(
            identified_intent=intent_result["identified_intent"],
            explanation=intent_result["explanation"]
        )

    prompt = f"""
You are an AI job intelligence engine.

User Message: {user_message}
Resume Text: {resume_text[:4000] if resume_text else "Not provided"}
Role Description: {role_description or "Not provided"}

Generate 10 realistic job opportunities.

Return STRICT JSON array.
"""

    llm_response = llm.invoke(prompt)

    try:
        jobs_data = json.loads(llm_response.content)
    except Exception:
        jobs_data = []

    jobs = [Job(**job) for job in jobs_data]

    return IntentResponse(
        identified_intent="JOB_DISCOVERY",
        explanation="Jobs generated and ranked using AI",
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
    if resume:
        try:
            resume_text = extract_resume_text(resume)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    if not resume_text:
        raise HTTPException(status_code=400, detail="Resume text required")

    analysis = analyze_resume_vs_jd(resume_text, job_description)
    return analysis

# -------------------------
# Resume Follow-up / Career Guidance
# -------------------------
@app.post("/resume-followup", response_model=FollowUpQuestionResponse)
async def resume_followup(payload: FollowUpQuestionRequest):
    """
    Handles both:
    1. Resume-related questions (requires analysis)
    2. General career guidance questions
    """

    try:
        answer = answer_user_doubt(
            question=payload.question,
            resume_text=payload.resume_text,
            job_description=payload.job_description,
            analysis=payload.analysis_summary
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    return FollowUpQuestionResponse(answer=answer)
