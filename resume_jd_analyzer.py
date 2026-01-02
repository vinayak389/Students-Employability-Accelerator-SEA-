from langchain_openai import ChatOpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

def analyze_resume_vs_jd(resume_text: str, job_description: str):
    """
    Returns resume vs JD analysis with overall score, skill gaps,
    ATS compatibility, and improvement suggestions
    """

    prompt = f"""
You are an expert ATS and HR resume analyzer.

Resume Text:
{resume_text[:4000]}

Job Description:
{job_description[:4000]}

Tasks:
1. Evaluate alignment of resume to JD.
2. Score overall match (0 to 1).
3. List missing keywords.
4. Highlight skill gaps.
5. Identify weak sections in resume.
6. Score ATS compatibility (0 to 1).
7. Provide actionable suggestions to improve resume for this JD.

Return STRICT JSON:

{{
  "overall_score": 0.0,
  "missing_keywords": [],
  "skill_gaps": [],
  "weak_sections": [],
  "ats_compatibility": 0.0,
  "improvement_suggestions": []
}}
"""

    response = llm.invoke(prompt)

    try:
        analysis = json.loads(response.content)
    except Exception:
        analysis = {
            "overall_score": 0.0,
            "missing_keywords": [],
            "skill_gaps": [],
            "weak_sections": [],
            "ats_compatibility": 0.0,
            "improvement_suggestions": []
        }

    return analysis


def answer_user_doubt(user_question: str, analysis: dict):
    """
    Answers user's resume-related questions using existing analysis
    """

    prompt = f"""
You are an AI resume coach.

Resume Analysis:
{json.dumps(analysis, indent=2)}

User Question:
"{user_question}"

Rules:
- Clearly explain rejection reasons
- Refer to missing keywords, ATS score, and skill gaps
- Give actionable suggestions
- Keep explanation simple

Answer:
"""

    response = llm.invoke(prompt)
    return response.content
