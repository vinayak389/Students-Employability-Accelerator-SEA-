from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.job_search_tool import search_jobs

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)

class SEAAgents:

    def job_search_agent(self):
        return Agent(
            role="Job Search Expert",
            goal="Find real jobs across multiple platforms",
            backstory="Expert in job portals and hiring trends",
            tools=[search_jobs],
            llm=llm,
            verbose=True
        )

    def resume_analysis_agent(self):
        return Agent(
            role="Resume Analyst",
            goal="Analyze resume vs job description",
            backstory="Expert in ATS and resume screening",
            llm=llm,
            verbose=True
        )

    def resume_writer_agent(self):
        return Agent(
            role="Resume Writer",
            goal="Rewrite resume tailored to job description",
            backstory="Professional resume writer",
            llm=llm,
            verbose=True
        )

    def interview_prep_agent(self):
        return Agent(
            role="Interview Coach",
            goal="Prepare candidates for interviews",
            backstory="Senior interview coach",
            llm=llm,
            verbose=True
        )

    def general_career_agent(self):
        return Agent(
            role="Career Mentor",
            goal="Answer general career-related questions",
            backstory="Experienced career guidance expert",
            llm=llm,
            verbose=True
        )
