# 🧠 RESUIN – Resume Analyzer & Company-Specific ATS Simulator (Minor Project)

## 📌 Overview

**RESUIN** is a Python-based command-line tool that analyzes resumes and simulates how various companies’ **Applicant Tracking Systems (ATS)** score and sort resumes based on a given **job description**.

It provides personalized suggestions to improve your resume **according to company-specific logic**, helping students and professionals better align their resumes with job requirements.

> 🚀 "We don’t just score resumes — we decode how companies think."

---

## 🎯 Key Objectives

- Simulate real-world ATS logic for companies like **Amazon**, **TCS**, etc.
- Provide **match scores** between a resume and job description.
- Suggest **missing keywords**, weak sections, and areas for improvement.
- Help users tailor their resumes to specific companies' hiring preferences.

---

## ⚙️ How It Works

### 🔄 Input:
1. A resume file (`.pdf` or `.docx`)
2. A job description file (`.txt`)
3. Target company name (e.g., `amazon`)

### 🧠 Processing:
1. Resume is parsed for key sections (Skills, Experience, Projects, etc.)
2. Job description is parsed to extract important keywords.
3. Company-specific ATS logic is loaded from configuration files (e.g., `amazon.json`)
4. The resume is scored using:
   - Keyword matching
   - Section completeness
   - Company-specific weights

### 📊 Output:
- ATS Match Score (0–100%)
- Matched keywords
- Missing keywords
- Suggestions for improvement (based on company profile)

---

## 🧰 Technologies Used

| Area                | Tech / Tools                                      |
|---------------------|---------------------------------------------------|
| Language            | Python 3.x                                        |
| Resume Parsing      | `PyMuPDF` for PDFs, `python-docx` for DOCX        |
| NLP & Keyword Extraction | `spaCy`, `re`, `sklearn.feature_extraction`       |
| CLI Interaction     | `argparse` (optional), raw input                  |
| Data Handling       | JSON (company profiles), basic file I/O           |
| Version Control     | Git + GitHub                                      |
| (Optional UI)       | Streamlit (not included in CLI version)           |

---

## 🧪 Project Structure

```bash
resume-analyzer-cli/
├── main.py                     # Entry point for CLI usage
├── resume_parser.py            # Extracts text from PDF/DOCX
├── jd_parser.py                # Extracts keywords from JD
├── ats_simulator.py            # Loads company logic, scores resume
├── suggestions.py              # Generates improvement tips (optional)
├── sample_resume.pdf           # Test resume
├── sample_jobdesc.txt          # Test job description
├── company_configs/            # Company-specific ATS logic
│   └── amazon.json
├── README.md                   # This file
