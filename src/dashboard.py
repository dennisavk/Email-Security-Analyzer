import streamlit as st
import json


st.title("🧠 Email Security Analyzer Dashboard")


email_file = st.file_uploader("Upload an .eml file", type=["eml"])


if email_file:
with open("samples/temp.eml", "wb") as f:
f.write(email_file.read())
from analyzer import analyze_email
result = analyze_email("samples/temp.eml")
st.subheader("Email Metadata")
st.write(f"**Subject:** {result['subject']}")
st.write(f"**Sender:** {result['sender']}")
st.write(f"**Phishing Score:** {result['phishing_score']}")
st.write(f"**Suspicious?:** {result['is_suspicious']}")


st.subheader("Header Checks")
st.json(result['header_checks'])


st.subheader("Links & VirusTotal Results")
st.json(result['virus_total_results'])


st.subheader("Attachments Scan")
st.json(result['attachments_scan'])
