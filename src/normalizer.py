class Normalizer:

    def get_skill_index(self, skill_description):

        filename = 'data/skills.txt'
        file = open(filename, 'r')
        index = 0

        skills = file.readlines()
        return skills.index(skill_description + '\n')


