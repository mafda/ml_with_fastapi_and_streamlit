"""Project: Prototyping a Machine Learning Application with Streamlit

CNN for training mnist dataset
"""

from tensorflow.keras import backend as K
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D, Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


def train_model(epochs, model_path):
    """Train model function

    Parameters
    ----------
    epochs : int
        epochs number
    model_path : str
        path to save model

    """

    # ======= LOAD DATA =======

    # load dataset
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # reshaping the inputs
    if K.image_data_format() == "channels_first":
        x_train = x_train.reshape(x_train.shape[0], 1, 28, 28)
        x_test = x_test.reshape(x_test.shape[0], 1, 28, 28)
        input_shape = (1, 28, 28)
    else:
        x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
        x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
        input_shape = (28, 28, 1)

    # normalizing the inputs
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    # Convert class vectors to binary class matrices
    y_train_cat = to_categorical(y_train, 10)
    y_test_cat = to_categorical(y_test, 10)

    # ======= DEFINE MODEL =======

    # building a linear stack of layers with the sequential model
    model = Sequential()

    # Add the input layer and hidden layer 1
    model.add(
        Conv2D(
            32, kernel_size=(3, 3), activation="relu", input_shape=input_shape
        )
    )

    # Add the input layer and hidden layer 2
    model.add(Conv2D(64, (3, 3), activation="relu"))

    # Flatten convolutional output
    model.add(Flatten())

    # Add the input layer and hidden layer 3
    model.add(Dense(128, activation="relu"))

    # Add the output layer
    model.add(Dense(10, activation="softmax"))

    # ======= COMPILE MODEL =======

    # compiling the sequential model
    model.compile(
        "rmsprop",
        loss="categorical_crossentropy",
        metrics=["categorical_accuracy"],
    )

    # ======= FIT MODEL =======

    # training the model and saving metrics in history
    model.fit(
        x_train,
        y_train_cat,
        batch_size=256,
        epochs=epochs,
        verbose=2,
        validation_data=(x_test, y_test_cat),
    )

    # ======= SAVE MODEL =======

    model.save(model_path)


if __name__ == "__main__":
    train_model(1, "./my_model/mnist-test.h5")
