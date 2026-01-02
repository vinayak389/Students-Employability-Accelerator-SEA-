from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# -------------------------
# Load environment
# -------------------------
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_KEY:
    raise ValueError("OPENAI_API_KEY missing in environment")

# -------------------------
# LLM Configuration
# -------------------------
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.6,  # Emergent, non-deterministic behavior
    openai_api_key=OPENAI_KEY
)

# -------------------------
# Intent Identification
# -------------------------
def identify_intent(user_message, resume_summary=None, role_description=None):
    """
    Identify user's primary intent in a dynamic, emergent way.
    """
    agent = Agent(
        role="Intent Manager",
        goal="Identify user intent from free-text input",
        backstory="You are an AI assistant that categorizes user queries into job-related, resume-related, or general career guidance.",
        llm=llm,
        verbose=False
    )

    task = Task(
        description=f"""
User Message: {user_message}
Resume: {resume_summary or "Not provided"}
Role Description: {role_description or "Not provided"}

First, reason carefully about what the user is trying to achieve.
Then decide the BEST primary intent.

Possible intents (not limited to):
- JOB_DISCOVERY
- RESUME_DIAGNOSIS
- RESUME_IMPROVEMENT
- CAREER_GUIDANCE
- UNKNOWN

Format STRICTLY:
Intent: <LABEL>
Explanation: <1-2 sentences of reasoning>
""",
        agent=agent
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential
    )

    result = crew.kickoff()

    intent, explanation = "UNKNOWN", "Unable to determine intent"

    for line in str(result).splitlines():
        if line.startswith("Intent:"):
            intent = line.replace("Intent:", "").strip()
        if line.startswith("Explanation:"):
            explanation = line.replace("Explanation:", "").strip()

    return {"identified_intent": intent, "explanation": explanation}


# -------------------------
# Answer User Doubts (Follow-up Q&A)
# -------------------------
def answer_user_doubt(question, resume_text=None, job_description=None, analysis=None):
    """
    Handles both:
    1. Resume-related questions (needs analysis)
    2. General career guidance (no resume required)
    """

    if analysis is None:
        # General career guidance
        system_prompt = f"""
You are a career guidance AI. Answer the user query in a helpful and actionable way.

User Question: {question}
"""
        response = llm.invoke([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ])
        return response.content

    # Resume-related question
    if not all([resume_text, job_description, analysis]):
        raise ValueError(
            "Please analyze your resume first using /analyze-resume-jd before asking resume-specific questions."
        )

    system_prompt = f"""
You are a career assistant AI.

Answer ONLY using the following information.
Be emergent, context-aware, and provide actionable advice.

Resume (truncated to 3000 chars):
{resume_text[:3000]}

Job Description (truncated to 3000 chars):
{job_description[:3000]}

Analysis Summary:
Overall Score: {analysis.overall_score}
ATS Compatibility: {analysis.ats_compatibility}
Missing Keywords: {analysis.missing_keywords}
Skill Gaps: {analysis.skill_gaps}
Weak Sections: {analysis.weak_sections}
Suggestions: {analysis.improvement_suggestions}

User Question: {question}
"""

    response = llm.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ])

    return response.content
