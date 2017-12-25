
class Normalizer:

    def get_skill_index(self, skill_description):

        filename = 'data/skills_list_uniques.txt'
        file = open(filename, 'r')
        index = 0

        skills = file.readlines()

        for skill in skills:
            skill = skill.upper()
            #print(skill)

        return skills.index(skill_description.upper())


if __name__ == '__main__':
    normalizer = Normalizer()

    jobs = ['skillsSoftDev', 'skillsSoftEng', 'skillsSysAnal', 'skillsWeb']
    job_index = 3
    job = jobs[job_index]

    filename = 'data/' + job + '_index.txt'
    file = open(filename, 'r')

    skills = file.readlines()
    skills_indexes = [None]

    cols = 100
    col_count = 0

    remainder = len(skills) % 100

    if remainder > 0:
        print(len(skills))
        print(remainder)
        remainder = 100 - remainder
        for i in range(remainder):
            skills.append('-1')


    for skill in skills:
        # skills_indexes.append(normalizer.get_skill_index(skill))
        col_count += 1
        out = open('data/training_set.csv', 'a')
        out.write(skill.rstrip() + ', ' + str(job_index))

        if col_count == 100:
            out.write('\n')
            col_count = 0

    out.write('\n')
    out.close()
