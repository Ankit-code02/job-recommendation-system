from utils.job_data import JOB_ROLES

def recommend_jobs(user_skills, domain):
    recommendations = []
    total_score = 0
    count = 0

    user_skills = [s.lower() for s in user_skills]

    for job in JOB_ROLES:
        if job["domain"] != domain:
            continue

        required_skills = [s.lower() for s in job["skills"]]

        matched_skills = set(user_skills) & set(required_skills)
        missing_skills = set(required_skills) - matched_skills

        score = len(matched_skills) / len(required_skills)
        score_percent = round(score * 100, 2)

        total_score += score
        count += 1

        recommendations.append({
            "title": job["title"],
            "score": score_percent,
            "matched_skills": list(matched_skills),
            "missing_skills": list(missing_skills),
            "total_required": len(required_skills)
        })

    overall_match_score = round((total_score / count) * 100, 2) if count else 0
    return recommendations, overall_match_score
