class Normalizer:

    def get_skill_index(self, skill_description):

        filename = 'data/skills.txt'
        file = open(filename, 'r')
        index = 0

        skills = file.readlines()

        for skill in skills:
            skill = skill.upper()
            print(skill)

        return skills.index(skill_description.upper())


if __name__ == '__main__':
    normalizer = Normalizer()

    job = 'skillsWeb'
    #filename = 'data/' + job + '.txt'
    filename = 'skills_list.txt'
    file = open(filename, 'r')

    skills = file.readlines()
    skills_indexes = [None]

    skills_set = list(set(skills))

    for skill in skills_set:
        out = open('skills_list_uniques.txt', 'a')

        #skills_indexes.append(skill)
        out.write(skill.upper())
        out.close()
        #skills_indexes.append(normalizer.get_skill_index(skill))
