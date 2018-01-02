
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

        index = skills.index(skill_description.upper())
        interpolated = float(self.interpolate(index, len(skills), -1))
        # float()print(interpolated)

        return interpolated

    def write_training_set(self, job_index):
        jobs = ['skillsSoftDev', 'skillsSoftEng', 'skillsSysAnal', 'skillsWeb']
        job = jobs[job_index]

        in_filename = 'data/' + job + '.txt'
        out_filename = 'data/' + job + '_index_interpolated.txt'
        
        file = open(in_filename, 'r')
        skills = file.readlines()
        skills_indexes = [None]

        cols = 100
        col_count = 0
        index = job_index
        remainder = len(skills) % 100

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

        in_filename = 'data/' + job + '_index_interpolated.txt'
        out_filename = 'data/training_set_interpolated.csv'

        file = open(in_filename, 'r')
        skills = file.readlines()
        skills_indexes = [None]

        cols = 100
        col_count = 0
        index = job_index
        remainder = len(skills) % 100

        print('writing to > ' + out_filename)

        if remainder > 0:
            print(len(skills))
            print(remainder)
            remainder = 100 - remainder
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


if __name__ == '__main__':
    normalizer = Normalizer()

    for i in range(4):
        normalizer.compile_training_set(i)
