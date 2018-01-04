import sqlite3
from resume_classifier import ResumeClassifier
from normalizer import Normalizer

classifier = ResumeClassifier()

def run():

def fetch_resume_ids(resume_count):
    return []

def fetch_skills(resume_id):
    return []

def categorize_resume():
    resume_ids = fetch_resume_ids()
    normalizer = Normalizer()

    for resume_id in resume_ids:
        skills = fetch_skills(resume_id)
        skills = normalizer.interpolate_skills(skills)
        classifier.classify(skills)



if __name__ == '__main__':
    run()