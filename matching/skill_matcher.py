# def skill_match_percentage(resume_skills, job_skills):
#     """
#     resume_skills, job_skills: strings (already preprocessed)
#     """

#     r = set(resume_skills.split())
#     j = set(job_skills.split())

#     if len(j) == 0:
#         return 0.0

#     match = r.intersection(j)
#     score = (len(match) / len(j)) * 100

#     return round(score, 2)

def smart_skill_match(resume_skills_text, job_skills_text):
    resume = set(s.strip().lower() for s in resume_skills_text.split(",") if s.strip())
    job_list = [s.strip().lower() for s in job_skills_text.split(",") if s.strip()]

    if not resume or not job_list:
        return 0.0

    # First 50% of JD skills = more important
    split = max(1, len(job_list)//2)
    important = set(job_list[:split])
    rest = set(job_list[split:])

    imp_match = resume.intersection(important)
    rest_match = resume.intersection(rest)

    # Weighted score (no manual labels)
    score = (
        0.7 * (len(imp_match) / len(important)) +
        0.3 * (len(rest_match) / len(rest) if rest else 0)
    )

    return round(score * 100, 2)

