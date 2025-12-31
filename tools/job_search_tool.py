from langchain.tools import tool
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_jobs(query: str):
    """
    Search jobs and return normalized job data
    """
    response = client.search(
        query=f"{query} job description",
        max_results=5
    )

    jobs = []

    for r in response.get("results", []):
        jobs.append({
            "title": r.get("title", "Unknown"),
            "company": r.get("source", "Unknown"),
            "location": "Not specified",
            "description": r.get("content", ""),
            "url": r.get("url")
        })

    return jobs
