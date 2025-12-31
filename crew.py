from crewai import Crew
from agents.sea_agents import SEAAgents
from tasks.sea_tasks import SEATasks
from utils.intent_router import detect_intent
from utils.job_ranker import rank_jobs  # adjust path if needed


class SEACrew:

    def run(self, user_query: str):
        agents = SEAAgents()
        tasks = SEATasks()

        intent = detect_intent(user_query)

        if intent == "job_search":
            agent = agents.job_search_agent()

            # Step 1: search jobs
            jobs = agent.tools[0].invoke(user_query)

            # Step 2: rank jobs if resume exists
            if "Resume:" in user_query:
                resume_text = user_query.split("Resume:")[1]
                ranked = rank_jobs(resume_text, jobs)
                return ranked

            return jobs

        elif intent == "resume_analysis":
            agent = agents.resume_analysis_agent()

            task = tasks.resume_analysis_task(
                agent,
                {
                    "resume": user_query.split("Resume:")[1].split("User Question:")[0],
                    "job_description": user_query.split("User Question:")[1]
                }
            )

        elif intent == "resume_rewrite":
            agent = agents.resume_writer_agent()

            resume_text = user_query.split("Resume:")[1].split("User Question:")[0]
            jd_text = user_query.split("User Question:")[1]

            task = tasks.resume_rewrite_task(
                agent,
                resume_text,
                jd_text
            )

        elif intent == "interview_prep":
            agent = agents.interview_prep_agent()
            task = tasks.interview_prep_task(agent, user_query)

        else:
            agent = agents.general_career_agent()
            task = tasks.general_task(agent, user_query)

        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True
        )

        return crew.kickoff()
