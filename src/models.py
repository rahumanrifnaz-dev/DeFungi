import tensorflow as tf

from . import config


def build_model_a(input_shape=(64, 64, 3), num_classes: int = config.NUM_CLASSES) -> tf.keras.Model:
    inputs = tf.keras.Input(shape=input_shape)
    x = tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu")(inputs)
    x = tf.keras.layers.MaxPooling2D(2)(x)
    x = tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu")(x)
    x = tf.keras.layers.MaxPooling2D(2)(x)
    x = tf.keras.layers.Conv2D(128, 3, padding="same", activation="relu")(x)
    x = tf.keras.layers.MaxPooling2D(2)(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(64, activation="relu")(x)
    outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
    return tf.keras.Model(inputs, outputs, name="model_a_standard_cnn")


def build_model_b(input_shape=(64, 64, 3), num_classes: int = config.NUM_CLASSES) -> tf.keras.Model:
    inputs = tf.keras.Input(shape=input_shape)
    x = tf.keras.layers.SeparableConv2D(32, 3, padding="same", activation="relu")(inputs)
    x = tf.keras.layers.MaxPooling2D(2)(x)
    x = tf.keras.layers.SeparableConv2D(64, 3, padding="same", activation="relu")(x)
    x = tf.keras.layers.MaxPooling2D(2)(x)
    x = tf.keras.layers.SeparableConv2D(96, 3, padding="same", activation="relu")(x)
    x = tf.keras.layers.MaxPooling2D(2)(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(48, activation="relu")(x)
    outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
    return tf.keras.Model(inputs, outputs, name="model_b_lightweight_sepconv")


def parameter_storage_kb(parameter_count: int, bytes_per_parameter: int = 4) -> float:
    return parameter_count * bytes_per_parameter / 1024


def separable_conv_parameter_count(input_channels: int, output_channels: int, kernel_size: int = 3) -> dict:
    depthwise = kernel_size * kernel_size * input_channels
    pointwise = input_channels * output_channels + output_channels
    return {
        "depthwise": depthwise,
        "pointwise": pointwise,
        "total": depthwise + pointwise,
    }
