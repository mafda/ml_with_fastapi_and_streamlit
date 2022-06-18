from tensorflow.keras import backend as K
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D, Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


def load_data():
    # load dataset
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # reshaping the inputs
    if K.image_data_format() == "channels_first":
        X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
        X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
        input_shape = (1, 28, 28)
    else:
        X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
        X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
        input_shape = (28, 28, 1)

    # normalizing the inputs
    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0

    # Convert class vectors to binary class matrices
    y_train_cat = to_categorical(y_train, 10)
    y_test_cat = to_categorical(y_test, 10)

    return input_shape, X_train, y_train_cat, X_test, y_test_cat


def define_model(input_shape):
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

    return model


def compile_model(model):
    # compiling the sequential model
    return model.compile(
        "rmsprop",
        loss="categorical_crossentropy",
        metrics=["categorical_accuracy"],
    )


def fit_model(model, X_train, y_train_cat, X_test, y_test_cat, epochs):
    # training the model and saving metrics in history
    return model.fit(
        X_train,
        y_train_cat,
        batch_size=256,
        epochs=epochs,
        verbose=2,
        validation_data=(X_test, y_test_cat),
    )


def save_model(model, model_path):

    return model.save(model_path)


def train_model(epochs, model_path):
    input_shape, X_train, y_train_cat, X_test, y_test_cat = load_data()
    model = define_model(input_shape)
    model = compile_model(model)
    model = fit_model(model, X_train, y_train_cat, X_test, y_test_cat, epochs)
    save_model(model_path)


train_model(100, "./my_model/mnist.h5")
