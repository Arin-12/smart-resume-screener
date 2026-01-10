from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(resume_text, job_text):
    emb = model.encode([resume_text, job_text],show_progress_bar=False)
    score = cosine_similarity([emb[0]], [emb[1]])[0][0]
    return round(float(score), 3)


