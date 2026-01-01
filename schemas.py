from pydantic import BaseModel
from typing import Optional, List

# -------------------------
# Job Models
# -------------------------
class Job(BaseModel):
    job_title: str
    company_name: str
    location: str
    job_platform: str
    job_url: str
    matching_score: float
    matching_rationale: str
    role_summary: str
    full_description: str

# -------------------------
# Resume ↔ JD Analysis Model
# -------------------------
class ResumeJDAnalysis(BaseModel):
    overall_score: float
    ats_compatibility: float
    missing_keywords: List[str]
    skill_gaps: List[str]
    weak_sections: List[str]
    improvement_suggestions: List[str]

# -------------------------
# API Request Models
# -------------------------
class IntentRequest(BaseModel):
    user_message: str
    resume_summary: Optional[str] = None
    role_description: Optional[str] = None

class ResumeJDRequest(BaseModel):
    job_description: str
    resume_text: Optional[str] = None  # optional if uploaded file is provided

# -------------------------
# Unified API Response
# -------------------------
class IntentResponse(BaseModel):
    identified_intent: str
    explanation: str
    jobs: Optional[List[Job]] = None
    resume_analysis: Optional[ResumeJDAnalysis] = None
