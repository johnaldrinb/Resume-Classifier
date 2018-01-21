import keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

import numpy as np
from numpy import genfromtxt

from sklearn.model_selection import train_test_split

import os.path
from csv_reader import CSVReader
# import  main


class ResumeClassifier:
    
    def __init__(self):
        # initialize model
        # load model if there's an existing one
        self._MODEL_FILE = 'model/resume_classifier_model_interpolated_8.h5'
        self._model = None
        self._input_size = 5

        if os.path.isfile(self._MODEL_FILE):
            # if model file exists
            self.__load_model()

        else:
            self.__init_model()

    def __init_model(self):
        # initialize model configuration
        self._model = Sequential()
        self._model.add(Dense(32, activation='relu', input_dim=self._input_size))
        self._model.add(Dropout(0.3))
        self._model.add(Dense(4, activation='softmax'))

        sgd = SGD(lr=0.001, decay=1e-5, momentum=0.9, nesterov=True)
        self._model.compile(loss='categorical_crossentropy',
                      optimizer=sgd,
                      metrics=['accuracy'])

    def __load_model(self):
        # loads existing model
        self._model = load_model(self._MODEL_FILE)

    def __save_model(self):
        # save current model configuration
        self._model.save(self._MODEL_FILE)

    def train(self):
        # train the neural network
        seed = 7
        training_set = np.genfromtxt('data/training_set_interpolated_5.csv',
                                     delimiter=',')

        x_train = training_set[:,0:self._input_size]
        y_train = training_set[:,-1]
        print(y_train)
        y_train_np = keras.utils.to_categorical(y_train, num_classes=4)
        # UNCOMMENT IF USING KFOL-CV
        # x_train, x_test, y_train, y_test = train_test_split(x_train,
        #                                                     y_train_np,
        #                                                     test_size=0.33,
        #                                                     random_state=seed)

        test_result = []

        self._model.fit(x_train,
                  y_train_np,
                  epochs=800,
                  batch_size=128)
        # UNCOMMENT IF USING KFOL-CV
        # self._model.fit(x_train,
        #           y_train,
        #           validation_data=(x_test,y_test),
        #           epochs=800,
        #           batch_size=35)

        # scores = self._model.evaluate(x_train[test],
        #                               y_train_np[test],
        #                               verbose=0)
        # print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
        # test_result.append(scores[1] * 100)

        # print("%.2f%% (+/- %.2f%%)" % (numpy.mean(test_result),
        #                                numpy.std(test_result)))
        self.__save_model()

        # score = self._model.evaluate(x_train, y_train_np, batch_size=100)
        # print("\n%s: %.2f%%" % (self._model.metrics_names[1], score[1]*100))

    def classify(self, inputs=None):
        # classify input
        # arguments: inputs - array of input
        # must return array of probabilities
        outputs = self._model.predict(inputs)
        return outputs