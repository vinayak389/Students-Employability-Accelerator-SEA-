def detect_intent(text: str) -> str:
    text = text.lower()

    if "ats" in text or "analyze" in text or "match" in text:
        return "resume_analysis"
    if "rewrite" in text or "optimize" in text or "tailor" in text:
        return "resume_rewrite"
    if "interview" in text:
        return "interview_prep"
    if "job" in text or "opening" in text:
        return "job_search"

    return "general"
