import random

class Normalizer:

    def interpolate(self, x, max, min):
        xIn = min;
        xOut = max;
        yIn = 1;
        yOut = -1;
        interpolated = (((x - xIn) * (yOut - yIn)) / (xOut - xIn)) + yIn;

        return interpolated

    def get_skill_index(self, skill_description):

        filename = 'data/skills_list_uniques.txt'
        file = open(filename, 'r')
        index = 0

        skills = file.readlines()
        skills_strip = []

        for skill in skills:
            skills_strip.append(skill.strip())

        # try:
        index = skills_strip.index(skill_description.upper().strip())
        interpolated = float(self.interpolate(index, len(skills_strip), -1))

        # print(interpolated)

        return interpolated
        # except:
        #     return -1
        # float()print(interpolated)

    def duplicate_training_set(self, job_index):
        jobs = ['skillsSoftDev', 'skillsSoftEng', 'skillsSysAnal', 'skillsWeb']
        job = jobs[job_index]

        in_filename = 'data/' + job + '_index_interpolated_5.txt'
        out_filename = 'data/' + job + '_index_interpolated_5_long.txt'        

        file = open(in_filename, 'r')
        skills = file.readlines()
        skills_indexes = random.sample(skills, len(skills))

        for skill in skills_indexes:
            out = open(out_filename, 'a')
            out.write(str(skill))
            # out.write('\n')

        out.close()

    def write_training_set(self, job_index):
        jobs = ['skillsSoftDev', 'skillsSoftEng', 'skillsSysAnal', 'skillsWeb']
        job = jobs[job_index]

        in_filename = 'data/' + job + '.txt'
        out_filename = 'data/' + job + '_index_interpolated_5.txt'
        
        file = open(in_filename, 'r')
        skills = file.readlines()
        skills_indexes = [None]

        cols = 5
        col_count = 0
        index = job_index
        remainder = len(skills) % cols

        print('writing to > ' + out_filename)

        for skill in skills:
            skill_index = normalizer.get_skill_index(skill)

            out = open(out_filename, 'a')
            out.write(str(skill_index))
            out.write('\n')

        out.write('\n')
        out.close()

    def compile_training_set(self, job_index):
        jobs = ['skillsSoftDev', 'skillsSoftEng', 'skillsSysAnal', 'skillsWeb']
        job = jobs[job_index]

        in_filename = 'data/' + job + '_index_interpolated_5.txt'
        out_filename = 'data/training_set_interpolated_5.csv'

        file = open(in_filename, 'r')
        skills = file.readlines()
        skills_indexes = [None]

        cols = 5
        col_count = 0
        index = job_index
        remainder = len(skills) % cols

        print('writing to > ' + out_filename)

        print(len(skills))

        if remainder > 0:
            print(remainder)
            remainder = cols - remainder
            for i in range(remainder):
                skills.append('-1')

        for skill in skills:
            # print(skill)
            # skills_indexes.append(normalizer.get_skill_index(skill))
            col_count += 1
            index += 1

            out = open(out_filename, 'a')
            out.write(skill.rstrip() + ', ')
            # out.write('\n')

            if col_count == cols:
                out.write(skill.rstrip() + ', ' + str(job_index))
                out.write('\n')
                col_count = 0

        out.write('\n')
        out.close()

    def interpolate_skills(self, skills):
        interpolated_skill = []

        for skill in skills:
            interpolated_skill.append(self.get_skill_index(skill))

        return interpolated_skill


if __name__ == '__main__':
    normalizer = Normalizer()
    counter = 0
    mode_writing_training_set = False
    mode_duplicating_training_set = False
    mode_compiling_training_set = True

    loop_range = 4

    if mode_duplicating_training_set is True:
        loop_range = 32

    for i in range(loop_range):
        if mode_writing_training_set is True:
            normalizer.write_training_set(i)

        elif mode_compiling_training_set is True:
            normalizer.compile_training_set(i)

        elif mode_duplicating_training_set is True:
            i = i%4
            counter+=1
            print(counter)
            normalizer.duplicate_training_set(i)
 