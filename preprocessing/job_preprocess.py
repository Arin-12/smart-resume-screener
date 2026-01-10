import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

text_cols = ["Title", "Skills", "Responsibilities", "Keywords"]

# -------------------------
# Text cleaning functions
# -------------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_text(text):
    text = clean_text(text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)

# -------------------------
# Experience parser (MEDIAN logic)
# -------------------------
def parse_experience(exp):
    """
    Convert experience strings to numeric value using MEDIAN for ranges.
    Examples:
      '0-1'        -> 0.5
      '2-5'        -> 3.5
      '5+'         -> 5.0
      '3-6 years'  -> 4.5
    """
    if pd.isna(exp):
        return 0.0

    exp = str(exp).lower().strip()

    # Case: '5+'
    if "+" in exp:
        nums = re.findall(r"\d+", exp)
        if nums:
            return float(nums[0])

    # Case: range '2-5', '3–6'
    if "-" in exp or "–" in exp:
        nums = re.findall(r"\d+", exp)
        if len(nums) >= 2:
            low = float(nums[0])
            high = float(nums[1])
            return (low + high) / 2

    # Case: already numeric like '3'
    try:
        return float(exp)
    except:
        return 0.0

# -------------------------
# Main preprocessing function
# -------------------------
def preprocess_job(df):
    # Text preprocessing
    for col in text_cols:
        df[col] = df[col].fillna("").apply(preprocess_text)

    # Raw experience column
    df["YearsOfExperience"] = df["YearsOfExperience"].fillna(0)

    # NEW: numeric experience with median logic
    df["YearsOfExperience_num"] = df["YearsOfExperience"].apply(parse_experience)

    return df
