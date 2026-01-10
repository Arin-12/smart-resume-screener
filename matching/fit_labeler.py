def get_fit_label(ats_score: float):
    """
    Convert ATS score (0–100) into a fit label
    """

    if ats_score >= 85:
        return "🟢 Excellent Fit"
    elif ats_score >= 70:
        return "🟡 Strong Fit"
    elif ats_score >= 55:
        return "🟠 Moderate Fit"
    else:
        return "🔴 Weak Fit"
