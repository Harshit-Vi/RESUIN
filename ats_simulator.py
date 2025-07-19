import json

def load_company_profile(company_name):
    with open(f'company_configs/{company_name.lower()}.json') as f:
        return json.load(f)

def score_resume(resume_text, jd_keywords, company_profile):
    score = 0
    found_keywords = []
    
    for kw in company_profile["must_have_keywords"]:
        if kw.lower() in resume_text.lower():
            score += company_profile["weights"]["skills"]
            found_keywords.append(kw)
    
    return {
        "score": min(score, 100),
        "found_keywords": found_keywords,
        "missing_keywords": list(set(company_profile["must_have_keywords"]) - set(found_keywords))
    }
