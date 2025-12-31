from langchain_openai import ChatOpenAI
from textwrap import dedent
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def ats_analysis(resume_text: str, jd_text: str) -> dict:
    prompt = dedent(f"""
    You are an ATS (Applicant Tracking System).

    Analyze the RESUME against the JOB DESCRIPTION.

    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {jd_text}

    Return ONLY valid JSON in this format:

    {{
      "ats_score": number (0-100),
      "semantic_match_score": number (0-100),
      "matched_skills": [list],
      "missing_skills": [list],
      "missing_keywords": [list],
      "strengths": [list],
      "weaknesses": [list]
    }}
    """)

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except Exception:
        return {
            "error": "Failed to parse ATS analysis",
            "raw_output": response.content
        }
