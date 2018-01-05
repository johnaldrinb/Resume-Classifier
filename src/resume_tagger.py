import sqlite3
import numpy
from resume_classifier import ResumeClassifier

from resume_classifier import ResumeClassifier
from normalizer import Normalizer

classifier = ResumeClassifier()

def run():
    categorize_resume()

def connect_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def fetch_resume_ids():
    id_file = open('data/resume_id.txt', 'r')
    id_list = id_file.readlines()

    id_file.close()
    print(id_list)

    return id_list

def fetch_skills(resume_id):
    
    conn = connect_db('data/main.db')
    cursor = conn.cursor()

    resume_id = int(resume_id)
    print(resume_id)

    cursor.execute('SELECT SKILL FROM SKILLS WHERE resume_id=?', (resume_id,))
    rows = cursor.fetchall()

    cursor.execute('SELECT FILENAME FROM RESUME WHERE resume_id=?', (resume_id,))
    resume = cursor.fetchall()
    print(resume)

    skills = []

    for row in rows:
        skills.append(row[0])

    conn.close()

    return skills

def update_resume_category(category, resume_id):

    conn = connect_db('data/main.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO RESUME (CATEGORY) VALUES (?) WHERE resume_id=?',
                    (category, resume_id,))

    conn.commit()
    conn.close()

def categorize_resume():
    resume_ids = fetch_resume_ids()
    normalizer = Normalizer()

    print(resume_ids)

    for resume_id in resume_ids:
        skills = fetch_skills(resume_id)

        print(skills)

        skills = normalizer.interpolate_skills(skills)
        lack = 0
        input_size = 75

        if len(skills) < input_size:
            lack = input_size - len(skills)

            for i in range(lack):
                skills.append('-1')

        skills = numpy.array([skills])
        outputs = classifier.classify(skills)
        index = numpy.argmax(outputs)
        category = ''

        print(outputs)

        if index == 0:
            category = 'Software Developer'
        elif index == 1:
            category = 'Software Engineer'
        elif index == 2:
            category = 'System Analyst'
        elif index == 3:
            category = 'Web Developer'

        print(category)
        # update_resume_category(category, resume_id)

if __name__ == '__main__':
    # classifier = ResumeClassifier()
    # classifier.train()
    run()