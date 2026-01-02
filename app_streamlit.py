import streamlit as st
import requests
import json

BASE_URL = "http://127.0.0.1:8000"

st.title("Students Employability Accelerator (SEA)")

# -------------------------
# Step 1: Discover Jobs
# -------------------------
with st.form("job_search"):
    st.subheader("Discover Jobs")
    user_message = st.text_input("What type of job are you looking for?")
    role_description = st.text_input("Role Description (optional)")
    resume_file = st.file_uploader("Upload Resume (optional)", type=["pdf", "docx"])
    submitted = st.form_submit_button("Discover Jobs")

if submitted:
    files = {"resume": resume_file} if resume_file else None
    data = {"user_message": user_message, "role_description": role_description}
    response = requests.post(f"{BASE_URL}/discover-jobs", data=data, files=files)
    if response.status_code == 200:
        result = response.json()
        st.write(result)
    else:
        st.error(response.text)

# -------------------------
# Step 2: Analyze Resume vs Job Description
# -------------------------
st.subheader("Analyze Resume vs Job Description (Optional)")
jd_text = st.text_area("Paste Job Description here")
resume_file2 = st.file_uploader("Upload Resume for Analysis", type=["pdf", "docx"], key="jd_resume")
if st.button("Analyze Resume vs JD"):
    files2 = {"resume": resume_file2} if resume_file2 else None
    data2 = {"job_description": jd_text}
    response2 = requests.post(f"{BASE_URL}/analyze-resume-jd", data=data2, files=files2)
    if response2.status_code == 200:
        analysis = response2.json()
        st.session_state["resume_analysis"] = analysis
        st.session_state["resume_text"] = resume_file2.getvalue().decode("utf-8") if resume_file2 else ""
        st.session_state["job_description"] = jd_text
        st.success("Resume analysis complete")
        st.write(analysis)
    else:
        st.error(response2.text)

# -------------------------
# Step 3: Follow-up / Career Guidance
# -------------------------
st.subheader("Ask a Career Question / Follow-up on Resume")
st.write("If your question is about your resume, please upload the same resume and/or job description.")

followup_resume = st.file_uploader("Upload Resume for Follow-up (optional)", type=["pdf", "docx"], key="followup_resume")
followup_jd = st.text_area("Paste Job Description (optional)", key="followup_jd")
question = st.text_input("Your question")

if st.button("Ask"):
    # Use session state from previous analysis if available
    resume_text = st.session_state.get("resume_text")
    job_description = st.session_state.get("job_description")
    analysis_summary = st.session_state.get("resume_analysis")

    # Override if user uploaded new resume or JD in follow-up
    if followup_resume:
        resume_text = followup_resume.getvalue().decode("utf-8")
    if followup_jd:
        job_description = followup_jd
    if not analysis_summary and (resume_text and job_description):
        st.warning("You need to analyze your resume first before asking resume-related questions!")
        st.stop()

    payload = {
        "question": question,
        "resume_text": resume_text,
        "job_description": job_description,
        "analysis_summary": analysis_summary
    }
    headers = {"Content-Type": "application/json"}
    response3 = requests.post(f"{BASE_URL}/resume-followup", data=json.dumps(payload), headers=headers)
    if response3.status_code == 200:
        answer = response3.json()["answer"]
        st.write(answer)
    else:
        st.error(response3.text)
