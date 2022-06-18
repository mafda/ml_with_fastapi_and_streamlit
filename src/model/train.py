from tensorflow.keras import backend as K
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Conv2D, Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

# ======= LOAD DATA =======

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

# ======= DEFINE MODEL =======

# building a linear stack of layers with the sequential model
model = Sequential()

# Add the input layer and hidden layer 1
model.add(
    Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=input_shape)
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
history = model.fit(
    X_train,
    y_train_cat,
    batch_size=256,
    epochs=5,
    verbose=2,
    validation_data=(X_test, y_test_cat),
)

# ======= SAVE MODEL =======

model.save("./my_model/mnist.h5")
