class CSVReader:
    def read(self, filname):
        file = open(filname, 'r')
        lines = file.readlines()

        output = []

        # print(lines)
        for line in lines:
            values = line.split(',')
            temp = []

            for value in values:
                value = float(value)
                temp.append(value)
                # print(value)
            
            output.append(temp)

        # for line in output:
        #     print(line)

        return output


if __name__ == '__main__':
    reader = CSVReader()
    reader.read('data/training_set.csv')