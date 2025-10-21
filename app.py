from flask import Flask, render_template, request
import pdfplumber, joblib, numpy as np, matplotlib.pyplot as plt, io, base64
# For future multi-format support:
# import docx # pip install python-docx
# from PIL import Image # pip install Pillow
# import pytesseract # pip install pytesseract (requires Tesseract-OCR installed)

from dummy_job_description import JOB_DESC

app = Flask(__name__)

# Load pre-trained model and vectorizer
try:
    model = joblib.load("resume_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except FileNotFoundError:
    print("Error: model.pkl or vectorizer.pkl not found. Please run train_model.py first.")
    # Exit or handle gracefully, e.g., by not allowing resume analysis
    model = None
    vectorizer = None

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file."""
    with pdfplumber.open(pdf_file) as pdf:
        return " ".join(page.extract_text() or "" for page in pdf.pages)

# Placeholder for future multi-format parsing
def extract_text_from_file(file):
    """
    Extracts text from various file types.
    NOTE: DOCX and image parsing are placeholders and require additional libraries
    and implementation.
    """
    file_extension = file.filename.split('.')[-1].lower()
    text = ""
    if file_extension == 'pdf':
        text = extract_text_from_pdf(file)
    elif file_extension in ['doc', 'docx']:
        # Placeholder for DOCX parsing
        # try:
        #     doc = docx.Document(file)
        #     text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        # except Exception as e:
        #     print(f"Error parsing DOCX: {e}")
        text = "DOCX parsing not yet implemented." # Dummy text
    elif file_extension in ['jpg', 'jpeg', 'png']:
        # Placeholder for Image OCR
        # try:
        #     img = Image.open(file)
        #     text = pytesseract.image_to_string(img)
        # except Exception as e:
        #     print(f"Error performing OCR on image: {e}")
        text = "Image OCR not yet implemented." # Dummy text
    else:
        text = "Unsupported file format."
    return text

def word_count(text):
    """Counts the total number of words in a given text."""
    return len(text.split())

def keyword_density(text, keyword="python"):
    """Calculates the density of a specific keyword in the text."""
    words = text.lower().split()
    if not words:
        return 0.0
    return round((words.count(keyword.lower()) / len(words)) * 100, 2)

def match_score(resume_text, job_desc):
    """Calculates a match score between resume text and job description."""
    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())
    if not job_words:
        return 0.0
    return round((len(resume_words.intersection(job_words)) / len(job_words)) * 100, 2)

def recommend_roles(skills):
    """Recommends job roles based on extracted skills."""
    # Convert skills to lowercase for consistent checking
    skills_lower = [s.lower() for s in skills]
    if 'python' in skills_lower and ('data analysis' in skills_lower or 'machine learning' in skills_lower):
        return ['Data Scientist', 'ML Engineer', 'Python Developer']
    elif 'python' in skills_lower:
        return ['Python Developer', 'Software Engineer (Python)']
    elif 'sql' in skills_lower:
        return ['Database Administrator (DBA)', 'Data Analyst (SQL)']
    elif 'java' in skills_lower:
        return ['Java Developer', 'Backend Developer']
    else:
        return ['General IT Support', 'Entry-Level Developer'] # More generic fallback

def get_tips(text):
    """Generates smart tips for resume improvement."""
    tips = []
    text_lower = text.lower()
    if "communication" not in text_lower and "teamwork" not in text_lower:
        tips.append("Consider adding soft skills like 'communication' and 'teamwork' to highlight your interpersonal abilities.")
    if "project" not in text_lower and "achievement" not in text_lower:
        tips.append("Include more quantified achievements and specific project details to showcase your impact.")
    if "certifications" not in text_lower and "courses" not in text_lower:
        tips.append("Highlight any relevant certifications or online courses to demonstrate continuous learning.")
    if not tips:
        tips.append("Your resume looks comprehensive! Keep it updated with your latest accomplishments.")
    return tips

def extract_skills(text):
    """Extracts a predefined list of skills from the text."""
    # Expanded skill list for better detection
    skills_list = [
        'python', 'java', 'c++', 'sql', 'excel', 'power bi', 'tableau',
        'machine learning', 'data analysis', 'deep learning', 'nlp',
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 'linux',
        'javascript', 'html', 'css', 'react', 'angular', 'node.js',
        'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch',
        'api', 'database', 'mongodb', 'postgresql', 'mysql',
        'communication', 'teamwork', 'problem-solving', 'leadership'
    ]
    found_skills = []
    text_lower = text.lower()
    for skill in skills_list:
        if skill in text_lower:
            found_skills.append(skill.capitalize()) # Capitalize for display
    return list(set(found_skills)) # Return unique skills

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    total_words = 0
    keyword_density_val = 0
    match_score_val = 0
    recommended_roles = []
    smart_tips = []
    skill_chart = None

    if request.method == "POST":
        file = request.files.get("resume")
        if file and file.filename != '':
            # Use the new multi-format text extraction function
            text = extract_text_from_file(file)

            if text in ["DOCX parsing not yet implemented.", "Image OCR not yet implemented.", "Unsupported file format."]:
                # Handle cases where parsing is not yet implemented
                prediction = "Parsing Error"
                smart_tips = [text + " Please upload a PDF for full analysis."]
            else:
                total_words = word_count(text)
                keyword_density_val = keyword_density(text)
                match_score_val = match_score(text, JOB_DESC)
                skills = extract_skills(text)
                recommended_roles = recommend_roles(skills)
                smart_tips = get_tips(text)

                # Generate Skill Chart only if skills are found
                if skills:
                    fig, ax = plt.subplots(figsize=(10, 6)) # Larger figure for better readability
                    # Create dummy values for chart (e.g., frequency or just index)
                    # For a real app, you'd count occurrences or assign weights
                    skill_counts = [text.lower().count(s.lower()) for s in skills]
                    # Sort skills by count for better visualization
                    sorted_skills = [s for _, s in sorted(zip(skill_counts, skills), reverse=True)]
                    sorted_counts = sorted(skill_counts, reverse=True)

                    ax.barh(sorted_skills, sorted_counts, color='#007bff', height=0.7) # Horizontal bars
                    ax.set_xlabel('Mentions (Dummy Count)', color='white')
                    ax.set_title('Your Key Skills Overview', color='white')
                    ax.tick_params(axis='x', colors='white')
                    ax.tick_params(axis='y', colors='white')
                    ax.set_facecolor('none') # Transparent plot background
                    fig.patch.set_alpha(0) # Transparent figure background

                    # Adjust layout and save
                    plt.tight_layout()
                    buf = io.BytesIO()
                    plt.savefig(buf, format='png', transparent=True) # Save with transparency
                    skill_chart = base64.b64encode(buf.getvalue()).decode()
                    plt.close(fig) # Close the figure to free memory
                else:
                    skill_chart = None # No chart if no skills

                # Placeholder for actual model prediction (if model is loaded)
                if model and vectorizer:
                    try:
                        resume_vectorized = vectorizer.transform([text])
                        predicted_category_index = model.predict(resume_vectorized)[0]
                        # In a real scenario, you'd map this index back to a category name
                        prediction = predicted_category_index # Using the raw prediction for now
                    except Exception as e:
                        prediction = f"Prediction Error: {e}"
                else:
                    prediction = "Model not loaded."

    return render_template("index.html",
                           prediction=prediction,
                           total_words=total_words,
                           keyword_density=keyword_density_val,
                           match_score=match_score_val,
                           recommended_roles=recommended_roles,
                           smart_tips=smart_tips,
                           skill_chart=skill_chart)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)


