from crewai import Task
from textwrap import dedent
from utils.ats_engine import ats_analysis
from utils.job_ranker import rank_jobs
from utils.resume_rewriter import rewrite_resume


class SEATasks:

    def job_search_task(self, agent, query):
        return Task(
            description=dedent(f"""
            Use web search to find relevant jobs.

            User query:
            {query}

            Provide:
            - Job Title
            - Company
            - Location
            - Platform
            - Apply URL
            """),
            expected_output="List of relevant jobs with application links",
            agent=agent
        )

    def resume_analysis_task(self, agent, resume_text, jd_text):
        return Task(
            description=dedent("""
            Perform ATS analysis between resume and job description.
            Provide structured ATS feedback.
            """),
            expected_output="ATS score, matched skills, missing keywords, suggestions",
            agent=agent,
            callback=lambda _: ats_analysis(resume_text, jd_text)
        )

    def job_ranking_task(self, agent, resume_text, jobs):
        return Task(
            description="Rank jobs based on resume match",
            expected_output="Jobs ranked by relevance score",
            agent=agent,
            callback=lambda _: rank_jobs(resume_text, jobs)
        )

    def resume_rewrite_task(self, agent, resume_text, jd_text):
        ats_result = ats_analysis(resume_text, jd_text)

        return Task(
            description="Rewrite resume using ATS analysis",
            expected_output="Rewritten resume optimized for ATS",
            agent=agent,
            callback=lambda _: rewrite_resume(
                resume_text,
                jd_text,
                ats_result
            )
        )

    def interview_prep_task(self, agent, query):
        return Task(
            description=dedent(f"""
            Create interview preparation roadmap.

            Input:
            {query}

            Provide:
            - 7-day plan
            - Technical questions
            - HR questions
            """),
            expected_output="Complete interview preparation plan",
            agent=agent
        )

    def general_task(self, agent, query):
        return Task(
            description=query,
            expected_output="Helpful and relevant career guidance",
            agent=agent
        )
