import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

text_cols = [
    "Skills", "Current_Job_Title", "Previous_Job_Titles",
    "Target_Job_Description", "Degrees",
    "Field_of_Study", "Certifications"
]

numeric_cols = ["Experience_Years"]
cat_cols = ["Education_Level"]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def preprocess_text(text):
    text = clean_text(text)
    tokens = text.split()
    tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words]
    return " ".join(tokens)

def preprocess_resume(df):
    for col in text_cols:
        df[col] = df[col].fillna("").apply(preprocess_text)

    for col in numeric_cols:
        df[col] = df[col].fillna(0)

    for col in cat_cols:
        df[col] = df[col].fillna("unknown").str.lower().str.strip()

    return df
