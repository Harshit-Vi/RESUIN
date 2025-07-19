from resume_parser import extract_text_from_pdf
from jd_parser import extract_keywords
from ats_simulator import load_company_profile, score_resume

resume_text = extract_text_from_pdf("sample_resume.pdf")

with open("sample_jobdesc.txt", "r") as f:
    jd_text = f.read()

jd_keywords = extract_keywords(jd_text)
company = input("Enter target company (e.g., amazon, tcs): ").strip().lower()
company_profile = load_company_profile(company)

result = score_resume(resume_text, jd_keywords, company_profile)

print("\n--- Analysis Result ---")
print("Score:", result["score"])
print("Matched Keywords:", result["found_keywords"])
print("Missing Keywords:", result["missing_keywords"])

