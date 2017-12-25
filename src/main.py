from resume_classifier import ResumeClassifier
import random
import numpy as np

def run():
    
    classifier = ResumeClassifier()
    classifier.train()

    # input_sample = []
    # for i in range(100):
    #     input_sample.append(random.randint(0, 3352))   

    inputs = np.loadtxt('data/training_set.csv', delimiter=',')
    # print(len(inputs[0][:-1]))

    # print('numbers')
    # for num in inputs[0]:
        # print(num)

    i = np.array([inputs[99][:-1]])

    classifier.classify(i)


if __name__ == '__main__':
    run()