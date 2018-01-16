# items = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# item_groups = []

# final_first = len(items) - 5
# current_first = 0

# print('length ' + str(len(items)))
# print('final first ' + items[final_first])

# for item in items:
#     temp_group = items[current_first:current_first+5]
#     item_groups.append(temp_group)

#     # print(temp_group)

#     current_first += 1

#     if current_first > final_first:
#         break



# print(item_groups)

import sqlite3

def connect_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def fetch_id():
    
    conn = connect_db('data/main.db')
    cursor = conn.cursor()

    # resume_id = int(resume_id)
    # print(resume_id)

    # cursor.execute('SELECT SKILL FROM SKILLS WHERE resume_id=?', (resume_id,))
    # rows = cursor.fetchall()

    name = 'AdministratorSoftware-Engineer.pdf'

    cursor.execute('SELECT resume_id FROM RESUME WHERE FILENAME=?', (name,))
    resume = cursor.fetchall()
    print(resume)

    # skills = []

    # for row in rows:
    #     skills.append(row[0])

    # conn.close()

    # return skills

if __name__ == '__main__':
    fetch_id()
