import sqlite3
from resume_classifier import ResumeClassifier
from normalizer import Normalizer

classifier = ResumeClassifier()

def run():

def connect_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def fetch_resume_ids(resume_count):
    return []

def fetch_skills(resume_id):
    
    conn = connect_db('data/main.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM SKILLS WHERE resume_id=?', (resume_id))
    rows = cursor.fetchall()

    conn.close()

    return rows

def update_resume_category(category, resume_id):

    conn = connect_db('data/main.db')
    cursor = conn.cursor()

    cursor.excecute('INSERT INTO RESUME (CATEGORY) VALUES ? WHERE resume_id=?',
                    (category, resume_id))

    conn.commit()
    conn.close()

def categorize_resume():
    resume_ids = fetch_resume_ids()
    normalizer = Normalizer()

    for resume_id in resume_ids:
        skills = fetch_skills(resume_id)
        skills = normalizer.interpolate_skills(skills)
        outputs = classifier.classify(skills)
        index = np.argmax(outputs)
        category = ''

        if index == 0:
            category = 'Software Developer'
        elif index == 1:
            category = 'Software Engineer'
        elif index == 2:
            category = 'System Analyst'
        elif index == 3:
            category = 'Web Developer'

        update_resume_category(category, resume_id)


if __name__ == '__main__':
    run()