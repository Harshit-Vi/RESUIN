import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

def extract_keywords(jd_text):
    words = re.findall(r'\b\w+\b', jd_text.lower())
    keywords = [word for word in words if word not in ENGLISH_STOP_WORDS]
    return list(set(keywords))

