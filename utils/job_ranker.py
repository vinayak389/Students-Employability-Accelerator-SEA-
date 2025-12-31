from utils.ats_engine import ats_analysis

def rank_jobs(resume_text: str, jobs: list) -> list:
    """
    jobs = [
      {
        "title": "",
        "company": "",
        "location": "",
        "description": "",
        "url": ""
      }
    ]
    """

    ranked_jobs = []

    for job in jobs:
        ats_result = ats_analysis(resume_text, job["description"])

        ranked_jobs.append({
            "job_title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "url": job["url"],
            "match_score": ats_result.get("semantic_match_score", 0),
            "ats_score": ats_result.get("ats_score", 0),
            "matched_skills": ats_result.get("matched_skills", []),
            "missing_skills": ats_result.get("missing_skills", []),
            "match_rationale": ats_result.get("strengths", [])
        })

    return sorted(
        ranked_jobs,
        key=lambda x: x["match_score"],
        reverse=True
    )
