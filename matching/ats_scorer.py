def compute_ats_score(skill_pct, exp_score, sem_score):
    """
    skill_pct: 0–100
    exp_score: 0–1
    sem_score: 0–1
    """

    ats = (
        0.4 * (skill_pct / 100) +
        0.3 * sem_score +
        0.3 * exp_score
    )

    return round(ats * 100, 2)   # final score out of 100
