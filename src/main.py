from resume_classifier import ResumeClassifier
from csv_reader import CSVReader
import random
import numpy as np

def run():
    
    classifier = ResumeClassifier()
    # classifier.train()
    inputs = np.loadtxt('data/training_data_normalized.csv', delimiter=',')
    i = inputs[1:2,0:100]
    y_train = inputs[:,-1]

    print(classifier.classify(i))


if __name__ == '__main__':
    run()