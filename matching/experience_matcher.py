def experience_score(resume_exp, job_exp):
    """
    resume_exp, job_exp: numeric (years)
    """

    try:
        resume_exp = float(resume_exp)
        job_exp = float(job_exp)
    except:
        return 0.0   # if conversion fails, give minimum score

    if job_exp == 0:
        return 1.0

    score = min(resume_exp / job_exp, 1.0)
    return round(score, 2)
