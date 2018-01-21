from resume_classifier import ResumeClassifier
import random
import numpy as np

def test(in1, in2, out):
    
    classifier = ResumeClassifier()
    # classifier.train()
    inputs = np.loadtxt('data/training_set_interpolated.csv', delimiter=',')
    i = inputs[in1:in2,0:100]

    outputs = classifier.classify(i)
    index = np.argmax(outputs)
    print(outputs)

    match = ''
    if index == out:
        match = 'Matched!'
    else:
        match = 'Not Matched!'

    if index == 0:
        print('Software Developer > ' + match)
    elif index == 1:
        print('Software Engineer > ' + match)
    elif index == 2:
        print('System Analyst > ' + match)
    elif index == 3:
        print('Web Developer > ' + match)

    if match == 'Matched!':
        return 1
    else:
        return 0


if __name__ == '__main__':
    # train before testing new k-test dataset
    classifier = ResumeClassifier()
    classifier.train()

    # classifications = 0
    # correct_classification = 0
    # incorrect_classification = 0

    # for i in range(13):
    #     i+=123
    #     classification = test(i, i+1, 3)

    #     if classification == 1:
    #         correct_classification+=1
    #     else:
    #         incorrect_classification+=1

    #     classifications+=1

    # print('test result: ' + str(correct_classification) + '/' +
    #  str(classifications))