from matching.fit_labeler import get_fit_label
from ocr.image_ocr import extract_text_from_image
from ocr.skill_extractor import extract_skills_from_text
from matching.semantic_matcher import semantic_similarity
from matching.skill_matcher import smart_skill_match
from matching.experience_matcher import experience_score
from matching.ats_scorer import compute_ats_score


# -----------------------------
# 1. Extract resume text via OCR
# -----------------------------
resume_text = extract_text_from_image("sample1.png")

print("\n--- OCR TEXT ---\n")
print(resume_text[:800])   # print first part only


# -----------------------------
# 2. Manual job input (for now)
# -----------------------------
job_skills = "Python, machine learning, deep learning, tensorflow, data analysis, pytorch, docker"
job_exp = 3
job_text = """
We are looking for a Data Scientist with strong experience in Python, SQL,
machine learning, and statistical analysis. The candidate should have hands-on
experience in building predictive models and working with large datasets.
"""


# -----------------------------
# 3. TEMP parsing from OCR text
# -----------------------------

resume_skills = extract_skills_from_text(resume_text)
resume_exp = 5


# -----------------------------
# 4. Run ATS pipeline
# -----------------------------
skill_pct = smart_skill_match(resume_skills, str(job_skills).lower())
exp_score = experience_score(resume_exp, job_exp)
sem_score = semantic_similarity(resume_text, job_text)

ats = compute_ats_score(skill_pct, exp_score, sem_score)
label = get_fit_label(ats)


# -----------------------------
# 5. Show results
# -----------------------------
print("\n========== ATS RESULT (FROM PDF OCR) ==========")
print("Skill Match %      :", skill_pct)
print("Experience Score   :", exp_score)
print("Semantic Similarity:", sem_score)
print("Final ATS Score    :", ats)
print("Fit Label          :", label)
print("==============================================\n")
