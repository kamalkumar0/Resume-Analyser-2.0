---
title: Resume Analyser2.0
emoji: 👀
colorFrom: red
colorTo: pink
sdk: docker
pinned: false
license: apache-2.0
short_description: This is simple prediction model based Flask app.
---

Here’s a professional-style README file in English for your project **Resume Analyser 2.0** (built with Flask). You can copy this into your repository and adjust any sections as needed.

---

# Resume Analyser 2.0

Live demo: [https://huggingface.co/spaces/kamalsharma0/Resume_Analyser2.0](https://huggingface.co/spaces/kamalsharma0/Resume_Analyser2.0)

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Getting Started](#getting-started)

   1. [Prerequisites](#prerequisites)
   2. [Installation](#installation)
   3. [Running the App](#running-the-app)
5. [Usage](#usage)
6. [Demo Screenshots](#demo-screenshots)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

## Overview

Resume Analyser 2.0 is a web application built with Flask that allows users to upload a resume (in e.g. PDF or DOCX format) and gets it analysed to extract key information, score it or provide suggestions (customise this section with your exact functionality). The app is hosted via the Hugging Face Spaces platform at the link above.

## Features

* Upload a resume file (PDF, DOCX, etc)
* Extract personal details, skills, experience summary (adjust according to what your analyzer does)
* Automated scoring or rating of resume (if applicable)
* Provide feedback or suggestions for improving the resume (if applicable)
* Simple and responsive web UI built using Flask

## Tech Stack

* **Backend**: Flask (Python)
* **Frontend**: HTML / CSS / JS (or if you used any framework mention here)
* **Hosting / Deployment**: Hugging Face Spaces
* **Others**: Any libraries you used (e.g., `pdfplumber`, `docx`, `Spacy`, `pandas`, etc) — list them

## Getting Started

### Prerequisites

* Python 3.x installed
* (Optional) Virtual environment tool (e.g., `venv` or `conda`)
* The required Python packages (see `requirements.txt`)

### Installation

1. Clone this repository:

   ```bash
   git clone https://huggingface.co/spaces/kamalsharma0/Resume_Analyser2.0
   cd Resume_Analyser2.0
   ```
2. Create and activate a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. Export or set environment variables (if required):

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development   # for debug mode
   ```
2. Run the Flask server:

   ```bash
   flask run
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000` (or the URL provided).
   *(If hosted on Hugging Face, the deployment URL is already live.)*

## Usage

* Navigate to the home page.
* Click the “Upload” button and select your resume file.
* The system will process the file and display extracted details / analysis.
* Review the results and see suggestions (if any).
* Download/save the analysis report (if the feature exists).

## Demo Screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e91587a5-aea3-4165-87ff-0a627d4e9801" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2fae737f-2a3d-4d8a-a9e1-6b9e650792cc" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9f815753-a2ff-41c0-b6cd-fe8034be6b2f" />


## Project Structure

```
Resume_Analyser2.0/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
├── resume_processing/
│   ├── extract.py
│   └── score.py
├── uploads/
└── README.md
```

*(Adjust the folder/file names to match your actual structure.)*

## Contributing

Contributions are welcome! If you’d like to help:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeatureName`
3. Make your changes and commit them: `git commit -m "Add your message"`
4. Push to the branch: `git push origin feature/YourFeatureName`
5. Create a Pull Request.

Please ensure your code follows styling guidelines, is well-documented, and includes tests (if applicable).

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Contact

**Kamal Sharma** — 

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
