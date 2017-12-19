import keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

import numpy as np

import os.path


class ResumeClassifier:

    MODEL_FILE = 'model/resume_classifier_model.h5'
    
    def __init__(self):
        # initialize model
        # load model if there's an existing one
        self._model = None

        if os.path.isfile(MODEL_FILE):
            # if model file exists
            self._load_model()

        else:
            self._init_model()
            self._save_model()

    def _init_model(self):
        # initialize model configuration
        self._model = Sequential()
        self._model.add(Dense(128, activation='relu', input_dim=50))
        self._model.add(Dropout(0.3))
        self._model.add(Dense(64, activation='relu'))
        self._model.add(Dropout(0.3))
        self._model.add(Dense(5, activation='softmax'))

        sgd = SGD(lr=0.02, decay=1e-6, momentum=0.9, nesterov=True)
        self._model.compile(loss='categorical_crossentropy',
                      optimizer=sgd,
                      metrics=['accuracy'])

    def _load_model(self):
        # loads existing model
        self._model = load_model(MODEL_FILE)

    def _save_model(self):
        # save current model configuration
        self._model.save(MODEL_FILE)

    def train(self):
        # train the neural network
        # temp training data
        x_train = np.random.random((1000, 50))
        y_train = keras.utils.to_categorical(np.random.randint(5, size=(1000, 1)), num_classes=5)
        x_test = np.random.random((100, 50))
        y_test = keras.utils.to_categorical(np.random.randint(5, size=(100, 1)), num_classes=5)
        x_input = np.random.random((1, 50))

        self._model.fit(x_train,
                  y_train,
                  epochs=150,
                  batch_size=10)
        self.save_model()
        #score = model.evaluate(x_test, y_test, batch_size=10)

    def classify(self, inputs):
        # classify input
        # arguments: inputs - array of input
        model.predict(inputs)



classifier = ResumeClassifier()
classifier.train()
        