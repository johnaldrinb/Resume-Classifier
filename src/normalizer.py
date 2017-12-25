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

    job = 'skillsSoftDev'
    filename = 'data/' + job + '.txt'
    file = open(filename, 'r')

    skills = file.readlines()
    skills_indexes = [None]

    for skill in skills:
        # skills_indexes.append(normalizer.get_skill_index(skill))
        out = open('data/' + job + '_index.txt', 'a')
        out.write(str(normalizer.get_skill_index(skill)))
        out.write('\n')
        out.close()

