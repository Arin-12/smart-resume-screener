import re

COMMON_SKILLS = [
    "python", "sql", "machine learning", "deep learning", "nlp",
    "data science", "statistics", "tensorflow", "pytorch",
    "docker", "aws", "git", "linux", "computer vision",
    "data analysis", "pandas", "numpy", "scikit-learn",
    "r", "tableau", "power bi","nltk","SQL","MongoDB","C#",".net core",
    "ci/cd"," Kubernetes", "REST APIs","Cybersecurity","Software Engineering",
    "Neural Networks","Java","Deep Learning","Generative AI","LLMs",
    "Problem-solving","Communication","Teamwork","Creativity",
    "Android Studio","Kotlin","UI/UX","Firebase","C++","JavaScript",
    "Node.js","Express.j","flask","Django","PostgreSQ","Azure",
    "Apache Spark",""
    ]

def extract_skills_from_text(text: str):
    text = text.lower()
    found = []

    for skill in COMMON_SKILLS:
        # match full skill phrase
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found.append(skill)

    return ", ".join(found)
