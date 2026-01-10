from ocr.pdf_ocr import extract_text_from_pdf
from ocr.skill_extractor import extract_skills_from_text
from matching.fit_labeler import get_fit_label
from matching.semantic_matcher import semantic_similarity
from matching.skill_matcher import smart_skill_match   # or your final matcher
from matching.experience_matcher import experience_score
from matching.ats_scorer import compute_ats_score


# -----------------------------
# 1. OCR from PDF
# -----------------------------
resume_text = extract_text_from_pdf("Arin Jain Resume.pdf")

print("\n--- OCR TEXT (first 800 chars) ---\n")
print(resume_text[:800])


# -----------------------------
# 2. Extract skills from OCR text
# -----------------------------
resume_skills = extract_skills_from_text(resume_text)

print("\nEXTRACTED SKILLS FROM OCR:")
print(resume_skills)


# -----------------------------
# 3. Job details (for testing)
# -----------------------------
job_skills = "python, machine learning, deep learning, tensorflow, data analysis, docker, git"
job_exp = 1

job_text = """
We are looking for a Machine Learning Engineer with strong skills in Python,
machine learning, deep learning and TensorFlow. Experience in data analysis,
Docker and Git is a plus.
"""


# -----------------------------
# 4. Temporary experience value
# -----------------------------
# (Later you can auto-extract from OCR)
resume_exp = 1


# -----------------------------
# 5. ATS pipeline
# -----------------------------
skill_pct = smart_skill_match(resume_skills, job_skills)
exp_score = experience_score(resume_exp, job_exp)
sem_score = semantic_similarity(resume_text, job_text)

ats = compute_ats_score(skill_pct, exp_score, sem_score)
label = get_fit_label(ats)


# -----------------------------
# 6. Final output
# -----------------------------
print("\n========== ATS RESULT (FROM PDF OCR) ==========")
print("Skill Match %      :", skill_pct)
print("Experience Score   :", exp_score)
print("Semantic Similarity:", sem_score)
print("Final ATS Score    :", ats)
print("Fit Label          :", label)
print("==============================================\n")
