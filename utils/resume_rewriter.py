from langchain_openai import ChatOpenAI
from textwrap import dedent
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

def rewrite_resume(resume_text: str, jd_text: str, ats_output: dict) -> dict:
    prompt = dedent(f"""
    You are a professional resume writer.

    Rewrite the resume to better match the job description,
    using the ATS analysis provided.

    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {jd_text}

    ATS ANALYSIS:
    Missing Skills: {ats_output.get("missing_skills")}
    Missing Keywords: {ats_output.get("missing_keywords")}

    RULES:
    - Do NOT invent experience
    - Improve wording, structure, impact
    - Use STAR format where applicable
    - Be ATS friendly

    Return ONLY valid JSON in this format:

    {{
      "optimized_summary": "string",
      "optimized_experience": [ "bullet 1", "bullet 2" ],
      "optimized_skills": [ "skill1", "skill2" ],
      "recommended_keywords": [ "keyword1", "keyword2" ]
    }}
    """)

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except Exception:
        return {
            "error": "Failed to rewrite resume",
            "raw_output": response.content
        }
