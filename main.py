import pandas as pd

from matching.fit_labeler import get_fit_label
from preprocessing.resume_preprocess import preprocess_resume
from preprocessing.job_preprocess import preprocess_job
from features.text_builder import build_resume_text, build_job_text
from matching.semantic_matcher import semantic_similarity
from matching.skill_matcher import smart_skill_match
from matching.experience_matcher import experience_score
from matching.ats_scorer import compute_ats_score

# Load data
resume = pd.read_csv("datasets/resume_dataset_1200.csv")
job = pd.read_csv("datasets/job_dataset.csv")

# Preprocess
resume = preprocess_resume(resume)
job = preprocess_job(job)

# Build text
resume = build_resume_text(resume)
job = build_job_text(job)

# -------------------------
# TEST: one resume vs one job
# -------------------------
r = resume.loc[1]
j = job.loc[1]

# 1. Skill match
skill_pct = smart_skill_match(r["Skills"], j["Skills"])

# 2. Experience match
exp_score = experience_score(
    r["Experience_Years"],
    j["YearsOfExperience_num"]
)


# 3. Semantic similarity
sem_score = semantic_similarity(
    r["resume_text"],
    j["job_text"]
)

# 4. Final ATS score
ats = compute_ats_score(skill_pct, exp_score, sem_score)
label = get_fit_label(ats)

print("\n========== ATS RESULT (FROM PDF OCR) ==========")
print("Skill Match %      :", skill_pct)
print("Experience Score   :", exp_score)
print("Semantic Similarity:", sem_score)
print("Final ATS Score    :", ats)
print("Fit Label          :", label)
print("==============================================\n")


