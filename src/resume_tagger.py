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
    # 
    #   returns a list of id
    # 
    id_file = open('data/resume_id.txt', 'r')
    id_list = id_file.readlines()

    id_file.close()
    # print(id_list)

    return id_list

def fetch_skills(resume_id):
    # 
    #   returns the list of skills of the desired resume
    # 
    
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

def group_list(list, group_size):
    # 
    # function for grouping array elements with desired size
    # 
    grouped_list = []
    temp_group = []
    counter = 0

    lack = 0

    if (len(list) % 5) != 0:
        lack = group_size - (len(list) % group_size)
        for i in range(lack):
            list.append('-1')

    # print(lack)

    # for item in list:
    #     counter += 1
    #     temp_group.append(item)

    #     if counter == group_size:
    #         grouped_list.append(temp_group)
    #         temp_group = []
    #         counter = 0

    final_first = len(list) - 5
    current_first = 0

    for item in list:
        temp_group = list[current_first:current_first+5]
        grouped_list.append(temp_group)

        # print(temp_group)

        current_first += 1

        if current_first > final_first:
            break

    # print(grouped_list)

    return grouped_list

def get_job_description(job_index):
    # 
    #   returns job description 
    # 
    if job_index == 0:
        category = 'Software Developer'
    elif job_index == 1:
        category = 'Software Engineer'
    elif job_index == 2:
        category = 'System Analyst'
    elif job_index == 3:
        category = 'Web Developer'

    return category

def get_max(list):
    # 
    #   returns the index of max value in array
    # 
    index = 0
    largest = 1

    for item in list:
        # print(item)
        # print(list[largest])
        if item > list[largest]:
            largest = list.index(item)
        else:
            largest = largest

        # print(largest)
        index += 1

        if index == 4:
            break

    return largest

def categorize_resume():
    resume_ids = fetch_resume_ids()
    normalizer = Normalizer()

    print(resume_ids)

    for resume_id in resume_ids:
        skills = fetch_skills(resume_id)
        output_group = [0, 0, 0, 0]

        print(skills)

        skills = normalizer.interpolate_skills(skills)
        lack = 0
        input_size = 5

        # print("grouped list")
        # print(group_list(skills, 5))

        grouped_skills = group_list(skills, 5)

        for group in grouped_skills:

            skills = numpy.array([group])
            outputs = classifier.classify(skills)
            index = numpy.argmax(outputs)
            category = get_job_description(index)

            print('\n')
            print(outputs)

            output_group.append(outputs)

            print(category)

            counter = 0
            out = outputs[0]

            for item in out:
                output_group[counter] += item
                # print(output_group[counter])
                counter += 1
                if counter == 4:
                    counter = 0

            # print(output_group)
            # print(len(output_group))
            output_group = output_group[0:4]
            index = get_max(output_group)
            category = get_job_description(index)

        # update_resume_category(category, resume_id)
        print('\nFinal-Output: ' + category)
        print('\n****\n')



if __name__ == '__main__':
    # classifier = ResumeClassifier()
    # classifier.train()
    run()