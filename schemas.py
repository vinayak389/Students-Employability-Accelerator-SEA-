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
# Follow-up Q&A Models
# -------------------------
class FollowUpQuestionRequest(BaseModel):
    question: str
    resume_text: Optional[str] = None
    job_description: Optional[str] = None
    analysis_summary: Optional[ResumeJDAnalysis] = None

class FollowUpQuestionResponse(BaseModel):
    answer: str

# -------------------------
# Unified API Response
# -------------------------
class IntentResponse(BaseModel):
    identified_intent: str
    explanation: str
    jobs: Optional[List[Job]] = None
    resume_analysis: Optional[ResumeJDAnalysis] = None
