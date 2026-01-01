from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# -------------------------
# Load .env file
# -------------------------
load_dotenv()  # must be before using OpenAI
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment. Please set it in your .env file.")

# -------------------------
# LLM (ChatOpenAI)
# -------------------------
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    openai_api_key=OPENAI_KEY  # explicitly pass the key
)


def identify_intent(user_message: str,
                    resume_summary: str | None = None,
                    role_description: str | None = None):
    """
    CrewAI Manager Agent:
    Identifies the user's primary intent with JOB_DISCOVERY as default
    """

    # -------------------------
    # Manager Agent
    # -------------------------
    manager = Agent(
        role="Intent Manager",
        goal="Identify the user's primary intent accurately",
        backstory="You are responsible for routing user requests to the correct AI agent.",
        llm=llm,
        verbose=True
    )

    # -------------------------
    # Task
    # -------------------------
    intent_task = Task(
        description=f"""
Analyze the following user input and identify the user's intent.

IMPORTANT RULES:
- If the user is asking about jobs, roles, opportunities, matching, or exploration → choose JOB_DISCOVERY
- If a resume is provided but the user does NOT explicitly ask for analysis → still choose JOB_DISCOVERY
- Choose RESUME_DIAGNOSIS ONLY if the user clearly asks to analyze or evaluate their resume
- Choose RESUME_IMPROVEMENT ONLY if the user asks how to improve or rewrite resume
- Default intent should ALWAYS be JOB_DISCOVERY

User Message:
{user_message}

Resume Summary (if any):
{resume_summary or "Not provided"}

Role Description (if any):
{role_description or "Not provided"}

Choose ONE intent label from:
- JOB_DISCOVERY
- RESUME_DIAGNOSIS
- RESUME_IMPROVEMENT
- INTERVIEW_PREPARATION
- CAREER_GUIDANCE
- UNKNOWN

Respond STRICTLY in this format:
Intent: <INTENT_LABEL>
Explanation: <short explanation>
""",
        expected_output="Intent label and explanation",
        agent=manager
    )

    # -------------------------
    # Crew
    # -------------------------
    crew = Crew(
        agents=[manager],
        tasks=[intent_task],
        process=Process.sequential
    )

    result = crew.kickoff()

    # -------------------------
    # Safe Output Parsing
    # -------------------------
    intent = "UNKNOWN"
    explanation = "Could not determine intent."

    for line in str(result).splitlines():
        if line.startswith("Intent:"):
            intent = line.replace("Intent:", "").strip()
        elif line.startswith("Explanation:"):
            explanation = line.replace("Explanation:", "").strip()

    return {
        "identified_intent": intent,
        "explanation": explanation
    }
