from resume_classifier import ResumeClassifier
from csv_reader import CSVReader
import random
import numpy as np

def run():
    
    classifier = ResumeClassifier()
    # classifier.train()

    # input_sample = []
    # for i in range(100):
    #     input_sample.append(random.randint(0, 3352))
    reader = CSVReader()
    # inputs = reader.read('data/training_set.csv')
    inputs = np.loadtxt('data/training_data_normalized.csv', delimiter=',')
    # print(len(inputs[0][:-1]))

    # print('numbers')
    # for num in inputs[0]:
        # print(num)
    # del inputs[:][100]
    i = inputs[0:1,0:100]
    y_train = inputs[:,-1]
    # i = np.array([inputs[99][:-1]])

    # for setx in x_train:
    #     print(setx)
    # print(x_train)
    # print(y_train)

    classifier.classify(i)


if __name__ == '__main__':
    run()