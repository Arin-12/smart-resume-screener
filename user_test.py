from matching.semantic_matcher import semantic_similarity
from matching.skill_matcher import skill_match_percentage
from matching.experience_matcher import experience_score
from matching.ats_scorer import compute_ats_score


def get_user_input():
    print("\n--- ENTER RESUME DETAILS ---")
    resume_skills = input("Enter your skills (comma separated): ")
    resume_exp = float(input("Enter your experience (in years): "))
    resume_text = input("Paste short resume summary / profile: ")

    print("\n--- ENTER JOB DETAILS ---")
    job_skills = input("Enter required job skills (comma separated): ")
    job_exp = float(input("Enter required experience (in years): "))
    job_text = input("Paste job description / responsibilities: ")

    return resume_skills, resume_exp, resume_text, job_skills, job_exp, job_text


def test_with_user_input():
    (
        r_skills, r_exp, r_text,
        j_skills, j_exp, j_text
    ) = get_user_input()

    # 1. Skill match
    skill_pct = skill_match_percentage(r_skills.lower(), j_skills.lower())

    # 2. Experience match
    exp_score = experience_score(r_exp, j_exp)

    # 3. Semantic similarity
    sem_score = semantic_similarity(r_text.lower(), j_text.lower())

    # 4. Final ATS score
    ats = compute_ats_score(skill_pct, exp_score, sem_score)

    print("\n========== RESULTS ==========")
    print("Skill Match %      :", skill_pct)
    print("Experience Score   :", exp_score)
    print("Semantic Similarity:", sem_score)
    print("Final ATS Score    :", ats)
    print("=============================\n")


if __name__ == "__main__":
    test_with_user_input()
