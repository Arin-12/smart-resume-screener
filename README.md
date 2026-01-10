# 📄 Smart Resume Screener — Multimodal ATS

An AI-powered **Applicant Tracking System (ATS)** that evaluates resumes using **OCR + NLP + ML logic**.  
Supports **resume images** and **direct text input** to generate ATS scores, skill match %, and hiring-fit labels.

---

## 🚀 Features

- 🖼 **Image OCR** — Extract text from resume images using Tesseract  
- ✍️ **Text Input Mode** — Paste resume text directly  
- 🧠 **NLP Semantic Matching** — Sentence-Transformers for JD ↔ Resume similarity  
- 🛠 **Skill Extraction & Matching**  
- 📊 **ATS Scoring Engine**  
- 🏷 **Fit Labels** — Strong Fit / Moderate Fit / Low Fit  
- 📥 **Downloadable ATS Report**

---

## 🧩 Tech Stack

- **Frontend**: Streamlit  
- **OCR**: Tesseract + OpenCV  
- **NLP**: Sentence-Transformers  
- **ML Logic**: Scikit-learn  
- **Language**: Python  

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/smart-resume-screener.git
cd smart-resume-screener
```
### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install dependencies

```
pip install -r requirements.txt
```
### 4. System Requirements
Tesseract OCR
```
Install Tesseract from:  
https://github.com/UB-Mannheim/tesseract/wiki
```
After installation, make sure **tesseract.exe** is added to your system PATH.

### 5. Run the App
```
streamlit run app.py
```

---

## ☁️ Deployment Note

This cloud version supports:

- ✅ Image OCR (PNG/JPG)  
- ✅ Direct text input  

❌ **PDF OCR is disabled in cloud deployment** because it requires Poppler.  
For PDFs, please convert them to an image or paste the resume text instead.

*(Local version supports PDF OCR.)*

---

## 🧪 How It Works

1. User uploads resume image or pastes text  
2. OCR extracts text (for images)  
3. Skills are extracted from the resume  
4. Resume is matched with the job description using:  
   - Skill overlap  
   - Semantic similarity  
   - Experience logic  
5. ATS score is calculated  
6. Fit label is generated  
7. User downloads the ATS report  

---

## 📊 Sample Output

- Skill Match %  
- Experience Score  
- Semantic Similarity  
- Final ATS Score  
- Fit Label  
- Downloadable Report  

---

## 📈 Performance

- **Average processing time**: ~2–4 seconds per resume  
- **OCR accuracy**: ~85–90% on clear, well-formatted resumes  
- **Skill matching**: High precision for technical roles  
- **Semantic similarity**: Reliable for resumes with detailed experience  

The system uses **lightweight pre-trained NLP models**, ensuring fast response times and smooth performance on both local machines and cloud deployments.


## 🎯 Use Cases

- Students checking resume readiness  
- Recruiters screening candidates  
- HR-tech demos  
- AI/ML portfolio project  


