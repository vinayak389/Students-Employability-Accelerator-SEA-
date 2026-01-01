import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Students Employability Accelerator (SEA)")

# Step 1: Discover Jobs
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

# Step 2: Resume ↔ JD Analysis
st.subheader("Analyze Resume vs Job Description (Optional)")
jd_text = st.text_area("Paste Job Description here")
resume_file2 = st.file_uploader("Upload Resume for Analysis", type=["pdf", "docx"], key="jd_resume")
if st.button("Analyze Resume vs JD"):
    files2 = {"resume": resume_file2} if resume_file2 else None
    data2 = {"job_description": jd_text}
    response2 = requests.post(f"{BASE_URL}/analyze-resume-jd", data=data2, files=files2)
    if response2.status_code == 200:
        analysis = response2.json()
        st.write(analysis)
    else:
        st.error(response2.text)
